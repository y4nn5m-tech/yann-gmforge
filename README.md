# yann-gmforge

Transformer un scénario du commerce en documents menables : un **livret de table** (l'aide de jeu) et
une **note d'arbitrage**. Le dépôt contient le modèle éditorial qui les définit et la chaîne qui les
fabrique.

Une source Markdown, trois sorties : **PDF** (charte d'impression), **HTML** (GitHub Pages),
**EPUB** (tablette).

```
python3 build.py note-bun-and-run
```

```
· note-bun-and-run — 7 fragments
  PDF   10 p.    71 Ko  sha b96da7d0b506a5d4
  HTML            47 Ko
  EPUB            26 Ko
```

## Arborescence

```
scripts/extraire.py   la passe mécanique : un PDF source → texte greppable + manifeste
assets/print.css      charte d'impression — la feuille canonique du socle
assets/screen.css     même identité, régime reflowable : site et EPUB
assets/web.css        extras du site seul : mode sombre, tableaux qui défilent
assets/fonts/         DejaVu embarquée — voir « reproductibilité »
filters/blocks.lua    les conventions d'écriture → HTML
src/<document>/       les fragments Markdown, un par section, préfixés 00-, 10-…
out/                  les trois sorties
modele/               le modèle lui-même, versionné — voir modele/README.md
```

`modele/` est une **copie** des docs du projet claude.ai, pas leur source : le dépôt ne les charge pas,
il les historise. La synchronisation est manuelle et le projet fait foi.

## Conventions d'écriture

Les cinq blocs de couleur, avec leur étiquette :

```markdown
::: {.warn lab="A1 — Sans Carl Cooler vivant, le scénario s'arrête"}
Il est le seul à connaître le rendez-vous.\
**Retenu :** le rendez-vous tient au costume de mascotte, pas à l'homme.
:::
```

Classes disponibles : `dire` · `jeu` · `mj` · `obj` · `warn`.

Un titre de section :

```markdown
## [1]{.num}Ce que la source ne tranche pas {.sec .brk}
```

`.brk` force un saut de page à l'impression, et n'a aucun effet à l'écran.

Un tableau — **grille**, avec les largeurs déclarées, jamais déduites du dessin :

```markdown
::: {.tight widths="26,18,56"}
+------------+------------+------------------------------+
| Trait      | Où ça tombe| Ce qu'on dit, et quand       |
+============+============+==============================+
| *Good Cop* | **Sc. 1**  | L'intervention **est** le…   |
+------------+------------+------------------------------+
:::
```

Les fusions de cellules sur plusieurs lignes marchent : il suffit d'omettre le trait horizontal
entre deux rangées.

Une micro-grille d'unité (aide de jeu) :

```markdown
::: {.loc}
- [Décor —]{.g .d} palmiers en plastique, néons verts
- [Indices —]{.g .i} la carte collector [*(Astuce, seuil 8)*]{.m}
- [PNJ —]{.g .p} Harvey, vexé et pas fou
:::
```

## Reproductibilité

Trois choses, et le PDF devient identique au bit près d'une machine à l'autre :

1. **la police est embarquée** dans `assets/fonts/` et appelée en `@font-face`. C'est le vrai
   risque : une DejaVu absente ou d'une autre version décale les retours à la ligne, et une unité
   d'aide de jeu qui tenait tout juste déborde ;
2. **`SOURCE_DATE_EPOCH` est fixé** par `build.py`. Sans ça, WeasyPrint horodate le PDF et deux
   compilations identiques donnent deux empreintes différentes ;
3. **les versions sont épinglées** dans le conteneur de build (WeasyPrint, pandoc, Pango).

Vérification :

```
python3 build.py && sha256sum out/*.pdf
python3 build.py && sha256sum out/*.pdf   # même empreinte
```

## Contrôles

`build.py` sort en code 1 si l'un échoue — c'est ce qui fait de la CI un garde-fou et non un
simple compilateur.

| Contrôle | Ce qu'il attrape |
|---|---|
| volume | une note d'arbitrage de plus de 15 pages : il y a de la recopie |
| pages presque vides | une page qui ne porte qu'une ou deux lignes |
| renvois d'arbitrage | un `(A4)` qui ne pointe sur aucun arbitrage défini |
| numéros de page | un « voir page 12 » dans le corps du texte, interdit par le socle |

## Chantiers ouverts

*Instantané, à relire d'un œil méfiant — cette section vieillit, contrairement à `CLAUDE.md`.*

- **Le calage de la CSS sur l'arbre de pandoc.** À la main, la note faisait 8 pages ; par la chaîne,
  10. La cause est diffuse : pandoc normalise l'arbre — enveloppe dans des `<p>`, ajoute des id,
  restructure les cellules — et la CSS rencontre un arbre différent de celui pour lequel elle a été
  réglée. C'est un réglage unique à faire une fois, après quoi la sortie de la chaîne devient la
  référence. Ne pas chercher un coupable unique.
- **La conversion de l'aide de jeu**, la partie difficile : sa règle centrale est « une unité = une
  page », et elle demande **le contrôle unité par unité**, qui existe déjà comme script dans le
  chapitre du livrable mais pas dans `build.py`.

## Ce que le régime reflowable change

Le PDF et l'EPUB ne sont pas le même document.

- La **note d'arbitrage** passe sans dommage : ce sont des sections qui coulent.
- L'**aide de jeu** perd sa règle centrale. « Une unité = une page » n'existe pas en reflowable :
  `screen.css` la traduit en « une unité = une section », et `--split-level=2` en fait un chapitre
  d'EPUB. C'est jouable sur une tablette, mais c'est une refonte, pas une conversion.
