#!/usr/bin/env python3
"""
revision_donnees.py — la matière des pages de révision.

Lu par scripts/revision.py, qui n'en connaît que la forme.

**Rien ne s'invente ici.** Chaque fait vient de preparation/magnitogorsk/,
et chaque question porte sa source dans le champ `ou` : c'est elle qui
s'affiche sous la correction, pour pouvoir aller vérifier.

Forme d'une fiche :

    {"id": "clé-courte", "nom": "…", "role": "…", "lieu": "…",
     "sait": ["…", "…"],          # ou une chaîne
     "cache": [...],              # facultatif
     "dit": [{"qui": "…", "quoi": "…"}],
     "replique": "…",             # citée mot pour mot
     "piege": "…",                # « à ne pas faire »
     "questions": [{"q": "…", "choix": [...], "bonne": 0,
                    "pourquoi": "…", "ou": "fichier.md"}]}

Les mauvaises réponses d'un QCM doivent être **plausibles** : une erreur
que le MJ pourrait réellement commettre à la table. Un leurre absurde
n'apprend rien.

**`bonne` vaut toujours 0 : la bonne réponse s'écrit en premier.** C'est une
convention d'écriture, pas ce que le joueur verra — scripts/revision.py tire
l'ordre des choix au sort à chaque affichage.
"""

TITRE = "Réviser Magnitogorsk"
CHAPEAU = ("Ce qu'il faut avoir en tête avant de mener, parce que ça ne se cherche pas "
           "en pleine scène. Trois modules, à parcourir ou à réviser par questions.")

# ══════════════════════════════════════════════════════════════════
#  1. Les gens
# ══════════════════════════════════════════════════════════════════

