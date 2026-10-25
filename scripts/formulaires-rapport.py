#!/usr/bin/env python3
"""
formulaires-rapport.py — les deux papiers de la dernière heure.

    python3 scripts/formulaires-rapport.py

Produit deux fichiers :

    out/formulaire-rapport.pdf   le rapport de mission, A4 recto-verso
    out/rapport-gusev.pdf        un demi-feuillet à en-tête, A5

## C'est un blanc de série, pas un imprimé fait pour eux

**Une administration n'imprime pas un formulaire pour une mission.**
Elle tire un modèle à des milliers d'exemplaires, et le bureau qui le
délivre remplit les champs variables à la machine. D'où la règle, qui
vaut pour les deux feuilles :

    composé         le titre, les rubriques, les filets, les champs
                    d'identification vides, et le pavé d'imprimerie en
                    pied — `Форма № 12-С`, l'atelier, le numéro de
                    commande, le tirage, une année **antérieure** à la
                    mission. C'est ce pavé qui dit que la feuille
                    existait avant eux
    dactylographié  le rappel de saisine seul — tapé par le bureau de
                    Moscou le jour de la remise, avec le décalage d'une
                    machine qu'on n'a pas calée sur le trait
    jamais rempli   **le cadre réservé à l'autorité saisie.** Une zone
                    qu'ils n'ont pas le droit de toucher prouve mieux
                    que tout que l'imprimé ne leur appartient pas

**Les rubriques ne posent aucune question.** Un formulaire administratif
réclame des pièces dans un ordre codifié — saisine, faits, mises en
cause, suites —, il n'interroge pas : les enquêtes sont trop diverses
pour ça.

## Le premier est sur la table depuis le jour 1

**Ils l'ont depuis Moscou** : les documents officiels de la mission sont
confiés au militaire, Voronin· le reçoit, Petrenko le réclame — le
rapport est son métier. Petite friction d'ouverture, gratuite, et en
caractère pour les deux.

**Les cases vides font le travail pendant six jours.** L'échéance est
posée sur la table, pas annoncée, et chaque découverte pose d'elle-même
la question *« est-ce que ça va dans le rapport ? »*.

**Le rappel de saisine est la pièce maîtresse** : tapé en tête, il dit
ce que Moscou croyait — *des sabotages*. Le document porte en haut le
postulat, et en bas ce qu'ils ont trouvé. **L'écart entre les deux est
l'épilogue**, et il est sous leurs yeux depuis le premier jour.

**Les rubriques suivent le squelette d'un rapport de mission** —
saisine, faits, éléments, personnes, mesures, exécution. Rien qui
désigne cette enquête-ci.

**Et « exécution de la mission » est la rubrique clé.** Tout rapport de
mission sépare ce qu'on a trouvé de la façon dont la mission s'est
déroulée : c'est la plus générique du document, elle accueillerait un
train en retard aussi bien qu'un mort. Elle reçoit les deux cases que
`105-epilogue-rapport.md` veut voir travailler, sans les nommer :

    concours et obstacles   elle **ne nomme personne**, et c'est
    auprès des services     capital. La mission est présentée comme une
    locaux                  enquête sur des sabotages précisément pour
                            ne pas révéler le manque de confiance
                            envers le chef de la police locale ; une
                            case qui le nommerait vendrait la mèche
                            avant l'arrivée. Elle devient cruelle à
                            remplir le jour où Igor se trahit
    incidents survenus      inutile le premier jour. Après la mine,
    en cours de mission     c'est autre chose

> **C'est là que le formulaire bat une feuille sortie à la fin.** Igor
> se trahit au briefing, et la case change de sens sans qu'on y ait
> touché. L'information était sous leurs yeux, et ils ne l'ont pas vue.

**Recto-verso, et pas davantage.** Un modèle de six pages à grandes
zones vierges produirait exactement ce que la note interdit : quatre
joueurs qui se taisent pendant que Petrenko rédige. **Des champs courts,
une ligne chacun** — la discussion reste orale, l'écriture ne fait que
l'enregistrer. Et c'est Petrenko qui dira *« je ne peux pas écrire
ça »*, ce qui vaut mieux que si le meneur le dit.

## Le second n'est pas un formulaire, et il ne doit pas l'être

**Une demi-page que Gusev· remplit seul**, pendant que le meneur s'isole
avec lui et que les autres attendent à côté. Deux papiers sur la table à
la fin, un public et un secret : c'est la dernière image de la campagne.

**Mais pas de blanc de série pour celui-là.** Une administration ne fait
pas tirer vingt-cinq mille exemplaires d'un imprimé destiné à ce qu'un
agent contredise ses coéquipiers : l'existence d'un formulaire
banaliserait le geste, alors que tout son poids vient de ce qu'il n'est
**pas prévu**. Ce genre d'écrit se fait sur papier libre, en main
propre.

**Et des rubriques le trahiraient.** « Le rapport collectif rend-il
compte des faits ? » n'a de sens que s'il existe un rapport collectif à
contredire : c'est du sur-mesure maquillé en imprimé.

D'où ce qu'il est : **du papier à en-tête réglé**, ce que toute
administration fournit. L'en-tête du service, le mot `РАПОРТ` — terme
générique d'un rapport d'agent à supérieur, qui n'annonce rien —, trois
champs d'identification, et des lignes vides.

> **Le guidage est oral, pas imprimé.** La décision se prend en aparté,
> après les discussions ; le meneur pose les questions, Gusev· écrit. Une
> feuille sans case est plus lourde à remplir que trois rubriques qui
> disent quoi répondre.

**Et il ne porte pas un mot de l'évaluation en cours.** Les joueurs
ignorent que la mission les teste ; un imprimé qui le dirait leur
donnerait la réponse de l'épilogue.

**Pas le jauni des dossiers.** Ces feuilles ont été délivrées à Moscou
le 24 avril ; elles ont voyagé sept jours dans une serviette et sont
restées six jours sur une table. Les rapports de police, eux, ont jauni
en archive pendant des mois. Le papier est déclaré dans `PAPIER`
ci-dessus — `python3 scripts/papiers.py` en fait la liste de courses.
Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "Le rapport de mission",
     "papier": "papier blanc", "grammage": "100 g", "ou": "maison",
     "format": "A4", "feuilles": 1,
     "note": "**recto-verso, retournement bord long** · 100 g passe en duplex automatique, dont le plafond est à 105. Du 80 g ordinaire convient aussi — un imprimé administratif mince qui laisse deviner son verso n'a rien d'un défaut"},
    {"doc": "Le rapport particulier de Gusev·",
     "papier": "papier blanc", "grammage": "100 g", "ou": "maison",
     "format": "A4", "feuilles": 1,
     "note": "A5 à découper dans une A4 · même stock que le précédent"},
]

T = "#1f2127"
LIGNE = 7.6      # la hauteur d'une ligne manuscrite


def lignes(n, haut=LIGNE):
    return "".join(f'<div class="l" style="height:{haut}mm"></div>' for _ in range(n))


def grille(colonnes, n, haut=LIGNE):
    """Un tableau à en-tête : une ligne par entrée, rien de plus."""
    larg = "".join(f'<col style="width:{w}%">' for _, w in colonnes)
    tete = "".join(f"<td>{t}</td>" for t, _ in colonnes)
    corps = "".join("<tr>" + "<td></td>" * len(colonnes) + "</tr>" for _ in range(n))
    return (f'<table style="--h:{haut}mm"><colgroup>{larg}</colgroup>'
            f'<tr class="th">{tete}</tr>{corps}</table>')


STYLE = f"""
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Machine; src: url({F}/SpecialElite-Regular.ttf); }}

