# Socle commun — à charger toujours

Recette d'application des instructions du projet. **Les instructions du projet priment.**
Ce fichier contient ce qui vaut pour **les deux livrables**, tout scénario et tout système.

## Déroulé d'une conversation

Une conversation de ce projet suit toujours le même ordre. Ne pas sauter d'étape.

1. **Le scénario d'abord.** Une conversation commence par la livraison d'un scénario — PDF, texte,
   peu importe la forme. **S'il n'y en a pas, le demander avant toute chose** et ne rien produire
   d'ici là.
2. **L'analyse, en conversation seulement.** Dépouiller le scénario en profondeur — structure, formes,
   scènes, lieux, PNJ, événements, contexte, mécaniques, zones floues — et **répondre en conversation,
   sans produire aucun document**. La grille de lecture est dans `modele/MODELE-analyse.md`.
3. **Demander le livrable.** Aide de jeu · **note d'arbitrage** (le « dossier de préparation » des
   instructions) · **scénario annoté**, qui remplace la note quand la source est en prose dense · ou
   plusieurs. **Ne jamais deviner.**
4. **Produire.** Si plusieurs sont demandés, **ce qui se lit avant vient d'abord** — la note ou
   l'annoté —, parce que ses arbitrages déterminent le découpage du livret.

L'analyse de l'étape 2 ne se réécrit pas dans les livrables : elle sert à décider le découpage en
unités, à trier les arbitrages, et à mesurer ce que la note aura à dire. Elle reste dans la
conversation — **à une exception près, et elle a coûté cher à découvrir** : ce que l'analyse établit
sur la **forme** du scénario ne survit nulle part. Trois semaines plus tard, la conversation a
disparu, et il reste une note qui s'ouvre sur « A1 » sans avoir dit de quoi elle parle. C'est
l'**explication de texte** en tête de note qui recueille cette part-là — voir son chapitre.

## Les deux livrables

Le projet produit deux documents distincts, qui ne se remplacent pas.

| Livrable | À quoi il sert | Quand on l'ouvre | Chapitre |
|---|---|---|---|
| **Aide de jeu** | Mener la partie. Un point de consultation par page, la matière pour *dire* le scénario. | Pendant la séance, le doigt sur la page. | `modele/MODELE-livrable-aide-de-jeu.md` |
| **Note d'arbitrage** | Trancher ce que la source ne tranche pas, rassembler ce qu'elle éparpille, croiser ce qu'elle n'a pas croisé. **Huit à douze pages.** | Une fois, avant la séance, **à côté du scénario**. | `modele/MODELE-livrable-dossier-prep.md` |
| **Scénario annoté** | La source ramenée à son ossature, dans son ordre, avec ce qu'elle ne dit pas. **Il absorbe la note.** | Plusieurs fois avant la séance, **à la place du scénario**. | `modele/MODELE-livrable-annote.md` |

**La frontière n'a pas deux côtés, mais trois : la source, le livret, la note.** Le MJ a le scénario
sous les yeux — c'est le premier destinataire de tout ce qu'on n'écrit pas. Ce qui reste se répartit
ensuite par le moment : ce qui se consulte *pendant* va au livret, ce qui se lit *avant* va à la note.

Conséquence à assumer, et c'est la correction la plus utile du modèle : **la plupart de ce qu'on retire
de l'aide de jeu ne va pas dans la note — ça retourne à la source, qui l'avait déjà.** Le tableau des
trois destinations est dans le chapitre de la note. Corollaire de volume : produire les deux ne fait pas
deux gros documents. Le livret rétrécit parce que ce qui se lit avant en sort ; la note reste courte
parce que ce qui est dans la source n'y entre pas.

## Avant de rédiger — charger aussi

| Fichier | Quand |
|---|---|
| `modele/MODELE-analyse.md` | **Toujours, et en premier** : la grille de lecture et les typologies servent dès l'étape 2, avant de savoir quel livrable est demandé. |
| `modele/MODELE-livrable-aide-de-jeu.md` | Si l'aide de jeu est demandée. |
| `modele/MODELE-livrable-dossier-prep.md` | Si la note d'arbitrage est demandée. |
| `modele/MODELE-livrable-annote.md` | Si le scénario annoté est demandé. **Le mesurer d'abord** : sur une source déjà écrite en mots-clés, il n'apporte rien. |
| `modele/MODELE-formes.md` | Toujours, pour les deux livrables. Lire le ou les chapitres correspondant à la forme du scénario. **Un scénario cumule souvent plusieurs formes.** |
| `modele/MODELE-systemes.md` | Toujours, pour les deux livrables. Lire le chapitre du système joué. |
| `modele/JOURNAL-passages.md` | Seulement pour auditer l'historique. Aucune utilité au moment de rédiger. |

