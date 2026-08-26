# Le modèle

Les neuf fichiers de ce répertoire **sont** le modèle. Ils ne sont pas chargés par la chaîne de
fabrication : ils sont ce que la chaîne applique, et ce qu'on lit avant d'écrire un document.

```
instructions-projet.md            le déroulé d'une demande, en quatre étapes
MODELE-socle.md                   le socle commun — déroulé, code couleur, charte, chaîne
MODELE-analyse.md                 la grille de lecture et les typologies
MODELE-formes.md                  les chapitres par forme d'intrigue (A → H)
MODELE-systemes.md                les chapitres par jeu
MODELE-livrable-aide-de-jeu.md    le chapitre du livret de table
MODELE-livrable-dossier-prep.md   le chapitre de la note d'arbitrage
MODELE-livrable-annote.md         le chapitre du scénario annoté
JOURNAL-passages.md               le retour d'expérience, scénario par scénario
```

## Ce qui a changé, et pourquoi ce répertoire fait foi

Ces fichiers ont d'abord vécu comme docs d'un projet claude.ai, et ce répertoire n'en était qu'une
copie versionnée : le projet faisait foi, la synchronisation était manuelle, et toute reprise du
modèle devait être reportée à la main. **Ce n'est plus le cas.** Le projet n'est plus utilisé, et
**le dépôt est désormais la seule source**.

Ce que ça simplifie, et il faut en profiter :

1. **plus rien à reporter.** Une règle qui change se modifie ici, une fois, et c'est fait ;
2. **l'historique est réel.** Un `git log` sur `MODELE-socle.md` dit quand une règle est apparue et à
   quel scénario elle répond — ce que le journal raconte en prose mais ne date pas ;
3. **plus de divergence possible** entre deux copies éditées en parallèle. La règle du socle sur la
   relecture avant écriture perd son objet : git gère les conflits, ce que `project_write` ne faisait
   pas.

Ce qui ne change pas : **`modele/` n'est pas du code**. Ne pas le reformater, ne pas le linter, ne
pas y passer d'outil automatique. Et le journal reste le seul endroit où s'écrit le retour
d'expérience — jamais dans le socle.

**Un fichier a changé de statut plus que les autres.** `instructions-projet.md` était le texte à
coller dans les réglages du projet ; il n'a plus de réglages où aller. Il reste ce qu'il a toujours
été sur le fond — le déroulé d'une demande en quatre étapes, qui prime sur le socle — et c'est à ce
titre que `CLAUDE.md` le fait lire en premier.

## Le seul point de contact réel avec la chaîne

`assets/print.css` est la feuille canonique du socle, versionnée, et c'est elle que la chaîne
applique. Le socle en garde une copie dans son texte — **une survivance** : elle servait à produire
des documents hors dépôt, et il n'y en a plus. Tant qu'elle est là, les deux doivent rester
identiques :

```
diff <(sed -n '/^```css/,/^```/p' modele/MODELE-socle.md | sed '1d;$d') assets/print.css
```

La sortie n'est pas vide, et elle ne le sera jamais : `assets/print.css` porte trois écarts assumés,
chacun marqué `/* [dépôt] */` — la police embarquée en `@font-face` (qui entraîne le renommage de la
famille partout où elle est appelée), le pied de page injecté par le build depuis les métadonnées, et
la largeur de tableau neutralisée pour pandoc. **Ce sont les seules divergences admises.** Toute règle
de mise en forme qui apparaît d'un côté sans l'autre est une dérive : la charte visuelle est arrêtée.
**Le plus simple serait de retirer le bloc CSS du socle et d'y renvoyer vers `assets/print.css`** —
cent lignes de moins à tenir en double, et plus aucun risque de dérive. C'est une décision à prendre,
pas un nettoyage à faire en passant.