*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: {T}; font-size: 9.2pt; }}

/* ── l'en-tête administratif ─────────────────────────────────── */
.tete {{ display: flex; justify-content: space-between; align-items: flex-start;
         gap: 6mm; }}
.org {{ font-size: 7.6pt; letter-spacing: .09em; line-height: 1.55; }}
.org .ru {{ color: #555b63; }}
.org .sec {{ margin-top: 1.4mm; }}
.secret {{ border: 1px solid {T}; padding: 1.2mm 3.4mm; text-align: center;
           white-space: nowrap; }}
.secret .ru {{ font-size: 7.4pt; letter-spacing: .18em; display: block; }}
.secret .fr {{ font-size: 8.6pt; letter-spacing: .26em; font-weight: bold;
               display: block; margin-top: .4mm; }}
.filet {{ border-bottom: 1.4px solid {T}; margin: 2.6mm 0 1px; }}
.filet + * {{ border-top: .5px solid {T}; padding-top: 4mm; }}

h1 {{ font-size: 15pt; font-weight: bold; letter-spacing: .2em; text-align: center;
      margin: 0 0 1.2mm; }}
.sous {{ text-align: center; font-size: 8pt; letter-spacing: .1em;
         color: #555b63; margin-bottom: 4.4mm; }}

/* ── les champs d'identification, laissés vides ──────────────── */
.id {{ margin-bottom: 4.4mm; }}
.id > div {{ display: flex; gap: 6mm; margin-bottom: 2.6mm; }}
.id .ch {{ display: flex; align-items: baseline; flex: 1; }}
.id .lb {{ flex: none; font-size: 8pt; letter-spacing: .07em; color: #555b63;
           margin-right: 2mm; white-space: nowrap; }}
.id .tr {{ flex: 1; border-bottom: .5px solid #878d95; height: 5mm; }}

h2 {{ font-size: 8.8pt; font-weight: bold; letter-spacing: .13em;
      margin: 2.4mm 0 1.6mm; }}
h2 .pt {{ font-weight: normal; font-size: 7.6pt; color: #555b63;
          letter-spacing: .03em; }}

.l {{ border-bottom: .5px solid #878d95; }}
/* Une rubrique peut se diviser sans devenir une rubrique de plus. */
.ss {{ font-size: 8pt; letter-spacing: .05em; color: #3f444c;
       margin: 1.6mm 0 1mm; }}

/* ── le rappel de saisine, tapé à la machine ─────────────────── */
.saisie {{ border: .5px solid #878d95; padding: 3mm 4mm 3.4mm;
           font-family: Machine, monospace; font-size: 9pt; line-height: 1.75; }}
.saisie div:nth-child(1) {{ position: relative; left: .4mm; }}
.saisie div:nth-child(2) {{ position: relative; left: -.3mm; top: .3mm; }}
.saisie div:nth-child(3) {{ position: relative; left: .8mm; top: -.2mm; }}
.saisie div:nth-child(4) {{ position: relative; left: .2mm; top: .4mm; }}

table {{ width: 100%; border-collapse: collapse; }}
table td {{ border: .5px solid #878d95; height: var(--h); padding: 0 2mm; }}
table tr.th td {{ height: 6mm; font-size: 7.8pt; letter-spacing: .07em;
                  color: #555b63; border-bottom-width: 1px; }}

.sign {{ display: flex; gap: 4mm; margin-top: 2mm; }}
.sign div {{ flex: 1; border-bottom: .5px solid {T}; height: 10mm; }}
.sign + .leg {{ display: flex; gap: 4mm; font-size: 7pt; color: #555b63;
                letter-spacing: .05em; margin-top: 1.2mm; }}
.sign + .leg span {{ flex: 1; }}

/* ── la zone qu'ils ne remplissent pas ───────────────────────── */
.autorite {{ border: 1px solid {T}; padding: 2.4mm 4mm 2mm; margin-top: 3.6mm; }}
.autorite .t {{ font-size: 8pt; font-weight: bold; letter-spacing: .13em;
                margin-bottom: .8mm; }}
.autorite .m {{ font-size: 7.2pt; color: #555b63; letter-spacing: .05em;
                margin-bottom: 2.6mm; }}
.autorite .s {{ font-size: 7.6pt; color: #555b63; letter-spacing: .06em;
                margin: 2.6mm 0 1.4mm; }}

.rappel {{ display: flex; justify-content: space-between; font-size: 7.6pt;
           letter-spacing: .1em; color: #555b63;
           border-bottom: .5px solid #878d95; padding-bottom: 1.4mm;
           margin-bottom: 3.4mm; }}
.pied {{ margin-top: 3.6mm; border-top: .5px solid #878d95; padding-top: 1.6mm;
         display: flex; justify-content: space-between;
         font-size: 7.2pt; color: #555b63; letter-spacing: .05em; }}
.verso {{ break-before: page; }}
"""

ENTETE = """
<div class="tete">
  <div class="org">
    <span class="ru">СОЮЗ СОВЕТСКИХ СОЦИАЛИСТИЧЕСКИХ РЕСПУБЛИК</span><br>
    UNION DES RÉPUBLIQUES SOCIALISTES SOVIÉTIQUES
    <div class="sec">
      <span class="ru">ОБЪЕДИНЁННОЕ ГОСУДАРСТВЕННОЕ ПОЛИТИЧЕСКОЕ УПРАВЛЕНИЕ · ОГПУ</span><br>
      DIRECTION POLITIQUE D'ÉTAT UNIFIÉE<br>
      SECTION SPÉCIALE — AFFAIRES INDUSTRIELLES
    </div>
  </div>
  <div class="secret"><span class="ru">СЕКРЕТНО</span><span class="fr">SECRET</span></div>
</div>
<div class="filet"></div>"""

TYPO = "Форма № 12-С · Тип. ОГПУ, зак. 4418, тир. 25 000 · 1931 г."


def champ(libelle):
    return f'<div class="ch"><span class="lb">{libelle}</span><span class="tr"></span></div>'


RAPPORT = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 14mm 16mm; }}
{STYLE}
</style></head><body>
{ENTETE}

<div>
<h1>RAPPORT DE MISSION</h1>
<div class="sous">À ÉTABLIR PAR LE CHEF DE MISSION — UN SEUL EXEMPLAIRE</div>

<div class="id">
  <div>{champ("Dossier n°")}{champ("Rapport n°")}{champ("Feuillet 1 sur")}</div>
  <div>{champ("Destinataire")}</div>
  <div>{champ("Rédigé par")}{champ("Qualité")}</div>
  <div>{champ("Fait à")}{champ("le")}</div>
</div>

<h2>I. OBJET DE LA MISSION <span class="pt">— rappel de la saisine</span></h2>
<div class="saisie">
  <div>Mission n° 112 / DMM — ordre de détachement du 24 avril 1932.</div>
  <div>Enquête sur une série d'actes de sabotage présumés sur le site</div>
  <div>du combinat métallurgique de Magnitogorsk, district de Tcheliabinsk.</div>
  <div>Échéance : trois semaines, aller-retour compris.</div>
</div>

<h2>II. FAITS EXAMINÉS ET CONCLUSION RETENUE POUR CHACUN</h2>
{grille([("Fait examiné", 38), ("Conclusion retenue", 62)], 8)}

<h2>III. ÉLÉMENTS RECUEILLIS <span class="pt">— déclarations, constatations,
  pièces et documents</span></h2>
{lignes(3)}
</div>

<div class="verso">
<div class="rappel"><span>SECRET · СЕКРЕТНО</span>
  <span>Dossier n° ................</span><span>Feuillet 2</span></div>

<h2>IV. PERSONNES CONCERNÉES</h2>
{grille([("Nom", 26), ("Fonction et service", 30), ("Lien avec les faits", 44)], 4)}

<h2>V. MESURES PRISES ET PROPOSITIONS</h2>
{lignes(3)}

<h2>VI. EXÉCUTION DE LA MISSION</h2>
<div class="ss">Concours et obstacles rencontrés auprès des services locaux</div>
{lignes(3)}
<div class="ss">Incidents survenus en cours de mission</div>
{lignes(3)}

<h2>VII. PIÈCES JOINTES <span class="pt">— le présent rapport comporte
  ........ feuillets et ........ annexes</span></h2>
{lignes(1)}

<h2>VIII. SIGNATURES</h2>
<div class="sign"><div></div><div></div><div></div><div></div><div></div><div></div></div>
<div class="leg"><span>Nom et qualité</span><span></span><span></span>
  <span></span><span></span><span></span></div>

<div class="autorite">
  <div class="t">RÉSERVÉ À L'AUTORITÉ SAISIE</div>
  <div class="m">Ne rien inscrire au-dessous de ce trait.</div>
  <div class="s">Observations</div>
  {lignes(1, 6.2)}
  <div class="s">Décision et instructions</div>
  {lignes(2, 6.2)}
  <div class="s">Date et visa</div>
  {lignes(1, 6.2)}
</div>

<div class="pied"><span>À remettre en main propre.</span><span>{TYPO}</span></div>
</div>

</body></html>"""

GUSEV = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size: A5; margin: 12mm 13mm; }}
{STYLE}
body {{ font-size: 8.6pt; }}
.org {{ font-size: 6.4pt; line-height: 1.5; }}
.secret .ru {{ font-size: 6.4pt; }} .secret .fr {{ font-size: 7.4pt; }}
h1 {{ font-size: 13pt; letter-spacing: .3em; margin-bottom: .6mm; }}
h1 .ru {{ display: block; font-size: 8.4pt; letter-spacing: .34em;
          color: #555b63; font-weight: normal; margin-bottom: 1mm; }}
.id {{ margin-bottom: 3mm; }}
.id .lb {{ font-size: 7.4pt; }}
.id .tr {{ height: 4.6mm; }}
.corps {{ margin-top: 1mm; }}
.bas {{ display: flex; gap: 6mm; margin-top: 4mm; }}
.bas div {{ flex: 1; border-bottom: .5px solid {T}; height: 11mm; }}
.bas + .leg {{ display: flex; gap: 6mm; font-size: 7pt; color: #555b63;
               letter-spacing: .05em; margin-top: 1.2mm; }}
.bas + .leg span {{ flex: 1; }}
</style></head><body>
{ENTETE}

<div>
<h1><span class="ru">РАПОРТ</span>RAPPORT</h1>

<div class="id">
  <div>{champ("À")}</div>
  <div>{champ("De")}{champ("Qualité")}</div>
  <div>{champ("Dossier n°")}{champ("Fait à")}{champ("le")}</div>
</div>

<div class="corps">{lignes(12)}</div>

<div class="bas"><div></div><div></div></div>
<div class="leg"><span>Signature</span><span></span></div>
</div>

</body></html>"""


def main():
    for nom, html in (("formulaire-rapport", RAPPORT), ("rapport-gusev", GUSEV)):
        cible = RACINE / "out" / f"{nom}.pdf"
        rendu.pdf(html, cible, RACINE)
        print(f"· {cible.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
