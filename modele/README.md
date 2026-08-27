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

## Le point de contact avec la chaîne

`assets/print.css` **est** la charte, et il n'en existe plus de copie. Le socle en portait une, du
temps où des documents se composaient hors dépôt ; elle avait divergé de quatre-vingt-cinq lignes
avant qu'on la retire. Ce que le socle garde à la place, ce sont les **valeurs arrêtées** — corps,
marges, teintes, régimes —, c'est-à-dire ce qui relève d'une décision éditoriale et non d'une
déclaration technique.

La règle qui reste, et elle vaut toujours : **`assets/print.css` ne se modifie pas sans demande
explicite.** Les corps, les couleurs, les marges ont été réglés à l'usage, sur des documents imprimés
et menés en partie. Et surtout pas au nom de la lisibilité à l'écran : `screen.css` et `web.css` sont
là pour ça.
