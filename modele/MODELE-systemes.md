# Systèmes — chapitres à charger selon le jeu

Complète `modele/MODELE-socle.md`, qui prime. **Sert aux deux livrables.**
Ce fichier ne contient que ce qui change **la façon d'écrire les mécaniques** : le vocabulaire, le
format des profils, les sous-systèmes qu'un scénario suppose connus.

## Règle qui vaut pour tous les systèmes

**Ne jamais importer une convention d'un système dans un autre.** Écrire les tests avec les mots
exacts du jeu joué : un MJ qui lit « Sauvegarde » dans une partie de Chroniques Oubliées s'arrête
pour traduire, en pleine scène.

**Distinguer la règle du système de la règle maison du scénario.** Un scénario du commerce remanie
souvent les règles pour ses besoins : ce remaniement ne vaut que pour lui. Le noter comme tel, et ne
pas le promouvoir en règle générale. Dans le dossier de préparation, le recopier intégralement en
bloc vert et le signaler comme règle maison ; dans l'aide de jeu, n'en garder que ce qui sert en jeu.
*Cas vécu : les paliers « échec / réussite simple / réussite excellente » de « Pour quelques clous »
étaient une règle maison de ce scénario, pas une règle de Cthulhu Hack. Repris par erreur comme
convention du modèle, ils ne s'appliquaient plus au scénario suivant.*

**Vérifier la cohérence entre les fiches de prétirés et les profils de PNJ.** Les deux sont souvent
rédigés par des mains différentes, à des moments différents. La même arme peut y avoir deux valeurs de
dégâts, la même protection deux effets. Harmoniser sur les fiches — elles sont plus nombreuses et ce
sont elles qui seront sur la table — et l'annoncer avant le premier tir.

---

## Transposer un scénario écrit pour un autre système

La règle ci-dessus interdit d'importer une convention d'un système dans un autre. Elle ne dit pas quoi
faire quand **la source entière est dans l'autre système** — un scénario de L'Appel de Cthulhu qu'on
veut mener en Cthulhu Hack, un module D&D qu'on veut mener en Shadowdark. C'est le même principe poussé
à son terme : **on ne traduit pas, on reconstruit.** Le document livré ne doit garder **aucune trace**
du système d'origine — ni un pourcentage, ni un nom de compétence, ni une valeur de dégâts. Un seul
« Discrétion 55 % » survivant dans un livret arrête le MJ en pleine scène, exactement comme une
« Sauvegarde » dans une partie de Chroniques Oubliées.

*Section née de « L'Or de La Rochelle » (L'Appel de Cthulhu → Cthulhu Hack).*

### 1. Chercher d'abord les équivalents exacts — il y en a toujours

Avant de convertir quoi que ce soit, **lire les règles maison de la source**. Elles tombent souvent pile
sur une mécanique du jeu cible et se transposent alors sans rien perdre. C'est le travail le moins cher,
et il faut le faire en premier parce qu'il réduit ce qu'il restera à arbitrer.

*Cas vécu, dans* L'Or de La Rochelle *: les « traits de personnalité » qui font lancer 2d100 et garder
le meilleur **sont** l'Avantage, mot pour mot ; les cinq d6 posés sur la table dont on retire chaque 6
**sont** un compte à rebours (livre de base, pp. 31-32). Deux des trois règles maison du scénario n'ont
demandé aucun arbitrage.*

### 2. La première question n'est pas « quelle Sauvegarde ? » mais « y a-t-il un jet ? »

C'est l'erreur qui coûte le plus cher, et elle est invisible. Un système à compétences chiffrées écrit
**un test par obstacle**, parce que c'est sa façon de décrire un obstacle. Converti ligne à ligne, cela
produit une partie où l'on jette dix fois par scène dans un jeu qui en demande deux.

Règle : **un obstacle de la source devient un jet seulement si la source y attache une conséquence
d'échec.** Sinon il devient de la fiction, et le personnage réussit.

*Cas vécu : l'acte 1 de* L'Or de La Rochelle *aligne quatre « défis » — convaincre le garde, tenir sa
couverture devant le lieutenant, traverser un kilomètre à découvert, convaincre les tunneliers.
**Aucun des quatre n'a de conséquence d'échec écrite.** Transposés en quatre Sauvegardes, ils font une
heure de dés pour rien.*

### 3. Trois destinations pour une compétence chiffrée, et le test qui les sépare

Une compétence en pourcentage ne devient pas mécaniquement un jet. Elle a trois destinations, et
**la plus fréquente est la troisième** :

- **une Sauvegarde** — quand c'est le corps ou la volonté du personnage qui décide, une fois, avec un
  échec qui coûte ;
- **un dé d'usage** — quand c'est une **ressource qui s'épuise**, c'est-à-dire quand le scénario fait
  tester la même chose plusieurs fois de suite. Chercher, repérer, se remémorer → Torche. Convaincre,
  baratiner, intimider dans la durée → Bagou ;
