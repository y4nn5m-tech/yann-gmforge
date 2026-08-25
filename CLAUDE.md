# Notes pour Claude Code

Ce dépôt fabrique des documents de table pour le jeu de rôle : une source Markdown, trois sorties
(PDF, HTML, EPUB). Lis d'abord `README.md` pour les conventions d'écriture, puis ce fichier pour ce
qu'il ne faut pas casser.

## La règle qui prime sur toutes les autres

**Le PDF est reproductible au bit près, et il doit le rester.** Ce n'est pas un confort : c'est le seul
moyen de savoir qu'une modification de contenu n'a pas déplacé la pagination. Trois choses le
garantissent, et chacune se casse en silence :

1. **la police est embarquée** dans `assets/fonts/` et appelée en `@font-face` sous le nom
   `DejaVuVendored`. Ne jamais la remplacer par un appel système, ne jamais « simplifier » le
   `font-family`. Une DejaVu absente ou d'une autre version décale les retours à la ligne, et une unité
   qui tenait tout juste déborde d'une ligne — invisible au diff, fatal au document ;
2. **`SOURCE_DATE_EPOCH` est fixé** en tête de `build.py`. Sans lui, WeasyPrint horodate le PDF et deux
   compilations identiques donnent deux empreintes différentes ;
3. **les versions sont épinglées** dans `.github/workflows/build.yml` (pandoc 3.1.3, WeasyPrint 69.0).
   Les relever est une décision à prendre exprès, suivie d'une vérification visuelle.

Vérification, à faire après toute modification de `build.py`, des `assets/` ou du filtre :

```
python3 build.py note-bun-and-run && sha256sum out/*.pdf
python3 build.py note-bun-and-run && sha256sum out/*.pdf   # doit être identique
```

## Ce qui ne se réorganise pas

- **`assets/print.css` est une charte arrêtée**, pas une feuille à améliorer. Les corps, les couleurs,
  les marges, la taille du texte ont été réglés à l'usage, sur des documents imprimés et menés en
  partie. Ne pas les toucher sans demande explicite — et surtout pas au nom de la lisibilité à l'écran :
  ce fichier ne sert qu'à l'impression.
- **Les cinq classes de couleur sont un langage, pas de la décoration** : `dire` (ce qu'on peut dire
  aux joueurs) · `jeu` (mécanique) · `mj` (information réservée) · `obj` (pilotage de scène) ·
  `warn` (arbitrage). N'en ajouter aucune, n'en renommer aucune.
- **L'arborescence est stable.** `src/<document>/` contient des fragments numérotés qui sont
  concaténés dans l'ordre alphabétique : la numérotation `00-`, `10-`, `20-`… est le plan du document.
- **Pas de dépendance JavaScript.** La chaîne est Python + pandoc + un filtre Lua. Il n'y a pas de
  `package.json`, et il n'y en a pas besoin : un lanceur de tâches ne justifie pas un toolchain Node.
  Si un jour le rendu PDF passe à Chromium, ce sera une décision de fond, discutée d'abord.

## Les contrôles ne sont pas décoratifs

`build.py` sort en code 1 quand un contrôle échoue, et c'est ce qui fait de la CI un garde-fou plutôt
qu'un compilateur. **Ne jamais désactiver un contrôle pour faire passer un build** : un contrôle qui
échoue signale un défaut du document, pas un défaut du script.

| Contrôle | Ce qu'il attrape |
|---|---|
| volume | une note d'arbitrage de plus de 15 pages : il y a de la recopie |
| pages presque vides | une page qui ne porte qu'une ou deux lignes |
| renvois d'arbitrage | un `(A4)` qui ne pointe sur aucun arbitrage défini |
| numéros de page | un « voir page 12 » dans le corps du texte, interdit par le modèle |

Le taux de remplissage se mesure en parcourant l'arbre de boîtes de WeasyPrint et en prenant le bas de
la dernière `LineBox` de chaque page — **en excluant les boîtes dont le nom de type contient `Margin`**.
Sans cette exclusion, le pied de page est compté et toutes les pages sortent à 102 %. La méthode a été
fausse deux fois avant d'être juste ; ne pas la « simplifier ».

## `modele/` n'est pas du code

Les huit fichiers de `modele/` sont la copie versionnée d'un modèle éditorial qui vit ailleurs (dans
les docs d'un projet claude.ai). Ils ne sont pas chargés par la chaîne : ils sont ce que la chaîne
applique. **Ne pas les éditer, ne pas les reformater, ne pas les linter.** Voir `modele/README.md`.

Seule exception, et c'est un vrai couplage : `assets/print.css` doit rester identique à la feuille
canonique recopiée dans `modele/MODELE-socle.md`, aux trois écarts près marqués `/* [dépôt] */`.

## Ce qui reste à faire

- **Le calage de la CSS sur l'arbre de pandoc.** À la main, la note faisait 8 pages ; via pandoc, 10.
  La cause est diffuse — pandoc normalise l'arbre (enveloppe dans des `<p>`, ajoute des id,
  restructure les cellules) et la CSS rencontre un arbre différent. Le travail est un réglage unique,
  après quoi la sortie de la chaîne devient la référence. Ne pas chercher un coupable unique.
- **La conversion de l'aide de jeu**, qui est la partie difficile : sa règle centrale est « une unité =
  une page » (`.unit { break-before: page }`), et elle demande un contrôle de débordement unité par
  unité qui n'existe pas encore dans `build.py`.
- **Le régime reflowable** ne préserve pas cette règle : en HTML et en EPUB, une unité devient une
  section. C'est une refonte assumée, pas un bug à corriger.
