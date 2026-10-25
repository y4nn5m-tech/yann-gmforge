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
           "en pleine scène. Neuf modules, à parcourir ou à réviser par questions.")

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

# ── Les seconds rôles ─────────────────────────────────────────────
#
#  Fiche courte : où on le trouve, ce qu'il donne, sa phrase s'il en a
#  une, le piège s'il y en a un. Ils n'ont pas besoin du même appareil
#  qu'Igor ou Nesteroff — mais **l'équipe du transport est sept
#  personnes**, et c'est là qu'on se mélange.


def _c(id, nom, role, lieu, donne, phrase=None, piege=None, q=None):
    f = {"id": id, "nom": nom, "role": role, "lieuLabel": "Où on le trouve", "lieu": lieu,
         "sait": donne}
    if phrase:
        f["replique"] = phrase
    if piege:
        f["piege"] = piege
    if q:
        f["questions"] = q
    return f


GENS += [
    # ── l'équipe du transport — sept personnes à ne pas confondre ──
    _c("moskalev", "Grigori Moskalev", "contremaître des convois",
       "la zone de stockage, un registre à la main — <b>il ne lève pas les yeux</b>. "
       "Il compte pendant qu'on lui parle, perd le fil, recommence.",
       ["<b>Il croit à un saboteur venu de l'extérieur</b> — c'est sa thèse et il la ressort "
        "à chaque fois. Aucun fait derrière.",
        "Agacé qu'on l'interrompe, pas hostile."],
       piege="Ne pas le confondre avec <b>Grigori Novikoff</b>, du Komsomol. "
             "Deux Grigori, et l'un est un meurtrier."),

    _c("udovenko", "Stepan Udovenko", "responsable du hangar aux wagonnets",
       "sous un wagonnet, ou accroupi devant une roue. Il sort pour répondre, "
       "les mains noires, puis il y retourne.",
       ["Professionnel, précis, méfiant qu'on touche à son matériel. "
        "Faddei lui fait confiance.",
        "<b>Il tient à la réputation de l'équipe — donc il minimise, par loyauté "
        "et non par calcul.</b>"]),

    _c("anna", "Anna Vasyukova", "ouvrière administrative",
       "assise au bureau, <b>à côté de Larissa</b>. Elle recopie des colonnes, "
       "de l'encre sur les doigts.",
       ["<b>C'est elle qui a écrit la fausse entrée au registre</b>, de sa propre initiative, "
        "pour couvrir ce qu'elle croyait être une visite au carré des tombes.",
        "Polie, nerveuse — <b>elle cherche l'approbation de quelqu'un en répondant</b>. "
        "Et elle sait de quoi il s'agit dès qu'on aborde le sujet."],
       phrase="« Elle m'a rien demandé. Je l'ai fait. »",
       q=[{"q": "Qui a écrit la fausse entrée du registre au 27 avril ?",
           "choix": ["Anna Vasyukova, de sa propre initiative",
                     "Larissa Kazakova elle-même",
                     "Boris Shcherbakov, chargé des présences",
                     "Faddei Nikitine, pour couvrir son équipe"],
           "bonne": 0,
           "pourquoi": "Elle croyait couvrir une visite au carré des tombes. "
                       "<b>C'est le premier élément qui désigne Larissa</b> — "
                       "et personne ne l'y a vue, aux tombes.",
           "ou": "85-secteur-transport.md:258"}]),

    _c("timur", "Timur Bakhytov", "conducteur de convoi",
       "<b>introuvable entre 8 h et 17 h</b> — il est sur la route. On ne l'attrape qu'au "
       "petit matin pendant l'attelage, ou le soir au retour, épuisé.",
       ["Il se plaint : des quotas, de la sécurité, de Faddei qui pousse.",
        "<b>Il est le suspect évident et il est innocent</b> — et il ne se rend pas compte "
        "qu'il se désigne."],
       piege="Une table qui cherche un mécontent le trouve en dix minutes et perd un créneau. "
             "<b>S'ils l'accusent, Igor est ravi, Timur part au bloc 27 — et un sabotage "
             "de plus tombe pendant qu'il y est.</b>",
       q=[{"q": "Les joueurs font arrêter Timur Bakhytov. Que se passe-t-il ?",
           "choix": ["Un sabotage de plus tombe pendant qu'il est au bloc 27",
                     "Il avoue sous la pression",
                     "Larissa prend peur et s'arrête",
                     "Igor refuse de l'incarcérer"],
           "bonne": 0,
           "pourquoi": "<b>C'est la preuve de son innocence, et elle coûte cher.</b> "
                       "Igor, lui, est ravi d'avoir un coupable.",
           "ou": "85-secteur-transport.md:321"}]),

    _c("zinaida", "Zinaida Plotnikova", "entretien des bêtes de somme",
       "au hangar, en train de panser un cheval ou de curer une stalle. "
       "Elle parle en travaillant, <b>sans se retourner</b>.",
       ["<b>C'est elle qui a vu Larissa partir vers les écuries</b> le 27 au matin — "
        "et elle le dira si on pose la question, <b>sans y attacher d'importance</b>.",
        "Directe, concrète, pas impressionnée par des gens de Moscou."]),

    _c("boris", "Boris Shcherbakov", "entretien des voies",
       "dehors, sur les voies, à plusieurs kilomètres. <b>Le plus difficile à trouver</b> : "
       "une demi-journée pour aller le chercher, ou l'attendre le soir.",
       ["<b>C'est lui que Faddei avait chargé de noter les présences</b> — et il dira qu'il "
        "ne l'a pas fait, <b>sans comprendre que c'est important</b>.",
        "Taciturne. Il répond par phrases courtes."],
       q=[{"q": "Boris Shcherbakov est le plus dur à atteindre. Combien coûte-t-il ?",
           "choix": ["Une demi-journée si on va le chercher, gratuit le soir",
                     "Un créneau entier", "Rien, il est au hangar",
                     "Deux créneaux, il est à 8 km"],
           "bonne": 0,
           "pourquoi": "Il est sur les voies à plusieurs kilomètres. "
                       "<b>L'attendre le soir ne coûte rien.</b>",
           "ou": "25-lieux-et-presences.md:66"}]),

    _c("bondarenko", "Yuri Bondarenko", "chargement et déchargement",
       "<b>en train de porter quelque chose, toujours.</b> Il ne peut pas s'arrêter sans que "
       "la chaîne s'arrête. Il répond entre deux charges, essoufflé.",
       ["Fataliste, amical. Proche de Zinaida Plotnikova.",
        "<b>Il a peur de perdre son poste</b> si on le retient trop longtemps."]),

    # ── le Komsomol ───────────────────────────────────────────────
    _c("avdotya", "Avdotya Kuzmina", "komsomolka, à l'entraînement",
       "le gymnase. <b>Détenue quatre jours pour rien</b> par Vinogradoff, qui l'avait "
       "imaginée rivale parce que c'était commode.",
       ["Elle dément la rivalité, et son alibi est confirmé par Messelier.",
        "<b>Elle donne la clé</b> : Zina s'était absentée en début d'après-midi et comptait "
        "s'entraîner plus tard que d'habitude ce soir-là."],
       piege="<b>Il faut lui parler en premier.</b> Interroger les komsomoltsy sans cette "
             "préparation ne donne rien : ils partent sur l'espionnage et l'agent de l'Ouest.",
       q=[{"q": "Par qui faut-il commencer, au Komsomol ?",
           "choix": ["Avdotya Kuzmina", "Grigori Novikoff, qui vient au-devant d'eux",
                     "Les responsables", "Macha Fenenka"],
           "bonne": 0,
           "pourquoi": "Sans elle, les komsomoltsy partent sur l'espionnage et l'agent de "
                       "l'Ouest. <b>L'ordre des créneaux compte.</b>",
           "ou": "25-lieux-et-presences.md:699"}]),

    _c("sofia", "Sofia Lysenka", "komsomolka",
       "au réfectoire ou au bâtiment principal",
       ["<b>L'échange d'horaires</b> : elle a parlé à Zina cet après-midi-là. Deuxième maillon "
        "de la reconstitution, entre Maxim et Grigori."]),

    _c("maxim", "Maxim Kazakoff", "le condamné du meurtre — et il est innocent",
       "le bloc 27. <b>Il part au goulag le 9 mai.</b>",
       ["Handicapé mental, <b>maltraité par les gardes</b>, et sa détresse est manifeste.",
        "Il réfute sa culpabilité et <b>il est incapable de formuler une défense</b> ou de "
        "donner la moindre piste.",
        "Il aimait bien Zina, <b>qui le défendait contre les brimades</b> — la photo et la "
        "mèche trouvées chez lui sont vraies et innocentes."],
       piege="<b>La scène la plus dure du scénario, et elle ne demande aucun jet.</b> "
             "Ne pas la jouer pour arracher une larme : platement, un homme qui ne comprend "
             "pas, des gardes qui s'en amusent, <b>et un quart d'heure qui ne donne rien</b>.",
       q=[{"q": "Que rapporte la visite à Maxim Kazakoff, au bloc 27 ?",
           "choix": ["Rien — et il faut la laisser ne rien rapporter",
                     "Il désigne Grigori Novikoff",
                     "Il décrit la cordelette",
                     "Il donne un alibi vérifiable"],
           "bonne": 0,
           "pourquoi": "Il ne comprend pas ce qu'on lui reproche, et il a signé. "
                       "<b>C'est à eux de décider s'ils ont un créneau à dépenser pour ça.</b>",
           "ou": "25-lieux-et-presences.md:605"}]),

    _c("ingenieurs", "Sorokin et Malysheff", "les deux ingénieurs de la machine",
       "le bloc 27, inculpés de négligence, en attente de jugement",
       ["Leur explication : quelque chose est entré dans les canalisations, un bouchon, "
        "montée en pression. <b>Du limon autour d'une branche</b> — le fleuve sert de "
        "décharge en amont.",
        "<b>Mais les grilles sont en place</b>, et une vérification le confirme.",
        "Sur les bruits suraigus : du métal sous pression, de la paréidolie — "
        "<b>ils n'étaient pas présents et ne les ont pas entendus</b>."],
       piege="<b>Ne pas les jouer en imbéciles.</b> Deux hommes compétents et honnêtes qui "
             "construisent la meilleure explication possible à partir de données incomplètes — "
             "exactement comme Nesteroff. Montrez-leur les résidus : ils regardent, ils "
             "réfléchissent, et ils disent qu'ils ne savent pas. <b>C'est la réponse d'un bon "
             "ingénieur.</b>"),

    # ── les étrangers, le culte, l'acte 2 ─────────────────────────
    _c("may", "Ernst May", "l'architecte du bureau d'études",
       "son bureau, des plans partout — <b>il reçoit volontiers</b>",
       ["Le portrait de Pavel Tkachenko : intelligent, compétent, réservé et anxieux.",
        "<b>Et un détail qu'il ne mesure pas</b> : « Je l'ai engagé moi-même, pour ses travaux "
        "à Petrograd » — il dit <b>« pour le gouvernement tsariste »</b> sans y penser."],
       piege="<b>Il livre une pièce à charge en croyant faire un éloge.</b> Avoir travaillé "
             "pour le gouvernement tsariste, en 1932, c'est un dossier — et un étranger ne "
             "mesure pas ce que ça pèse.",
       q=[{"q": "Qu'est-ce qu'Ernst May livre sans s'en rendre compte ?",
           "choix": ["Que Pavel a travaillé pour le gouvernement tsariste",
                     "Que Pavel préparait sa fuite",
                     "Que Pavel était en contact avec l'étranger",
                     "Que Pavel détestait Igor"],
           "bonne": 0,
           "pourquoi": "Il le dit en faisant son éloge. <b>En 1932, c'est un dossier</b>, "
                       "et c'est aux joueurs de décider ce qu'ils en font.",
           "ou": "25-lieux-et-presences.md:877"}]),

    _c("kelley", "Matthew Kelley", "un étranger de Berezki",
       "chez lui, <b>et il a bu</b> — c'est son état par défaut. Son message arrive devant "
       "leur baraquement le soir, gratuitement ; aller le voir coûte le créneau.",
       ["<b>Il a vu la créature.</b> Il ne sait plus exactement où, sa description est floue — "
        "parce qu'il était ivre, <b>et parce que la chose n'a pas de forme stable</b>.",
        "Sur place, rien : le sol est meuble à cause du dégel, piétiné toute la journée."],
       piege="<b>C'est le seul témoignage exact de tout l'acte 1, et il est inutilisable.</b> "
             "Les étrangers disent « il boit, il a toujours bu » — et c'est vrai, et ça ne "
             "suffit pas. Garder ça pour l'acte 2 : quand ils auront vu, <b>c'est Kelley "
             "qu'ils se rappelleront</b>.",
       q=[{"q": "À quoi sert le témoignage de Matthew Kelley ?",
           "choix": ["À rien dans l'acte 1 — il servira à l'acte 2, de mémoire",
                     "À localiser la créature",
                     "À prouver que les étrangers mentent",
                     "À obtenir la substance noire"],
           "bonne": 0,
           "pourquoi": "<b>Le seul témoignage exact de l'acte 1, et personne ne peut le "
                       "croire.</b> Quand ils auront vu, c'est lui qu'ils se rappelleront.",
           "ou": "25-lieux-et-presences.md:1011"}]),

    _c("akmaral", "Akmaral", "la très vieille femme du hangar zéro",
       "le hangar zéro, la nuit, avec une poignée de familles kazakhes et bachkires",
       ["Respectée, héritière de savoirs ancestraux. <b>Du tengrisme — un chamanisme "
        "turco-mongol.</b>",
        "<b>Il n'y a rien de surnaturel</b> : des rituels qui paraîtront étranges à des Russes "
        "élevés dans la modernité."],
       piege="<b>Elle et ses familles sont la réponse facile</b> au moment de rédiger le "
             "rapport, et elle est à portée de main. Ne jamais le proposer. "
             "Ne jamais l'empêcher."),

    _c("survivants", "Akim Korolyoff et Dmitri Volkoff", "les deux survivants de l'acte 2",
       "sous terre. <b>Akim</b> au fond du puits, jambe cassée, fou de douleur, mutique de "
       "longues minutes. <b>Dmitri</b>, le frère de Kassym, dans la troisième strate.",
       ["Akim remonte seul au petit matin du 9 mai <b>s'ils ne sont pas descendus</b>.",
        "Dmitri est <b>vivant, fou, et connecté aux créatures</b>. Il meurt en une dizaine "
        "de secondes."]),
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


# ══════════════════════════════════════════════════════════════════
#  0. Le socle — ce qui tient tout le reste
# ══════════════════════════════════════════════════════════════════

SOCLE = [
    {"id": "mission", "nom": "La mission", "role": "trois niveaux, à ne pas confondre",
     "lieuLabel": "Ce qu'on leur dit à Moscou",
     "lieu": "<i>« Enquêter sur des incidents récents susceptibles d'être liés à des actes "
             "de sabotage. »</i> Une mission contre <b>les ennemis du peuple</b>, "
             "<b>trois semaines aller-retour compris</b> — et <b>aucun incident n'est "
             "nommé</b>.",
     "sait": ["<b>La vraie raison, qu'ils ignorent</b> : les doutes du Directeur sur "
              "l'efficacité et la fidélité d'Igor Pavlenko. La Guépéou, jugeant peu probable "
              "qu'il soit un traître, <b>profite de l'occasion pour tester un groupe "
              "d'éléments extérieurs en cours d'évaluation</b>.",
              "<b>Ce qu'ils trouvent en arrivant</b> : cinq dossiers sur la table d'Igor. "
              "C'est leur première information concrète.",
              "Quatre de ces cinq ont motivé le signalement — le noyé, le déserteur, la "
              "machine, l'empoisonnement. <b>Le cinquième, les sabotages, Igor l'ajoute "
              "lui-même</b> : c'est le seul qu'il n'avait pas ouvert."],
     "cache": ["Cinq autres pistes se découvrent en route et ne sont dans aucun dossier : "
               "les disparitions de matériel, le meurtre au Komsomol, le pêcheur, Kelley, "
               "le culte. <b>Rien ne les oblige à les mentionner au rapport.</b>"],
     "piege": "Ne jamais laisser entendre que la mission vise Igor. Les joueurs doivent le "
              "déduire de ce qu'il dit, pas l'apprendre d'une confidence.",
     "questions": [
        {"q": "Pourquoi la Guépéou envoie-t-elle vraiment cette équipe ?",
         "choix": ["Pour tester le groupe, en profitant des doutes du Directeur sur Igor",
                   "Parce qu'elle soupçonne un réseau de saboteurs étrangers",
                   "Parce qu'Igor a demandé des renforts",
                   "Pour enquêter sur la disparition de Pavel Tkachenko"],
         "bonne": 0,
         "pourquoi": "Deux choses à la fois : <b>les doutes du Directeur sur Igor</b>, et "
                     "l'occasion d'évaluer des éléments extérieurs. <b>Les PJ ignorent les "
                     "deux.</b>",
         "ou": "105-epilogue-rapport.md"},
        {"q": "Combien de dossiers les attendent sur la table d'Igor au briefing ?",
         "choix": ["Cinq", "Sept", "Trois", "Dix"],
         "bonne": 0,
         "pourquoi": "Cinq. <b>Sept existent</b> — les deux autres dorment aux archives. Et "
                     "le cinquième, les sabotages, est celui qu'Igor ajoute de son propre chef.",
         "ou": "105-epilogue-rapport.md · 70-rapports-imprimes.md"},
        {"q": "Que sait l'équipe des incidents avant d'arriver ?",
         "choix": ["Rien : aucun incident n'est nommé dans l'ordre de mission",
                   "Les cinq dossiers lui ont été transmis à Moscou",
                   "Elle connaît les sabotages, pas le reste",
                   "Le Directeur l'a briefée en détail avant le départ"],
         "bonne": 0,
         "pourquoi": "<b>Rien.</b> Ils découvrent la matière de leur mission dans le bureau "
                     "de l'homme sur lequel ils enquêtent sans le savoir — <b>c'est tout le "
                     "dispositif de l'acte 1</b>.",
         "ou": "105-epilogue-rapport.md"}]},

    {"id": "dispositif", "nom": "Le dispositif", "role": "pourquoi l'acte 1 fonctionne",
     "lieuLabel": "En une phrase",
     "lieu": "Ils enquêtent sur des incidents <b>dans le bureau de l'homme sur lequel ils "
             "enquêtent sans le savoir</b>, et c'est lui qui leur tend les dossiers.",
     "sait": ["<b>Igor se trahit tout seul, au briefing, dès le premier jour.</b> Un homme "
              "qui se défend d'une accusation que personne n'a portée dit tout.",
              "Cinq répliques, <b>espacées, jamais dans la même minute</b>. La plus lourde : "
              "<i>« Le camarade Directeur a ses humeurs. »</i> — <b>il nomme le Directeur "
              "alors que personne ne lui en a parlé.</b>",
              "S'ils n'ont pas réagi, il pose la question lui-même sur le pas de la porte : "
              "<i>« On vous a parlé de moi, à Moscou ? »</i>"],
     "cache": ["<b>Le dossier Igor n'a ni lieu ni créneau</b> : il se construit avec ce que "
               "disent les autres, gratuitement, et il décide de l'épilogue."],
     "piege": "Ne pas le rendre lucide. <b>Igor ne sait pas que sa fiabilité est l'objet "
              "d'un rapport</b> — il craint seulement qu'on ait parlé de lui.",
     "questions": [
        {"q": "Comment le groupe apprend-il qu'il y a une seconde mission ?",
         "choix": ["Igor se défend d'une accusation que personne n'a portée",
                   "Une lettre scellée remise par Voronin· à l'arrivée",
                   "Le Directeur les convoque le deuxième jour",
                   "Gusev· finit par le leur dire"],
         "bonne": 0,
         "pourquoi": "Cinq répliques au briefing, et la dernière <b>nomme le Directeur</b> "
                     "sans que personne l'ait évoqué. Aucune scène supplémentaire.",
         "ou": "40-igor-se-trahit.md"},
        {"q": "Combien de créneaux coûte le dossier sur Igor ?",
         "choix": ["Aucun : il se construit avec ce que disent les autres",
                   "Un créneau aux archives", "Deux, comme les disparitions",
                   "Un créneau par source interrogée"],
         "bonne": 0,
         "pourquoi": "<b>Ni lieu ni créneau.</b> Six sources en parlent gratuitement, et "
                     "c'est ce dossier-là qui décide de l'épilogue.",
         "ou": "91-dossier-igor.md"}]},

    {"id": "verite", "nom": "La vérité", "role": "ce que les joueurs ne sauront peut-être jamais",
     "lieuLabel": "Le phénomène",
     "lieu": "Des <b>larves amorphes</b> vivent sous le site. Elles ne veulent pas la surface : "
             "les humains sont <b>des nuisibles un peu gênants</b>. Rien de ce qui arrive "
             "n'est dirigé contre quiconque.",
     "sait": ["<b>Trois incidents, un seul phénomène</b> : la machine, l'empoisonnement, le "
              "corps du pêcheur. La même substance sur les trois — <b>c'est le seul "
              "recoupement qui ouvre le fond du scénario</b>.",
              "L'empoisonnement : une larve s'est infiltrée <b>volontairement</b> dans une "
              "conduite d'eau potable et y a laissé des résidus. <b>Elle est repartie.</b>",
              "La machine : une larve emportée par le courant, ébouillantée, coincée dans un "
              "coude — <b>la montée en pression a fait exploser les tuyaux</b>."],
     "cache": ["<b>Et la vérité ne les aidera pas.</b> Leur mission est un rapport à la "
               "Guépéou, <i>« celle-ci ne goûtant guère aux élucubrations des illuminés »</i>. "
               "<b>Plus ils descendent, moins leur rapport est crédible.</b>"],
     "piege": "Les trois incidents ne se recoupent que si les joueurs le font. <b>Ne jamais "
              "poser le rapprochement à leur place.</b>",
     "questions": [
        {"q": "Quels incidents partagent la même substance ?",
         "choix": ["La machine, l'empoisonnement et le corps du pêcheur",
                   "La machine, les sabotages et le noyé",
                   "L'empoisonnement, le meurtre au Komsomol et le noyé",
                   "Les quatre incidents du carnet de Faddei"],
         "bonne": 0,
         "pourquoi": "<b>Trois incidents, un seul phénomène.</b> Les sabotages sont humains "
                     "— c'est Larissa — et le noyé est un accident.",
         "ou": "88-empoisonnement.md"},
        {"q": "Que veulent les larves ?",
         "choix": ["Rien des humains : ce sont des nuisibles un peu gênants",
                   "Coloniser la surface", "Se venger de l'exploitation de la mine",
                   "Être découvertes et comprises"],
         "bonne": 0,
         "pourquoi": "Elles ne veulent pas la surface. <b>Ils ne sont pas des ennemis. "
                     "Ils ne sont rien du tout.</b>",
         "ou": "103-acte2-strate3.md · 105-epilogue-rapport.md"}]},
]


# ══════════════════════════════════════════════════════════════════
#  5. Les actes
# ══════════════════════════════════════════════════════════════════

ACTES = [
    {"id": "acte1", "nom": "Acte 1 — l'enquête", "role": "quatre jours, huit créneaux",
     "lieuLabel": "Le régime",
     "lieu": "On choisit où aller, <b>on paie un créneau par lieu</b>, on recoupe. "
             "Investigation 5/5.",
     "sait": ["<b>Huit créneaux pour dix pistes.</b> Le jour 1 part en arrivée et briefing ; "
              "restent quatre jours pleins à deux demi-journées.",
              "<b>On prépare en dossiers, on arbitre en lieux.</b> Trois lieux seulement "
              "portent plusieurs dossiers : le dispensaire, les archives, le bloc 27.",
              "<b>Ce qui le termine</b> : la galerie est rouverte le 7 au soir, et Kassym "
              "demande à descendre. La descente a lieu le 8."],
     "cache": ["<b>Le minimum vital est de treize créneaux</b> pour tout faire — ils en ont "
               "huit. <b>Le scénario est conçu pour qu'ils n'aillent pas partout.</b>"],
     "questions": [
        {"q": "Qu'est-ce qui met fin à l'acte 1 ?",
         "choix": ["La galerie rouverte le 7 au soir, et Kassym qui demande à descendre",
                   "L'épuisement des huit créneaux",
                   "Igor qui les convoque une seconde fois",
                   "L'arrestation de Larissa Kazakova"],
         "bonne": 0,
         "pourquoi": "Quatre jours de déblaiement, galerie rouverte le 7 au soir. "
                     "<b>Kassym demande une fois, et part seul si on refuse.</b>",
         "ou": "100-acte2-cadrage.md · 50-temporalite.md"}]},

    {"id": "acte2", "nom": "Acte 2 — la descente", "role": "trois à cinq heures, trois strates",
     "lieuLabel": "Le régime",
     "lieu": "<b>Une descente linéaire</b>, et aucun des principes de l'acte 1 ne s'y "
             "applique : pas de choix de lieu, pas de créneau. Exploration 4/5, "
             "fantastique 4/5.",
     "sait": ["<b>Rien ne les pousse à aller jusqu'au bout</b> sinon la curiosité des joueurs.",
              "<b>Strate 1, les disparus</b> — la seule où l'horreur est concrète. Deux "
              "branches depuis le campement : A ne mène nulle part et porte tout l'enjeu "
              "humain, B descend.",
              "<b>Strate 2, le déphasage</b> — les tubes en trois phases, le bassin, les "
              "effets de Mœbius, l'attaque du double temporel. Intercaler, jamais enchaîner.",
              "<b>Strate 3, la Grande Galerie</b> — le point de non-retour, Dmitri, la "
              "première larve, le Nexus, puis l'alerte."],
     "cache": ["<b>C'est l'enterrement de la famille de Kassym, un corps à la fois</b>, et "
               "les PJ sont ceux qui les trouvent. Il y perd six personnes.",
               "<b>Tous les accessoires quittent la table</b> : illisibles dans le noir, et "
               "ils sont tous de l'acte 1."],
     "piege": "Ne pas orienter vers l'une ou l'autre branche. <b>Kassym prend celle qu'on lui "
              "indique</b> — il n'en sait pas plus qu'eux.",
     "questions": [
        {"q": "Que trouve-t-on dans la branche A de la première strate ?",
         "choix": ["Les deux morts de l'éboulement et Akim vivant — et c'est un cul-de-sac",
                   "La peinture, puis la corniche",
                   "Le conduit qui mène à la strate 2",
                   "Le bassin et le double d'Aksinia"],
         "bonne": 0,
         "pourquoi": "<b>Elle ne mène nulle part, et c'est elle qui porte presque tout "
                     "l'enjeu humain.</b> Un groupe pressé la saute et perd Akim, le père de "
                     "Kassym et son oncle.",
         "ou": "101-acte2-strate1.md"},
        {"q": "Combien de proches Kassym perd-il dans l'acte 2 ?",
         "choix": ["Six", "Quatre", "Deux", "Toute sa famille, soit onze personnes"],
         "bonne": 0,
         "pourquoi": "Son père, son oncle, sa mère, deux frères, sa sœur. <b>Il ne lui reste "
                     "rien.</b> Quatre sont parmi les onze disparus, deux sont morts dans "
                     "l'effondrement lui-même.",
         "ou": "100-acte2-cadrage.md"},
        {"q": "Dans quel ordre jouer les trois phases des tubes ?",
         "choix": ["L'ouïe, la vue, le toucher — en intercalant d'autres scènes entre elles",
                   "Les trois à la suite, pour l'effet de montée",
                   "Le toucher d'abord, c'est le plus marquant",
                   "L'ordre n'a pas d'importance"],
         "bonne": 0,
         "pourquoi": "<b>On l'entend avant de la voir, on la voit avant de la subir.</b> "
                     "Et les enchaîner gâche le dosage : il faut d'autres scènes entre elles.",
         "ou": "102-acte2-strate2.md"}]},

    {"id": "acte3", "nom": "Acte 3 — la fuite", "role": "une heure, et il est facultatif",
     "lieuLabel": "Le régime",
     "lieu": "<b>Cinématique et QTE</b> : des descriptions entrecoupées de très courtes "
             "phases d'action — un ou deux jets, ou une décision en quelques secondes. "
             "Action 5/5.",
     "sait": ["<b>Il se joue dans la continuité du précédent</b> : pas de pause, pas de "
              "changement de séance.",
              "<b>Un groupe qui remonte avant le point de non-retour ne le joue jamais.</b>",
              "Les larves ont <b>une minute d'avance en moyenne</b>.",
              "Le dernier des trois jets d'horreur de la campagne est ici : <b>la vision</b>, "
              "la salle à la Escher."],
     "questions": [
        {"q": "Qu'est-ce qui rend l'acte 3 facultatif ?",
         "choix": ["Un groupe qui remonte avant le point de non-retour ne le joue pas",
                   "Il ne se joue que si un PJ est mort dans l'acte 2",
                   "Il dépend du choix de Gusev·",
                   "Il remplace l'épilogue si le rapport n'est pas rendu"],
         "bonne": 0,
         "pourquoi": "Le point de non-retour <b>ne s'annonce pas</b> : il se constate quand "
                     "ils cherchent le conduit et qu'il n'y est plus.",
         "ou": "104-acte3-fuite.md · 103-acte2-strate3.md"}]},

    {"id": "epilogue", "nom": "L'épilogue — le rapport", "role": "une bonne heure, autour d'une table",
     "lieuLabel": "L'étau",
     "lieu": "Le rapport se rend <b>en main propre, dans deux jours</b>. Il faut "
             "<b>sept jours</b> pour aller à Moscou. <b>Les cinq jours volés ne coûtent pas "
             "du temps d'enquête : ils coûtent le délai.</b>",
     "sait": ["<b>Tout le reste n'a servi qu'à décider de ce qu'ils vont écrire dedans.</b>",
              "Trois stratégies : révéler la vérité <i>(une des pires solutions)</i> · des "
              "incidents sans rapport entre eux <i>(le piège)</i> · de faux coupables "
              "<i>(moralement douteux, et ça marche)</i>.",
              "<b>Un seul scribe : Petrenko.</b> Les autres discutent, il écrit — et c'est "
              "lui qui dira <i>« je ne peux pas écrire ça »</i>."],
     "cache": ["<b>Gusev· rédige son propre rapport, et sa crédibilité est supérieure.</b> "
               "S'il soutient la même version, leur sort est commun. S'il prétend qu'ils ont "
               "menti et propose mieux, <b>il s'en sort avec les honneurs et ils sont "
               "condamnés</b>.",
               "Sa décision se prend <b>en aparté, après les discussions</b>. Jamais devant "
               "les autres."],
     "questions": [
        {"q": "Pourquoi les cinq jours volés sont-ils graves ?",
         "choix": ["Ils coûtent le délai du rapport, pas du temps d'enquête",
                   "Ils réduisent le nombre de créneaux de l'acte 1",
                   "Ils font manquer le train du 10 mai",
                   "Ils laissent Larissa s'enfuir"],
         "bonne": 0,
         "pourquoi": "Rapport dû dans deux jours, sept jours de train. <b>C'est maintenant "
                     "que la mécanique du temps rend son verdict, et il n'y a rien à faire "
                     "contre.</b>",
         "ou": "105-epilogue-rapport.md"},
        {"q": "Que se passe-t-il si Gusev· prétend que les autres ont menti ?",
         "choix": ["Il s'en sort avec les honneurs, et ils sont condamnés",
                   "Personne ne le croit : sa parole vaut la leur",
                   "Une contre-enquête vérifie les deux versions",
                   "Il est mis à l'écart avec condescendance"],
         "bonne": 0,
         "pourquoi": "<b>Sa crédibilité est supérieure à la leur.</b> La mise à l'écart "
                     "condescendante, c'est l'autre cas : quand il révèle le surnaturel.",
         "ou": "105-epilogue-rapport.md"}]},
]


# ══════════════════════════════════════════════════════════════════
#  3 bis. Les noms — l'appariement, et il se génère
# ══════════════════════════════════════════════════════════════════
#
#  **Rien ne s'écrit ici à la main.** Les questions se construisent à
#  partir des fiches de GENS : le nom et le rôle y sont déjà, et les
#  recopier serait se condamner à les désynchroniser.
#
#  **Les leurres viennent du même groupe.** Proposer « Isidor Nesteroff »
#  comme contremaître des convois n'apprend rien ; proposer Moskalev,
#  Udovenko et Bondarenko oblige à distinguer les neuf du transport entre
#  eux, ce qui est le vrai travail.
#
#  **Les deux sens.** Du rôle vers le nom *(« qui est le contremaître ? »)*
#  et du nom vers le rôle *(« Moskalev, c'est qui ? »)* — on retient mal
#  dans un seul sens.

import random as _rnd  # noqa: E402  — le tirage des leurres, à graine fixe
import re as _re  # noqa: E402

GROUPES = [
    ("La police", "igor yelena oleg vinogradoff",
     "<b>Yelena Nikitina</b> n'a rien à voir avec <b>Faddei Nikitine</b>, du transport."),
    ("Le secteur transport", "faddei larissa moskalev udovenko anna timur zinaida boris "
     "bondarenko",
     "<b>Grigori Moskalev</b> est le contremaître. <b>Grigori Novikoff</b>, au Komsomol, est "
     "le meurtrier — <b>deux Grigori, et l'un des deux tue</b>."),
    ("Les entrepôts de l'ouest", "zykov nikiforov gordeeva",
     "<b>Zykov et Nikiforov sont les deux qui ne bougent jamais</b> du tableau des "
     "affectations. Gordeeva tient l'entrepôt n°7 et son carnet d'écarts."),
    ("Le Komsomol", "kassym grigori tolia macha avdotya sofia maxim",
     "<b>Maxim Kazakoff</b> est le condamné innocent. <b>Larissa Kazakova</b>, au transport, "
     "est la vraie coupable des sabotages — <b>aucun lien entre eux</b>."),
    ("Les autres", "nesteroff orloff cheskov may kelley akmaral ingenieurs survivants", ""),
]


def _court(role):
    """Le rôle sans son âge : « 16 ans, komsomolets » → « komsomolets ».

    L'âge est une information de fiche, pas un métier : le laisser
    rendrait la question « 16 ans, komsomolets — qui est-ce ? », qui se
    répond sans rien savoir.
    """
    return _re.sub(r"^\d+ ans, ", "", role)


def _noms():
    par_id = {g["id"]: g for g in GENS}
    tirage = _rnd.Random(1932)
    fiches = []
    for titre, ids, piege in GROUPES:
        membres = [par_id[i] for i in ids.split() if i in par_id]
        autres = [g for g in GENS if g not in membres]
        questions = []
        for m in membres:
            role = _court(m["role"])
            pool = [x for x in membres if x is not m] or autres
            leurres = tirage.sample(pool, min(3, len(pool)))
            while len(leurres) < 3:
                leurres.append(tirage.choice(autres))
            questions.append(
                {"q": f"{role[0].upper() + role[1:]} — qui est-ce ?",
                 "choix": [m["nom"]] + [x["nom"] for x in leurres],
                 "bonne": 0, "pourquoi": f"<b>{m['nom']}</b> — {role}.",
                 "ou": "module Les gens"})
            questions.append(
                {"q": f"{m['nom']}, c'est qui ?",
                 "choix": [role] + [_court(x["role"]) for x in leurres],
                 "bonne": 0, "pourquoi": f"<b>{m['nom']}</b> — {role}.",
                 "ou": "module Les gens"})
        fiches.append(
            {"id": "n-" + titre.lower().split()[-1], "nom": titre,
             "role": f"{len(membres)} personnes",
             "lieuLabel": "Qui est qui",
             "lieu": " · ".join(f"<b>{m['nom']}</b> — {_court(m['role'])}" for m in membres),
             "sait": [piege] if piege else [],
             "questions": questions})
    return fiches


NOMS = _noms()


# ══════════════════════════════════════════════════════════════════
#  4 bis. Les lieux — l'unité d'arbitrage
# ══════════════════════════════════════════════════════════════════
#
#  **On prépare en dossiers, on arbitre en lieux.** C'est la règle de
#  `50-temporalite.md`, et elle décide de tout le tempo : un créneau se
#  paie pour un lieu, jamais pour un dossier, une action ou un
#  interlocuteur. D'où ce module, qui double celui des pistes.

LIEUX = [
    {"id": "baraquements", "nom": "Les baraquements", "role": "lieu 11 — leur base",
     "lieuLabel": "Le coût",
     "lieu": "<b>Jamais un créneau : ils y dorment.</b> Et c'est d'ici qu'on mesure toutes "
             "les distances.",
     "sait": ["<b>Dossiers : tous, et aucun.</b> C'est le point de départ de chaque "
              "demi-journée.",
              "<b>Le réfectoire</b> — un repas par jour, sur présentation de la carte. "
              "Leur carte permet de passer devant la file : <b>un petit choix social qui se "
              "repose chaque jour</b>.",
              "<b>La salle commune, le soir</b>, et c'est le cœur : la rumeur y circule plus "
              "vite qu'eux. Ce qu'ils ont demandé dans la journée, quelqu'un l'a répété ici."],
     "cache": ["Ce qui y arrive sans qu'ils fassent rien : <b>le message de Kelley</b> déposé "
               "devant leur porte · <b>Kassym qui ne vient pas</b>, au matin du jour 2."],
     "questions": [
        {"q": "Combien coûte une soirée à la salle commune des baraquements ?",
         "choix": ["Rien : les trois soirées sont gratuites",
                   "Un créneau, comme tout lieu travaillé",
                   "Un demi-créneau", "Un créneau la première fois seulement"],
         "bonne": 0,
         "pourquoi": "<b>Ils y dorment.</b> Les soirées, les trajets en ville et le pêcheur "
                     "si on est déjà au dispensaire ne coûtent rien.",
         "ou": "90-creneaux.md · 25-lieux-et-presences.md"}]},

    {"id": "dispensaire", "nom": "Le dispensaire", "role": "trois minutes, le plus proche",
     "lieuLabel": "Le coût",
     "lieu": "<b>Un créneau — mais il porte quatre dossiers.</b> C'est le meilleur rapport "
             "de tout l'acte 1.",
     "sait": ["<b>Dossiers : l'empoisonnement · le noyé · l'autopsie de Zina · le corps du "
              "pêcheur.</b> Plus Igor, qu'on peut y croiser.",
              "<b>Isidor Nesteroff</b>, médecin-chef : il penche pour une contamination "
              "alimentaire, et il ne cache pas qu'il ne comprend pas ce qu'il voit.",
              "<b>Le corps du pêcheur est sur sa banquette</b>, sous leurs yeux. Dire « c'est "
              "un autre dossier, ça coûte un créneau » serait absurde."],
     "piege": "C'est <b>le</b> lieu qui justifie d'arbitrer en lieux et non en dossiers. "
              "Quatre pistes pour une demi-journée.",
     "questions": [
        {"q": "Combien de dossiers vivent au dispensaire ?",
         "choix": ["Quatre — l'empoisonnement, le noyé, l'autopsie de Zina, le pêcheur",
                   "Un seul : l'empoisonnement",
                   "Deux : l'empoisonnement et le noyé",
                   "Trois, plus le meurtre au Komsomol"],
         "bonne": 0,
         "pourquoi": "<b>Trois lieux seulement portent plusieurs dossiers</b> : le "
                     "dispensaire, les archives et le bloc 27. Le dispensaire est le plus "
                     "chargé des trois.",
         "ou": "25-lieux-et-presences.md · 90-creneaux.md"}]},

    {"id": "police", "nom": "Le bureau de police", "role": "en ville — chez Igor",
     "lieuLabel": "Le coût",
     "lieu": "Un créneau. <b>Les archives s'y trouvent, et elles ont leur propre prix</b> : "
             "par la voie officielle, un créneau <i>plus</i> une journée d'attente.",
     "sait": ["<b>Dossiers : les archives (deux dossiers y dorment) · Yelena Nikitina · "
              "Igor lui-même.</b>",
              "Un secteur à part, entouré de barbelés, des casernes à côté, et derrière "
              "<b>de grandes tentes où sont parqués les prisonniers de droit commun</b>."],
     "questions": [
        {"q": "Que coûte la consultation des archives par la voie officielle ?",
         "choix": ["Un créneau, plus une journée d'attente",
                   "Un créneau", "Rien, Igor donne tout", "Deux créneaux consécutifs"],
         "bonne": 0,
         "pourquoi": "C'est l'une des <b>quatre seules actions qui coûtent plus d'un "
                     "créneau</b>, avec Berezki, les mines et l'exhumation du noyé.",
         "ou": "90-creneaux.md"}]},

    {"id": "entrepots", "nom": "Les entrepôts de l'ouest", "role": "1,4 km — le plus loin en ville",
     "lieuLabel": "Le coût",
     "lieu": "Un créneau, et <b>dix-sept minutes de marche qui ne se paient pas</b> : aucun "
             "trajet en ville n'est facturé.",
     "sait": ["<b>Dossiers : les disparitions de matériel · les sabotages · tout ce qui se "
              "vend.</b>",
              "<b>Margarita Gordeeva</b> tient l'entrepôt n°7 et <b>ne propose jamais "
              "rien</b> : le tableau des affectations et son carnet d'écarts, il faut les "
              "lui demander.",
              "Le matin elle compte des bobines et répond entre deux chiffres ; "
              "<b>l'après-midi, assise, elle sort son carnet d'elle-même</b>."],
     "questions": [
        {"q": "Comment obtient-on le tableau des affectations de Gordeeva ?",
         "choix": ["Il faut le lui demander : elle ne propose jamais rien",
                   "Elle le sort spontanément dès qu'on parle des vols",
                   "Il est affiché au mur de l'entrepôt",
                   "Il faut passer par le palais administratif"],
         "bonne": 0,
         "pourquoi": "Elle réclame du monde chaque semaine et tient ce tableau <b>pour "
                     "elle</b>. Le carnet d'écarts, en revanche, elle le sort de son propre "
                     "chef — mais l'après-midi seulement.",
         "ou": "87-disparitions.md"}]},

    {"id": "bloc27", "nom": "Le bloc 27 — la prison", "role": "650 m, huit minutes",
     "lieuLabel": "Le coût",
     "lieu": "Un créneau, <b>deux dossiers</b> : les deux ingénieurs de la machine, et "
             "Maxim Kazakoff, le condamné du meurtre.",
     "sait": ["<b>Sorokin et Malysheff</b> partagent la même version : quelque chose s'est "
              "retrouvé dans le réseau de canalisations et a été emporté par le flux. "
              "<b>C'est l'aiguillage vers la conduite</b>.",
              "Il faut <b>faire pression sur la police</b> pour les interroger."],
     "questions": [
        {"q": "Qui est enfermé au bloc 27 ?",
         "choix": ["Les deux ingénieurs de la machine, et Maxim Kazakoff",
                   "Larissa Kazakova", "Pavel Tkachenko, le déserteur",
                   "Les deux ingénieurs seulement"],
         "bonne": 0,
         "pourquoi": "Deux dossiers pour un créneau. Et les ingénieurs donnent la phrase qui "
                     "mène à la conduite d'eau.",
         "ou": "25-lieux-et-presences.md"}]},

    {"id": "komsomol", "nom": "Le quartier du Komsomol", "role": "600-700 m, huit minutes",
     "lieuLabel": "Le coût",
     "lieu": "Un créneau. <b>Dossier : le meurtre de Zina Krylova</b> — et la page qui "
             "manque au dossier dort au dispensaire.",
     "sait": ["<b>Grigori Novikoff</b>, komsomolets modèle, est le meurtrier. "
              "<b>Tolia Zaïtsev</b> est le complice.",
              "<b>Maxim Kazakoff est condamné, et il est innocent</b> — jugement rendu le "
              "2 mai, la veille de leur arrivée."],
     "questions": [
        {"q": "Où se trouve la pièce qui détruit l'enquête sur le meurtre de Zina ?",
         "choix": ["Au dispensaire : la copie de l'autopsie, que personne n'est venu chercher",
                   "Aux archives de la police", "Dans le dossier d'Igor",
                   "Au gymnase du Komsomol"],
         "bonne": 0,
         "pourquoi": "<b>Elle dormait dans un tiroir à deux cents mètres de Vinogradoff.</b> "
                     "Le dossier de police porte le renvoi à un rapport d'autopsie absent : "
                     "c'est ça, l'indice.",
         "ou": "89-komsomol.md"}]},

    {"id": "mines", "nom": "Le mont Magnitnaïa — les mines", "role": "5 km à l'est",
     "lieuLabel": "Le coût",
     "lieu": "<b>Un créneau entier, aller-retour compris, et rien d'autre dans la "
             "demi-journée.</b> L'un des deux seuls trajets qui se paient.",
     "sait": ["<b>Dossiers : les disparitions de matériel</b> — c'est là qu'Oleg Belousoff a "
              "été muté après avoir voulu insister."],
     "questions": [
        {"q": "Quels sont les deux seuls trajets qui coûtent un créneau entier ?",
         "choix": ["Les mines du mont Magnitnaïa (5 km) et Berezki (8 km)",
                   "Les entrepôts et les mines",
                   "Berezki et le bureau d'études",
                   "Les mines et le hangar zéro"],
         "bonne": 0,
         "pourquoi": "Tout le reste est à moins de vingt minutes à pied et <b>ne se paie "
                     "pas</b>. C'est écrit sur le plan que Kassym leur donne.",
         "ou": "50-temporalite.md"}]},

    {"id": "berezki", "nom": "Berezki", "role": "8 km — le village des étrangers",
     "lieuLabel": "Le coût",
     "lieu": "<b>Un créneau entier — sauf par la porte d'entrée, qui est gratuite</b> : "
             "le dîner chez Igor.",
     "sait": ["<b>Dossiers : enquêter sur Igor · le promeneur (Kelley).</b>",
              "<b>Matthew Kelley</b>, un étranger, dépose un message devant leur porte sans "
              "qu'ils aient rien demandé."],
     "questions": [
        {"q": "Comment aller à Berezki sans payer un créneau entier ?",
         "choix": ["Le dîner chez Igor : c'est la porte gratuite",
                   "Y passer en revenant des mines",
                   "Envoyer Kassym seul", "Ce n'est pas possible"],
         "bonne": 0,
         "pourquoi": "<b>La seule porte gratuite vers Berezki</b>, et c'est aussi une "
                     "occasion de voir Igor hors de son bureau.",
         "ou": "25-lieux-et-presences.md · 90-creneaux.md"}]},

    {"id": "fouiller", "nom": "Les six lieux à fouiller", "role": "personne dedans",
     "lieuLabel": "La règle commune",
     "lieu": "<b>L'absence d'indice est l'indice.</b> Une berge qui ne s'est pas effondrée, "
             "des grilles intactes, une eau dont l'analyse est négative. <b>Chaque fois, la "
             "bonne explication est écartée par un fait matériel</b> — et il n'en reste "
             "aucune.",
     "sait": ["<b>Le lac artificiel</b> <i>(le noyé)</i> — 870 m · <b>la berge de l'Oural</b> "
              "<i>(le pêcheur)</i> — 400 m · <b>le lieu de l'explosion</b> <i>(la machine)</i> "
              "— 750 m · <b>la Section D</b> <i>(l'empoisonnement)</i> — 600 m · "
              "<b>le logement de Tkachenko</b> <i>(le déserteur)</i> — 250 m · "
              "<b>le hangar zéro</b> <i>(le culte)</i> — 1,2 km",
              "<b>Le hangar zéro ne coûte jamais un créneau</b> : c'est une soirée, et on y "
              "arrive par une rumeur ou par une filature improvisée."],
     "piege": "Ne jamais souligner. <b>Donner le fait, platement, et passer.</b>",
     "questions": [
        {"q": "Qu'ont en commun les six lieux à fouiller ?",
         "choix": ["L'absence d'indice est l'indice : un fait matériel écarte chaque "
                   "explication raisonnable",
                   "Ils portent tous la même substance",
                   "Ils sont tous à moins de dix minutes",
                   "Ils ne coûtent aucun créneau"],
         "bonne": 0,
         "pourquoi": "Une berge qui ne s'est pas effondrée, des grilles intactes, une analyse "
                     "d'eau négative. <b>Il ne reste aucune explication — et c'est ça, "
                     "l'information.</b>",
         "ou": "25-lieux-et-presences.md"},
        {"q": "Que coûte le hangar zéro ?",
         "choix": ["Une soirée, jamais un créneau", "Un créneau",
                   "Un créneau entier, comme les mines", "Deux créneaux : il faut y revenir"],
         "bonne": 0,
         "pourquoi": "On y arrive par une rumeur sur « des individus louches qui se déplacent "
                     "la nuit », ou par hasard en se promenant. <b>Les trois soirées sont "
                     "gratuites.</b>",
         "ou": "25-lieux-et-presences.md · 90-creneaux.md"}]},
]


# ══════════════════════════════════════════════════════════════════
#  6. Les PJ
# ══════════════════════════════════════════════════════════════════
#
#  **Les dix fiches sont des copies carbone** : mêmes caractéristiques,
#  mêmes dés, mêmes capacités au mot près. Seul l'accord change, et
#  l'équipement de Voronin·. Le genre se choisit à la table.

PJ = [
    {"id": "aparte", "nom": "Les quatre apartés", "role": "deux minutes chacun, montre en main",
     "lieuLabel": "Le dispositif",
     "lieu": "<b>Chaque personnage a son aparté, et les quatre durent le même temps.</b> "
             "C'est ce qui permet de donner sa mission à Gusev· <b>sans que la table "
             "remarque qu'il s'est passé quelque chose de particulier avec lui</b>.",
     "sait": ["<b>Petrenko</b> — il a déposé sa candidature à la Guépéou. Cette mission est "
              "le test.",
              "<b>Krasnov·</b> — la mission est un test de fidélité, et son association "
              "savante en dépend.",
              "<b>Voronin·</b> — la vraie mission, dite de vive voix, absente des ordres "
              "écrits.",
              "<b>Gusev·</b> — surveiller les trois autres et écrire un second rapport."],
     "cache": ["Les quatre ont la même forme : <b>une chose que le personnage sait, qu'il ne "
               "peut pas dire, et qui ne l'oblige à rien.</b> Aucun ne pèse plus que les "
               "autres."],
     "piege": "Volkov· n'a pas d'aparté : le cinquième personnage est le komsomolets, et "
              "Kassym joue à côté de lui.",
     "questions": [
        {"q": "Pourquoi les quatre apartés durent-ils exactement le même temps ?",
         "choix": ["Pour que celui de Gusev· ne se remarque pas",
                   "Pour tenir le rythme de la séance d'introduction",
                   "Parce qu'ils contiennent la même quantité d'information",
                   "Pour que chaque joueur ait son moment seul avec le meneur"],
         "bonne": 0,
         "pourquoi": "Deux minutes, montre en main, et toujours le même rituel. <b>Si celui "
                     "de Gusev· durait plus longtemps, la table le saurait.</b>",
         "ou": "30-scenes-introduction.md"}]},

    {"id": "petrenko", "nom": "Petrenko", "role": "bureaucrate — 10 PV (d8)",
     "lieuLabel": "Capacités",
     "lieu": "Notes de frais · Jargon juridique · Méticuleux·se",
     "sait": ["<b>Bureaucrate, pas ingénieur</b> : droit à l'Université d'État de Moscou, "
              "« un talent certain pour la compréhension et la mémorisation des "
              "réglementations ».",
              "FOR 12 · DEX 13 · INT 14 · CON 10 · SAG 8 · CHA 12",
              "Porte <i>Nouvelles procédures administratives en vigueur au 1er mai 1932</i>, "
              "312 pages. Et <b>une réserve de tabac (d6)</b> — une monnaie d'échange dans "
              "une ville où tout manque.",
              "<b>C'est le scribe du rapport final</b>, et c'est lui qui dira « je ne peux "
              "pas écrire ça »."],
     "questions": [
        {"q": "Quel est le métier de Petrenko ?",
         "choix": ["Bureaucrate — droit, pas ingénierie", "Ingénieur",
                   "Juriste militaire", "Comptable du combinat"],
         "bonne": 0,
         "pourquoi": "<b>Bureaucrate, pas ingénieur.</b> Sa compétence est la réglementation, "
                     "et c'est elle qui fait de lui le scribe de l'épilogue.",
         "ou": "10-personnages.md"}]},

    {"id": "krasnov", "nom": "Krasnov·", "role": "scientifique — 10 PV (d8)",
     "lieuLabel": "Capacités",
     "lieu": "Érudit·e · Déduction · Naturaliste",
     "sait": ["Porte les <i>Souvenirs entomologiques</i> de J.-H. Fabre, <b>édition "
              "anglaise</b>, 396 pages — <b>un livre étranger dans une valise qu'on peut "
              "fouiller</b>.",
              "<b>L'anglais tient dans les deux cas</b>, quel que soit le genre choisi : "
              "c'est ce qui permet de parler à Kelley."],
     "questions": [
        {"q": "Qu'est-ce qui rend le livre de Krasnov· dangereux ?",
         "choix": ["C'est une édition anglaise, dans une valise qu'on peut fouiller",
                   "Il est dédicacé", "Il traite de biologie non soviétique",
                   "Il est interdit depuis 1930"],
         "bonne": 0,
         "pourquoi": "<b>Un livre étranger</b> en 1932. Le Staline de Gusev· est dédicacé, "
                     "ce qui est un autre genre de problème — et une autre question.",
         "ou": "10-personnages.md"}]},

    {"id": "voronin", "nom": "Voronin·", "role": "militaire / gymnaste — 12 PV (d8)",
     "lieuLabel": "Capacités",
     "lieu": "Entraîné·e · Athlète · Artiste (chant)",
     "sait": ["FOR 14 · DEX 14 · INT 10 · CON 12 · SAG 9 · CHA 10",
              "<b>C'est lui qui reçoit les documents officiels de la mission</b> — l'ordre "
              "de détachement, le formulaire de rapport. <b>Petrenko les réclame.</b>",
              "<b>La médaille des Spartakiades</b>, si Voronina remplace la montre : c'est "
              "la seule différence d'équipement entre les deux versions."],
     "questions": [
        {"q": "Qui porte les documents officiels de la mission ?",
         "choix": ["Voronin·, parce que c'est l'officier",
                   "Petrenko, parce que le rapport est son métier",
                   "Gusev·, parce qu'il est de la Guépéou",
                   "Personne : ils sont remis à Igor à l'arrivée"],
         "bonne": 0,
         "pourquoi": "<b>Les documents officiels sont confiés au militaire.</b> Petrenko les "
                     "réclame — petite friction d'ouverture, gratuite, et en caractère pour "
                     "les deux.",
         "ou": "105-epilogue-rapport.md"}]},

    {"id": "gusev", "nom": "Gusev·", "role": "agent·e officieux·se — 12 PV (d8)",
     "lieuLabel": "Capacités",
     "lieu": "Prudent·e · Cartésien·ne · Inquisiteur·rice",
     "sait": ["Porte les <i>Fondations du Léninisme</i> de Staline, 164 pages, "
              "<b>dédicacé</b> — par qui, et ce que ça dit de ses relations, reste ouvert.",
              "<b>Sa mission : surveiller les trois autres et écrire un second rapport.</b> "
              "Les autres joueurs l'ignorent.",
              "<b>Sa crédibilité est supérieure à la leur à l'épilogue.</b> S'il les "
              "dénonce, il s'en sort avec les honneurs et ils sont condamnés."],
     "piege": "<b>C'est l'exception de la règle « chaque PJ trouve ce que les autres ne "
              "peuvent pas »</b> — c'est son métier, pas un privilège de joueur.",
     "questions": [
        {"q": "Quelle est la vraie mission de Gusev· ?",
         "choix": ["Surveiller les trois autres et écrire un second rapport",
                   "Vérifier la fidélité d'Igor Pavlenko",
                   "Rapporter directement au Directeur du combinat",
                   "S'assurer que le surnaturel ne figure pas au rapport"],
         "bonne": 0,
         "pourquoi": "Dite en aparté, de la même durée que les trois autres — <b>pour que la "
                     "table ne remarque rien</b>.",
         "ou": "30-scenes-introduction.md · 105-epilogue-rapport.md"}]},

    {"id": "volkov", "nom": "Volkov·", "role": "komsomolets / komsomolka — 10 PV (d6)",
     "lieuLabel": "Capacités",
     "lieu": "Crochetage — et c'est la seule, mais elle ouvre les portes fermées.",
     "sait": ["<b>Des outils de crochetage et une bobine de ficelle.</b> Le gamin du "
              "Komsomol entre là où les autres frappent.",
              "<b>Le d6 de vie</b> est le plus bas du groupe : c'est le personnage le plus "
              "fragile de l'acte 2."],
     "questions": [
        {"q": "Lequel des cinq a le dé de vie le plus bas ?",
         "choix": ["Volkov·, avec un d6", "Petrenko, avec un d6",
                   "Krasnov·, avec un d6", "Ils ont tous un d8"],
         "bonne": 0,
         "pourquoi": "Volkov· — 10 PV, <b>mais un d6</b>. Petrenko et Krasnov· ont 10 PV "
                     "avec un d8 ; Voronin· et Gusev· ont 12.",
         "ou": "10-personnages.md"}]},
]


# ══════════════════════════════════════════════════════════════════
#  7. La table — quel papier sort quand
# ══════════════════════════════════════════════════════════════════
#
#  Quinze documents ont été fabriqués. Savoir lequel donner à quel
#  moment est exactement le genre de chose qui se cherche mal en pleine
#  scène — et en donner un trop tôt coûte une scène entière.

TABLE = [
    {"id": "depart", "nom": "Au départ", "role": "avant même d'arriver",
     "lieuLabel": "Ce qui est déjà dans leurs mains",
     "lieu": "<b>L'ordre de détachement</b> — remis à Voronin· à Moscou, le 24 avril. "
             "<b>Le formulaire de rapport</b> — même paquet, et il reste sur la table "
             "jusqu'à la dernière heure. <b>Le dossier de Gusev·</b>, à son aparté.",
     "sait": ["<b>Les cases vides du formulaire font le travail pendant six jours.</b> "
              "L'échéance est posée, pas annoncée, et chaque découverte pose d'elle-même la "
              "question « est-ce que ça va dans le rapport ? »",
              "<b>Les chevalets</b> se posent devant chaque joueur dès la première scène."],
     "questions": [
        {"q": "Quand le formulaire de rapport arrive-t-il sur la table ?",
         "choix": ["Dès le départ : ils l'ont depuis Moscou",
                   "À l'épilogue, quand il faut le remplir",
                   "Au briefing, remis par Igor",
                   "Au retour, dans le train"],
         "bonne": 0,
         "pourquoi": "<b>C'est ce qui le rend meilleur qu'une feuille sortie à la fin</b> : "
                     "Igor se trahit au briefing, et la case « conduite des services locaux » "
                     "change de sens sans qu'on y ait touché.",
         "ou": "105-epilogue-rapport.md"}]},

    {"id": "jour1", "nom": "Le premier jour", "role": "arrivée, briefing",
     "lieuLabel": "Ce que Kassym remet",
     "lieu": "<b>Les clés des chambres, les cartes de repas, et le plan du combinat</b> — "
             "qu'il sort <b>quand on lui demande où on va</b>, pas avant.",
     "sait": ["<b>Ce qu'Igor remet au briefing</b> : cinq dossiers sur les sept. Les deux "
              "autres dorment aux archives.",
              "<b>La feuille du temps</b> se pose au centre, vierge. <b>Rien n'y est coché "
              "d'avance, pas même le 3 mai</b> : une case cochée par le meneur est une "
              "annonce, une case cochée par un joueur est une décision.",
              "<b>Les deux dépositions de Faddei</b> sont agrafées au dossier des sabotages."],
     "piege": "Le plan ne porte <b>aucun lieu nommé</b>, seulement les quartiers. Les "
              "adresses se demandent — c'est le métier de Kassym.",
     "questions": [
        {"q": "Combien de dossiers Igor remet-il au briefing, sur les sept qui existent ?",
         "choix": ["Cinq", "Sept", "Quatre", "Six"],
         "bonne": 0,
         "pourquoi": "Deux dorment aux archives. Et le cinquième, les sabotages, <b>c'est "
                     "Igor qui l'ajoute de son propre chef</b> — le seul qu'il n'avait pas "
                     "ouvert.",
         "ou": "105-epilogue-rapport.md · 70-rapports-imprimes.md"},
        {"q": "Que porte la feuille du temps quand elle arrive sur la table ?",
         "choix": ["Rien : elle est entièrement vierge, même le 3 mai",
                   "Le premier jour est déjà coché",
                   "Les 8 et 9 mai sont grisés",
                   "La bande de déblaiement est marquée"],
         "bonne": 0,
         "pourquoi": "<b>Une case cochée d'avance est une annonce du meneur.</b> Et le "
                     "déblaiement nommerait un chantier dont ils n'ont pas entendu parler.",
         "ou": "50-temporalite.md"}]},

    {"id": "demande", "nom": "Sur demande, pendant l'acte 1", "role": "il faut aller les chercher",
     "lieuLabel": "Ce qui ne vient pas tout seul",
     "lieu": "<b>Le carnet de Faddei</b>, trois pages données séparément · <b>le tableau des "
             "affectations</b> et <b>le carnet d'écarts de Gordeeva</b>, aux entrepôts · "
             "<b>la copie de l'autopsie de Zina</b>, au dispensaire.",
     "sait": ["<b>Les trois pages du carnet de Faddei ne se donnent pas ensemble</b> : la "
              "première quand ils demandent ce qu'il sait, la deuxième sur l'équipe, la "
              "troisième sur les horaires ou leurs soupçons.",
              "<b>Gordeeva ne propose jamais rien</b> : le tableau se demande. Le carnet "
              "d'écarts, elle le sort d'elle-même — mais l'après-midi seulement.",
              "<b>L'autopsie n'a jamais quitté le dispensaire.</b> « Section de police "
              "prévenue le 7.IV. Personne n'est venu le chercher. »"],
     "piege": "Les pages 1 et 2 du carnet de Faddei portent le croisement du dossier, et "
              "<b>elles ne se rencontrent nulle part</b> : les incidents sont sur l'une, les "
              "convois lourds sur l'autre. <b>Ne jamais faire le rapprochement à leur "
              "place.</b>",
     "questions": [
        {"q": "Pourquoi les pages 1 et 2 du carnet de Faddei sont-elles séparées ?",
         "choix": ["Les incidents sont sur l'une, les convois lourds sur l'autre : le "
                   "croisement appartient aux joueurs",
                   "Parce que Faddei les a écrites à deux moments différents",
                   "Pour qu'on puisse en donner une sans l'autre selon le temps",
                   "La page 2 est une pièce du dossier de police"],
         "bonne": 0,
         "pourquoi": "Quatre des cinq convois lourds du mois ont été frappés. <b>Un seul est "
                     "passé sans rien</b>, et ce convoi épargné est volontaire : un motif "
                     "parfait se repère trop vite.",
         "ou": "86-carnet-faddei.md"}]},

    {"id": "jamais", "nom": "Ce qui ne sort jamais", "role": "et l'acte 2 vide la table",
     "lieuLabel": "Pour le meneur seul",
     "lieu": "<b>L'organigramme du secteur transport</b> · <b>les cinq aides de l'acte 2</b> "
             "· <b>le tableau des affectations en version remplie</b>, qui dit quoi écrire "
             "dans chaque case.",
     "sait": ["<b>À l'acte 2, tous les accessoires quittent la table.</b> Rapports, plan, "
              "carnet, cartes de repas : illisibles dans le noir, et <b>ils sont tous de "
              "l'acte 1</b>. La descente est le moment où les documents disparaissent.",
              "<b>Le rapport particulier de Gusev·</b> ne sort qu'à l'aparté final, pendant "
              "que les autres attendent à côté."],
     "questions": [
        {"q": "Que deviennent les accessoires pendant l'acte 2 ?",
         "choix": ["Ils quittent tous la table : ils sont de l'acte 1 et illisibles dans le noir",
                   "Seul le plan reste, pour s'orienter dans la mine",
                   "On garde les dossiers, au cas où",
                   "Ils restent, mais on allume une lampe pour les lire"],
         "bonne": 0,
         "pourquoi": "<b>La descente est le moment où les documents disparaissent.</b> "
                     "Ne restent que les cinq cartons du meneur, en gros caractères.",
         "ou": "100-acte2-cadrage.md"}]},
]


MODULES = {
    "socle": {"titre": "Le socle",
              "quoi": "La mission, le dispositif, la vérité. Se lit une fois, tient tout le reste.",
              "fiches": SOCLE},
    "actes": {"titre": "Les actes",
              "quoi": "La structure d'ensemble : les régimes, les durées, ce qui bascule.",
              "fiches": ACTES},
    "noms": {"titre": "Les noms",
             "quoi": "Qui fait quoi — l'appariement pur, dans les deux sens, "
                     "par secteur. Pour cesser de les confondre.",
             "fiches": NOMS},
    "gens": {"titre": "Les gens",
             "quoi": "Qui est qui, ce qu'il sait, ce qu'il tait, et ce qu'il dit des autres.",
             "fiches": GENS},
    "lieux": {"titre": "Les lieux",
              "quoi": "L'unité d'arbitrage : ce que chacun coûte, et quels dossiers y vivent.",
              "fiches": LIEUX},
    "pistes": {"titre": "Les pistes",
               "quoi": "Pour chacune : la version d'Igor, la vérité, et ce qui fait basculer.",
               "fiches": PISTES},
    "pj": {"titre": "Les PJ",
           "quoi": "Les cinq prétirés, leurs capacités, leurs objets, et les quatre apartés.",
           "fiches": PJ},
    "comptes": {"titre": "Les comptes",
                "quoi": "Le calendrier, les créneaux, les distances, ce qui se compte.",
                "fiches": COMPTES},
    "table": {"titre": "La table",
              "quoi": "Quel papier sort quand, et lequel ne sort jamais.",
              "fiches": TABLE},
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


_CHAINE = [
    ("Zinaida Plotnikova", "entretien des bêtes",
     "« Elle n'était pas au dépôt ce matin-là.", "Je l'ai vue partir vers les écuries. »"),
    ("Boris Shcherbakov", "entretien des voies",
     "« C'est Faddei qui m'a demandé de noter", "les présences. Je ne l'ai pas fait. »"),
    ("Anna Vasyukova", "ouvrière administrative",
     "« Elle m'a rien demandé.", "Je l'ai fait. »"),
    ("Le carré des tombes", "personne ne l'y a vue",
     "Une matinée entière", "inexpliquée."),
    ("Sacha Orloff", "à la gare",
     "« Une femme du transport.", "Elle demandait des explosifs. »"),
]


def _chaine():
    """La chaîne du registre, dans l'ordre — quatre témoins et une preuve.

    C'est le seul endroit du scénario où l'ordre des interrogatoires
    compte autant, et c'est ce qu'un diagramme tient mieux que sept fiches.
    """
    H, x = 104, 16
    haut = 44 + H * len(_CHAINE)
    el = [f'<svg viewBox="0 0 330 {haut}" xmlns="http://www.w3.org/2000/svg" '
          f'font-family="system-ui, sans-serif" role="img" '
          f'aria-label="La chaîne des témoignages du registre">',
          f'<text x="{x}" y="22" font-size="12.5" font-weight="600" fill="#132c3c">'
          f'LE 27 AVRIL — ce que dit le registre, et ce qu\'il ne dit pas</text>']
    for i, (nom, role, l1, l2) in enumerate(_CHAINE):
        y = 44 + H * i
        dernier = i == len(_CHAINE) - 1
        c = "#b3271e" if dernier else "#34566b"
        el.append(f'<circle cx="{x + 10}" cy="{y + 14}" r="9" fill="{c}"/>')
        el.append(f'<text x="{x + 10}" y="{y + 18}" font-size="11" fill="#fff" '
                  f'text-anchor="middle" font-weight="600">{i + 1}</text>')
        el.append(f'<text x="{x + 30}" y="{y + 12}" font-size="13" font-weight="600" '
                  f'fill="#132c3c">{nom}</text>')
        el.append(f'<text x="{x + 30}" y="{y + 28}" font-size="10.5" fill="#8aa4b2">'
                  f'{role}</text>')
        el.append(f'<text x="{x + 30}" y="{y + 48}" font-size="11.5" fill="#46555f">'
                  f'{l1}</text>')
        el.append(f'<text x="{x + 30}" y="{y + 63}" font-size="11.5" fill="#46555f">'
                  f'{l2}</text>')
        if not dernier:
            el.append(f'<line x1="{x + 10}" y1="{y + 25}" x2="{x + 10}" y2="{y + H - 12}" '
                      f'stroke="#c3cfd7" stroke-width="1.6"/>')
            el.append(f'<path d="M {x + 6} {y + H - 18} L {x + 10} {y + H - 11} '
                      f'L {x + 14} {y + H - 18}" fill="none" stroke="#c3cfd7" '
                      f'stroke-width="1.6"/>')
    el.append(f'<text x="{x}" y="{haut - 8}" font-size="11" fill="#b3271e" '
              f'font-style="italic">On ne prend jamais Larissa en défaut. '
              f'On prend le document en défaut.</text>')
    el.append("</svg>")
    return "".join(el)


SCHEMAS = {
    "gens": [
        {"titre": "La chaîne du registre",
         "leg": "Les quatre témoignages qui démontent la fausse entrée du 27 avril, dans "
                "l'ordre où il faut les obtenir — puis la seule preuve matérielle de toute "
                "l'enquête. Chacun est sincère, et aucun ne désigne personne tout seul.",
         "svg": _chaine()},
    ],
    "comptes": [
        {"titre": "Les huit jours",
         "leg": "Les points rouges sont les échéances qu'on ne déplace pas. "
                "La bande jaune est le déblaiement : il finit le 7 au soir, et c'est lui "
                "qui donne sa longueur à l'acte 1.",
         "svg": _frise()},
    ],
}