- **rien du tout, et c'est un fait de fiche** — quand la compétence dit ce que le personnage **sait** :
  Latin, Histoire, Bibliothèque, Médecine, Navigation, Occultisme. Le personnage sait, on ne jette pas.

Le test tient en une question : **la compétence dit-elle ce que le personnage sait, ou ce qu'il
tente ?** Sait → fait de fiche. Tente une fois → Sauvegarde. Tente plusieurs fois sur la durée → dé
d'usage.

**Le tri se double d'un second, sur les indices, et c'est lui qui décide du rythme d'une enquête** :
un **indice essentiel** — celui sans lequel la suite est injouable — **s'obtient automatiquement**, par
la profession du personnage ou par le simple fait qu'il soit sur place. On ne le fait jamais dépendre
d'un jet. Un **indice périphérique** se gagne sur une action décrite par le joueur, et c'est là que
tombent les dés d'usage : Torche pour ce qui se cherche dans le monde physique, Bagou pour ce qui
s'obtient de quelqu'un. Un scénario en pourcentages ignore cette distinction — il met un seuil partout,
y compris devant sa propre conclusion.

Corollaire : **une règle maison qui donne la même compétence à tout le monde est un fait de fiche
déguisé.** *La « compétence de Métier à 65 % » de* L'Or de La Rochelle *ne devient pas un jet : elle
devient la ligne « ce que ce personnage fait sans jeter ». Le scénario y gagne.*

### 4. Les profils d'adversaires ne se convertissent pas : ils se recalculent

C'est le piège le plus dangereux, parce que les Points de Vie portent le même nom dans les deux jeux et
invitent à la recopie. Ils ne mesurent pas la même chose : ce qui compte n'est pas le nombre, c'est
**combien de Moments le combat va durer**.

Méthode, dans cet ordre :

1. **chiffrer le débit du groupe réel** — la somme des dégâts que les PJ infligent par Moment, armure
   déduite. Le faire sur les fiches, jamais de mémoire ;
2. **décider combien de Moments le combat doit durer** — c'est une décision de pilotage, pas un calcul ;
3. **fixer les PV à partir des deux.** Le nombre de la source n'entre jamais dans l'opération.

Une heuristique donne le point de départ, jamais le résultat : **un profil au-delà de 20 PV se divise
par deux**, et l'on vérifie ensuite par les trois étapes ci-dessus. Les humains de Cthulhu Hack tiennent
**10 à 20 PV**, ce qui est aussi le plafond d'un adversaire ordinaire.

Repères attestés dans ce dépôt : un PJ de Cthulhu Hack tient **10 à 13 PV** ; un groupe mal armé inflige
**environ 2 PV par Moment** (*Grand froid*, cinq détectives dont un à mains nues — c'est un plancher,
pas une moyenne) ; un adversaire de fin de scénario est à **26 PV et 3 d'armure** (la Couleur) ou
**60 PV en deux phases** (le Wendigo).

*Cas vécu : les Abîmes de Khéopsie sont données à 30 Points de Vie. Recopiées, elles deviennent chacune
l'équivalent d'un adversaire de fin de scénario — alors que la source les fait apparaître **en groupe**
et à répétition. Un profil recopié transforme une créature de meute en climax. L'heuristique les met à
15 ; c'est le débit réel du groupe qui dit si ce chiffre tient.*

**Les dégâts se calent sur une échelle fixe, arme par arme, et non sur les dés de la source.** Un pistolet
inflige un dé standard ; tout le reste se range autour. Une source qui écrit `3D4` a chiffré pour une
autre courbe de probabilités, et reporter ses dés déséquilibre l'échelle du jeu cible sans qu'on le voie.

### 5. Ce qui n'a pas d'équivalent se refond ou se coupe — jamais ne se porte

Une règle sans équivalent laissée telle quelle est une règle que le MJ cherchera dans son livre de base
et n'y trouvera pas. Deux issues, et il faut **en choisir une** :

- **la refondre** dans une ressource existante du jeu cible, et la signaler comme notre règle maison ;
- **la couper**, et dire ce qui la remplace.

*Cas vécu : le « Golpe de la Fortuna » — sacrifier 1d6 points de Santé mentale pour tester la compétence
Chance. Cthulhu Hack n'a ni Chance ni points de Santé mentale. Refonte retenue : **dépenser un cran de
Santé mentale pour qu'un coup du sort intervienne**, une fois par personnage et par partie. La mécanique
d'origine — payer sa raison pour acheter un miracle — est intacte ; ses deux chiffres ont disparu.*

### 6. La Santé mentale : convertir la gradation en fréquence, jamais en ampleur

