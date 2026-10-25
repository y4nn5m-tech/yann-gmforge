#!/usr/bin/env python3
"""
organigramme-transport.py — qui est où, et la chaîne qui mène à Larissa.

    python3 scripts/organigramme-transport.py

Produit out/organigramme-transport.pdf : une A4 recto, **pour le meneur
seul**. Elle ne se pose pas sur la table.

## Ce qu'elle porte, et pourquoi dans cet ordre

**Neuf personnes, et ce qui les distingue n'est pas leur poste : c'est
où on les trouve.** L'un sous un wagonnet les mains noires, l'autre
introuvable entre huit heures et dix-sept, un troisième à plusieurs
kilomètres sur les voies — `85-secteur-transport.md`. C'est la colonne
qu'on consulte en pleine scène, quand un joueur dit *« on va voir le
conducteur »* et qu'il faut répondre tout de suite.

**Puis la chaîne du registre**, qui est l'ossature du dossier des
sabotages. Elle existe en prose dans `86-carnet-faddei.md`, et en prose
elle ne se consulte pas : il faut la voir d'un coup pour savoir quel
maillon manque encore.

> **Chaque maillon est facultatif.** S'ils s'arrêtent avant, il reste la
> veille nocturne. La chaîne n'est pas un passage obligé, c'est une
> carte de ce qu'ils ont déjà.

**Rien ne désigne Larissa avant Vasyukova.** Tout ce qui précède
construit un profil — quelqu'un qui connaît le matériel, qui est petit,
qui travaille la nuit et qui est au poste le matin.

Fond blanc : l'impression se fait sur du blanc ordinaire.
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
    {"doc": "L'organigramme du secteur transport",
     "papier": "papier blanc", "grammage": "80 g", "ou": "maison",
     "format": "A4", "feuilles": 1,
     "note": "**pour le meneur seul** · recto · ne se pose pas sur la table"},
]

T = "#1b1d21"

# (nom, poste, où on le trouve, posture, ce qu'il porte dans la chaîne)
EQUIPE = [
    ("Faddei Nikitine", "ingénieur, responsable",
     "au bureau toute la journée — plans le matin, registres l'après-midi",
     "débordé, coopératif, inquiet. Il <i>veut</i> qu'on l'aide",
     "le carnet, les quatre pièces"),
    ("Larissa Kazakova", "suivi administratif",
     "au bureau le matin, dans les hangars l'après-midi — <b>elle va partout, "
     "et personne ne s'en étonne</b>",
     "calme, serviable, précise. <b>Elle aide les enquêteurs</b>",
     "<b>C'EST ELLE</b>"),
    ("Anna Vasyukova", "ouvrière administrative",
     "assise au bureau, à côté de Larissa, de l'encre sur les doigts",
     "polie, nerveuse, cherche l'approbation de quelqu'un",
     "<b>elle a écrit la présence au registre</b>"),
    ("Zinaida Plotnikova", "entretien des bêtes",
     "au hangar, en train de panser un cheval — elle parle sans se retourner",
     "directe, concrète, pas impressionnée par Moscou",
     "<b>elle a vu Larissa partir vers les écuries</b>"),
    ("Boris Shcherbakov", "entretien des voies",
     "dehors, à plusieurs kilomètres — <b>une demi-journée pour aller le "
     "chercher</b>, ou l'attendre le soir",
     "taciturne, phrases courtes",
     "<b>il devait noter les présences et ne l'a pas fait</b>"),
    ("Grigori Moskalev", "contremaître des convois",
     "zone de stockage, un registre à la main — il compte en parlant et perd "
     "le fil",
     "agacé qu'on l'interrompe, pas hostile",
     "sa thèse : un saboteur venu de l'extérieur"),
    ("Stepan Udovenko", "hangar aux wagonnets",
     "sous un wagonnet, les mains noires — il sort pour répondre et y retourne",
     "professionnel, méfiant qu'on touche à son matériel",
     "il minimise, par loyauté"),
    ("Timur Bakhytov", "conducteur de convoi",
     "<b>introuvable de 8 h à 17 h</b> — au petit matin pendant l'attelage, ou "
     "le soir au retour",
     "il se plaint. Des quotas, de la sécurité, de Faddei",
     "<b>le suspect évident, et il est innocent</b>"),
    ("Yuri Bondarenko", "chargement",
     "en train de porter quelque chose, toujours — il répond entre deux charges",
     "fataliste, amical. Proche de Plotnikova",
     "peur de perdre son poste si on le retient"),
]


def equipe():
    return "".join(
        f'<tr class="{"cle" if "C\'EST ELLE" in porte else ""}">'
        f'<td class="n"><b>{nom}</b><br><span class="p">{poste}</span></td>'
        f'<td class="ou">{ou}</td>'
        f'<td class="po">{posture}</td>'
        f'<td class="ch">{porte}</td></tr>'
        for nom, poste, ou, posture, porte in EQUIPE)


CHAINE = """
<div class="et">
  <div class="bo dep"><b>LE REGISTRE</b> — carnet de Faddei, p. 1 et 3<br>
    « Kazakova au dépôt, le 27, 8 h – 11 h 30 »</div>
  <div class="fl">contredit par</div>
  <div class="deux">
    <div class="bo"><b>PLOTNIKOVA</b><br>« partie aux écuries avant le départ »</div>
    <div class="bo"><b>SHCHERBAKOV</b><br>« Faddei m'avait demandé de noter.<br>Je l'ai pas fait. »</div>
  </div>
  <div class="fl">donc : qui a écrit ?</div>
  <div class="bo"><b>VASYUKOVA</b> avoue : c'est elle.<br>
    Raison donnée — « elle était au carré, voir ses petits »
    <span class="av">SINCÈRE, ET FAUX</span></div>
  <div class="fl">vérification</div>
  <div class="bo"><b>LE CARRÉ DES TOMBES</b> — personne ne l'y a vue.
    Trois planches, même nom.<br><b>Une matinée inexpliquée.</b></div>
  <div class="fl">le dernier maillon</div>
  <div class="bo fin"><b>SACHA ORLOFF</b>, à la gare<br>
    « une femme du transport, elle demandait des explosifs »<br>
    <b>Seule preuve matérielle — et un rendez-vous demain</b></div>