GENS = [
    {"id": "igor", "nom": "Igor Pavlenko", "role": "chef de la section de police",
     "lieu": "son bureau, porte ouverte — il parle fort pour qu'on l'entende. "
             "Il habite Berezki.",
     "sait": ["Que le Directeur a écrit à Moscou. <b>Personne ne le lui a dit.</b>",
              "Il ne sait pas que sa fiabilité est l'objet d'un rapport. <b>Il le craint.</b>"],
     "cache": ["Qu'il protège le trafic contre des livraisons chez lui, à Berezki.",
               "Qu'il a <b>détruit</b> — pas classé — la page de conclusion de Belousoff, "
               "et muté l'agent six jours après.",
               "Un train de vie que son salaire n'explique pas : cognac français, conserves "
               "étrangères, une nappe introuvable en ville."],
     "dit": [{"qui": "ses agents", "quoi": "« J'ai des agents compétents » — "
                                           "<b>et il ne peut en citer aucun</b>"},
             {"qui": "Yelena Nikitina", "quoi": "<b>rien. Il ne la mentionne jamais</b>, "
                                                "et c'est ce qui la désigne"},
             {"qui": "l'empoisonnement", "quoi": "« la faible constitution des intellectuels "
                                                 "urbains. Un mal pour un bien. »"}],
     "replique": "« Le camarade Directeur a ses humeurs. Ça ne regarde pas le travail "
                 "de la police. »",
     "piege": "Ne pas le rendre lucide. <b>Un homme qui sait se tait, un homme qui craint parle "
              "trop.</b> Et au dîner de Berezki, ne pas le rendre inquiétant : il est content "
              "de recevoir.",
     "questions": [
        {"q": "Comment le groupe apprend-il qu'il doit aussi juger Igor ?",
         "choix": ["Igor se trahit lui-même au briefing",
                   "Le Directeur le leur dit en les recevant",
                   "Voronin· est obligé de partager son aparté",
                   "Un employé de l'administration les prévient"],
         "bonne": 0,
         "pourquoi": "Il se défend d'une accusation que personne n'a portée. La plus lourde : "
                     "<b>« le camarade Directeur a ses humeurs »</b> — il le nomme alors que "
                     "personne ne lui en a parlé.",
         "ou": "40-igor-se-trahit.md"},
        {"q": "Si personne ne tilte au briefing, quel filet est le plus sûr ?",
         "choix": ["Yelena Nikitina, dès qu'ils l'approchent",
                   "Igor qui revient à la charge le lendemain",
                   "Gusev· qui laisse échapper une remarque",
                   "Kassym, qui a entendu une rumeur"],
         "bonne": 0,
         "pourquoi": "C'est le seul qui <b>ne dépend pas de l'intuition des joueurs</b> : "
                     "il suffit qu'ils enquêtent. Elle veut sa place et attend l'occasion.",
         "ou": "40-igor-se-trahit.md"},
        {"q": "Qu'est-ce qui, dans sa manière de parler de ses collègues, désigne Yelena ?",
         "choix": ["Il ne la mentionne jamais", "Il en dit du mal",
                   "Il la couvre d'éloges", "Il la rend responsable des disparitions"],
         "bonne": 0,
         "pourquoi": "Il vante « des agents compétents » sans pouvoir en nommer un, "
                     "et <b>il ne la cite pas une fois</b>.",
         "ou": "25-lieux-et-presences.md:543"}]},

    {"id": "yelena", "nom": "Yelena Nikitina", "role": "superviseure au bureau de police",
     "lieu": "la salle commune du poste, une table comme les agents — <b>elle n'a pas de bureau "
             "à elle</b>. La salle est déserte : les subalternes draguent les lacs.",
     "sait": ["Que la mutation de Belousoff était <b>un ordre direct d'Igor</b>, "
              "et qu'elle n'a pas été consultée.",
              "Elle avait validé l'initiative d'Oleg. Igor a classé, muté, "
              "et lui a passé un savon."],
     "cache": ["Elle n'a rien dit — <b>et elle le referait.</b>",
               "<b>Elle ne mettra jamais rien par écrit.</b>"],
     "dit": [{"qui": "la mutation d'Oleg, en façade",
              "quoi": "« Un rééquilibrage annuel des effectifs » — <b>et la date concorde "
                      "vraiment</b>"}],
     "replique": "« Vous êtes venus pour les déraillements, ou pour lui ? »",
     "piege": "<b>Ne pas la jouer en victime</b> : elle a choisi de se taire, et elle le "
              "referait. Elle n'est pas coupable, et c'est ce qui la rend difficile à jouer.",
     "questions": [
        {"q": "Comment obtient-on quelque chose de Yelena sur Igor ?",
         "choix": ["En lui demandant son avis sur les autres responsables",
                   "En lui demandant directement ce qu'elle pense d'Igor",
                   "En lui promettant sa place",
                   "En la menaçant d'un rapport"],
         "bonne": 0,
         "pourquoi": "On n'obtient rien en demandant ce qu'elle pense de lui. "
                     "<b>C'est en parlant des autres qu'elle se désigne.</b>",
         "ou": "91-dossier-igor.md:33"}]},

    {"id": "nesteroff", "nom": "Isidor Nesteroff", "role": "médecin-chef du dispensaire",
     "lieu": "le dispensaire. <b>Il ne s'arrête jamais</b> — il répond en marchant, en se lavant "
             "les mains. L'après-midi il fait ses écritures : c'est là qu'on obtient les "
             "rapports.",
     "sait": ["Le rapport du noyé, avec <b>la marque au mollet</b> que personne ne commente.",
              "<b>La copie de l'autopsie de Zina Krylova</b> — celle qui manque aux archives.",
              "L'autopsie du pêcheur, s'ils insistent. Et il reconnaît que les résidus sont les "
              "mêmes partout — <b>en disant sans détour qu'il est incapable de les "
              "identifier</b>."],
     "cache": ["Rien. Mais il croit à la contamination alimentaire — "
               "<b>raisonnement juste sur des données incomplètes</b>."],
     "dit": [{"qui": "Igor", "quoi": "« Un rustre sans éducation et gonflé d'orgueil. Il arrive "
                                     "avec sa conclusion et il attend que mon rapport la "
                                     "confirme. »"},
             {"qui": "le corps du pêcheur", "quoi": "« On dirait que quelqu'un a joué avec ce "
                                                    "corps comme avec une marionnette. »"}],
     "replique": "« Pendant que vous y êtes — l'affaire de la gymnaste. J'ai rendu un rapport il "
                 "y a un mois. Personne n'est venu le chercher. Il est toujours là. »",
     "piege": "<b>C'est le seul PNJ qui sanctionne la mauvaise manière.</b> Si les PJ se "
              "comportent comme Igor — exigences, menaces, conclusion déjà faite — il se ferme "
              "et ne donne plus que le minimum réglementaire.",
     "questions": [
        {"q": "Qu'est-ce qui arrive si les joueurs le traitent comme Igor le traite ?",
         "choix": ["Il se ferme et ne donne que le minimum réglementaire",
                   "Il les dénonce à la police", "Il ment sur les rapports",
                   "Il refuse de les recevoir"],
         "bonne": 0,
         "pourquoi": "<b>C'est le seul PNJ du scénario qui sanctionne directement la mauvaise "
                     "manière.</b>",
         "ou": "25-lieux-et-presences.md:262"},
        {"q": "Quand lâche-t-il la remarque sur le rapport de la gymnaste ?",
         "choix": ["Au deuxième passage, sans qu'on demande rien",
                   "Dès la première visite",
                   "Seulement si on l'interroge sur le Komsomol",
                   "Jamais, il faut le trouver aux archives"],
         "bonne": 0,
         "pourquoi": "<b>Ce n'est pas une demande, c'est une humeur.</b> "
                     "Dite une fois, jamais répétée.",
         "ou": "25-lieux-et-presences.md:336"}]},

    {"id": "kassym", "nom": "Kassym Volkoff", "role": "16 ans, komsomolets, leur guide",
     "lieu": "il vient les chercher à la gare le jour 1, et <b>rentre dormir à la yourte "
             "familiale</b>. Absent au matin du jour 2.",
     "sait": ["Où dormir, où manger, l'eau, les horaires, le troc, qui commande. "
              "Les raccourcis — <b>sa seule vraie compétence de guide</b>.",
              "<b>Le tengrisme.</b> Il est kazakh, il sait — et il ne dira rien à des envoyés "
              "de Moscou qu'il admire."],
     "cache": ["Qu'il a peur d'Igor Pavlenko.",
               "<b>Trois lieux où il n'est jamais allé</b> — le palais, Berezki, le bureau "
               "d'études — et il les place faux sur son plan."],
     "dit": [{"qui": "Grigori Novikoff", "quoi": "« C'est un tyran » — si la confiance est là, "
                                                 "<b>et sans faire le lien avec le meurtre</b>"},
             {"qui": "Berezki", "quoi": "« On n'y va pas. »"},
             {"qui": "la carte de repas", "quoi": "« Vous, vous n'attendez pas. » — "
                                                  "sans y mettre de jugement"}],
     "piege": "<b>Il ne déballe rien de lui-même.</b> S'il explique tout d'affilée, c'est le MJ "
              "qui fait un cours pendant que personne ne joue. Il pose <b>une</b> question, et "
              "ne la repose pas. Ses erreurs de plan ne se signalent pas : ils les découvriront "
              "en se perdant.",
     "questions": [
        {"q": "Que fait-on de ses erreurs sur le plan de la ville ?",
         "choix": ["Rien — ils les découvriront en se perdant",
                   "Le corriger discrètement",
                   "Lui faire refaire le plan",
                   "Les signaler pour éviter de perdre un créneau"],
         "bonne": 0,
         "pourquoi": "Trois lieux où il n'est jamais allé : le palais, Berezki, le bureau "
                     "d'études. <b>Ne pas le signaler.</b>",
         "ou": "60-kassym.md:175"},
        {"q": "Sans Kassym à la filature du hangar zéro, que se passe-t-il ?",
         "choix": ["La table repart avec un culte inquiétant sur les bras",
                   "Ils ne trouvent pas le hangar",
                   "Les cultistes les repèrent",
                   "La scène ne peut pas avoir lieu"],
         "bonne": 0,
         "pourquoi": "Lui seul peut les identifier comme des familles kazakhes. "
                     "<b>Et c'est exactement ce que le scénario veut.</b>",
         "ou": "25-lieux-et-presences.md:1340"}]},

    {"id": "larissa", "nom": "Larissa Kazakova", "role": "suivi administratif des convois",
     "lieu": "au bureau le matin, dans les hangars l'après-midi. <b>Elle va partout, et personne "
             "ne s'en étonne : c'est son travail.</b>",
     "sait": ["Tout. Trois morts dans sa famille : mari, fille de 5 ans, fils de 3 ans."],
     "cache": ["Sa version ne bouge jamais : « J'étais au dépôt. Je suis passée aux écuries en "
               "début de matinée. » <b>Elle ne se contredit jamais</b> — sa version absorbe même "
               "le témoignage de Zinaida.",
               "Le 27 avril au matin, elle était à la gare <b>pour commander des explosifs</b> : "
               "le seul moment où elle a quitté le secteur."],
     "piege": "<b>Six tells, un par jour maximum. Ne jamais appuyer.</b> Si un joueur relève, "
              "ne pas confirmer ; si personne ne relève, ne pas insister — il reste la veille "
              "nocturne. <b>On ne prend jamais Larissa en défaut : on prend le document en "
              "défaut.</b>",
     "questions": [
        {"q": "Pourquoi ne peut-on pas coincer Larissa par l'interrogatoire ?",
         "choix": ["Sa version ne se contredit jamais et absorbe les témoignages",
                   "Elle refuse de parler",
                   "Elle a un alibi vérifiable",
                   "Elle est protégée par Faddei"],
         "bonne": 0,
         "pourquoi": "Elle est administrative : aller partout <b>est</b> son travail. "
                     "On prend le document en défaut, pas elle.",
         "ou": "85-secteur-transport.md:225"}]},

    {"id": "faddei", "nom": "Faddei Nikitine", "role": "ingénieur, responsable du transport",
     "lieu": "son bureau de planches dans l'entrepôt principal — debout devant ses plans le "
             "matin, assis devant ses registres l'après-midi. <b>Une caisse fermée à clé sous "
             "la table</b> : les quatre pièces.",
     "sait": ["Les quatre incidents, leurs dates, leurs causes.",
              "L'anomalie du registre au 27 avril — <b>sans en tirer la moindre conclusion</b>.",
              "Qu'il faudrait vérifier qui a les clés du local de rangement. "
              "<b>La question n'a jamais été posée.</b>"],
     "dit": [{"qui": "le registre", "quoi": "« Le registre dit qu'elle était là. Je ne me "
                                            "souviens pas l'y avoir vue, mais je ne vois pas "
                                            "tout. » — <b>il n'en tire rien</b>"},
             {"qui": "Timur Bakhytov", "quoi": "lui reproche de privilégier les quotas"},
             {"qui": "Stepan Udovenko", "quoi": "confiance — il le juge professionnel"}],
     "piege": "<b>Il ne soupçonne personne.</b> Débordé, coopératif, inquiet — il <i>veut</i> "
              "qu'on l'aide, répond longuement et s'excuse de ne pas savoir.",
     "questions": [
        {"q": "Sa déposition du 10 avril porte combien d'incidents ?",
         "choix": ["Deux", "Quatre", "Trois", "Un seul"],
         "bonne": 0,
         "pourquoi": "Le moyeu (2 avril) et la lanière (8 avril). Les deux autres suivent — "
                     "<b>et personne n'est venu</b>.",
         "ou": "86-carnet-faddei.md"},
        {"q": "Combien de jours entre son dépôt au palais et l'arrivée à la police ?",
         "choix": ["Dix-neuf", "Cinq", "Trente", "Deux"],
         "bonne": 0,
         "pourquoi": "Déposé le <b>10 avril</b>, parvenu le <b>29</b>. Puis Igor l'ouvre "
                     "et le laisse : seul ce second retard lui est imputable.",
         "ou": "70-rapports-imprimes.md"}]},

    {"id": "grigori", "nom": "Grigori Novikoff", "role": "22 ans, komsomolets modèle — "
                                                         "le meurtrier",
     "lieu": "le Komsomol. <b>Il vient au-devant des PJ à chaque visite</b> : il s'occupe des "
             "visiteurs, c'est son rôle, et il l'a pris.",
     "sait": ["Tout. Il a étranglé Zina avec un complice, puis <b>caché la cordelette chez "
              "Maxim Kazakoff</b> en espérant une fouille."],
     "cache": ["<b>Trois excès, gratuits</b> : un éloge trop long de Zina qui finit en « nous "
               "étions amis » — mensonge que n'importe qui dément ; il désigne Maxim sans qu'on "
               "le lui demande ; il demande où en est l'enquête, trop tôt et trop précisément."],
     "dit": [{"qui": "sa dernière rencontre avec Zina",
              "quoi": "« Elle venait me poser des questions sur l'organisation de son voyage à "
                      "Stalingrad. » — <b>c'est faux, et il est le dernier à l'avoir vue</b>"}],
     "piege": "<b>Rien n'oblige à relever ses excès, et rien ne doit les souligner.</b> "
              "Accusé sans Macha ni Tolia : il nie, les responsables le défendent, "
              "<b>et il devient prudent</b>.",
     "questions": [
        {"q": "Grigori accusé sans Macha Fenenka ni Tolia Zaïtsev — que se passe-t-il ?",
         "choix": ["Il nie, on le défend, et il devient prudent",
                   "Il avoue sous la pression de la Guépéou",
                   "Il s'enfuit du complexe",
                   "Les responsables le livrent"],
         "bonne": 0,
         "pourquoi": "C'est le pire résultat possible : <b>il devient prudent</b>, "
                     "et la porte se referme.",
         "ou": "89-komsomol.md:244"}]},

    {"id": "tolia", "nom": "Tolia Zaïtsev", "role": "19 ans, le complice",
     "lieu": "parmi la troupe de Grigori",
     "sait": ["Il était là. <b>Il a tenu les poignets.</b> Il n'a pas dormi depuis un mois.",
              "<b>C'est le seul témoignage direct du dossier.</b>"],
     "piege": "<b>Il casse si on le sépare de Grigori</b> — exactement comme Nikiforov aux "
              "entrepôts. Et comme lui, il ne demande pas pardon : <b>il demande ce qu'il "
              "risque</b>.",
     "questions": [
        {"q": "Quel PNJ des entrepôts fonctionne exactement comme Tolia Zaïtsev ?",
         "choix": ["Anton Nikiforov", "Kirill Zykov", "Viktor Cheskov", "Margarita Gordeeva"],
         "bonne": 0,
         "pourquoi": "Les deux cassent une fois séparés de leur chef, et <b>tous deux demandent "
                     "ce qu'ils risquent</b> au lieu d'avouer. C'est le même ressort, posé deux "
                     "fois.",
         "ou": "89-komsomol.md:214"}]},

    {"id": "macha", "nom": "Macha Fenenka", "role": "komsomolka, la victime que Zina a sauvée",
     "lieu": "<b>invisible — elle évite le Komsomol depuis l'agression.</b> "
             "On ne la trouve pas en demandant.",
     "sait": ["L'agression, et que <b>Zina est entrée dans la salle et l'a sauvée</b>."],
     "cache": ["Tout, par terreur."],
     "piege": "<b>Ne pas détailler l'agression.</b> Ce qui compte, c'est le profil de Grigori et "
              "le fait que Zina en a été témoin. Le reste se laisse hors champ.",
     "questions": [
        {"q": "À quelles conditions trouve-t-on Macha Fenenka ?",
         "choix": ["Avoir compris ce qu'est Grigori, être discret, offrir des garanties",
                   "Demander aux responsables du Komsomol",
                   "Passer par Kassym",
                   "La convoquer au bureau de police"],
         "bonne": 0,
         "pourquoi": "<b>On ne la trouve pas en demandant.</b> Elle évite le Komsomol, "
                     "et elle exige des garanties crédibles.",
         "ou": "25-lieux-et-presences.md:719"}]},

    {"id": "zykov", "nom": "Kirill Zykov", "role": "chef d'équipe, zone de déchargement ouest",
     "lieu": "debout sur le quai, <b>jamais assis</b> — c'est son seul tic visible. "
             "Sur la défensive avant même qu'on parle.",
     "sait": ["Tout le dispositif. <b>Il a eu cinq semaines pour préparer.</b>"],
     "cache": ["La vraie raison de la permanence de Nikiforov aux premiers wagons.",
               "<b>Il prévient Orloff le soir même</b> si on le presse."],
     "dit": [{"qui": "Nikiforov", "quoi": "« C'est mon meilleur. Rapide, il compte juste. "
                                          "J'y mets celui en qui j'ai confiance. »"},
             {"qui": "les écarts", "quoi": "« Les inventaires sont faits par des gamins "
                                           "qui ne savent pas compter. »"},
             {"qui": "Igor, s'il est pressé", "quoi": "« Le camarade Pavlenko a déjà regardé "
                                                      "tout ça » — <b>il croit que c'est un "
                                                      "bouclier</b>"}],
     "piege": "<b>Zykov ne craque jamais.</b> Il a plus à perdre et il est plus intelligent. "
              "Ne jamais l'interroger avec Nikiforov : <b>Zykov parle et Nikiforov acquiesce.</b>",
     "questions": [
        {"q": "Pourquoi ne jamais interroger Zykov et Nikiforov ensemble ?",
         "choix": ["Zykov parle et Nikiforov acquiesce",
                   "Ils se contredisent et se mettent sur leurs gardes",
                   "Nikiforov refuse de parler devant témoin",
                   "Zykov prévient Orloff aussitôt"],
         "bonne": 0,
         "pourquoi": "Séparés, ils donnent deux versions qui s'annulent. "
                     "Ensemble, il n'y en a plus qu'une.",
         "ou": "87-disparitions.md:183"}]},

    {"id": "nikiforov", "nom": "Anton Nikiforov", "role": "déchargement, premiers wagons",
     "lieu": "l'allée du fond, à ranger des caisses — <b>il ne lève pas les yeux</b>",
     "sait": ["Il sort des caisses et les pose à un endroit convenu. "
              "<b>C'est tout ce qu'il sait, et c'est sincère.</b>",
              "<b>Il ne connaît pas Orloff par son nom</b> — « le petit homme de la gare ». "
              "S'il lâche ça, c'est énorme, et il ne s'en rend pas compte."],
     "dit": [{"qui": "son poste", "quoi": "« Les premiers wagons ? Personne n'en veut. "
                                          "Ceux qui ont le bras long passent au second train. "
                                          "Moi j'ai pas le bras long. »"},
             {"qui": "Zykov", "quoi": "<b>rien.</b> Il ne parle pas devant lui, "
                                      "et il ne dira rien contre lui"}],
     "replique": "« Si je dis quelque chose, il se passe quoi pour moi ? » — <b>c'est l'aveu.</b>",
     "piege": "<b>C'est le maillon qui se casse</b>, et il faut qu'on le sente dès la première "
              "rencontre <b>sans que ce soit comique</b>. Il a peur de tout le monde : de Zykov, "
              "de la police, des PJ.",
     "questions": [
        {"q": "Zykov et Nikiforov décrivent le même poste. Qu'est-ce qui les trahit ?",
         "choix": ["L'un décrit une récompense, l'autre une punition",
                   "Les dates ne concordent pas",
                   "L'un parle de quatre caisses, l'autre de six",
                   "Nikiforov nie y avoir travaillé"],
         "bonne": 0,
         "pourquoi": "On ne met pas son meilleur homme à la corvée que personne ne veut, trois "
                     "fois par semaine, pendant dix-huit mois. <b>Ils mentent sur le sens.</b>",
         "ou": "87-disparitions.md:171"}]},

    {"id": "gordeeva", "nom": "Margarita Gordeeva", "role": "responsable de l'entrepôt n°7",
     "lieu": "son bureau à cloison. Le matin elle compte des bobines, agacée ; "
             "<b>l'après-midi elle est assise et elle parle</b> — seul moment où elle sort son "
             "carnet sans qu'on insiste.",
     "sait": ["La rotation anormale des effectifs.",
              "<b>Le tableau des affectations</b>, qu'elle a parce qu'elle réclame du monde "
              "chaque semaine.",
              "<b>Un carnet d'écarts qui court jusqu'à fin avril</b> — dont deux lignes "
              "postérieures au classement du dossier."],
     "dit": [{"qui": "la rotation", "quoi": "« Trois fois en six mois, pour deux postes. "
                                            "Ici, personne ne reste. » — <b>la clé du dossier, "
                                            "donnée en s'excusant</b>"},
             {"qui": "Zykov", "quoi": "« Il tient son équipe. Je n'ai rien à lui reprocher. » — "
                                      "<b>sur un ton qui dit le contraire</b>"}],
     "replique": "« J'ai écrit deux fois. On m'a répondu que mes hommes comptaient mal. "
                 "Maintenant je note, et je ne transmets plus. »",
     "piege": "<b>Elle ne propose jamais rien.</b> Elle répond à ce qu'on lui demande, "
              "complètement et sans détour. <b>Tout le dossier est chez elle, et elle ne le sait "
              "pas.</b>",
     "questions": [
        {"q": "Elle donne la clé du dossier des disparitions. Laquelle ?",
         "choix": ["« Trois fois en six mois, pour deux postes. Ici, personne ne reste. »",
                   "Le nom de Nikiforov",
                   "Les horaires des convois",
                   "L'adresse du réduit de la gare"],
         "bonne": 0,
         "pourquoi": "La rotation <b>est l'indice, pas l'obstacle</b> : si tout le monde tourne, "
                     "ceux qui ne bougent pas sautent aux yeux. Elle la donne en s'excusant.",
         "ou": "87-disparitions.md:209"}]},

    {"id": "oleg", "nom": "Oleg Belousoff", "role": "agent muté à la surveillance des mines",
     "lieu": "le mont Magnitnaïa, à 5 km, dans une guérite. <b>Il n'est pas au fond : il "
             "surveille.</b> Une punition de poste, pas de métier.",
     "sait": ["Qu'il flairait un trafic organisé, sans preuve.",
              "Que sa prochaine piste était <b>Sacha Orloff</b>.",
              "<b>Ce qu'il y avait sur la page retirée</b>, qu'il récite mot pour mot."],
     "cache": ["<b>Il croit d'abord à un test d'Igor</b> et répond par la version officielle, "
               "mot pour mot — ce qui est en soi une information."],
     "dit": [{"qui": "ses collègues", "quoi": "« Ils savent pourquoi je suis ici. "
                                              "Personne ne me parle. »"},
             {"qui": "ce qu'il n'a pas pu vérifier",
              "quoi": "« Je voulais la liste des affectations. On me l'a promise, et puis j'ai "
                      "été muté. » — <b>il désigne l'entrée par les papiers sans le savoir</b>"}],
     "piege": "Ce qui le fait basculer n'est <b>pas un jet de Bagou — c'est une prise de "
              "risque</b> : un PJ doit dire quelque chose qui le mettrait en danger si Oleg le "
              "rapportait. Et <b>ne pas en faire un allié</b> : il donne, et il retourne à sa "
              "guérite.",
     "questions": [
        {"q": "Qu'est-ce qui fait parler Oleg Belousoff ?",
         "choix": ["Qu'un PJ prenne un vrai risque devant lui",
                   "Un jet de Bagou réussi",
                   "La promesse d'une réaffectation",
                   "Lui montrer le dossier amputé"],
         "bonne": 0,
         "pourquoi": "Il croit d'abord à un test d'Igor. Il faut dire quelque chose qui <b>le "
                     "mettrait en danger s'il le rapportait</b>.",
         "ou": "87-disparitions.md:267"}]},

    {"id": "orloff", "nom": "Sacha Orloff", "role": "tenancier du café de la gare — "
                                                    "et indicateur d'Igor",
     "lieu": "son café bâché entre deux wagons, à la gare",
     "sait": ["Tout le réseau. Et que <b>Larissa lui a commandé des explosifs</b>, "
              "rendez-vous pris.",
              "<b>Il est prévenu avant leur arrivée</b> — par Zykov ou par Igor. "
              "Son calme est l'information."],
     "cache": ["Il livre <b>par paliers</b>. Jamais un mot contre Zykov ni Nikiforov : "
               "il les protège par intérêt. Il lâche Cheskov au palier 2 — <b>le maillon du "
               "milieu</b>. Igor seulement au palier 3, et sans le nommer."],
     "dit": [{"qui": "Igor, au palier 3", "quoi": "« certaines personnes bien placées préfèrent "
                                                  "que la marchandise circule librement »"},
             {"qui": "les PJ", "quoi": "« Vous êtes les premiers depuis longtemps à poser les "
                                       "bonnes questions. » — flatterie <b>et</b> avertissement"}],
     "piege": "<b>Tout ce qu'on lui dit remonte à Igor.</b> À la deuxième visite il a changé de "
              "posture, pas de décor : il ne vient plus à vous, il attend que vous traversiez "
              "les vingt mètres. <b>Ne pas cacher qu'il est prévenu.</b>",
     "questions": [
        {"q": "Orloff ne donne jamais de coupable. Que donne-t-il ?",
         "choix": ["Igor", "Zykov", "Nikiforov", "Larissa"],
         "bonne": 0,
         "pourquoi": "Il protège les siens par intérêt et sacrifie Cheskov. "
                     "<b>Orloff s'en sort toujours</b> — mais au palier 3, il livre Igor.",
         "ou": "87-disparitions.md:447"}]},

    {"id": "cheskov", "nom": "Viktor Cheskov", "role": "transporteur à la charrette",
     "lieu": "<b>jamais à la gare en journée</b> — il vient la nuit. Au quai ouest vers 2 h "
             "la nuit du 6 au 7.",
     "sait": ["<b>Le réduit derrière la gare</b> — il est le seul avec Orloff.",
              "Il livre aussi chez Igor, à Berezki."],
     "cache": ["Tout — mais <b>pris de court, il nie mal</b>."],
     "dit": [{"qui": "Orloff", "quoi": "il le protège <b>par intérêt, pas par loyauté</b> : "
                                       "montrez-lui qu'Orloff le donnera le premier, "
                                       "et il devient bavard"}],
     "piege": "<b>Il n'est dans aucun document</b> — ni le dossier d'Oleg, ni les plaintes. "
              "C'est pour ça qu'il est atteignable : il ne s'est jamais fait interroger "
              "et <b>il n'a pas de version prête</b>.",
     "questions": [
        {"q": "Pourquoi Cheskov est-il le maillon le plus facile à casser ?",
         "choix": ["Il n'est dans aucun document, il n'a pas de version prête",
                   "Il déteste Orloff",
                   "Il a déjà été arrêté",
                   "Il veut quitter la ville"],
         "bonne": 0,
         "pourquoi": "Tous les autres ont été interrogés ou se savent surveillés. "
                     "Lui n'a jamais eu à préparer quoi que ce soit.",
         "ou": "87-disparitions.md:295"}]},

    {"id": "vinogradoff", "nom": "Leonid Vinogradoff", "role": "gradé — l'enquêteur du Komsomol",
     "lieu": "le bureau de police",
     "sait": ["Rien de plus que son rapport. <b>Il ignore ce qu'est devenu le rapport "
              "d'autopsie, et il s'en fiche.</b>"],
     "cache": ["Rien. Il a enfermé Avdotya Kuzmina quatre jours pour la faire avouer, "
               "<b>parce qu'une rivale était commode</b>, puis s'est rabattu sur Maxim."],
     "dit": [{"qui": "l'affaire", "quoi": "« Le coupable a été identifié. L'affaire est close. » "
                                          "— sans l'ombre d'un doute"},
             {"qui": "Maxim Kazakoff", "quoi": "« Il n'a pas nié longtemps. » — "
                                               "il a signé un aveu qu'il ne pouvait pas "
                                               "comprendre"}],
     "piege": "<b>Il n'est pas corrompu : il est satisfait.</b> Ne pas le jouer en brute — "
              "il est poli, compétent dans sa logique, et parfaitement tranquille. "
              "C'est ce que fait la police ici quand elle croit bien travailler, "
              "<b>et c'est pire que la corruption d'Igor</b>.",
     "questions": [
        {"q": "Pourquoi le rapport d'autopsie de Zina manque-t-il au dossier ?",
         "choix": ["Vinogradoff ne l'a jamais lu ni cherché",
                   "Igor l'a détruit",
                   "Le médecin ne l'a jamais rendu",
                   "Grigori l'a fait disparaître"],
         "bonne": 0,
         "pourquoi": "<b>L'incompétence a fait le travail de la dissimulation.</b> "
                     "Et c'est ce qui distingue ce dossier de celui des disparitions, "
                     "où Igor a détruit la page lui-même.",
         "ou": "89-komsomol.md:110"}]},
]