Si la forme ou le système n'a pas encore de chapitre : rédiger avec le socle seul, puis **créer le
chapitre** à partir de ce que le scénario a appris.

## Code couleur — commun aux deux livrables

Les quatre catégories viennent des instructions du projet. Une cinquième, l'ambre, est une couleur de
service propre à la note d'arbitrage.

| Catégorie | Classe | Teinte | Usage |
|---|---|---|---|
| Description / à dire aux joueurs | `.dire` | bleu `#1f6fa8` | Décors, sons, odeurs, apparences, témoignages, répliques |
| Mécanismes de jeu | `.jeu` | vert `#2e7d43` | Tests, difficultés, dégâts, durées, minuteurs |
| Informations MJ uniquement | `.mj` | rouge `#b3271e` | La vérité, les intentions cachées, les mensonges des PNJ |
| Pilotage de scène | `.obj` | violet `#6a4bb0` | Objectif visé, leviers à actionner sur les joueurs |
| Arbitrages *(note)* | `.warn` | ambre `#c9a227` | Incohérences et lacunes de la source, à trancher avant de jouer |

Chaque bloc porte une **étiquette en petites capitales** qui dit à quoi il sert : « Ambiance — à
piocher », « Interroger — Bagou », « La vérité du trou », « Objectif de la scène ». L'étiquette est ce
qui rend le document navigable ; ne jamais l'omettre.

Un même paragraphe (PNJ, lieu, scène, événement) enchaîne librement plusieurs blocs de couleurs
différentes.

**Le poids relatif des cinq couleurs n'est pas fixe : il dépend du système.** Dans la plupart des jeux,
le violet est le bloc le plus court d'une unité. Dans un jeu où l'échec d'un joueur oblige le MJ à
agir — PbtA et sa famille —, le violet devient le bloc **le plus long et le plus utile**, parce que
c'est lui qui porte la réserve de conséquences. Vérifier ce point dans le chapitre du système avant de
doser les blocs.

## Règles de fond communes

- **Ne jamais reformuler en prose ce que la source donne déjà en mots-clés** — le recopier tel quel.
- **Un document ne se commente pas lui-même.** Ni encart « mode d'emploi », ni tableau qui explique ses
  propres étiquettes, ni « règle de ce document », ni note sur la version de la source, ni
  justification de la méthode. Si une règle d'écriture mérite d'être connue, elle est **dans le
  modèle**, pas dans le livrable : le MJ connaît sa façon de travailler, le document l'applique au lieu
  de la décrire.
  **Seule exception : la légende des couleurs**, parce qu'elle porte une consigne opérationnelle
  (« ne jamais lire le rouge à voix haute »). Une table de routage qui dit *quand* on ouvre chaque
  partie est admise dans la note : elle route, elle n'explique pas.
  *Il a fallu trois occurrences pour dégager ce principe — l'encart « mode d'emploi » de Grand froid,
  le tableau des étiquettes de Bun & Run v1, puis les encarts « règle du document » et « version de la
  source » de la note d'arbitrage. Chaque fois, la même correction.*
- **Ne jamais découper une description par les sens.** Ni « ce qu'on voit / ce qu'on entend / ce qu'on
  sent », ni aucune variante : personne ne présente un lieu en énumérant d'abord tout ce qui s'y voit,
  puis tout ce qui s'y entend. Un MJ qui lit un document rangé ainsi le récite dans cet ordre, et la
  scène meurt.
  **Une description se construit par paliers de distance, du plan large au détail à portée de main**,
  et les sens s'intercalent au palier où ils se perçoivent : une odeur qui porte loin au palier
  lointain, un grain de surface ou une chaleur sur la peau au palier proche. Le dernier palier se
  termine **à hauteur d'homme** — quelque chose qu'un PJ pourrait toucher, ou quelqu'un qui le regarde :
  c'est ce qui donne aux joueurs l'envie de parler. Vaut pour les deux livrables ; la forme concrète
  (titres de paliers, nombre de lignes) est dans le chapitre de l'aide de jeu.
