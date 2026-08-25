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
scripts/index.py      la page d'accueil du site, reconstruite à chaque build
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

## L'en-tête YAML

Dans le **premier** fragment, et lui seul :

```yaml
---
title: "Bun & Run"
subtitle: "Note d'arbitrage"
scenario: "Bun & Run"        # groupe les documents d'un scénario sur l'index
type: note                   # note | aide — décide quels contrôles s'appliquent
jeu: "Fevertown — kit de découverte v1.2"
pied: "BUN & RUN — note d'arbitrage"
lang: fr
---
```

`type` est le seul champ dont l'absence a une conséquence silencieuse : sans lui, le type est deviné en
cherchant le mot « note » dans `pied`, et un pied libellé autrement laisse passer une note de 20 pages.

## La page d'accueil

`scripts/index.py` lit les en-têtes YAML de `src/`, regarde ce qui existe dans `out/`, et écrit
`out/index.html` : un bloc par scénario, ses documents en dessous, chacun avec ses trois formats et son
nombre de pages. **Aucune liste à tenir à jour** — ajouter un scénario, c'est ajouter un répertoire
dans `src/`. La CI la reconstruit à chaque passage avant de déployer.

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

**Où placer un encart :** un encart doit répondre à une phrase qui vient d'être dite. S'il peut
remonter de trois paragraphes sans que rien ne se casse, il est mal placé ; s'il n'est rattaché à
aucune phrase, ce n'est pas un encart mais de la matière à dire, donc un palier. Un contrôle le
vérifie.

Un bloc de lignes à dire (aide de jeu) — **une idée par ligne**, à piocher, jamais à lire d'un
trait :

```markdown
::: {.say}
- Le lac est gelé sur des centaines de mètres, plat et gris jusqu'à l'horizon.
- [« Parlez doucement, s'il vous plaît. Mon mari dort. »]{.q}
:::
```

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

| Contrôle | Sur quoi | Ce qu'il attrape |
|---|---|---|
| volume | note | une note d'arbitrage de plus de 15 pages : il y a de la recopie |
| pages presque vides | note | une page qui ne porte qu'une ou deux lignes |
| renvois d'arbitrage | note | un `(A4)` qui ne pointe sur aucun arbitrage défini |
| numéros de page | les deux | un « voir page 12 » dans le corps du texte, interdit par le socle |
| **charte d'impression** | **les deux** | **un avertissement de WeasyPrint : sélecteur invalide, police introuvable** |
| **une unité = une page** | **aide** | **une unité rendue seule qui tient sur deux pages** |
| **encarts à leur place** | **aide** | **plus de deux encarts avant le premier palier, ou en pied d'unité** |

Les trois premiers ne s'appliquent **qu'à la note**, et le dernier **qu'à l'aide de jeu** : dans un
livret, une unité qui remplit la moitié de sa page est normale — ce qui s'y mesure, c'est le
débordement. C'est aussi pourquoi les renvois `— A4` du livret, qui pointent vers la note, ne sont
pas vérifiés.

**Le contrôle des encarts est le seul qui porte sur l'éditorial**, et c'est un avertissement : une
unité se lit dans l'ordre où la scène se joue — ce qu'il faut savoir avant de parler, puis la descente
par paliers avec **chaque encart au point où sa matière tombe**, puis la sortie. Une pile d'encarts en
pied de page est le signe qu'on a rédigé la description d'abord et rangé le reste après ; à table, le
MJ cherche alors le jet trois écrans plus bas que la réplique qui l'appelle. Les unités qui ne
descendent pas par paliers — la conclusion, un profil, une table de mécanique — en sont exclues
automatiquement.

**Le contrôle de la charte est celui qui protège la reproductibilité en amont.** WeasyPrint signale
les défauts de feuille en avertissement *et produit le PDF quand même* : un sélecteur invalide, une
police introuvable, et le document sort silencieusement dégradé. Il ne porte que sur `print.css` —
`screen.css` et `web.css` visent un navigateur et utilisent légitimement des règles que WeasyPrint
ignore (`@media`, `overflow-x`).

## Chantiers ouverts

*Instantané, à relire d'un œil méfiant — cette section vieillit, contrairement à `CLAUDE.md`.*

- ~~**Le calage de la CSS sur l'arbre de pandoc.**~~ **Clos.** La cause n'était pas diffuse, et ce
  n'était pas un problème de réglage : c'étaient **deux bugs**, trouvés en comparant un PDF écrit
  hors chaîne à la même source compilée.
  1. Un **commentaire CSS imbriqué** en tête de `print.css` (`… signalées par /* [dépôt] */.`) : les
     commentaires CSS ne s'imbriquent pas, ce `*/` refermait l'en-tête, et le sélecteur invalide qui
     s'ensuivait **avalait le premier `@font-face`** — celui de la police régulière. `pdffonts` ne
     montrait que Bold, Italic et Bold-Italic ; le texte courant tombait sur une substitution
     système, plus large, et les unités débordaient. C'était aussi une bombe de reproductibilité :
     le rendu dépendait des polices de la machine de build.
  2. Le filtre insérait un **`<br>` après chaque étiquette de bloc**, alors que `.lab` est
     `display:block` dans les deux feuilles — une ligne vide par bloc coloré, cinq par unité de
     livret.
  Plus un calage réel, celui-là : `.head p { margin:0 }`, parce que pandoc enveloppe l'étiquette
  d'usage dans un `<p>` que la feuille canonique n'a pas (même famille que `td p` et `.loc .ln p`).
  **Vérification** : *Bun & Run*, sans qu'une ligne change, est passée de 10 à 8 pages — la valeur
  que le journal attribuait à la composition « à la main ».
- **La conversion de l'aide de jeu.** Le régime `.unit`, les lignes à dire et le contrôle unité par
  unité sont passés dans la chaîne avec *Grand froid* — c'est ce contrôle qui a attrapé la villa
  Moore, qui débordait sur deux pages. Reste à éprouver sur une autre forme d'intrigue : le
  découpage par victime est le seul qu'on ait fait tourner.

## Ce que le régime reflowable change

Le PDF et l'EPUB ne sont pas le même document.

- La **note d'arbitrage** passe sans dommage : ce sont des sections qui coulent.
- L'**aide de jeu** perd sa règle centrale. « Une unité = une page » n'existe pas en reflowable :
  `screen.css` la traduit en « une unité = une section », et `--split-level=2` en fait un chapitre
  d'EPUB. C'est jouable sur une tablette, mais c'est une refonte, pas une conversion.
