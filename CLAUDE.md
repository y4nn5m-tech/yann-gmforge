# Notes pour Claude Code

`yann-gmforge` transforme un scénario du commerce en documents menables. Le dépôt contient trois
couches qu'il ne faut pas confondre : le **modèle** (`modele/`, la doctrine éditoriale — ce qui dure),
la **chaîne** (`build.py`, `filters/`, `assets/` — remplaçable), les **documents** (`src/`).

Deux chemins, et ils n'ont presque rien en commun. Lis celui qui correspond à la demande.

---

# 1. Produire un document

## D'abord lire le modèle, toujours

**Ne commence pas à écrire avant d'avoir lu `modele/`.** Ce n'est pas de la documentation d'appoint :
c'est l'autorité sur le contenu, et rien dans ce dépôt ne la remplace.

Dans l'ordre :

1. `modele/instructions-projet.md` — le déroulé d'une demande, en quatre étapes. **Il s'applique ici
   aussi.** En particulier : l'analyse se fait **en conversation, sans produire aucun document**, et on
   **ne devine jamais** quel livrable est demandé — on le demande ;
2. `modele/MODELE-socle.md` — le socle commun : code couleur, charte, règles qui valent pour les deux
   livrables. Il indique en tête les autres chapitres à charger ;
3. `modele/MODELE-analyse.md` — **toujours, et en premier** parmi les chapitres : la grille de lecture
   et les typologies servent dès l'analyse ;