Un total de points et un dé d'usage ne sont pas des grandeurs comparables : le total disparaît, et **ce
qui compte n'est plus la taille d'une perte mais le nombre de tests**. Une source qui gradue ses
horreurs en `1d4 SAN` et `1d8 SAN` a écrit une gradation réelle qu'il ne faut pas perdre — mais elle se
reporte sur la **fréquence**, pas sur l'ampleur.

Correspondance retenue : une vision unique = **un test** · une horreur majeure = **un test à
Désavantage** · une exposition continue = **un test par étape**. Jamais « plus de dégâts » : un dé
d'usage n'en inflige pas.

### 7. La table — L'Appel de Cthulhu (BRP) → Cthulhu Hack

| Source (BRP) | Cthulhu Hack | Comment |
|---|---|---|
| Caractéristique | **Sauvegarde, bornée 8-15** | Deux éditions, deux chemins, le même chiffre. Sur l'échelle **3-18** (6ᵉ éd., celle de cette source) : **recopier** — BRP teste à `car × 5` sur d100, CH réussit `N × 5 %` en lançant 1d20 sous N, donc Force 13 = 65 % des deux côtés. En **pourcentages** (7ᵉ éd.) : **diviser par 5**. Puis plafonner |
| Taille · Éducation | **rien** | Aucun équivalent. Éducation devient un fait de fiche |
| Apparence | fondue dans **Charisme** | |
| Pouvoir | fondu dans **Sagesse** | |
| Compétence en % | Sauvegarde · dé d'usage · **fait de fiche** | Le test du §3. Ne jamais convertir le pourcentage lui-même |
| Compétence de métier | **fait de fiche** | |
| Points de Vie | **recalculés** | §4. Ne jamais recopier le nombre |
| Dégâts `3D4`, `1D6` | **échelle fixe du jeu cible** | Recalibrés arme par arme sur le débit du groupe, jamais transposés |
| Attaque à `55 %` | **malus au toucher** | Le pourcentage disparaît |
| SAN en points · `1d4` / `1d8` | dé de **Santé mentale** | §6 : la gradation devient une fréquence |
| Compétence Chance | **rien** | Refondre ou couper — §5 |
| Bonus et malus en % | **Avantage / Désavantage** | Le seul modificateur du jeu cible |

**Plafonner, toujours — la conversion donne l'ordre de grandeur, pas l'échelle.** Les Sauvegardes de
Cthulhu Hack tiennent entre **8 et 15** : 11-12 pour un personnage moyen, 14-15 pour un point fort. Une
conversion fidèle sort régulièrement au-dessus, et il faut l'y ramener — une Sauvegarde à 18 réussit
neuf fois sur dix, ce qui retire au jeu son seul levier de tension.
*Cas vécu : les prétirés de* L'Or de La Rochelle *portent Force 18 et Éducation 20 — la seconde hors même
de l'échelle 3-18 que la source utilise partout ailleurs. Éducation et Taille n'ayant pas de Sauvegarde,
seule la Force pose question : elle descend à 15.*

**Et n'autoriser qu'un seul plafond par personnage.** Tronquer à 15 aplatit le haut de la fiche : une
source qui donne 18, 16 et 15 produit trois Sauvegardes identiques, et le personnage devient infaillible
dans tout un registre. Règle : **la plus haute caractéristique passe à 15, toutes les autres sont
plafonnées à 14**, leur ordre d'origine étant conservé. Chaque personnage garde ainsi exactement une
Sauvegarde qui le définit. *Cas vécu : Montfaucon — Force 18, Constitution 16, Dextérité 15 — sortait à
15/15/15 ; il sort à 15/14/14, reste le corps du groupe et cesse d'être imbattable.*

**Un écart extrême ne se convertit pas en petit dé, mais en Désavantage.** Une compétence sociale à 20 %
donnerait un Bagou d4, c'est-à-dire une ressource épuisée en deux jets — le personnage perd son dé au
lieu d'être mauvais avec. Plancher à **d6**, et porter la faiblesse en **Désavantage permanent** sur ce
dé. *Cas vécu : Montfaucon, Négocier 20 %, garde un Bagou d6 qu'il lance à Désavantage.*

### 8. Ordre de travail, et le contrôle qui termine

1. relever les **règles maison** de la source et leurs équivalents exacts (§1) ;
2. lister **tous les jets** que la source demande, et couper ceux qui n'ont pas de conséquence
   d'échec (§2) ;
3. trier les **compétences** en trois tas (§3) ;
4. chiffrer le **débit du groupe**, puis les profils (§4) ;
5. traiter les **orphelines** — refonte ou coupe, jamais report (§5) ;
6. reporter la **gradation d'horreur** en fréquence (§6) ;
7. **relire le document en cherchant `%`, les noms de compétences de la source et ses dés d'origine.**
   Il ne doit rien en rester. C'est le seul contrôle mécanique de cette section, et il attrape ce que
   la relecture laisse passer.

---

## Cthulhu Hack