</div>"""


HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A4; margin: 11mm 12mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: {T}; font-size: 8.4pt; line-height: 1.3; }}

h1 {{ font-size: 13pt; letter-spacing: .14em; margin: 0 0 .8mm; }}
.sous {{ font-size: 8.4pt; color: #5b616a; letter-spacing: .05em;
         border-bottom: 1.6px solid {T}; padding-bottom: 1.6mm; margin-bottom: 3mm; }}
.sous b {{ color: {T}; }}

table {{ width: 100%; border-collapse: collapse; }}
td {{ border-bottom: .6px solid #9aa0a8; padding: 1.5mm 2mm 1.5mm 0;
      vertical-align: top; }}
tr.cle td {{ background: #ececec; border-bottom-color: {T}; }}
.n {{ width: 23%; }}
.n .p {{ font-size: 7.4pt; color: #5b616a; }}
.ou {{ width: 31%; }}
.po {{ width: 25%; color: #41464e; }}
.ch {{ width: 21%; }}

h2 {{ font-size: 9.4pt; letter-spacing: .13em; margin: 5mm 0 2.4mm;
      border-bottom: 1.6px solid {T}; padding-bottom: 1.2mm; }}

.et {{ text-align: center; }}
.bo {{ border: 1px solid {T}; padding: 1.6mm 2.4mm; display: inline-block;
       max-width: 112mm; }}
.bo.dep {{ border-width: 1.8px; }}
.bo.fin {{ border-width: 1.8px; background: #ececec; }}
.fl {{ font-size: 7.4pt; color: #5b616a; font-style: italic; margin: 1.2mm 0;
       position: relative; }}
.fl::before {{ content: "↓"; display: block; font-size: 11pt; font-style: normal;
               line-height: 1; color: {T}; }}
.deux {{ display: flex; gap: 4mm; justify-content: center; }}
.deux .bo {{ flex: 1; max-width: 72mm; }}
.av {{ display: block; font-size: 7.4pt; letter-spacing: .1em; margin-top: .8mm; }}

.note {{ margin-top: 4mm; border-top: .6px solid #9aa0a8; padding-top: 2mm;
         font-size: 7.8pt; color: #41464e; }}
</style></head><body>

<h1>SECTEUR TRANSPORT</h1>
<div class="sous"><b>Pour le meneur seul.</b> Ne se pose pas sur la table.</div>

<table>{equipe()}</table>

<h2>LA CHAÎNE DU REGISTRE</h2>
{CHAINE}

<div class="note"><b>Chaque maillon est facultatif.</b> S'ils s'arrêtent avant, il reste
la veille nocturne. <b>Rien ne désigne Larissa avant Vasyukova</b> — tout ce qui précède
construit un profil : quelqu'un qui connaît le matériel, qui est petit, qui travaille la
nuit et qui est au poste le matin.</div>

</body></html>"""

cible = RACINE / "out" / "organigramme-transport.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