4. puis, selon le cas : `modele/MODELE-livrable-aide-de-jeu.md` ou
   `modele/MODELE-livrable-dossier-prep.md`, `modele/MODELE-formes.md` (selon la forme d'intrigue),
   `modele/MODELE-systemes.md` (selon le jeu).

Après un scénario traité, le retour d'expérience se consigne dans `modele/JOURNAL-passages.md` —
jamais dans le socle. Attention : ces fichiers sont une **copie** de docs qui vivent ailleurs, et la
synchronisation est manuelle dans un seul sens. Voir `modele/README.md` avant d'en modifier un.

## Dépouiller la source : la passe mécanique d'abord

Quand la source est un PDF, **ne pas la lire page à page en image**. Lancer d'abord :

```
python3 scripts/extraire.py <le.pdf> --nom <nom-du-scenario>
```

Ça produit `sources/<nom>/texte.txt` — greppable, ce qui est le vrai bénéfice : toute la méthode du
modèle repose sur des croisements que l'auteur n'a pas faits, et `grep -n` les rend exhaustifs au lieu
de les faire dépendre de ce qu'on se rappelle avoir vu vingt pages plus tôt.

Et surtout `sources/<nom>/manifeste.md`, qui **signale ce que l'extraction n'a pas su lire**. Une page
dont la densité de texte s'effondre porte le plan ou une pleine page illustrée. Ces pages-là — et
elles seules — se regardent en image :

```
python3 scripts/extraire.py <le.pdf> --nom <nom> --rendre
```

Le manifeste rappelle aussi ce qu'on **ne peut pas** trancher depuis le texte à plat : le niveau
typographique (dont dépend le test « la source est-elle lisible ? »), les légendes d'illustration, les
tableaux, les colonnes. Sur ces quatre points, revenir au PDF.

`sources/` est ignoré par git : c'est le texte du scénario mot pour mot, pas une reformulation.

## Démarrer un document

Un document est un répertoire `src/<nom>/` contenant des fragments Markdown. **La numérotation est le
plan** : les fragments sont concaténés dans l'ordre alphabétique, et `00-`, `10-`, `20-` laissent la
place d'insérer une section sans tout renommer.

```
src/note-bun-and-run/
  00-couverture.md     ← porte l'en-tête YAML
  10-arbitrages.md
  20-annonces.md
  …
```

L'en-tête YAML va dans le **premier** fragment, et lui seul :

```yaml
---
title: "Bun & Run"
subtitle: "Note d'arbitrage"
scenario: "Bun & Run"        # groupe les documents d'un même scénario sur l'index
type: note                   # note | aide — déclare le type, ne le laisse pas deviner
jeu: "Fevertown — kit de découverte v1.2"
pied: "BUN & RUN — note d'arbitrage"
lang: fr
---
```

**`type` n'est pas décoratif : c'est lui qui décide des contrôles** — le volume et le remplissage
pour une note, le débordement d'unité pour une aide de jeu. Il a été deviné un temps en reniflant le mot « note » dans `pied`, si bien qu'un pied
libellé autrement désactivait l'alarme en silence ; le reniflage reste en repli, mais un document neuf
déclare `type`.

`scenario` et `jeu` ne servent qu'à la page d'accueil du site : ils regroupent les documents d'un même
scénario et nomment le jeu au-dessus. Les omettre ne casse rien — le titre sert alors de groupe.

## Écrire

Les conventions — blocs de couleur, sections, tableaux de grille à largeurs déclarées, micro-grilles —
sont dans `README.md`, avec un exemple de chacune. Deux rappels qui coûtent cher quand on les oublie :

- **les cinq couleurs sont un langage**, pas de la mise en forme : `dire` (ce qu'on peut dire aux
  joueurs) · `jeu` (mécanique) · `mj` (réservé au MJ) · `obj` (pilotage de scène) · `warn`
  (arbitrage). N'en ajoute aucune, n'en détourne aucune ;
- **ne jamais renvoyer à un numéro de page** dans le corps du texte : la pagination bouge à chaque
  reprise. Renvoyer par le titre. Un contrôle le vérifie.

## Valider le fond avant de compiler

**L'échange sur le contenu se fait sur le Markdown, en conversation.** Ne pas compiler pour montrer le
résultat, ne pas ouvrir de navigateur, ne rien rendre en local pour faire valider : ce qui se discute
à cette étape, c'est le fond — les arbitrages retenus, les chiffres, les croisements, le découpage.
La mise en forme est arrêtée depuis longtemps et n'a pas besoin d'être revue à chaque document.

Tant que le fond n'est pas validé, on itère sur les fragments. Rien d'autre.

## Puis compiler — comme un lint, pas comme un aperçu

Une fois le fond validé :

```
python3 build.py <nom-du-document>
```

Trois sorties dans `out/`, puis les contrôles. **C'est le seul but de cette compilation locale** :
les contrôles n'existent qu'au moment du build, et sans elle on découvrirait en CI, après le push,
qu'une note fait 17 pages. Le PDF produit ne se montre pas et ne s'ouvre pas — il n'est là que pour
être mesuré.

**Un contrôle qui échoue signale un défaut du document, pas un défaut du script** — ne jamais le
désactiver pour faire passer un build. Corriger les fragments, recompiler.

| Contrôle | Sur quoi | Ce qu'il attrape |
|---|---|---|
| volume | note | une note d'arbitrage de plus de 15 pages : il y a de la recopie |
| pages presque vides | note | une page qui ne porte qu'une ou deux lignes |
| renvois d'arbitrage | note | un `(A4)` qui ne pointe sur aucun arbitrage défini |
| numéros de page | les deux | un « voir page 12 » dans le corps du texte |
| une unité = une page | aide | une unité rendue seule qui tient sur deux pages |

**Les contrôles ne sont pas les mêmes selon `type:`.** Une aide de jeu n'est pas mesurée au
remplissage — une unité à moitié pleine y est normale — et ses renvois `— A4` pointent vers la note,
donc ils ne sont pas vérifiés. Ce qui s'y mesure, c'est le débordement, et lui seul.

Un avertissement (`·`) n'arrête pas le build : une page à 27 % est souvent une fin de section
légitime. Un `ÉCHEC` sort en code 1.

## Commit, push, et c'est la CI qui publie

**Ne jamais committer ni pousser sans accord explicite.** Le fond validé et les contrôles passés, le
demander, puis committer les fragments (`src/`) — jamais `out/`, ni `sources/`, tous deux ignorés.

Le push déclenche la CI, qui recompile, rejoue les contrôles, **vérifie la reproductibilité** en
compilant deux fois et en comparant les empreintes, reconstruit la page d'accueil et déploie sur
GitHub Pages. C'est **là** que le document se regarde : sur le site déployé, pas en local.

La page d'accueil (`scripts/index.py`) se reconstruit entièrement à chaque passage, en lisant les
en-têtes YAML de `src/`. Il n'y a aucune liste à tenir à jour : ajouter un scénario, c'est ajouter un
répertoire.

---

# 2. Toucher à la chaîne

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

Vérification, après toute modification de `build.py`, des `assets/` ou du filtre :

```
python3 build.py <doc> && sha256sum out/*.pdf
python3 build.py <doc> && sha256sum out/*.pdf   # doit être identique
```

## Ce qui ne se réorganise pas

- **`assets/print.css` est une charte arrêtée**, pas une feuille à améliorer. Les corps, les couleurs,
  les marges, la taille du texte ont été réglés à l'usage, sur des documents imprimés et menés en
  partie. Ne pas y toucher sans demande explicite — et surtout pas au nom de la lisibilité à l'écran :
  ce fichier ne sert qu'à l'impression.
- **`assets/print.css` doit rester identique à la feuille canonique** recopiée dans
  `modele/MODELE-socle.md`, aux trois écarts près marqués `/* [dépôt] */` (police embarquée, pied
  injecté par le build, largeur de tableau neutralisée pour pandoc). C'est le seul couplage réel entre
  le modèle et la chaîne.
- **L'arborescence est stable**, et la numérotation des fragments est le plan des documents.
- **Pas de dépendance JavaScript.** La chaîne est Python + pandoc + un filtre Lua. Il n'y a pas de
  `package.json` et il n'en faut pas : un lanceur de tâches ne justifie pas un toolchain Node. Si un
  jour le rendu PDF passe à Chromium, ce sera une décision de fond, discutée d'abord.
- **`modele/` n'est pas du code** : ne pas le reformater, ne pas le linter, ne pas y passer d'outil
  automatique.

## Un piège de mesure, déjà tombé deux fois

Le taux de remplissage se calcule en parcourant l'arbre de boîtes de WeasyPrint et en prenant le bas de
la dernière `LineBox` de chaque page — **en excluant les boîtes dont le nom de type contient
`Margin`**. Sans cette exclusion, le pied de page est compté et toutes les pages sortent à 102 %. La
méthode a été fausse deux fois avant d'être juste ; ne pas la « simplifier ».

## Ce que le régime reflowable ne peut pas rendre

En HTML et en EPUB, la règle centrale de l'aide de jeu — « une unité = une page », `.unit
{ break-before: page }` — n'existe pas : `screen.css` la traduit en « une unité = une section ». C'est
une refonte assumée, pas un bug à corriger.