- **Les fiches de personnage couvrent la description des PJ.** Ni portrait physique, ni
  caractéristiques, ni équipement dans nos documents. Ce qui nous concerne, c'est ce que le
  *scénario* donne au PJ : son accroche du jour, ce qu'il sait que les autres ignorent, ses liens
  avec le groupe.
- **Quand le scénario fournit des prétirés, croiser chaque trait avec les scènes.** Les fiches disent
  ce qu'un personnage sait faire ; elles ne disent jamais *où* ça tombe. C'est notre travail : pour
  chaque atout, chaque formation et chaque point faible, **nommer la scène qui le déclenche**, et dire
  au MJ de l'annoncer au joueur **au moment exact** — un point faible signalé une réplique trop tard ne
  produit rien. C'est souvent le meilleur contenu de la note, parce que les auteurs écrivent les fiches
  et les scènes séparément : les rencontres qu'ils n'ont pas vues sont là, et elles sont gratuites.
  Recopier les traits **verbatim**, avec leur nom exact — c'est ce nom que le joueur cherchera sur sa
  fiche. Et **compter combien de croisements la source a faits elle-même** : c'est la mesure directe de
  ce que ce travail va rapporter.
- **Quand il n'y a pas de prétirés, les questions d'ouverture sont la fiche.** Beaucoup de jeux — toute
  la famille PbtA, et de plus en plus d'autres — ouvrent la partie en posant une question à chaque
  personnage : « avec quel autre PJ voyages-tu, et de quoi vous disputiez-vous juste avant ? », « quelle
  arme as-tu prise et pourquoi celle-là ? », « quel détail macabre t'a fait comprendre que vous n'êtes
  pas les premiers ici ? ». Chaque réponse **crée un fait** de la fiction, et le travail est exactement
  celui de la règle précédente : **nommer, pour chaque question, la zone ou la scène où sa réponse se
  paie**. Recopier la question verbatim, la faire suivre de son point de chute. Une question sans point
  de chute est une question décorative — et les auteurs n'en écrivent presque jamais le point de chute
  eux-mêmes.
- **Ne pas mélanger, sur une même page, ce qui concerne le groupe et ce qui concerne un personnage.**
  L'accroche collective, le savoir partagé et le décor appartiennent à la scène ; l'accroche
  individuelle appartient au personnage. Une page qui empile les deux devient illisible au moment
  précis où l'on en a besoin.
- **Relever les contradictions de la source plutôt que les lisser** : soit les arbitrer, soit les
  transformer en indice. Elles vont dans la note en bloc ambre, **numérotées**, et dans l'aide de jeu en
  une ligne sur la page concernée, rappelée par son numéro.
- **Un arbitrage a un niveau, et le niveau dit quoi faire.** Bloquant (à trancher avant, sinon ça casse
  à table) · de table (à trancher **et à prononcer**, à un moment précis) · cosmétique (corrigé en
  silence). Une liste plate donne le même poids à « sans ce PNJ le scénario s'arrête » et à « ce nom est
  mal orthographié dans sa seule occurrence ». Seuls les deux premiers niveaux méritent une ligne dans
  l'aide de jeu ; le troisième ne mérite rien.
- **Signaler les incohérences de notation** : un scénario qui donne certains profils en valeurs brutes
  et d'autres en modificateurs se corrige avant la partie, pas en pleine bagarre.
- **Signaler tout profil d'adversaire qui ne se lit pas comme un profil de combat.** Quatre cas, et il
  faut les traiter tous les quatre. **Les trois premiers poussent à fournir des chiffres, le quatrième
  les interdit** : commencer par identifier lequel s'applique, et la réponse est dans le chapitre du
  système, pas dans le scénario.
  - **sans aucun chiffre**, quand c'est volontaire : donner la liste des jets qui remplacent le
    profil, pour que le MJ ne cherche pas des PV qui n'existent pas ;
  - **chiffré mais sans attaque** : PV et armure renseignés, aucune ligne de dégâts — parce que la
    créature n'agit que par des jets subis par les PJ (possession, dévitalisation, terreur, gel). Le
    piège est de lire ce profil comme un profil de mêlée et d'attendre une attaque qui ne viendra
    jamais. Écrire noir sur blanc **« ne frappe jamais »**, et lister ce qu'elle fait à la place ;
  - **absent par oubli**, ce qui n'est pas la même chose qu'absent par choix. Le signe qui ne trompe
    pas : le scénario **chiffre ses seconds couteaux et oublie son antagoniste principal**, alors que
    celui-ci est armé et que le texte propose lui-même l'affrontement comme issue. C'est une lacune.
    Dans ce cas, **fournir un profil de substitution** — calibré sur les profils que la source donne
    par ailleurs, pour ne pas déséquilibrer sa propre échelle — et le signaler explicitement comme le
    nôtre. L'accompagner de la liste des jets qui le remplacent tant qu'on ne se bat pas ;
  - **inexistant par construction** : certains systèmes ne chiffrent **aucun** adversaire — ni PV, ni
    armure, ni dégâts, ni défense — et le MJ n'y lance jamais de dé. L'adversaire est un paquet de
    fiction : des **étiquettes**, un **instinct** en une ligne, une **liste de manœuvres**. **Ne pas
    fournir de profil de substitution** : ce serait un corps étranger, que le MJ chercherait en vain
    dans ses règles. Ce qu'on écrit à la place, c'est exactement ces trois choses, plus la
    signification mécanique des étiquettes.