- **Résolution** : « Sauvegarde de <caractéristique> » — Force, Dextérité, Constitution, Sagesse,
  Intelligence, Charisme. Binaire : réussie ou ratée. Pas de paliers, sauf règle maison du scénario.
- **Dés d'usage** : « test de Torche » (repérer, se remémorer, chercher) et « test de Bagou »
  (contraindre, socialiser, intimider). Plus « Santé mentale » pour l'horreur.
- **Avantage / Désavantage**, y compris **double désavantage** dans certains scénarios.
- **Unité de temps du combat** : le **Moment**.
- **Compte à rebours** : mécanique du livre de base (pp. 31-32). Excellent support de minuteur — voir
  le chapitre C de `MODELE-formes.md`.
- **Format d'un profil** : Dés de Vie · Points de Vie · Points d'Armure · Malus au toucher ·
  attaques et dégâts · capacités spéciales.
- **Ressource de dégâts** : les Dés de Vie servent de réserve ; un scénario peut ajouter des règles de
  blessures légères qui dégradent le DVie d'un cran.
- **Usure permanente** : un scénario d'horreur cosmique fait perdre, en plus des PV, des **points de
  Sauvegarde** (parfois sur les six à la fois) et des **niveaux de Dé de Vie** — définitivement. Ces
  pertes ne se voient pas dans un profil d'adversaire : elles s'écrivent dans le **suivi des
  séquelles**, une case par occurrence et par PJ, sinon la table les oublie et le combat final est
  faussé.
- **Les niveaux de Santé mentale se regagnent** : les récompenses de fin s'expriment couramment en
  niveaux récupérés, et non en argent ou en objets. Les porter dans la même planche de séquelles, avec
  des cases « perdu » et des cases « regagné » — c'est le seul endroit où le MJ fera le solde.
- **Malus au toucher noté « 0 » et « −0 »** selon les profils d'un même scénario : c'est la même chose,
  aucun malus. Harmoniser dans le livret.
- **Un dé d'usage qui s'épuise est une horloge gratuite : chercher, dans le scénario, la ressource
  qu'il mesure déjà.** Torche, Bagou et Santé mentale descendent d10 → d8 → d6 → d4 → épuisé, un cran
  sur 1 ou 2 ; c'est un compte à rebours par personnage, déjà chiffré, que les sources ne relient
  jamais à ce qu'elles décrivent en prose. Vérifier d'abord si le scénario impose une contrainte
  continue — la lumière, la crédibilité d'une couverture, la raison — puis la faire porter par le dé
  correspondant, en annonçant **un test par étape**. Ne rien inventer : le dé existe, il suffit de
  nommer ce qu'il compte.
  *Cas vécu, dans* Magnitogorsk *: un acte entier joué sous terre, « il leur faudra à minima des
  sources de lumière » d'un côté et « leurs sources de lumière les lâchent les unes après les autres »
  cinquante pages plus loin, aucun décompte entre les deux, et aucun prétiré équipé d'une lanterne. La
  **Torche** porte la lampe, seize étapes du campement au Nexus, et l'espérance de l'échelle place le
  d6 dans le noir au milieu du parcours, les d8 aux deux tiers, les d10 juste avant la fin — mot pour
  mot ce que la source décrivait sans l'avoir chiffré.*

## Chroniques Oubliées Fantasy

- **Résolution** : « jet de <CAR> difficulté N » — FOR, DEX, CON, INT, SAG, CHA. Toujours écrire la
  difficulté chiffrée : « jet de DEX difficulté 15 ». Ne jamais écrire « Sauvegarde ».
- **Format d'un profil** : FOR / DEX / CON / INT / SAG / CHA, puis **DEF · PV · Init**, puis armes avec
  bonus d'attaque et **DM** (« Épée longue +5 DM 1d8+2 »), armures avec leur bonus de DEF, puis
  capacités. Éventuellement **NC** (niveau de challenge) et le niveau du PNJ.
- **Attention aux deux notations** : les scénarios donnent tantôt des **valeurs brutes** (FOR 12),
  tantôt des **modificateurs** (FOR +1) — parfois dans la même page. Harmoniser dans le livret et le
  signaler en rouge : c'est une erreur qui se paie en pleine bagarre.