# ══════════════════════════════════════════════════════════════════
#  2. Les pistes — la version d'Igor, la vérité, la bascule
# ══════════════════════════════════════════════════════════════════


def _p(id, nom, dossier, igor, verite, bascule, coupable, faux, questions):
    """Une piste a toujours la même forme, et c'est voulu : on révise un
    triplet — ce qu'on dit, ce qui est, ce qui fait passer de l'un à l'autre."""
    return {"id": id, "nom": nom, "role": dossier,
            "lieuLabel": "Ce qu'Igor en dit", "lieu": igor,
            "sait": ["<b>La vérité.</b> " + verite, "<b>La bascule.</b> " + bascule,
                     "<b>Qui.</b> " + coupable],
            "cache": faux, "questions": questions}


PISTES = [
    _p("deserteur", "Le déserteur", "1932-07/DIS — Pavel Tkachenko",
       "Espionnage au profit d'une puissance étrangère. Il travaillait sous les ordres d'un "
       "Allemand, il a été éliminé ou contraint de fuir. Ses hommes sondent les lacs.",
       "Pavel est <b>en fuite, et encore sur le territoire</b>. Parti tôt le matin avec ses "
       "bagages.",
       "La fouille de sa chambre : <b>tous ses vêtements manquent, le matériel de dessinateur "
       "est resté</b>. Un homme enlevé ne fait pas sa valise. Et le rapport le disait déjà — "
       "il a brûlé des papiers trois jours avant.",
       "Personne. Il n'y a pas de coupable, il y a un dilemme : le dénoncer ou noyer le poisson.",
       ["Le cadavre à retrouver : théorie qu'Igor a inventée seul.",
        "Les deux portraits contradictoires de Pavel — <b>ce n'est pas une contradiction à "
        "résoudre, personne ne ment</b>.",
        "Le dossier est sacrifiable. <b>Le lieu ne l'est pas</b> : au bureau d'études, "
        "les étrangers témoignent par écrit contre Igor."],
       [{"q": "Qu'est-ce qui prouve en dix secondes que Tkachenko n'a pas été enlevé ?",
         "choix": ["Ses vêtements ont disparu, son matériel de travail est resté",
                   "Un témoin l'a vu monter dans le train",
                   "Sa chambre a été fouillée avant la police",
                   "Il a laissé une lettre"],
         "bonne": 0,
         "pourquoi": "<b>Un homme enlevé ne fait pas sa valise.</b> Igor cherche un cadavre, "
                     "la chambre répond à la question que la police n'a jamais posée.",
         "ou": "25-lieux-et-presences.md:1289"},
        {"q": "Ce dossier est jugé sacrifiable. Qu'est-ce qui ne l'est pas ?",
         "choix": ["Le bureau d'études, seul endroit où on témoigne par écrit contre Igor",
                   "L'autopsie, qu'il faut demander",
                   "La fouille de la chambre", "Le sondage des lacs"],
         "bonne": 0,
         "pourquoi": "Les architectes étrangers <b>signent</b> — les Russes refusent, "
                     "les agents se taisent, les ouvriers ont peur.",
         "ou": "25-lieux-et-presences.md:906"}]),

    _p("noye", "Le noyé", "1932-05/DEC — Venyamin Kurbanoff · CLASSÉ",
       "Accident : chute le long d'une berge escarpée, effondrement de la rive, choc et noyade. "
       "Classé en deux jours, sur une demi-page.",
       "Ni chute, ni berge effondrée. <b>Il s'est noyé là où il avait pied.</b> La cause réelle "
       "n'est écrite nulle part — mais ce qui tue dans cette ville vit dans l'eau.",
       "Deux faits qui s'annulent. Au lac : <b>aucune trace d'effondrement</b>, la berge est "
       "stabilisée, pierre et remblai tassé. Au dispensaire : <b>une marque au mollet droit, "
       "« comme une très grosse corde enroulée »</b> — et personne ne la commente.",
       "Non nommé. Acquis : ni accident de berge, ni noyade par profondeur.",
       ["La strangulation : <b>interdite</b>. C'est la mort de Zina Krylova, dans un autre "
        "dossier. Un joueur qui la lit ici part dans une direction que rien ne soutient.",
        "Les ouvriers de la station n'ont rien vu, et c'est vrai."],
       [{"q": "Qu'est-ce qui fait tomber l'explication d'Igor, sur place ?",
         "choix": ["La berge n'a aucune trace d'effondrement récent",
                   "Un témoin a vu quelqu'un le pousser",
                   "L'heure du décès ne colle pas",
                   "Il ne savait pas nager"],
         "bonne": 0,
         "pourquoi": "Elle est abrupte sur tout le pourtour et <b>stabilisée</b>. "
                     "Et le rapport le disait déjà : « l'eau n'y est pas profonde — "
                     "un homme adulte y a pied ».",
         "ou": "25-lieux-et-presences.md:1210"},
        {"q": "Quel détail du rapport médico-légal n'est commenté par personne ?",
         "choix": ["Une marque au mollet, comme une grosse corde enroulée",
                   "L'absence d'eau dans les poumons",
                   "Une fracture du crâne", "Des traces de lutte sous les ongles"],
         "bonne": 0,
         "pourquoi": "Le rapport de police la range dans les lésions « compatibles avec une "
                     "chute ». <b>C'est le document le plus important du dispensaire pour ce "
                     "dossier.</b>",
         "ou": "25-lieux-et-presences.md:328"}]),

    _p("machine", "La machine", "1932-04/SAB — explosion du 16 avril · CLASSÉ",
       "Accident technique : du limon venu du fleuve dans les conduites de refroidissement. "
       "Deux ingénieurs inculpés de négligence, au bloc 27, en attente de jugement.",
       "Ni limon ni branche : <b>les grilles de filtrage sont intactes et en place</b>. "
       "Sur le site, des résidus organiques projetés en tous sens — <b>les mêmes que sur le corps "
       "du pêcheur et dans le tuyau de l'empoisonnement</b>.",
       "L'explication officielle est <b>matériellement impossible</b>, et il n'en reste aucune "
       "autre. Appui : les ouvriers ont entendu des <b>bruits suraigus, comme un animal qui "
       "souffre</b>, quelques secondes avant — les ingénieurs parlent de métal sous pression, "
       "sans les avoir entendus eux-mêmes.",
       "Aucun coupable humain. Sorokin et Malysheff sont innocents de la cause.",
       ["Le limon du fleuve : écarté par les grilles.",
        "Les ingénieurs <b>ne sont pas incompétents</b> : ils ont tort faute d'une donnée.",
        "Le soupçon de sabotage initial — à ne pas confondre avec le dossier 1932-09/SAB."],
       [{"q": "Pourquoi l'explication officielle de l'explosion est-elle impossible ?",
         "choix": ["Les grilles de filtrage sont intactes et en place",
                   "Le limon ne peut pas obstruer ces conduites",
                   "La pression relevée était trop basse",
                   "L'entretien avait été fait la veille"],
         "bonne": 0,
         "pourquoi": "Rien de la taille d'une branche n'a pu les franchir. <b>Une vérification "
                     "le confirme</b> — et il ne reste alors aucune explication.",
         "ou": "25-lieux-et-presences.md:1253"},
        {"q": "Quel élément relie la machine, le pêcheur et l'empoisonnement ?",
         "choix": ["Les mêmes résidus organiques",
                   "Les mêmes témoins", "La même date", "Le même agent instructeur"],
         "bonne": 0,
         "pourquoi": "Nesteroff confirme leur identité si on les lui montre — "
                     "et il dit sans détour qu'il est <b>incapable de les identifier</b>.",
         "ou": "25-lieux-et-presences.md:370"}]),

    _p("empoisonnement", "L'empoisonnement", "1932-08/EMP — ouvert",
       "« Constitutions faibles, rien de plus. » Contamination naturelle, on attend les analyses. "
       "Et c'est un mal pour un bien : la nature trie le bon grain de l'ivraie.",
       "<b>Une larve s'est infiltrée dans une conduite d'eau potable</b> desservant la Section D "
       "et y a laissé des résidus. Elle est partie, l'eau analysée est propre, "
       "<b>mais les résidus sont toujours dans le tuyau</b>.",
       "Double. Le rapport <b>démolit sa propre conclusion</b> : les victimes mangent aux "
       "réfectoires B, C et D — trois cantines. Et la colonne qui manque est l'affectation : "
       "<b>la bonne question est « où travaillent-elles », pas « où mangent-elles »</b>.",
       "La larve. Aucun coupable humain. Action utile sans résoudre : <b>faire condamner "
       "le robinet</b> — gratuit, et ça arrête les nouveaux cas.",
       ["La contamination alimentaire, portée par Nesteroff — <b>son raisonnement est juste</b>, "
        "il lui manque une donnée. Ne jamais le jouer en incompétent.",
        "« La maladie frappe surtout les cadres » : <b>on a lu le document correctement et "
        "on s'est trompé</b>.",
        "Des gens ont bu la même eau sans être malades — ça ressemble à un argument pour Igor, "
        "et ça n'en est pas un : les symptômes mettent <b>une journée</b> à venir."],
       [{"q": "Qu'est-ce qui démolit la conclusion du rapport d'empoisonnement ?",
         "choix": ["Les victimes mangent dans trois réfectoires différents",
                   "Le médecin a refusé de signer",
                   "Les dates ne concordent pas",
                   "Un témoin a vu quelqu'un près des cuisines"],
         "bonne": 0,
         "pourquoi": "Réfectoires B, C et D. <b>Si la cantine était en cause, elles mangeraient "
                     "au même endroit.</b> Le document se contredit tout seul.",
         "ou": "88-empoisonnement.md:34"},
        {"q": "Quelle colonne manque au tableau des victimes — et c'est voulu ?",
         "choix": ["Leur affectation de travail", "Leur âge",
                   "La date des premiers symptômes", "Leur baraquement"],
         "bonne": 0,
         "pourquoi": "Elles travaillent toutes dans la <b>Section D</b>. "
                     "Ne jamais ajouter cette colonne au document : la question doit se poser.",
         "ou": "88-empoisonnement.md:112"},
        {"q": "L'analyse de l'eau du robinet ne donne rien. Pourquoi ?",
         "choix": ["La larve est partie, les résidus sont sur les parois du tuyau",
                   "L'analyse a été truquée",
                   "Ce n'est pas le bon robinet",
                   "Le laboratoire n'a pas le matériel"],
         "bonne": 0,
         "pourquoi": "Il faut <b>faire démonter la tuyauterie</b> pour les trouver "
                     "à l'intérieur.",
         "ou": "88-empoisonnement.md:127"}]),

    _p("sabotages", "Les sabotages", "1932-09/SAB — ouvert, instruit par Igor lui-même",
       "Un saboteur extérieur au complexe, dont la présence resterait à établir. "
       "Aucun suspect identifié ni interrogé. Les pièces n'ont pas été examinées.",
       "<b>Larissa Kazakova</b>, suivi administratif des convois. Trois morts dans sa famille — "
       "mari, fille de 5 ans, fils de 3 ans. Elle frappe <b>la nuit qui précède un convoi "
       "important</b>, et le registre dit lesquels.",
       "<b>La fausse entrée du registre au 27 avril.</b> Zinaida dit ne pas l'avoir vue au dépôt ; "
       "Boris dit qu'il n'a pas tenu le registre ce jour-là ; <b>Anna Vasyukova avoue l'avoir "
       "écrite</b> pour couvrir ce qu'elle croyait être une visite aux tombes. "
       "Et personne ne l'a vue aux tombes : une matinée entière inexpliquée.",
       "Larissa Kazakova. Prise, elle avoue sans regret — sauf celui de n'avoir pas eu le temps.",
       ["<b>Timur Bakhytov, le suspect évident, est innocent.</b> Une table qui cherche un "
        "mécontent le trouve en dix minutes et perd un créneau.",
        "Le saboteur extérieur : thèse d'Igor et de Moskalev, aucun fait derrière.",
        "<b>Le mobile ne suffit pas.</b> La douleur de Larissa ne la désigne pas — sinon "
        "l'enquête se résout par « cherchez qui a le plus souffert ».",
        "Deux homonymies à tenir : Moskalev ≠ Novikoff, et Larissa Kazakova ≠ Maxim Kazakoff."],
       [{"q": "Quel raisonnement fait passer de « trois accidents bizarres » à « un saboteur » ?",
         "choix": ["Les méthodes diffèrent toutes, l'objectif est toujours le même",
                   "Les incidents tombent toujours un mercredi",
                   "Les pièces portent les mêmes marques d'outil",
                   "Un témoin a vu une silhouette"],
         "bonne": 0,
         "pourquoi": "Un moyeu, un harnais, un rail — <b>rien en commun, sauf la conséquence</b> : "
                     "interrompre le transport du minerai.",
         "ou": "80-sabotages.md:62"},
        {"q": "Sur quoi repose tout le dossier des sabotages ?",
         "choix": ["Une fausse entrée au registre des convois, le 27 avril",
                   "Les aveux d'un complice",
                   "Une empreinte sur le rail déformé",
                   "La perquisition du baraquement 5"],
         "bonne": 0,
         "pourquoi": "<b>On ne prend jamais Larissa en défaut. On prend le document en défaut.</b> "
                     "Trois témoins démontent l'entrée, et il reste une matinée inexpliquée.",
         "ou": "85-secteur-transport.md:214"},
        {"q": "Comment prédire la nuit où elle frappera ?",
         "choix": ["Croiser le registre : elle vise les convois lourds",
                   "Elle frappe toutes les six nuits",
                   "Elle suit les nuits sans lune",
                   "C'est impossible, il faut veiller au hasard"],
         "bonne": 0,
         "pourquoi": "Quatre des cinq convois lourds ont été frappés. Des joueurs qui ont lu le "
                     "registre <b>prédisent la bonne nuit</b> ; les autres tirent au sort.",
         "ou": "86-carnet-faddei.md:170"}]),

    _p("pecheur", "Le pêcheur", "aucun dossier — et c'est l'information",
       "Pas d'enquête. C'est un koulak : « quelqu'un qui passe ses nerfs sur un koulak est plutôt "
       "à ranger du côté des Amis de la Révolution. » Le corps sera enterré dans les 24 h.",
       "Piotr Karpenko, retrouvé au petit matin, <b>les membres dans des positions que les "
       "articulations ne permettent pas</b>. Os brisés, vertèbres désaxées — « on dirait que "
       "quelqu'un a joué avec ce corps comme avec une marionnette ».",
       "<b>Obtenir l'autopsie en insistant</b> — personne ne voulait la faire. Elle donne "
       "<b>aucune marque de contrainte</b> et <b>une asphyxie sans noyade</b>. Puis montrer les "
       "résidus à Nesteroff : ce sont les mêmes que sur les autres incidents.",
       "Non nommé. Même substance que la machine et l'empoisonnement.",
       ["La vase — conclusion rapide de Nesteroff, « un peu vite ».",
        "<b>La berge de l'Oural : il n'y a rien à trouver.</b> Le dossier du pêcheur est au "
        "dispensaire, pas là-bas.",
        "S'ils n'insistent pas, le corps part et ne revient pas. <b>Ne pas les relancer.</b>"],
       [{"q": "Le pêcheur est le dossier le moins cher du scénario. Pourquoi ?",
         "choix": ["Son autopsie coûte zéro créneau si on est déjà au dispensaire",
                   "Igor donne le dossier spontanément",
                   "Le corps est à côté des baraquements",
                   "Un témoin raconte tout gratuitement"],
         "bonne": 0,
         "pourquoi": "<b>C'est le moyen le moins cher d'obtenir la substance</b> — à condition "
                     "d'insister pour l'autopsie, que personne ne voulait faire.",
         "ou": "90-creneaux.md:119"},
        {"q": "Qu'est-ce qui ferme toute explication humaine de sa mort ?",
         "choix": ["Aucune marque de contrainte, et une asphyxie sans noyade",
                   "L'absence de témoin", "L'heure du décès", "La position du corps sur la berge"],
         "bonne": 0,
         "pourquoi": "<b>On ne plie pas un homme sans laisser de traces aux points d'appui.</b> "
                     "Et il est asphyxié sans avoir ses poumons pleins d'eau.",
         "ou": "25-lieux-et-presences.md:365"}]),

    _p("culte", "Le culte", "aucun dossier — une soirée, jamais un créneau",
       "Rien. Des rumeurs d'habitants sur « des individus louches qui se déplacent la nuit » — "
       "et les gens précisent que ce ne sont pas les trafiquants. Le gardien de nuit du hangar "
       "est membre : la porte n'est jamais fermée, rien n'est jamais signalé.",
       "Une poignée de familles kazakhes et bachkires autour d'<b>Akmaral</b>, très vieille femme "
       "respectée. <b>Du tengrisme — un chamanisme turco-mongol.</b> Il n'y a rien de surnaturel.",
       "<b>Kassym doit être de la filature.</b> Lui seul peut les identifier pour ce qu'ils sont : "
       "ses parents ont fait appel à des chamans pour soigner des bêtes. S'il n'y est pas, la "
       "table repart avec un culte inquiétant sur les bras — <b>et c'est exactement ce que le "
       "scénario veut</b>.",
       "Personne. Aucun crime. Le danger est l'usage qu'on peut en faire : des boucs émissaires "
       "au moment de rédiger le rapport. <b>Ne jamais le proposer. Ne jamais l'empêcher.</b>",
       ["<b>Le culte entier est la fausse piste</b>, et elle est voulue : elle se referme en dix "
        "minutes."],
       [{"q": "Qui sont réellement les gens du hangar zéro ?",
         "choix": ["Des familles kazakhes et bachkires pratiquant le tengrisme",
                   "Un culte du Mythe", "Les trafiquants de matériel",
                   "Des ouvriers qui jouent aux cartes"],
         "bonne": 0,
         "pourquoi": "Un chamanisme turco-mongol, autour d'Akmaral. <b>Rien de surnaturel</b> — "
                     "des rituels qui paraîtront étranges à des Russes élevés dans la modernité.",
         "ou": "25-lieux-et-presences.md:1330"},
        {"q": "Qu'est-ce qui décide de la manière dont la table comprendra le culte ?",
         "choix": ["La présence ou non de Kassym pendant la filature",
                   "Un jet d'Érudition",
                   "Le nombre de fois qu'ils y retournent",
                   "Le moment de la soirée où ils arrivent"],
         "bonne": 0,
         "pourquoi": "Lui seul peut les identifier. <b>Sans lui, ils repartent avec un culte "
                     "inquiétant</b> — et des boucs émissaires tout trouvés pour le rapport.",
         "ou": "25-lieux-et-presences.md:1336"}]),

    _p("archives", "Les archives", "pas une affaire — un lieu-péage",
       "La procédure demande la signature du Directeur. « J'ai des agents compétents » — "
       "et il ne peut en citer aucun.",
       "<b>Deux dossiers entiers y dorment et n'existent pas avant d'y être allé</b> : les "
       "disparitions de matériel et le meurtre au Komsomol. Dix dossiers dorment dans les "
       "armoires pendant que toute la force d'Igor drague des flaques.",
       "Deux pièces manquent, <b>pour deux raisons opposées</b>. La page d'Oleg Belousoff a été "
       "<b>détruite par Igor</b> ; le rapport d'autopsie de Zina manque parce que "
       "<b>Vinogradoff ne l'a jamais lue</b>. L'incompétence a fait le travail de la "
       "dissimulation.",
       "Igor pour la page détruite. Personne pour l'autopsie.",
       ["Les deux premiers dossiers de l'année manquent à la numérotation — bagarres et larcins "
        "ont leur propre registre.",
        "<b>Ne pas attendre d'écrit de Belousoff</b> : il ne témoignera jamais par écrit."],
       [{"q": "Deux pièces manquent aux archives. Qu'est-ce qui les distingue ?",
         "choix": ["L'une a été détruite par Igor, l'autre n'a jamais été lue",
                   "Elles ont été détruites le même jour",
                   "L'une est au dispensaire, l'autre chez le Directeur",
                   "Les deux ont été volées"],
         "bonne": 0,
         "pourquoi": "La page d'Oleg : <b>malveillance</b>. L'autopsie de Zina : "
                     "<b>incompétence</b> — et elle fait le même travail.",
         "ou": "89-komsomol.md:108"},
        {"q": "En étalant la pile des sept dossiers, qu'est-ce qui trahit Igor sans un mot ?",
         "choix": ["Les quatre clos sont signés à leur date, les trois ouverts tous du 2 mai",
                   "Ils sont tous de la même écriture",
                   "Les numéros ne se suivent pas",
                   "Aucun ne porte de signature"],
         "bonne": 0,
         "pourquoi": "Il les a fait taper <b>la veille du briefing</b>, pour être remis. "
                     "Les dates le trahissent seules.",
         "ou": "70-rapports-imprimes.md:13"}]),

    _p("disparitions", "Les disparitions de matériel", "1932-03/ENT — CLASSÉ, deux pages",
       "« Erreurs de comptage lors des inventaires ou problèmes d'organisation imputables aux "
       "équipes. » Et l'agent Belousoff est réaffecté aux mines au 1<sup>er</sup> avril, "
       "« dans le cadre du rééquilibrage annuel des effectifs ».",
       "Un réseau de vol qui tient : <b>Zykov organise · Nikiforov exécute · Cheskov transporte · "
       "Orloff revend · Igor ferme les yeux</b> contre des livraisons chez lui, à Berezki. "
       "Pas de surnaturel : du vol ordinaire protégé par un chef de police.",
       "Trois entrées, chacune suffisante. <b>Par les papiers</b> : dans une équipe où tout le "
       "monde tourne, Zykov et Nikiforov n'ont jamais bougé en dix-huit mois. <b>Par les gens</b> : "
       "Zykov dit « c'est mon meilleur », Nikiforov dit « personne n'en veut » — on ne met pas son "
       "meilleur homme à la corvée pendant dix-huit mois. <b>Par la nuit</b> : le convoi du 6 mai, "
       "prélevé la nuit du 6 au 7.",
       "Zykov, Nikiforov, Cheskov, Orloff — et Igor. Orloff s'en sort toujours ; "
       "<b>ce qu'il donne, c'est Igor</b>.",
       ["« Trop de temps a passé, ils sont tous partis » : piège explicite. "
        "<b>La rotation est l'indice, pas l'obstacle.</b>",
        "Vassili Petrov n'est pas une piste — mutation ordinaire, et un créneau perdu.",
        "Yelena Nikitina n'est pas coupable, et elle ne mettra jamais rien par écrit."],
       [{"q": "Dans une équipe où tout le monde tourne, qu'est-ce qui désigne les coupables ?",
         "choix": ["Deux hommes n'ont jamais bougé en dix-huit mois",
                   "Trois absences le même jour",
                   "Un nom qui revient dans les plaintes",
                   "Les signatures manquantes sur les bordereaux"],
         "bonne": 0,
         "pourquoi": "Et sur les cinq dates de plainte, <b>Nikiforov est le seul nom présent "
                     "à chaque fois</b>. Le recoupement que personne n'a fait, pas même Oleg.",
         "ou": "87-disparitions.md:75"},
        {"q": "Interrogés séparément, Zykov et Nikiforov se contredisent. Sur quoi ?",
         "choix": ["Le sens du poste : une faveur pour l'un, une corvée pour l'autre",
                   "La date du dernier convoi",
                   "Le nom de leur chef d'équipe",
                   "Le contenu des caisses"],
         "bonne": 0,
         "pourquoi": "« C'est mon meilleur » contre « personne n'en veut ». Plausibles "
                     "séparément, <b>elles s'annulent ensemble</b>. Nikiforov craque le premier.",
         "ou": "87-disparitions.md:171"},
        {"q": "Que change la découverte qu'une page a été retirée du dossier ?",
         "choix": ["On n'enquête plus sur un vol, on tient un chef de section",
                   "Le dossier devient inutilisable",
                   "Il faut la signature du Directeur",
                   "Belousoff accepte de témoigner par écrit"],
         "bonne": 0,
         "pourquoi": "C'est la bascule de <b>nature</b> du dossier. Et le tampon CLASSÉ affirme "
                     "une clôture sur un dossier dont une page a été arrachée.",
         "ou": "87-disparitions.md:341"}]),

    _p("komsomol", "Le meurtre au Komsomol", "1932-06/MRT — Zina Krylova · CLASSÉ",
       "Maxim Kazakoff est coupable : une photo de la victime, une mèche de cheveux et une "
       "cordelette tachée de sang chez lui. Jugé le 2 mai, départ au goulag le 9.",
       "<b>Grigori Novikoff</b>, 22 ans, komsomolets modèle, à la tête d'un groupe qui terrorise "
       "les plus faibles. Zina l'a surpris en pleine agression, a sauvé <b>Macha Fenenka</b>, "
       "et l'a prévenu qu'elle parlerait. Il a paniqué — <b>et il n'était pas seul</b>.",
       "<b>La copie de l'autopsie, au dispensaire</b> : la tenue simultanée des deux poignets est "
       "difficilement compatible avec une strangulation par un seul homme. "
       "<b>Maxim était seul, et il fallait être deux.</b>",
       "Grigori Novikoff, avec <b>Tolia Zaïtsev</b> qui tenait les poignets. Maxim est innocent.",
       ["La cordelette <b>ne prouve rien</b> : objet banal, n'importe qui a pu l'y mettre. "
        "La photo et la mèche sont vraies et innocentes — Maxim aimait bien Zina, qui le "
        "défendait contre les brimades.",
        "Avdotya Kuzmina : rivale imaginée <b>parce que c'était commode</b>. Quatre jours de "
        "détention pour rien.",
        "L'espionnage étranger : c'est là que partent les komsomoltsy si on les interroge "
        "<b>avant</b> Avdotya.",
        "<b>Vinogradoff n'est pas corrompu, il est satisfait</b> — et c'est pire."],
       [{"q": "Qu'est-ce qui prouve que Maxim Kazakoff n'a pas pu agir seul ?",
         "choix": ["L'autopsie : les deux poignets étaient tenus",
                   "Il a un alibi pour la soirée",
                   "La victime était plus forte que lui",
                   "Deux témoins l'ont vu ailleurs"],
         "bonne": 0,
         "pourquoi": "Le légiste l'écrit en réserve professionnelle. <b>La pièce est au "
                     "dispensaire, le dossier n'a que le renvoi.</b>",
         "ou": "89-komsomol.md:105"},
        {"q": "Comment les joueurs apprennent-ils que cette autopsie existe ?",
         "choix": ["Nesteroff râle, au deuxième passage, sans qu'on demande rien",
                   "Le renvoi figure au dossier d'archives",
                   "Vinogradoff finit par l'avouer",
                   "Avdotya Kuzmina en parle"],
         "bonne": 0,
         "pourquoi": "« J'ai rendu un rapport il y a un mois. Personne n'est venu le chercher. » "
                     "<b>Dit une fois, jamais répété.</b>",
         "ou": "89-komsomol.md:128"},
        {"q": "Sans quel témoin le détail du légiste reste-t-il sans débouché ?",
         "choix": ["Tolia Zaïtsev, le complice, séparé de Grigori",
                   "Macha Fenenka", "Avdotya Kuzmina", "Le médecin légiste lui-même"],
         "bonne": 0,
         "pourquoi": "Comme Nikiforov, <b>il casse une fois séparé de son chef — et il demande "
                     "ce qu'il risque</b>. C'est lui qui fait tomber Grigori.",
         "ou": "89-komsomol.md:217"},
        {"q": "Pourquoi les victimes de Grigori n'ont-elles jamais été crues ?",
         "choix": ["Son image de modèle suffisait à les discréditer",
                   "Elles n'ont jamais parlé",
                   "Les responsables étaient complices",
                   "Elles avaient peur de la police"],
         "bonne": 0,
         "pourquoi": "<b>La bascule n'est pas matérielle, elle est d'autorité</b> : "
                     "devant la Guépéou, l'image ne vaut plus rien.",
         "ou": "89-komsomol.md:232"}]),
]