- **Signaler les risques de blocage** : « sans ce PNJ, les joueurs ignoreront le point faible ». Noir
  sur blanc, à l'endroit concerné. Méthode de repérage : la **règle des trois indices**, dans
  `MODELE-analyse.md`.
- **Faire d'avance l'arithmétique de l'antagoniste** : si sa puissance dépend des événements, donner
  le calcul et l'enjeu.

---

# Charte visuelle — à appliquer sans variation

**Tous les documents du projet doivent être visuellement interchangeables.** Aucune adaptation de la
palette au thème du scénario : pas de bleu glacé pour un scénario d'hiver, pas d'ocre pour un
scénario désertique. Un seul habillage, pour que la collection se reconnaisse et que le MJ retrouve
ses repères d'un document à l'autre.

Ce qui change d'un document à l'autre : le titre, le sous-titre de couverture, le texte du pied de
page. Rien d'autre.

**Une seule feuille de style pour les trois livrables**, avec deux régimes de mise en page :
l'aide de jeu utilise `.unit` (une unité = une page) ; la note **et le scénario annoté** utilisent
`h2.sec` et `.card` (sections qui coulent librement sur plusieurs pages).

## La feuille de style

**Elle vit dans `assets/print.css`, versionnée, et nulle part ailleurs.**

Ce fichier était recopié ici en entier, du temps où des documents se composaient hors dépôt. Il n'y en
a plus. La copie a survécu à sa raison d'être, et elle a fait ce que font toutes les duplications :
elle a divergé. **Quatre-vingt-cinq lignes d'écart au moment où on l'a retirée**, alors que le modèle
en annonçait trois — dont les calages pandoc (`.head p`, les marges de `p` et `ul` dans les blocs) et
l'ajout de `strong` à côté de `b`, sans lesquels un document composé d'après le socle sortait
différent de ceux du dépôt.

Ce qui reste ici, c'est ce qui relève d'une **décision éditoriale** et non d'une déclaration technique.
Ces valeurs ont été réglées à l'usage, sur des documents imprimés et menés en partie : les changer est
une décision, pas un réglage.

| Ce qui est arrêté | Valeur |
|---|---|
| Format et marges | A4, 12 mm de marge, 13 mm en pied |
| Corps du texte | **8,6 pt**, interligne 1,34 |
| Tableaux | 7,8 pt · en régime `.tight`, **7,2 pt** |
| Titre de couverture · titre d'unité · titre de section | 31 pt · 16 pt · 13 pt |
| Étiquette d'un bloc coloré | 6,3 pt, petites capitales, `letter-spacing` 1 pt |
| Les cinq teintes | voir le tableau du code couleur, plus haut |
| Étiquettes d'usage | `À DIRE` ardoise · `À LIRE AVANT` **ambre** · `À CONSULTER` **violet** |
| Les deux régimes | `.unit { break-before: page }` pour le livret · `h2.sec` et `.card` pour ce qui coule |

**Aucune adaptation de la palette au thème du scénario**, et aucune règle de mise en forme qui
n'existerait que d'un côté : la charte est identique pour les trois livrables, et c'est ce qui fait
qu'on les reconnaît.

## Chaîne de production

HTML + CSS → **WeasyPrint** (`pip install weasyprint --break-system-packages`).

Écrire le document en plusieurs fichiers fragments si nécessaire, puis concaténer : le premier porte
`<!DOCTYPE html>`, la balise `<style>` et `<body>` ; le dernier ferme `</body></html>`.
**Vérifier que le fragment de tête contient bien `</body>` avant de faire un `replace` dessus** — sinon
la concaténation avale silencieusement la suite du document. Mieux : **assertions dans le script de
concaténation** — présence du doctype dans le premier fragment, absence dans les suivants, fermeture
correcte à la fin.

