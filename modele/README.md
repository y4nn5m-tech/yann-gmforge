# Le modèle

Les huit fichiers de ce répertoire sont la **copie versionnée** du modèle. Ils ne sont pas chargés par
la chaîne de fabrication : ils sont ce que la chaîne applique.

```
instructions-projet.md            les instructions du projet claude.ai (à coller dans les réglages)
MODELE-socle.md                   le socle commun — déroulé, code couleur, charte, chaîne
MODELE-analyse.md                 la grille de lecture et les typologies
MODELE-formes.md                  les chapitres par forme d'intrigue (A → H)
MODELE-systemes.md                les chapitres par jeu
MODELE-livrable-aide-de-jeu.md    le chapitre du livret de table
MODELE-livrable-dossier-prep.md   le chapitre de la note d'arbitrage
JOURNAL-passages.md               le retour d'expérience, scénario par scénario
```

## Ce que cette copie n'est pas

**Mettre le modèle dans le dépôt ne le fait pas charger par claude.ai.** Le mécanisme de chargement
reste les **docs du projet** — c'est là que vivent les fichiers de référence, et c'est là qu'il faut
les modifier. Les instructions du projet nomment d'ailleurs des chemins `claude/…`, pas des chemins de
dépôt.

Cette copie sert à trois choses, et à rien d'autre :

1. **l'historique.** Un `git log` sur `MODELE-socle.md` dit quand une règle est apparue, et à quel
   scénario elle répond — ce que le journal raconte en prose mais ne date pas ;
2. **le diff.** Avant de réécrire un fichier du modèle, comparer la version du dépôt à la version du
   projet montre ce qui a bougé depuis la dernière fois ;
3. **la sauvegarde.** Un doc de projet supprimé par erreur se retrouve ici.

## La synchronisation est manuelle

Rien ne recopie automatiquement dans un sens ou dans l'autre. La règle :

- **le projet fait foi**, toujours. C'est lui que Claude lit en séance ;
- après une conversation qui a modifié le modèle, **reporter les fichiers touchés ici** et committer,
  en nommant le scénario qui a provoqué le changement ;
- ne jamais éditer un fichier ici en espérant que le projet suive.

Le socle porte déjà la règle qui va avec, et elle vaut aussi entre les deux copies : **toujours relire
un fichier juste avant de l'écrire**, parce que l'écriture remplace le fichier entier sans fusion.

## Le seul point de contact réel avec la chaîne

`assets/print.css` est la feuille canonique du socle, versionnée. Le socle en garde une copie dans son
texte tant que des documents sont produits hors dépôt, et **les deux doivent rester identiques** :

```
diff <(sed -n '/^```css/,/^```/p' modele/MODELE-socle.md | sed '1d;$d') assets/print.css
```

La sortie n'est pas vide, et elle ne le sera jamais : `assets/print.css` porte trois écarts assumés,
chacun marqué `/* [dépôt] */` — la police embarquée en `@font-face` (qui entraîne le renommage de la
famille partout où elle est appelée), le pied de page injecté par le build depuis les métadonnées, et
la largeur de tableau neutralisée pour pandoc. **Ce sont les seules divergences admises.** Toute règle
de mise en forme qui apparaît d'un côté sans l'autre est une dérive : la charte visuelle est arrêtée,
et un document produit hors dépôt doit sortir identique à un document produit par la chaîne.