# ══════════════════════════════════════════════════════════════════
#  3. Les comptes
# ══════════════════════════════════════════════════════════════════

COMPTES = [
    {"id": "creneaux", "nom": "Les créneaux", "role": "huit pour dix pistes",
     "lieuLabel": "La règle", "lieu": "<b>Un lieu travaillé = une demi-journée.</b> Coût fixe, "
                                      "pas de négociation. Ils annoncent où ils vont, "
                                      "on coche une case. <b>Un lieu, pas une action, pas un "
                                      "dossier, pas un interlocuteur.</b>",
     "sait": ["Deux créneaux par jour. Le jour 1 part en arrivée et briefing : "
              "restent quatre jours pleins, soit <b>huit créneaux</b> — et dix pistes.",
              "Deux personnes au même endroit coûtent un créneau. <b>Dix aussi.</b>",
              "<b>Trois lieux seulement portent plusieurs dossiers</b> : le dispensaire, "
              "les archives, le bloc 27. Partout ailleurs, un lieu = un dossier.",
              "On prépare en dossiers, <b>on arbitre en lieux</b>."],
     "cache": ["<b>Quatre actions seulement coûtent plus d'un créneau</b> : Berezki (un créneau "
               "entier, rien d'autre) · les mines (idem) · les archives par la voie officielle "
               "(un créneau + une journée d'attente) · faire exhumer le noyé (un créneau, "
               "puis un second le lendemain). Tout le reste coûte un créneau et un seul.",
               "<b>Gratuit</b> : tous les trajets en ville · les trois soirées · le pêcheur "
               "si on est déjà au dispensaire · enquêter sur Igor (six sources) · "
               "le message de Kelley."],
     "questions": [
        {"q": "Combien de créneaux d'enquête pour combien de pistes ?",
         "choix": ["Huit créneaux, dix pistes", "Dix créneaux, dix pistes",
                   "Huit créneaux, huit pistes", "Douze créneaux, dix pistes"],
         "bonne": 0,
         "pourquoi": "Quatre jours pleins à deux demi-journées. "
                     "<b>C'est l'arbitrage central de l'acte 1</b>, et il sort tout seul "
                     "des chiffres.",
         "ou": "50-temporalite.md"},
        {"q": "Ils se séparent en deux groupes. Combien ça coûte ?",
         "choix": ["Deux lieux pour un seul créneau", "Deux créneaux",
                   "Un créneau et demi", "C'est interdit"],
         "bonne": 0,
         "pourquoi": "Le temps fictif ne double pas. <b>C'est le meilleur gain du jeu</b>, "
                     "et il se paie en sécurité et en compétences.",
         "ou": "50-temporalite.md"},
        {"q": "Ils retournent sur un lieu déjà visité. Combien ?",
         "choix": ["Un créneau plein", "Un demi-créneau", "Gratuit", "Deux créneaux"],
         "bonne": 0,
         "pourquoi": "Ils y retournent parce qu'ils ont une nouvelle question. <b>Ça se paie.</b>",
         "ou": "50-temporalite.md"},
        {"q": "Quels sont les trois lieux qui portent plusieurs dossiers ?",
         "choix": ["Le dispensaire, les archives, le bloc 27",
                   "Les entrepôts, la gare, le Komsomol",
                   "Le palais, le poste de police, Berezki",
                   "Le dispensaire, la gare, les mines"],
         "bonne": 0,
         "pourquoi": "Partout ailleurs, un lieu = un dossier : les deux comptes donnent le même "
                     "résultat. <b>Toute la différence tient sur ces trois lignes.</b>",
         "ou": "50-temporalite.md"},
        {"q": "Un créneau au dispensaire bien mené en vaut combien ?",
         "choix": ["Trois", "Deux", "Un", "Quatre"],
         "bonne": 0,
         "pourquoi": "C'est le meilleur rendement du scénario : quatre dossiers y passent, "
                     "plus deux lignes sur Igor et Akim.",
         "ou": "90-creneaux.md:61"},
        {"q": "Ils attendent une signature ou un corps. Que se passe-t-il ?",
         "choix": ["Le créneau est perdu, mais ils peuvent faire autre chose",
                   "Le créneau est gratuit",
                   "Ils sont bloqués sur place",
                   "Ça coûte deux créneaux"],
         "bonne": 0,
         "pourquoi": "<b>Ne pas les enfermer</b> : l'attente se mène ailleurs.",
         "ou": "50-temporalite.md"}]},

    {"id": "calendrier", "nom": "Le calendrier", "role": "du 26 avril au 20 mai",
     "lieuLabel": "Le cadre", "lieu": "Mandat de <b>trois semaines</b>, aller-retour compris. "
                                      "Sept jours de train dans chaque sens, sept jours sur "
                                      "place. Départ de Moscou le 26 avril au soir, échéance "
                                      "le 17 mai.",
     "sait": ["<b>3 mai</b> — arrivée le matin, briefing l'après-midi, "
              "<b>l'effondrement le soir</b>.",
              "<b>4 au 7 mai</b> — deux créneaux par jour. Kassym manque au rendez-vous le 4. "
              "Le déblaiement court sur ces quatre jours.",
              "<b>7 mai au soir</b> — la galerie est rouverte. Aucun survivant de l'autre côté.",
              "<b>8 mai</b> — la descente. Dernier jour où elle ne coûte que trois jours "
              "de retard.",
              "<b>9 mai</b> — Maxim part pour le goulag. S'ils ne sont pas descendus, "
              "Akim remonte au petit matin.",
              "<b>10 mai au soir</b> — dernier départ possible pour tenir l'échéance."],
     "cache": ["<b>13 mai</b> — la sortie dans le lit de l'Oural. Une trentaine d'heures vécues, "
               "cinq jours facturés.",
               "<b>17 mai</b> — l'échéance. Ils n'y sont pas.",
               "<b>20 mai</b> — l'arrivée réelle. Trois jours de retard.",
               "<b>Ces trois dates ne figurent pas sur la feuille du temps</b> : les cinq jours "
               "volés ne doivent pas être prévisibles."],
     "questions": [
        {"q": "Combien de temps dure le déblaiement de la galerie ?",
         "choix": ["Quatre jours", "Deux jours", "Une semaine", "Six jours"],
         "bonne": 0,
         "pourquoi": "Du soir du 3 mai au soir du 7. <b>C'est lui qui fixe la longueur de "
                     "l'acte 1.</b>",
         "ou": "50-temporalite.md:39"},
        {"q": "Que tombe-t-il le soir même de leur arrivée ?",
         "choix": ["L'effondrement de la mine", "Le corps du pêcheur",
                   "La mort de Kurbanoff", "Le départ de Maxim"],
         "bonne": 0,
         "pourquoi": "Arrivée le matin, briefing l'après-midi, <b>effondrement le soir</b>. "
                     "Le jour 1 ne donne aucun créneau.",
         "ou": "50-temporalite.md:27"},
        {"q": "Que montre la feuille du temps, et que cache-t-elle ?",
         "choix": ["Elle s'arrête au 10 mai : ni le 13, ni le 17, ni le 20",
                   "Elle montre tout le calendrier jusqu'au retour",
                   "Elle ne montre que les quatre jours d'enquête",
                   "Elle porte la descente mais pas la sortie"],
         "bonne": 0,
         "pourquoi": "<b>Les cinq jours volés ne doivent pas être prévisibles.</b> "
                     "La ligne du retour y est : départ le 10, arrivée le 17.",
         "ou": "50-temporalite.md:253"},
        {"q": "Que se passe-t-il le 9 mai s'ils ne sont pas descendus ?",
         "choix": ["Akim Korolyoff remonte seul au petit matin",
                   "La galerie se referme",
                   "Le Directeur les convoque",
                   "Kassym descend sans eux"],
         "bonne": 0,
         "pourquoi": "Et le même jour, Maxim Kazakoff part pour le goulag.",
         "ou": "50-temporalite.md:33"}]},

    {"id": "distances", "nom": "Les distances", "role": "ce qui se marche, ce qui se paie",
     "lieuLabel": "La règle", "lieu": "<b>Tous les trajets en ville sont gratuits.</b> "
                                      "Le lieu le plus éloigné est à dix-sept minutes de marche. "
                                      "Seuls les mines et Berezki se paient.",
     "sait": ["<b>Berezki</b> — 8 km, deux heures de marche dans chaque sens. "
              "Un créneau entier, et rien d'autre.",
              "<b>Les mines du mont Magnitnaïa</b> — 5 km, une heure et quart. Idem.",
              "La ville fait <b>2,3 km</b> de large."],
     "cache": ["Depuis le baraquement : le dispensaire à 3 min · la berge de l'Oural à 5 min · "
               "la Guépéou et le bloc 27 à 8 min · le Komsomol à 8 min · la yourte de Kassym "
               "à 10 min · le lac du noyé à 11 min · le bureau d'études, le hangar zéro et le "
               "palais à 15 min · <b>les entrepôts à 17 min</b>, le plus loin.",
               "Le Komsomol : <b>un seul créneau couvre les deux bâtiments</b>, "
               "séparés par vingt mètres."],
     "questions": [
        {"q": "Quels sont les deux seuls lieux dont le trajet coûte un créneau entier ?",
         "choix": ["Berezki et les mines", "Les entrepôts et la gare",
                   "Le palais et Berezki", "Les mines et le lac"],
         "bonne": 0,
         "pourquoi": "8 km et 5 km. <b>Tout le reste est en ville</b>, et le plus éloigné "
                     "est à dix-sept minutes.",
         "ou": "50-temporalite.md:78"}]},

    {"id": "acte2", "nom": "Sous terre", "role": "l'acte 2, ce qui se compte",
     "lieuLabel": "Le cadre", "lieu": "Trois à cinq heures de jeu, une quinzaine de scènes, "
                                      "<b>trois strates</b> — et <b>une bougie par strate</b>. "
                                      "Le changement de bougie est l'entracte.",
     "sait": ["<b>Seize étapes</b> entre le campement et le Nexus, un test de Torche à chacune : "
              "sept en première strate, quatre en deuxième, cinq en troisième.",
              "<b>Onze disparus</b>, plus deux morts dans l'effondrement lui-même. "
              "<b>Kassym perd six personnes</b> : père, oncle, mère, deux frères, sa sœur.",
              "<b>Deux survivants</b> : Akim Korolyoff, jambe cassée et fou de douleur, "
              "et Dmitri Volkoff, fou et connecté aux créatures.",
              "<b>Trois jets d'horreur, et trois seulement</b> : la peinture, le corps "
              "d'Anatoli, le double temporel.",
              "Une trentaine d'heures vécues sous terre, <b>cinq jours en surface</b>."],
     "cache": ["La montre tient un jour et demi à remontage manuel, et <b>trois dérèglements "
               "sont prévus, un par strate</b>.",
               "Quand le dé de Torche tombe, <b>tu souffles sur la bougie</b>. Rien à annoncer."],
     "questions": [
        {"q": "Combien d'étapes entre le campement et le Nexus ?",
         "choix": ["Seize", "Douze", "Vingt", "Huit"],
         "bonne": 0,
         "pourquoi": "Sept en première strate, quatre en deuxième, cinq en troisième — "
                     "un test de Torche à chacune.",
         "ou": "src/note-magnitogorsk/30-chiffres.md:49"},
        {"q": "Combien de personnes Kassym perd-il dans l'acte 2 ?",
         "choix": ["Six", "Quatre", "Deux", "Onze"],
         "bonne": 0,
         "pourquoi": "Son père, son oncle, sa mère, deux frères et sa sœur. "
                     "Quatre sont parmi les onze disparus, <b>deux sont morts dans "
                     "l'effondrement lui-même</b>.",
         "ou": "100-acte2-cadrage.md:35"},
        {"q": "Combien de jets d'horreur dans tout l'acte 2 ?",
         "choix": ["Trois", "Un par strate, soit trois, plus les rencontres",
                   "Autant que de scènes marquantes", "Cinq"],
         "bonne": 0,
         "pourquoi": "<b>Trois, et trois seulement</b> : la peinture, le corps d'Anatoli, "
                     "le double temporel. Le budget d'horreur est fixé.",
         "ou": "100-acte2-cadrage.md:229"},
        {"q": "Que fais-tu quand le dé de Torche tombe ?",
         "choix": ["Tu souffles sur la bougie, sans rien annoncer",
                   "Tu annonces que la lumière faiblit",
                   "Tu fais éteindre une frontale",
                   "Tu changes de strate"],
         "bonne": 0,
         "pourquoi": "Rien à dire. <b>La lumière le dit.</b> "
                     "(Faire éteindre une frontale, c'est la limite invisible de la strate 2.)",
         "ou": "100-acte2-cadrage.md:117"}]},

    {"id": "epilogue", "nom": "Le retour", "role": "l'acte 3 et l'épilogue",
     "lieuLabel": "Le cadre", "lieu": "L'acte 3 dure <b>une heure, action 5/5</b>. "
                                      "L'épilogue en demande une autre — dont une heure de "
                                      "discussion entre joueurs.",
     "sait": ["Les larves les suivent avec <b>une minute d'avance en moyenne</b>.",
              "S'ils courent tout droit : quatre étapes, et la dernière est "
              "<b>la mort du groupe entier</b>.",
              "<b>Quatre événements</b> : la rencontre, le labyrinthe, la vision, le gouffre.",
              "Le rapport se rend <b>en main propre, dans deux jours</b>.",
              "<b>Cinq dossiers</b> sur la table d'Igor au briefing — mais quatre seulement "
              "ont motivé le signalement : le cinquième, les sabotages, c'est Igor qui l'ajoute."],
     "cache": ["<b>Les deux monnaies de l'épilogue</b> : Larissa, qui ferme un dossier, "
               "et le dossier Igor issu des disparitions, qui fait tomber un homme.",
               "Les cinq jours volés <b>ne coûtent pas du temps d'enquête : ils coûtent le "
               "délai</b>. Il n'y a rien à faire contre."],
     "questions": [
        {"q": "Que leur a-t-on réellement commandé ?",
         "choix": ["Vérifier s'il y a sabotage et traîtrise, et juger le chef de la police",
                   "Résoudre les dix dossiers",
                   "Enquêter sur la disparition de Tkachenko",
                   "Faire un état des lieux du complexe"],
         "bonne": 0,
         "pourquoi": "Quatre incidents ont motivé le signalement, et <b>le cinquième dossier "
                     "est ajouté par Igor lui-même</b>. Les cinq autres, ils les découvrent "
                     "en route : rien ne les oblige.",
         "ou": "105-epilogue-rapport.md:68"},
        {"q": "Quelles sont les deux monnaies d'échange de l'épilogue ?",
         "choix": ["Larissa et le dossier contre Igor",
                   "Maxim Kazakoff et Grigori Novikoff",
                   "Les archives et le carnet de Faddei",
                   "Le culte et les étrangers"],
         "bonne": 0,
         "pourquoi": "L'une <b>ferme un dossier</b>, l'autre <b>fait tomber un homme</b>. "
                     "C'est ce qu'ils ont à poser sur la table.",
         "ou": "90-creneaux.md:100"},
        {"q": "S'ils courent tout droit vers la sortie, dans l'acte 3 ?",
         "choix": ["Coincés entre deux hordes : mort de tout le groupe",
                   "Ils sortent épuisés mais vivants",
                   "Ils perdent un personnage",
                   "Ils se perdent et doivent revenir"],
         "bonne": 0,
         "pourquoi": "Quatre étapes, et la quatrième ne pardonne pas. "
                     "Les larves ont <b>une minute d'avance en moyenne</b>.",
         "ou": "104-acte3-fuite.md:50"}]},
]