**Découper en fragments dès le départ, un par section ou par groupe d'unités.** Les retouches
demandées après lecture portent presque toujours sur une seule partie du document ; un fichier unique
oblige à le réécrire en entier, avec le risque d'y introduire des écarts.

**Pièges de rendu, tous vérifiés au moins une fois :**

- un tableau **sans** `table-layout: fixed`, ou avec une largeur manquante sur une colonne, peut voir
  cette colonne réduite à 16 mm : les cellules deviennent des colonnes de mots et le tableau triple
  de hauteur. Invisible dans le HTML, visible seulement au rendu ;
- `break-inside: avoid` sur une `.card` longue produit des pages à moitié vides. Le réserver aux
  blocs colorés ;
- appliquer les propriétés de bloc directement aux classes `.dire/.jeu/.mj/.obj/.warn`, jamais via une
  classe utilitaire qu'on oublie d'ajouter sur la moitié des blocs.

**Mesurer le remplissage des pages plutôt que de les regarder une par une.** Parcourir l'arbre de boîtes
de WeasyPrint, relever le bas de la dernière `LineBox` de chaque page **en excluant les boîtes de marge**
(sinon le pied de page fausse toutes les mesures), et signaler les pages remplies à moins de 62 %. Puis
distinguer les fins de section (normales) du reste. C'est le contrôle qui trouve les trous que l'œil
laisse passer.

**Contrôle avant livraison :** rasteriser quelques pages (`pdftoppm -png -r 55 doc.pdf p`) et les
regarder. Pour l'aide de jeu, le contrôle unité par unité est en plus **obligatoire** — script dans
son chapitre.

**Ne jamais renvoyer à un numéro de page dans le corps du texte.** La pagination bouge à chaque
recompilation, et un « voir page 20 » devient faux sans qu'on s'en aperçoive. Renvoyer au **numéro de
section** ou au **repère de l'élément** (« voir l'arbitrage A6 ») : cela survit à toutes les révisions.

## Entretien du modèle

Le retour d'expérience s'écrit dans **`modele/JOURNAL-passages.md`** — jamais ailleurs.

Ensuite, et seulement si c'est généralisable, promouvoir la leçon dans le bon fichier :

- **valable pour les deux livrables, tout scénario, tout système** → ici, dans le socle ;
- **valable pour un livrable** → son chapitre `MODELE-livrable-*.md` ;
- **valable pour une forme d'intrigue** → `MODELE-formes.md` ;
- **valable pour un système** → `MODELE-systemes.md` ;
- **un type de PNJ, de scène, de lieu ou d'événement jamais rencontré** → `MODELE-analyse.md`, avec sa
  colonne « vu dans ». Jamais de type sans occurrence réelle ;
- **anecdotique** → elle reste dans le journal, et nulle part ailleurs.

Signe qu'une règle est mal rangée : elle commence par « quand le scénario… », « si le système… » ou
« dans l'aide de jeu… ». Un conditionnel dans le socle est une règle qui appartient à un chapitre.
Cas fréquent et légitime : le socle énonce le **principe** (« ne pas découper une description par les
sens »), le chapitre du livrable en donne la **forme** (titres de paliers, nombre de lignes, balises).

**Se méfier des définitions, pas seulement des règles.** Deux corrections majeures du modèle sont
venues non d'une règle fausse mais d'une **phrase de définition** : « le document doit servir à préparer
la partie » (corrigé en *mener*, après Grand froid) et « la note doit être complète, c'est le seul
document qui permet de répondre à une question imprévue » (corrigé en *complément de la source*, après
le second passage de Bun & Run). Une définition trop généreuse produit des dizaines de pages inutiles
sans qu'aucune règle particulière soit enfreinte. Quand un livrable devient lourd, relire d'abord sa
définition.

**Toujours relire un fichier du modèle juste avant de l'écrire.** La raison d'origine a disparu — le
modèle vivait en double, et deux conversations qui l'éditaient en parallèle s'écrasaient en silence ;
il n'existe plus qu'en un seul endroit, versionné. La règle tient pour une autre raison, plus banale
et plus fréquente : **une règle qu'on croit se rappeler a presque toujours bougé depuis**, et on
réécrit alors une version antérieure par-dessus la bonne.