- **Progression** : le scénario indique les passages de niveau et où ils tombent. À porter au tableau
  de bord, avec les récompenses monétaires (pièces d'argent, contrats), parce que c'est de
  l'information de pilotage.
- **Adversaires sans profil** : la gamme assume qu'un monstre puisse n'avoir aucune ligne de
  caractéristiques et se jouer entièrement par des jets des PJ (esquives, escalade, compteur de
  dégâts sur un point faible). Ne pas chercher à le statter ; l'écrire explicitement dans les rappels.
- **Vocabulaire d'univers** à respecter s'il est donné : provinces, baronnies, noms de lieux.

## Shadowdark

OSR moderne. Tout le jeu tient sur deux ressources : **la lumière** et **l'or**.
*Chapitre né de « La Citadelle perdue du minotaure écarlate ».*

- **Résolution** : « **<CAR> ND N** » — ND pour *niveau de difficulté*. FOR, DEX, CON, INT, SAG, CHA.
  Écrire exactement dans cet ordre et avec ce mot : « **DEX ND 12** », « **FOR ND 18** ». Jamais
  « difficulté », jamais « Sauvegarde ».
  Échelle observée : **9** facile · **12** normal · **15** difficile · **18** très difficile ·
  **20** extrême.
- **Format d'un profil** : **CA · PV**, puis attaques et dégâts, puis les modificateurs de
  caractéristiques, puis niveau et alignement. Un objet peut avoir un profil (« émeraude : CA 20, 1 PV »).
- **Les scénarios ne chiffrent presque jamais leurs créatures** : la gamme renvoie au bestiaire du
  livre de base. C'est un choix éditorial, pas un oubli — mais cela impose un travail qui nous revient :
  **dresser la liste des créatures à sortir du bestiaire avant la séance**, avec la zone où chacune
  apparaît. Un scénario de 27 zones peut convoquer dix profils sans en donner un seul.
- **La lumière est la mécanique centrale, et c'est un compte à rebours réel.** Obscurité totale par
  défaut ; les torches se consomment en **temps réel de table**. Conséquence à écrire noir sur blanc :
  **tous les habitants du lieu voient dans le noir, les PJ sont les seuls à avoir besoin de lumière** —
  donc les seuls visibles à distance, et les seuls que l'extinction d'une torche met en danger. Une
  table de rencontres qui contient « un courant d'air éteint toutes les torches » n'est pas une
  péripétie d'ambiance : c'est l'événement le plus dangereux de la table.
- **L'or est l'expérience.** Le butin n'est pas une récompense accessoire, c'est le compteur de
  progression. Le chiffrer zone par zone et le totaliser — voir la micro-grille `Décor / Danger / Butin`
  du chapitre G de `MODELE-formes.md`.
- **Niveau de danger du site** — Inoffensif, Peu risqué, **Risqué**, Mortel. Il fixe la fréquence du
  test de rencontre : à « Risqué », **tous les 2 rounds d'exploration, ou dès que les PJ font du
  bruit** (1d6, 1 = rencontre). Le porter au tableau de bord avec les autres horloges.
- **« X chances sur 6 » et « 1 chance sur N cumulative »** sont l'idiome de la gamme, et il faut le
  recopier tel quel — pas le traduire en pourcentage. Le **cumulatif** monte à chaque tentative : c'est
  le moteur de tension du jeu (retirer les bouchons d'un bassin, forcer une porte chauffée, fouiller un
  tas d'ossements). Signaler chaque compteur cumulatif comme tel, sinon le MJ le joue comme un jet fixe
  et la tension disparaît.
- **Jetons de Chance** : ressource distribuée par certains lieux, souvent une fois par personnage. Les
  signaler, ils changent la façon dont la table aborde le danger suivant.
- **Perte permanente de caractéristique** : certains lieux retirent des points de FOR, SAG, etc., avec
  effet définitif à zéro (catatonie, mort). À porter dans le suivi des séquelles, et à **annoncer en
  fiction avant que le PJ ne s'engage** — sinon c'est une mort sans avertissement.

Pièges de notation :

- **Le plan est une page de règles, pas une illustration.** La légende de la carte porte des valeurs
  qui n'existent nulle part dans le texte : « **V** Verrouillé : DEX ND 20 pour crocheter, FOR ND 18
  pour forcer », « **B** Barricadé : FOR ND 18 », « **T** Statue de taureau : activée par le mouvement,
  3/6 charge, DEX ND 15 sinon 2d6 », « **S** Porte secrète : le mur pivote en silence quand on le
  pousse ». **Toujours réclamer le plan et dépouiller sa légende** au même titre que le texte des zones.
- **Les mécaniques d'escalade peuvent produire une spirale de mort.** Cas vécu : un malus cumulatif de
  −2 sur la table de rencontre à chaque apparition de l'antagoniste, « les résultats inférieurs à 1
  comptant comme des 1 » — au bout de trois ou quatre apparitions, on le tire mécaniquement à chaque
  test. Dire si c'est voulu, et à quel palier le site devient invivable.
- **Deux règles de présence qui se superposent.** Le même antagoniste peut avoir « 3 chances sur 6
  qu'il soit là », « 1 chance sur 6 cumulative par round qu'il revienne » et « revient au moins une
  fois par heure ». Trancher l'ordre d'application et l'écrire.
- **Les effectifs de faction ne sont pas gérés** : un chiffre par zone, plus une table aléatoire qui en
  ajoute, sans total. Prévoir le compteur.

## Fevertown

Comédie policière, uchronie années 80. Système délibérément minimal : tout l'écart entre deux
personnages passe par l'Avantage. *Chapitre né de « Bun & Run », kit de découverte v1.2.*

- **Résolution** : « **jet de <Attribut>** » — Physique, Adresse, Astuce, Social. **1 D20**, seuil
  **10** par défaut. 2-9 échec · 10-19 réussite · **20** réussite critique · **1** échec critique.
- **Les attributs n'ont aucune valeur chiffrée** : ils nomment l'action, ils ne modifient pas le dé.
  Ne jamais écrire « jet de Physique +2 » ni « difficulté N » — cela n'existe pas.
- **Le nom de l'action est libre** (« défonçage express », « observation passive-agressive ») : la
  mécanique ne change pas. Dans nos documents, garder le nom d'attribut nu — c'est au joueur d'habiller.
- **Ce qui bouge, c'est le seuil de situation**, et c'est le levier de pilotage principal du jeu :
  **chaotique 12** (obscurité, panique, foule, terrain instable, pression immédiate — et tout tir au
  corps à corps) · **neutre 10** · **bénéfique 8** (cible entravée, position dominante, **plan
  préparé**, terrain maîtrisé). L'écrire chiffré à chaque fois, avec le mot du jeu :
  « situation chaotique — 12 ». Le seuil est **indépendant** de l'Avantage : le contexte modifie le
  seuil, l'atout modifie la façon de lancer.
- **Format d'un profil** : **PV · Armure · Arme · Dégâts · Atout.** Cinq lignes, dans cet ordre, rien
  d'autre. Pas d'attributs, pas d'initiative, pas de défense. **Dégâts fixes**, jamais en dés. Critique
  = dégâts ×2.
- **Unité de temps** : le **tour**, qui se termine quand tous les joueurs ont agi. **Pas d'initiative
  chiffrée** : les joueurs choisissent l'ordre entre eux, y compris pour agir simultanément.
  **Conséquence d'écriture décisive :** les ennemis agissent **en réaction aux échecs des PJ**. Ne
  jamais écrire « au tour 3, l'adversaire fait X » — écrire « **au premier échec d'un PJ**, il fait X ».
  Une **« menace majeure »** peut agir sans attendre l'échec : le signaler nommément, c'est la seule
  façon de rendre un adversaire dangereux dans ce système.

Sous-systèmes qu'un scénario suppose connus :

- **Avantage / Désavantage** = 2D20, meilleur / pire. **Ils ne se cumulent pas** — deux sources
  d'Avantage ne donnent pas 3D20, sauf atout qui le dit explicitement.
- **Les critiques ne sont jamais annulés.** Un **1 naturel** reste un échec critique même avec
  Avantage : la réussite est acquise, avec une conséquence imprévue. Un **20 naturel** reste une
  réussite critique même avec Désavantage : l'échec tient, teinté d'un effet positif. C'est le
  sous-système le plus rentable à exploiter par écrit — **donner d'avance deux ou trois conséquences
  imprévues** par scène, sinon le MJ improvisera à sec.
- **Jet de défi**, deux usages : **opposition directe** (le plus haut D20) et **séquence cumulative**
  (objectif 25 ou 30, chacun additionne tour après tour, le premier à l'atteindre remporte la scène).
  Toute poursuite s'écrit avec un **objectif chiffré** et un obstacle décrit par tour.
- **Jets de chance** — 5 facile / 10 moyen / 15 difficile. Pour ce qui dépend du monde et non du
  personnage. Les préparer : un scénario en pose trois ou quatre.
- **Fusillade** : à couvert, aucun tir direct ne touche, mais on ne peut pas attaquer. **Tir de
  couverture** : pas de jet, consomme le chargeur, crée une zone dangereuse — la cible qui sort et
  échoue prend les dégâts. **Tir balayage** : armes automatiques, jusqu'à cinq cibles. Préciser si un
  PNJ du scénario a une arme automatique — souvent aucun.
- **Blessures** : **4 PV ou moins = Désavantage sur tous les jets** (la grille de la fiche souligne ce
  seuil) · **0 PV = inconscient, pas mort** · **La Muerte** : mort définitive si aucun soin dans la
  scène suivante, ou si nouveaux dégâts inconscient. Le dire à la table avant la première scène
  dangereuse : c'est ce qui rend un assaut raté irréversible.
- **Repos court** = la moitié des PV perdus · **repos long** = tout. **Arrondi toujours au supérieur**,
  quelle que soit la formule. **Conséquence à écrire dans un one-shot :** les atouts « 1 fois par repos
  long » sont **1 fois par partie**. Le dire, sinon les joueurs les gardent pour une scène qui
  n'existera pas. Et **repérer la seule fenêtre de repos court** du scénario : la nommer.
- **Le cadre légal est une mécanique déguisée.** Huit devoirs (respecter les civils, éviter les bavures
  *surtout devant les caméras*, limiter les dégâts matériels, arrêter dans les règles, armes
  homologuées, rester dans sa juridiction, rédiger les rapports, obéir), six sanctions **narratives**
  (arme confisquée, standard de nuit, circulation, retenue sur salaire, archives, blâme), et la mise à
  pied comme seule fin de personnage. Tout scénario de flics s'appuie dessus : le porter en
  **compteur**, et lister d'avance les devoirs que le scénario fait enfreindre d'office.
- **Atouts, formations, points faibles** : c'est là qu'est tout le personnage. Les **recopier verbatim**
  depuis les fiches dans le dossier, avec leur nom exact, et **dire à quelle scène chacun tombe** (voir
  la règle du socle sur les prétirés). C'est la valeur ajoutée principale d'un dossier sur ce système.

Pièges de notation :

- **Le gilet pare-balles.** Le kit énonce **1 point d'armure** *et* « les dégâts d'armes à feu sont
  divisés par deux », sans dire l'ordre — et les fiches de prétirés portent les deux sur la même ligne.
  Trancher et l'annoncer : **diviser d'abord** (arrondi au supérieur), **puis retirer 1**.
- **La même arme n'a pas les mêmes dégâts partout** : le 9 mm fait **8** sur les cinq fiches de
  prétirés et **7** dans un profil de PNJ. Harmoniser sur les fiches, et **dire la conséquence** — à
  8 dégâts, un PJ à 12 PV tombe en deux balles.
- **La Réputation existe sur la fiche, pas dans les règles.** Cinq étoiles imprimées, une allumée,
  aucune mécanique associée (le kit dit que le système « existe mais n'est pas utilisé »). Ne pas
  l'ignorer : **s'en servir comme compteur de partie**, +1 pour un acte de flic modèle devant les
  caméras, −1 par bavure. C'est le support tout prêt du compteur de bavures.
- **Les deux voies d'entrée.** *Crack de l'académie* = **une relance de dé par partie**. *Légende du
  bitume* = **+4 PV déjà inclus** dans le total de la fiche : ne pas les rajouter. Un atout peut en
  ajouter 4 de plus, ce qui explique des totaux identiques par des chemins différents.
- **Les prétirés déplacent les seuils de critique** : réussite critique sur 18-20 avec l'arme de
  formation, ou sur un 13 par atout ; échec critique élargi à 1 **et** 2 par point faible. Faire un
  **tableau des seuils par PJ** : c'est l'erreur d'arbitrage la plus probable de la partie.
- **« Les attributs déterminent le nombre de dés »** est trompeur dans le texte du kit : le nombre de
  dés vient de l'Avantage, pas de l'attribut. Ne pas recopier cette formulation.

## PbtA — Escape from Dino Island

Famille *Powered by the Apocalypse*. Ce chapitre est écrit sur *Escape from Dino Island* (Sam Tung &
Sam Roberts), mais l'essentiel — les paliers, la manœuvre, le 6-, l'absence de profils — vaut pour
toute la famille. *Chapitre né de « L'Île du D. Raslov ».*

- **Résolution** : « **lance+<Attribut>** » — 2d6 + attribut, trois paliers **10+ / 7-9 / 6-**.
  Écrire exactement comme la source : « lance+Astuce ». Jamais « jet de », jamais « difficulté ».
  Attributs observés dans EFDI : **Calme, Astuce, Forme**. Un jet peut être **lance+0** — aucune
  compétence n'aide, c'est le monde qui décide.
- **Il n'existe aucune difficulté à régler.** Le MJ ne fixe pas de seuil, ne module pas un chiffre :
  son seul levier est **quelle manœuvre se déclenche** et **quelle conséquence il tire**. C'est
  l'équivalent, ici, du seuil de situation de Fevertown — sauf qu'il n'y a rien à écrire en chiffres.
- **La manœuvre est l'unité d'écriture du jeu.** Format invariable : une **phrase-déclencheur** (« Quand
  vous fuyez la meute de chien dans la jungle »), l'attribut, puis les trois paliers. La
  phrase-déclencheur est de la **fiction**, pas de la mécanique : la recopier **verbatim**, c'est elle
  que le MJ reconnaît au moment où la situation arrive. Rendu : bloc vert, paliers en `.pal`
  (`.x` pour 10+, `.r` pour 7-9, `.e` pour 6-) — la feuille de style canonique les porte déjà, aucune
  retouche nécessaire.
- **Le 6- n'est pas un échec, c'est un tour du MJ.** Conséquence d'écriture décisive : **chaque 6- exige
  une conséquence préparée d'avance**, et c'est à cela que servent les **manœuvres de MJ**, une réserve
  par zone. Donc, dans un document PbtA, **le bloc violet de pilotage devient le bloc principal** — plus
  long que le vert, et plus utile. C'est l'inverse du poids qu'il a dans tous les autres systèmes
  couverts ici, et c'est le point à ne pas rater.
- **Format d'un profil : il n'y en a pas, et il ne faut pas en fabriquer.** Un adversaire, c'est
  **des étiquettes** (*Humain, Intelligent, Terrifiant* · *Groupe, Organisé* · *Objet*), **des armes
  étiquetées** (*fusil à lunette : loin, handicapant* · *poignard à dents : contact, sanglant* · *croc
  et griffe : contact*), un **Instinct** en une ligne (« améliorer ses chiens et protéger son secret »),
  et **une liste de manœuvres**. Aucun PV, aucune armure, aucun dégât chiffré, aucune défense, et
  **le MJ ne lance jamais de dé**. Voir le quatrième cas de la règle du socle sur les profils
  illisibles : ici l'absence est totale et structurelle. Ce qu'on écrit à la place : l'instinct, les
  manœuvres, et ce que veulent dire les étiquettes.
- **Aucune unité de temps.** Pas de round, pas d'initiative, pas de tour. Ne jamais écrire « au tour 3,
  l'adversaire fait X ». La fiction avance manœuvre par manœuvre.
- **Les dégâts sont des états nommés**, pas des points : « tu es blessé », « 1 Fracture ». Les recopier
  tel quel et **réclamer au livre de base ce que chaque état fait** — un extrait de scénario ne le dit
  jamais, et c'est une pièce manquante au sens de `MODELE-analyse.md`.
- **« +1 continu »** est l'idiome du bonus persistant (par opposition au bonus d'un seul jet). Les
  sources l'écrivent **sans condition de fin** : en fournir une (jusqu'à la fin de la scène, jusqu'au
  prochain repos, jusqu'à ce que l'état soit soigné).
- **Pas de prétirés : des livrets choisis à la table**, parfois avec la consigne d'en retirer certains.
  La règle du socle sur les prétirés n'a donc pas d'objet — mais son équivalent, oui, et il est plus
  rentable encore : voir la règle du socle sur les **questions d'ouverture**.
- **Les horloges à cocher** sont le compteur universel de la famille, et il y en a toujours plusieurs.
  C'est là que se répond la sixième question de création de chapitre : ce jeu n'a pas de ressource
  unique, il a une **pile d'horloges** — et c'est donc une **planche d'horloges** qui tient le rôle du
  suivi. Voir le chapitre H de `MODELE-formes.md`, qui les trie en deux familles.

Pièges de notation :

- **La même caractéristique nommée deux fois dans la même manœuvre.** Cas vécu : « 10+ gagne +1 continu
  sur **Forme** », « 7-9 gagne +1 continu sur **Force** », à trois lignes d'écart. Harmoniser et le
  signaler.
- **Deux manœuvres avec le même déclencheur et deux résolutions différentes.** Cas vécu : « quand tu
  sautes du haut de la cascade en espérant fuir tes poursuivants » apparaît deux fois sur la même page,
  une fois avec un jet et trois paliers, une fois sans aucun jet et avec une autre issue. Trancher : la
  version sans jet est en général la variante à réserver à un contexte précis, ou la conséquence du 6-.
- **Un bonus sur un tirage de table n'est pas forcément un bonus.** « 10+ : lancez sur les salles avec
  +1 » n'a de sens que si la table est ordonnée par danger. Vérifier, et dire au MJ dans quel sens joue
  le décalage.
- **Le texte à lire aux joueurs cache des règles.** Voir `MODELE-analyse.md` : dans Raslov, « les PJ
  n'ont plus aucun inventaire » est glissé entre parenthèses au milieu d'une page de prose narrative.

---

## Comment créer un nouveau chapitre

Pour un système non encore couvert, répondre à cinq questions et rien de plus :

1. Comment s'écrit **un test** ? (nom exact, échelle, difficulté chiffrée ou non)
2. Comment s'écrit **un profil d'adversaire** ? (ordre des lignes, abréviations — et **s'il en existe**)
3. Quelles sont les **unités de temps** du combat ?
4. Quels **sous-systèmes** un scénario risque-t-il de supposer connus ? (compte à rebours, corruption,
   progression, ressources, usure permanente, lumière)
5. Quels **pièges de notation** la gamme comporte-t-elle ?

Sixième question, quand le jeu appuie sur une **ressource unique** — la lumière en Shadowdark, la
Santé mentale en Cthulhu Hack, l'Avantage en Fevertown : **où cette ressource se compte-t-elle dans
nos documents ?** Une ressource centrale sans planche de suivi est une ressource que la table oublie.
Un jeu peut n'en avoir **aucune** et faire tourner plusieurs compteurs à la place (PbtA) : c'est alors
la **planche d'horloges** qui tient ce rôle, et elle est d'autant plus nécessaire.