MODULES = {
    "gens": {"titre": "Les gens",
             "quoi": "Qui est qui, ce qu'il sait, ce qu'il tait, et ce qu'il dit des autres.",
             "fiches": GENS},
    "pistes": {"titre": "Les pistes",
               "quoi": "Pour chacune : la version d'Igor, la vérité, et ce qui fait basculer.",
               "fiches": PISTES},
    "comptes": {"titre": "Les comptes",
                "quoi": "Le calendrier, les créneaux, les distances, ce qui se compte.",
                "fiches": COMPTES},
}

# ══════════════════════════════════════════════════════════════════
#  Les schémas
# ══════════════════════════════════════════════════════════════════

_JOURS = [("3 mai", "arrivée · briefing", "effondrement le soir", True),
          ("4 mai", "2 créneaux", "déblaiement", False),
          ("5 mai", "2 créneaux", "", False),
          ("6 mai", "2 créneaux", "", False),
          ("7 mai", "2 créneaux", "galerie rouverte le soir", True),
          ("8 mai", "la descente", "", True),
          ("9 mai", "Maxim part", "", False),
          ("10 mai", "dernier départ", "", True)]


def _frise():
    L, H, x0 = 86, 250, 54
    larg = x0 + L * len(_JOURS) + 20
    el = [f'<svg viewBox="0 0 {larg} {H}" xmlns="http://www.w3.org/2000/svg" '
          f'font-family="system-ui, sans-serif" role="img" '
          f'aria-label="Calendrier du 3 au 10 mai 1932">']
    el.append(f'<line x1="{x0 - 14}" y1="96" x2="{larg - 14}" y2="96" '
              f'stroke="#8aa4b2" stroke-width="1.6"/>')
    el.append(f'<rect x="{x0 + L}" y="88" width="{L * 4}" height="16" rx="8" '
              f'fill="#c9a227" opacity=".22"/>')
    el.append(f'<text x="{x0 + L * 3}" y="118" font-size="11" fill="#8a6d3b" '
              f'text-anchor="middle">déblaiement — quatre jours</text>')
    for i, (jour, quoi, note, fort) in enumerate(_JOURS):
        x = x0 + L * i
        el.append(f'<circle cx="{x}" cy="96" r="{6 if fort else 4}" '
                  f'fill="{"#b3271e" if fort else "#34566b"}"/>')
        el.append(f'<text x="{x}" y="72" font-size="13" font-weight="600" fill="#132c3c" '
                  f'text-anchor="middle">{jour}</text>')
        el.append(f'<text x="{x}" y="54" font-size="11" fill="#6b7c88" '
                  f'text-anchor="middle">{quoi}</text>')
        if note:
            for n, bout in enumerate(note.split(" le ")):
                el.append(f'<text x="{x}" y="{146 + n * 15}" font-size="11" fill="#b3271e" '
                          f'text-anchor="middle">{bout}</text>')
    el.append(f'<text x="{x0 - 14}" y="200" font-size="11.5" fill="#6b7c88">'
              f'puis : 13 mai, la sortie · 17 mai, l\'échéance manquée · '
              f'20 mai, trois jours de retard</text>')
    el.append("</svg>")
    return "".join(el)


SCHEMAS = {
    "comptes": [
        {"titre": "Les huit jours",
         "leg": "Les points rouges sont les échéances qu'on ne déplace pas. "
                "La bande jaune est le déblaiement : il finit le 7 au soir, et c'est lui "
                "qui donne sa longueur à l'acte 1.",
         "svg": _frise()},
    ],
}
