#!/usr/bin/env python3
"""
rapports-police.py — les sept dossiers de la section de Magnitogorsk.

    python3 scripts/rapports-police.py                     # les sept
    python3 scripts/rapports-police.py mrt dec             # ceux-là seulement
    python3 scripts/rapports-police.py dep                 # la déposition manuscrite
    python3 scripts/rapports-police.py --sans-annotations  # blanc réservé

Produit out/rapport-<code>.pdf, un par dossier. **Fond blanc** :
l'impression se fait sur du papier déjà jauni.

Ce que ces documents doivent faire, et c'est tout l'enjeu :

    du réalisme,     ce sont des pièces d'archives, pas des fiches
    pas une aide     d'indices. Si la table bloque, le MJ aide à la
                     table — pas le document
    du bruit         formules administratives, précisions sans intérêt,
                     un témoin qui n'apporte rien et qu'on consigne
                     quand même
    de la densité    petits caractères, marges étroites. Un document
                     administratif réel ne respire pas

**La longueur dit le soin qu'on y a mis.** Le noyé tient en une
demi-page — Igor voulait le classer et on l'a expédié ; les
disparitions en font deux, parce qu'un agent zélé l'a monté et qu'il a
été muté pour ça. Le contraste en dit plus sur lui que n'importe quel
tampon.

Les **trois dossiers ouverts** portent en tête une mention de
synthèse : ils n'ont pas été tapés à leur ouverture, mais la veille
du briefing, pour être remis. C'est ce qui justifie qu'un dossier où
personne n'a été interrogé existe en version dactylographiée — et ce
qui dit, sans le dire, que ces pages ont été préparées pour eux.

Un huitième document échappe à la règle : les **deux dépositions
manuscrites de Faddei** (`rapport-dep-faddei.pdf`, deux feuillets),
agrafées au dossier des sabotages. Voir plus bas.

**Quatre dossiers sur sept portent CLASSÉ**, et quatre seulement : la
pile montre alors ce qu'Igor ferme vite et ce qu'il laisse en plan.

Les annotations de sa main sont imprimées en Caveat. `--sans-annotations`
les omet, pour les porter au stylo sur l'épreuve : la note étant hors du
flux, rien n'est à réserver — on écrit où l'on veut.

Textes dans preparation/magnitogorsk/71-rapports-textes.md.
Rendu par Chrome — voir scripts/rendu.py.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
MANUSCRIT = "--sans-annotations" not in sys.argv
GRILLE = "--grille" in sys.argv
F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "Les sept dossiers de police",
     "papier": "papier jauni", "grammage": "160 g", "ou": "maison", "stock": True,
     "format": "A4", "feuilles": 8,
     "note": "recto seul · 1932-03/ENT fait deux feuillets"},
    {"doc": "Les deux dépositions de Faddei",
     "papier": "papier jauni", "grammage": "160 g", "ou": "maison", "stock": True,
     "format": "A4", "feuilles": 2,
     "note": "recto seul"},
    {"doc": "Les chemises des dossiers",
     "papier": "chemise cartonnée kraft ou gris-beige", "grammage": "~250 g",
     "ou": "papeterie", "format": "A4", "feuilles": 10,
     "note": "**rien d'imprimé dessus** : le titre, la cote et les dates se portent "
             "à la main, même stylo pour les huit · sans rabat ni élastique · "
             "huit en service, deux de rab"},
]


def classe(date):
    """Le cachet de classement : rectangulaire, encre mangée.

    **La date s'écrit en texte simple** : un `<sup>` dans un `<text>` SVG
    n'est pas rendu, et Chrome rejette le morceau orphelin en pied de page.
    """
    return f"""
<svg class="classe" viewBox="0 0 300 108" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <filter id="cl" x="-15%" y="-25%" width="130%" height="150%">
    <feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="3" seed="23" result="b"/>
    <feDisplacementMap in="SourceGraphic" in2="b" scale="2.4"
                       xChannelSelector="R" yChannelSelector="G" result="d"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.07" numOctaves="2" seed="41" result="t"/>
    <feColorMatrix in="t" type="matrix"
      values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.7 0 0 0 -0.3" result="m"/>
    <feComposite in="d" in2="m" operator="out"/>
  </filter>
 </defs>
 <g filter="url(#cl)" fill="#8c2b22">
  <rect x="5" y="5" width="290" height="98" fill="none" stroke="#8c2b22" stroke-width="5"/>
  <text x="150" y="48" font-size="34" letter-spacing="9" text-anchor="middle"
        font-family="PT" font-weight="bold">В ДЕЛО</text>
  <text x="150" y="82" font-size="21" letter-spacing="2.4" text-anchor="middle"
        font-family="PT">CLASSÉ · {date}</text>
 </g>
</svg>"""


def grille():
    """Le quadrillage de --grille : abscisses en rouge, ordonnées en bleu,
    un trait tous les 20 mm. Les repères vivent **dans** la page : la marge
    de @page n'est pas rendue, un trait posé dedans serait invisible."""
    if not GRILLE:
        return ""
    e = []
    # Les ordonnées courent sur toute la hauteur du corps, pages suivantes
    # comprises : un document de deux pages se repère jusqu'au bout.
    for x in range(0, 180, 20):
        e.append(f'<b style="left:{x}mm; top:0; width:.25mm; height:100%"></b>')
        # l'abscisse se rappelle tous les 60 mm, sinon elle manque page 2
        for rappel in range(0, 600, 60):
            e.append(f'<i style="left:{x + .6}mm; top:{rappel + .5}mm">{x}</i>')
    for y in range(0, 600, 20):
        e.append(f'<b class="v" style="left:0; top:{y}mm; height:.25mm; width:100%"></b>')
        e.append(f'<i class="v" style="left:.6mm; top:{y + .6}mm">{y}</i>')
    return f'<div class="regle">{"".join(e)}</div>'


def doc(corps, tampon="", annot="", hauteur_annot="12mm", cotes=None, coupures=False,
        portrait="", main=""):
    # Igor écrit au stylo, en vitesse : pas d'encre mangée, mais la main
    # tremble un peu plus que pour un document qu'on soigne.
    bloc = (f'<div class="plume annot" style="{main}">'
            f'{ecrire(annot, graine=abs(hash(annot)) % 997, amplitude=1.15)}</div>'
            if (MANUSCRIT and annot)
            else f'<div style="height:{hauteur_annot}"></div>' if annot else "")
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Machine; src: url({F}/SpecialElite-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4; margin: 13mm 16mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Machine, serif; font-size: 8.3pt; line-height: 1.44;
        color: #1a1713; position: relative; }}
{"p, .temoin, .cadre {{ hyphens: auto; -webkit-hyphens: auto; }}" if coupures else ""}
.frappe {{ filter: url(#frappe); }}

.bandeau {{ font-family: PT, serif; font-size: 6.6pt; letter-spacing: .14em;
            border-bottom: 1.6px solid #1a1713; padding-bottom: 1.6mm; margin-bottom: 3.4mm;
            padding-left: 38mm; padding-right: 20mm; }}
.bandeau .ru {{ letter-spacing: .2em; }}

.entete {{ display: flex; justify-content: space-between; align-items: flex-start;
           margin-bottom: 3.6mm; gap: 6mm; }}
.entete .g {{ width: 63%; }}
.entete .d {{ width: 33%; font-size: 7.6pt; line-height: 1.6; text-align: right; }}
.num {{ font-family: PT, serif; font-size: 11.6pt; font-weight: bold; letter-spacing: .07em; }}
.objet {{ font-size: 8.2pt; margin-top: .8mm; }}
.synthese {{ font-family: PT, serif; font-size: 6.9pt; font-style: italic; color: #40382f;
             letter-spacing: .04em; border-left: 2.2px solid #1a1713; padding-left: 2.6mm;
             margin: -1.6mm 0 3.6mm; line-height: 1.5; }}

h2 {{ font-family: Machine, serif; font-size: 8.3pt; font-weight: normal;
      letter-spacing: .22em; text-decoration: underline; text-underline-offset: 1.6px;
      text-decoration-thickness: .6px; margin: 3.8mm 0 1.9mm; }}
p {{ margin: 0 0 2mm; text-align: justify; }}
/* ── la photo collée, et le cachet qui mord dessus ──────────── */
.photo {{ float: right; position: relative; z-index: 1; width: 29mm; margin: 0 0 2.5mm 5mm;
          background: #fff; padding: 1.4mm 1.4mm 0; border: .4px solid #b9b2a6;
          transform: rotate(1.4deg); }}
.photo img {{ display: block; width: 100%; filter: contrast(1.06) brightness(.98); }}
.photo .leg {{ font-family: PT, serif; font-size: 5.4pt; letter-spacing: .06em;
               text-align: center; padding: .7mm 0 .9mm; color: #3a342c; }}
svg.sceau {{ position: absolute; width: 17mm; height: 17mm; right: -4mm; bottom: -2mm;
             mix-blend-mode: multiply; }}

.fiche {{ margin: 0 0 2.4mm; line-height: 1.75; }}
.fiche .k {{ display: inline-block; width: 44mm; }}
.temoin {{ margin: 0 0 2.2mm 4mm; }}
.temoin .q {{ font-weight: bold; }}

table {{ width: 100%; border-collapse: collapse; font-size: 7.8pt; margin: 1mm 0 2.6mm;
         table-layout: fixed; }}
th {{ text-align: left; font-family: PT, serif; font-weight: bold; font-size: 6.8pt;
      letter-spacing: .08em; border-bottom: .8px solid #1a1713; padding: 0 2mm 1mm 0; }}
td {{ padding: .8mm 2mm .8mm 0; vertical-align: top; }}

.cadre {{ border: .9px solid #1a1713; padding: 2.2mm 3mm; margin: 2.4mm 0; }}
.sign {{ margin-top: 5mm; text-align: right; font-size: 8pt; line-height: 1.7; }}
.pied {{ margin-top: 4.5mm; border-top: .7px solid #1a1713; padding-top: 1.3mm;
         font-family: PT, serif; font-size: 6.4pt; letter-spacing: .07em; text-align: center; }}

/* ── les deux cotes d'archive, deux inventaires successifs ──── */
/* --grille : une règle sur les deux bords, pour relever une position
   et la dicter. Pas un quadrillage : le document doit rester lisible. */
.regle {{ position: absolute; inset: 0; pointer-events: none; }}
.regle b {{ position: absolute; background: #d33; opacity: .33; }}
.regle b.v {{ background: #39c; }}
.regle i {{ position: absolute; font-family: PT, serif; font-size: 5.2pt; color: #d33;
            font-style: normal; }}
.regle i.v {{ color: #2a7fa8; }}

.cotes {{ position: absolute; right: 0; top: -4.5mm; text-align: right; line-height: 1; }}
.cotes .tampon {{ font-family: PT, serif; font-size: 13pt; font-weight: bold; color: #2a2724; }}
.cotes .crayon {{ font-family: Plume, cursive; font-size: 13pt; color: #6b6356;
                  display: block; margin: .4mm -1.5mm 0 0; transform: rotate(-3deg); }}

.plume {{ font-family: Plume, cursive; color: #233a66; }}
/* Hors du flux : une note manuscrite ne pousse pas le texte tapé, elle
   se glisse dans un blanc ou passe par-dessus. Position donnée en
   millimètres depuis le coin haut-gauche de la zone imprimée. */
.annot {{ position: absolute; z-index: 9; font-size: 13pt; line-height: 1.25;
          transform-origin: left center; white-space: nowrap; }}
.registre {{ position: absolute; left: 1mm; top: -1mm; font-size: 11.5pt;
             transform: rotate(-2.5deg); white-space: nowrap; }}
.registre small {{ font-size: 8.5pt; }}

/* Le coin droit est pris par la photo et les cotes d'archive : le cachet
   se pose à gauche, en travers du texte — ce qu'il fait de toute façon
   sur un vrai dossier. */
svg.classe {{ position: absolute; width: 52mm; height: 19mm;
              left: 17mm; top: 96mm; transform: rotate(-6deg);
              opacity: .55; mix-blend-mode: multiply; }}
</style></head><body>

{FILTRES}
<svg width="0" height="0" style="position:absolute">
 <filter id="frappe">
   <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" seed="3" result="n"/>
   <feDisplacementMap in="SourceGraphic" in2="n" scale="0.55"
                      xChannelSelector="R" yChannelSelector="G"/>
 </filter>
</svg>

{grille()}
<div class="frappe">
{cotes or ""}
<div class="bandeau">
  <div class="ru">РАБОЧЕ-КРЕСТЬЯНСКАЯ МИЛИЦИЯ — МАГНИТОГОРСК</div>
  <div>SECTION DE POLICE DE MAGNITOGORSK — DOCUMENT DE SERVICE</div>
</div>
{corps.replace("<!--ANNOT-->", bloc).replace("<!--PHOTO-->", portrait)}
</div>
{tampon}
</body></html>"""


NOMS = ["Pavlenko", "Stepanoff", "Petroff", "Vinogradoff", "Nesteroff", "Nikitine",
        "Belousoff", "Nikitina", "Tkachenko", "Kurbanoff", "Kazakoff", "Orloff",
        "Gordeeva", "Nikiforov", "Zykov"]


def capitales(corps):
    """Les noms propres se frappent en capitales — usage du temps.

    Hors des blocs déjà composés en capitales (en-tête, signature, pied) et
    hors des annotations manuscrites, qui sont d'une autre main.
    """
    garde = []

    def met_de_cote(m):
        garde.append(m.group(0))
        return f"\x00{len(garde) - 1}\x00"

    corps = re.sub(r'<div class="(?:entete|sign|pied|plume registre)".*?</div>\s*(?=<|$)',
                   met_de_cote, corps, flags=re.S)
    corps = re.sub(r"<!--ANNOT-->", met_de_cote, corps)
    for n in NOMS:
        corps = re.sub(rf"\b{n}\b", n.upper(), corps)
    return re.sub(r"\x00(\d+)\x00", lambda m: garde[int(m.group(1))], corps)



# ══════════════════════════════════════════════════════════════════
#  Les photographies agrafées aux dossiers
# ══════════════════════════════════════════════════════════════════
#
#  Trois portraits, tirés des images livrées avec le scénario et
#  choisis dans preparation/magnitogorsk/15-photographies.md.
#
#  **Le dossier du déserteur n'en a pas, et c'est voulu** : aucune
#  image ne colle à un urbaniste de quarante-deux ans, et un dossier
#  de disparition sans portrait du disparu dit à lui seul le soin
#  qu'on y a mis.
#
#  Les sources ne sont pas versionnées. Si elles manquent, la
#  vignette est simplement absente et le document se compose quand
#  même — on ne casse pas une génération pour une image.

ARCHIVE = RACINE / "sources" / "magnitogorsk" / "Archive" / "archives photos"

PORTRAITS = {
    # dossier : (fichier, cadre de recadrage ou None, légende)
    "dec": ("img36.jpg", (40, 20, 560, 700), "KURBANOFF, V. A."),
    "emp": ("img118.jpg", None, "IGNATIEVA, N."),
    "mrt": ("img145.jpg", (10, 20, 300, 504), "KRYLOVA, Z. P."),
}


def vignette(code):
    """La photo collée au dossier, un peu de travers, sous son cachet.

    Tirage noir et blanc à marge blanche, comme un vrai tirage d'époque
    — c'est la marge qui fait l'objet collé plutôt que l'image imprimée.
    """
    if code not in PORTRAITS:
        return ""
    nom, cadre, legende = PORTRAITS[code]
    src = ARCHIVE / nom
    if not src.is_file():
        print(f"  · {code} : {nom} absent, vignette omise")
        return ""
    try:
        from PIL import Image
    except ImportError:
        print("  · Pillow absent, vignettes omises")
        return ""
    import base64
    import io

    im = Image.open(src).convert("L")
    if cadre:
        im = im.crop(cadre)
    im.thumbnail((420, 560))
    tampon = io.BytesIO()
    im.save(tampon, format="JPEG", quality=88)
    b64 = base64.b64encode(tampon.getvalue()).decode()
    return f"""<div class="photo">
  <img src="data:image/jpeg;base64,{b64}" alt="">
  <div class="leg">{legende}</div>
  <svg class="sceau" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
   <g filter="url(#frappe)" fill="none" stroke="#8c2b22" opacity=".55">
     <circle cx="60" cy="60" r="52" stroke-width="2.4"/>
     <circle cx="60" cy="60" r="44" stroke-width="1"/>
   </g>
   <text x="60" y="56" font-size="13" letter-spacing="1.4" text-anchor="middle"
         font-family="PT" font-weight="bold" fill="#8c2b22" opacity=".5">МИЛИЦИЯ</text>
   <text x="60" y="74" font-size="10" letter-spacing="1" text-anchor="middle"
         font-family="PT" fill="#8c2b22" opacity=".5">МАГНИТОГОРСК</text>
  </svg>
</div>"""


# ══════════════════════════════════════════════════════════════════
#  Les sept dossiers
# ══════════════════════════════════════════════════════════════════

MRT = """
<div class="entete">
  <div class="g">
    <div class="num">RAPPORT D'ENQUÊTE N° 1932-06/MRT</div>
    <div class="objet">Homicide — quartier du Komsomol, complexe industriel</div>
  </div>
  <div class="d">
    Agent instructeur : L. Vinogradoff<br>Agent de police, 2<sup>e</sup> classe<br>
    Ouvert le : 5 avril 1932<br>Classé le : 28 avril 1932
  </div>
</div>

<!--PHOTO-->
<h2>FICHE D'IDENTITÉ — VICTIME</h2>
<div class="fiche">
<span class="k">Nom :</span><b>KRYLOVA, Zinaïda Pavlovna</b><br>
<span class="k">Date de naissance :</span>12 septembre 1912 — Leningrad<br>
<span class="k">Fonction :</span>Gymnaste — membre active du Komsomol<br>
<span class="k">Domicile :</span>Baraquement n°5, chambre 8<br>
<span class="k">Date du décès :</span>Dans la nuit du 4 au 5 avril 1932<br>
<span class="k">Lieu de découverte :</span>Abords du gymnase du Komsomol — côté nord<br>
<span class="k">Cause du décès :</span>Strangulation — établie par le rapport d'autopsie du Dr Nesteroff
</div>

<h2>I. CIRCONSTANCES DE LA DÉCOUVERTE</h2>
<p>Le corps de la camarade Krylova a été découvert aux premières heures du matin du 5 avril 1932 par
un membre du Komsomol se rendant à une séance d'entraînement matinale. Il avait neigé toute la nuit
et les éventuelles traces au sol avaient disparu.</p>

<h2>II. TÉMOIGNAGES ET INVESTIGATIONS</h2>
<div class="temoin"><span class="q">E. May et membres du bureau d'études</span> — interrogés les 6
et 7 avril. Aucun élément pertinent recueilli. Les ressortissants étrangers ont été systématiquement
interrogés sur leurs activités dans la nuit du 4 au 5 avril. Leurs déclarations ont été jugées
satisfaisantes.</div>
<div class="temoin"><span class="q">A. Kuzmina, komsomolka</span> — placée en détention le 10 avril,
relâchée le 14 avril. Initialement suspectée en raison de sa proximité avec la victime dans le cadre
des activités de gymnastique. Sa détention n'a pas permis d'obtenir d'aveux relatifs au meurtre. Elle
a déclaré avoir passé la nuit du crime au domicile d'un ressortissant français, J.-B. Messelier, ce
que ce dernier a confirmé lors de son audition. Suspicion levée.</div>
<div class="temoin"><span class="q">Fouille de la chambre de M. Kazakoff</span> — réalisée le
18 avril. A permis de découvrir : une photographie de la victime, une mèche de cheveux pouvant lui
appartenir, et une cordelette portant des traces de sang séché. Ces éléments constituent les preuves
principales à charge retenues contre le suspect.</div>

<!--ANNOT-->

<h2>PERSONNE INCULPÉE</h2>
<div class="fiche">
<span class="k">Nom :</span><b>KAZAKOFF, Maxim Illitch</b> — agent d'entretien, Komsomol<br>
<span class="k">Chef d'inculpation :</span>Homicide volontaire<br>
<span class="k">Lieu de détention :</span>Prison, bloc 27 — Magnitogorsk<br>
<span class="k">Jugement :</span>Prononcé le 2 mai 1932 — départ pour le Goulag, semaine du 8 mai
</div>

<h2>III. CONCLUSION</h2>
<div class="cadre"><p>L'enquête établit que Maxim Kazakoff, agent d'entretien au Komsomol, a commis
le meurtre de la camarade Krylova dans la nuit du 4 au 5 avril 1932. Les preuves matérielles
découvertes à son domicile, associées à l'incapacité du suspect à fournir une version cohérente des
faits, permettent de conclure à sa culpabilité. L'affaire est classée.</p></div>

<div class="sign">
  L. VINOGRADOFF — agent de police, 2<sup>e</sup> classe<br>
  Section de police de Magnitogorsk<br>L'an mil neuf cent trente-deux, le vingt-huit avril.<br>
  <i>Approuvé</i> — I. PAVLENKO, chef de section · 28 avril 1932
</div>
<div class="pied">RAPPORT N° 1932-06/MRT — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0412 · 5.IV.32</div>
"""

DIS = """
<div class="entete">
  <div class="g">
    <div class="num">RAPPORT DE DISPARITION N° 1932-07/DIS</div>
    <div class="objet">Disparition d'un ressortissant soviétique — complexe industriel</div>
  </div>
  <div class="d">
    Agent instructeur : I. Stepanoff<br>Agent de police, 4<sup>e</sup> classe<br>
    Ouvert le : 29 avril 1932<br>Enquête en cours
  </div>
</div>

<div class="synthese">
Synthèse établie pour transmission — état du dossier au 2 mai 1932.<br>
Le dossier demeure ouvert. Les pièces originales restent au registre de la section.
</div>
<h2>FICHE D'IDENTITÉ — PERSONNE DISPARUE</h2>
<div class="fiche">
<span class="k">Nom :</span><b>TKACHENKO, Pavel Semyonovitch</b><br>
<span class="k">Date de naissance :</span>14 février 1890 — Petrograd<br>
<span class="k">Profession :</span>Urbaniste — bureau d'études de Sotsgorod<br>
<span class="k">Affectation :</span>Projet Sotsgorod, Magnitogorsk — depuis août 1931<br>
<span class="k">Domicile :</span>Baraquement n°3, chambre 4<br>
<span class="k">Signalement :</span>Taille moyenne, cheveux bruns grisonnants, lunettes rondes<br>
<span class="k">Dossier Guépéou :</span><b>Surveillé</b> — antécédents au service du gouvernement
tsariste. Famille déportée.
</div>

<h2>I. CIRCONSTANCES DE LA DISPARITION</h2>
<p>Le nommé Tkachenko Pavel S. n'a pas rejoint son poste au bureau d'études le mardi 26 avril 1932 au
matin. Son supérieur hiérarchique, l'architecte E. May, a signalé son absence en fin de journée
auprès de l'administration du complexe. Le signalement n'est parvenu aux services de police que le
29 avril, soit trois jours plus tard, en raison d'un délai de transmission administratif.</p>

<h2>II. TÉMOIGNAGES RECUEILLIS</h2>
<div class="temoin"><span class="q">E. May, architecte</span> — interrogé le 29 avril. Décrit
Tkachenko comme un collaborateur compétent mais d'humeur anxieuse ces dernières semaines. Affirme
n'avoir reçu aucun avertissement de départ. Ne soupçonne aucun de ses collaborateurs étrangers
d'être impliqué. Se dit choqué et préoccupé par l'avenir du projet.</div>
<div class="temoin"><span class="q">Collègues du bureau d'études</span> — interrogés collectivement
le 30 avril. Décrivent un homme réservé et peu liant. Plusieurs notent une nervosité accrue depuis
plusieurs semaines. L'un d'eux signale avoir vu Tkachenko brûler des papiers dans le poêle de la
salle commune environ trois jours avant sa disparition — fait jugé anodin sur le moment.</div>

<h2>III. HYPOTHÈSE PRINCIPALE RETENUE</h2>
<p>Au vu des éléments recueillis et compte tenu du profil de l'intéressé — antécédents politiques,
famille déportée, surveillance active de la Guépéou — il est probable que la disparition soit liée à
une activité de renseignement au profit d'une puissance étrangère. L'intéressé travaillait sous les
ordres directs d'un ressortissant allemand et entretenait des contacts réguliers avec plusieurs
ingénieurs étrangers dont les allégeances restent à établir. Il est possible que Tkachenko ait été
éliminé ou contraint de fuir. Des recherches sont en cours le long des berges du fleuve et des lacs
artificiels.</p>

<!--ANNOT-->

<h2>IV. ÉTAT DES RECHERCHES AU 2 MAI 1932</h2>
<div class="cadre"><p>Sondage systématique des lacs artificiels et des rives de l'Oural sur trois
kilomètres en aval de la ville — aucun corps retrouvé à ce jour. Une demande de renseignements a été
transmise à la Guépéou de Moscou concernant les contacts connus de l'intéressé. Réponse attendue.</p></div>

<h2>V. DIRECTIVES EN COURS</h2>
<p>Poursuivre les sondages. Vérifier si des fonds ou documents auraient pu être transmis à l'étranger
via les ingénieurs américains récemment partis pour Moscou. Ne pas ébruiter l'affaire au-delà des
services concernés.</p>

<div class="sign">
  I. PAVLENKO — chef de section<br>
  Section de police de Magnitogorsk · 2 mai 1932
</div>
<div class="pied">RAPPORT N° 1932-07/DIS — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0589 · 29.IV.32</div>
"""

VICTIMES = [
    ("Lebedev, K.", "Ingénieur en chef fonderie", "Décédé — J+3", "Réfectoire B"),
    ("Ignatieva, N.", "Comptable principale", "Décédée — J+4", "Réfectoire B"),
    ("Blokhin, F.", "Contremaître fonderie", "Décédé — J+5", "Réfectoire C"),
    ("Gratchev, S.", "Ingénieur adjoint tuyauterie", "Coma — pronostic engagé", "Réfectoire B"),
    ("Maltseva, I.", "Technicienne contrôle qualité", "Coma — pronostic engagé", "Réfectoire C"),
    ("Rjevski, R.", "Ouvrier moulage", "Inconscient — stable", "Réfectoire D"),
    ("Koulikova, A.", "Ouvrière entretien machines", "Inconsciente — stable", "Réfectoire C"),
]

EMP = """
<div class="entete">
  <div class="g">
    <div class="num">RAPPORT D'ENQUÊTE N° 1932-08/EMP</div>
    <div class="objet">Affection d'origine indéterminée — personnel du complexe industriel</div>
  </div>
  <div class="d">
    Agent instructeur : A. Petroff<br>Agent de police, 3<sup>e</sup> classe<br>
    Ouvert le : 18 avril 1932<br>État des constatations au : 2 mai 1932
  </div>
</div>

<div class="synthese">
Synthèse établie pour transmission — état du dossier au 2 mai 1932.<br>
Le dossier demeure ouvert. Les pièces originales restent au registre de la section.
</div>
<!--PHOTO-->
<h2>I. OBJET</h2>
<p>Depuis la fin du mois de mars 1932, plusieurs membres du personnel du complexe industriel ont été
victimes d'une affection grave d'origine indéterminée. Les symptômes, signalés par le médecin-chef
I. Nesteroff, consistent en des douleurs intestinales évoluant vers une incapacité totale à se
nourrir, suivie d'une perte de connaissance. Trois décès ont été enregistrés à ce jour. La nature de
l'affection — contamination alimentaire, empoisonnement volontaire ou simple maladie — n'a pas
encore été établie avec certitude.</p>

<h2>II. PERSONNES ATTEINTES</h2>
<table>
<colgroup><col style="width:21%"><col style="width:33%"><col style="width:27%"><col style="width:19%"></colgroup>
<tr><th>NOM</th><th>FONCTION</th><th>ÉTAT</th><th>RÉFECTOIRE HABITUEL</th></tr>
LIGNES
</table>
<p>Des cas similaires ont été signalés parmi les ouvriers ordinaires. Leur faible gravité relative
n'a pas permis d'établir avec certitude qu'il s'agit de la même affection ; ils n'ont pas été
consignés au présent dossier.</p>

<h2>III. PISTE PRIVILÉGIÉE</h2>
<p>Au vu de la diversité des profils touchés et des réfectoires fréquentés, l'hypothèse d'une
contamination dans un lieu commun unique paraît peu probable. Le médecin-chef Nesteroff évoque une
contamination de l'eau ou un changement brutal de régime alimentaire mal supporté par des personnes
habituées aux conditions urbaines.</p>

<!--ANNOT-->

<h2>IV. CONCLUSION PROVISOIRE</h2>
<div class="cadre"><p>L'affection semble liée à une contamination d'origine naturelle, probablement
l'eau ou la nourriture, aggravée par les conditions sanitaires dégradées du site. Aucun élément ne
permet à ce stade d'établir un acte volontaire. Le dossier reste ouvert dans l'attente des résultats
des analyses médicales.</p></div>

<h2>V. DIRECTIVES EN COURS</h2>
<p>Attendre les conclusions du médecin-chef. Surveiller l'apparition de nouveaux cas. Entendre les
responsables des réfectoires B et C en cas de confirmation d'une contamination alimentaire.</p>

<div class="sign">
  A. PETROFF — agent de police, 3<sup>e</sup> classe<br>
  Section de police de Magnitogorsk · 2 mai 1932
</div>
<div class="pied">RAPPORT N° 1932-08/EMP — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0523 · 18.IV.32</div>
""".replace("LIGNES", "\n".join(
    f"<tr><td>{n}</td><td>{f}</td><td>{e}</td><td>{r}</td></tr>" for n, f, e, r in VICTIMES))

SAB4 = """
<div class="entete">
  <div class="g">
    <div class="num">RAPPORT D'ENQUÊTE N° 1932-04/SAB</div>
    <div class="objet">Explosion d'une conduite de refroidissement — fonderie n°1</div>
  </div>
  <div class="d">
    Agent instructeur : V. Morozoff<br>Agent de police, 3<sup>e</sup> classe<br>
    Ouvert le : 17 avril 1932<br>Classé le : 22 avril 1932
  </div>
</div>

<h2>I. RÉCIT DES FAITS</h2>
<p>Le 16 avril 1932 en début de matinée, une impressionnante pièce de machinerie de la fonderie n°1 a
explosé, mettant à mal l'ensemble de la chaîne de refroidissement de l'installation. Cet incident
entraîne un blocage d'une partie de la production du complexe dans l'attente de la livraison de
pièces de remplacement dont le délai reste indéterminé. <b>Aucune victime n'est à déplorer.</b></p>

<p>Des soupçons de sabotage ayant initialement été soulevés, une enquête a été ouverte et les
ingénieurs responsables de l'installation, Dmitri Sorokin et Ivan Malysheff, ont été placés en
détention provisoire au bloc 27. Suite à leur interrogatoire, il a été déterminé que l'incident est
un simple accident. Du limon provenant du fleuve se serait accumulé dans les conduites de
refroidissement, entraînant une montée progressive de la pression jusqu'à provoquer l'explosion. Les
ingénieurs demeurent aux arrêts dans l'attente de leur jugement pour négligence.</p>

<!--ANNOT-->

<h2>PERSONNES INCULPÉES</h2>
<div class="fiche">
<span class="k">Nom :</span><b>SOROKIN, Dmitri Vladimirovitch</b> — ingénieur responsable
maintenance, fonderie n°1<br>
<span class="k">Nom :</span><b>MALYSHEFF, Ivan Nikolaïevitch</b> — ingénieur adjoint maintenance<br>
<span class="k">Chef d'inculpation :</span>Négligence grave ayant entraîné l'arrêt d'une
installation de production stratégique<br>
<span class="k">Lieu de détention :</span>Prison, bloc 27 — Magnitogorsk
</div>

<h2>II. CONCLUSION</h2>
<div class="cadre"><p>L'explosion est due à un simple accident technique causé par l'accumulation de
sédiments dans les conduites de refroidissement, consécutive à un défaut d'entretien du système de
filtrage. Aucune preuve d'un acte de sabotage intentionnel n'a été relevée. Les ingénieurs Sorokin
et Malysheff sont inculpés pour négligence et seront jugés conformément à l'article 111 du code
pénal. L'affaire est classée.</p></div>

<div class="sign">
  V. MOROZOFF — agent de police, 3<sup>e</sup> classe<br>
  Section de police de Magnitogorsk<br>L'an mil neuf cent trente-deux, le vingt-deux avril.<br>
  <i>Approuvé</i> — I. PAVLENKO, chef de section · 22 avril 1932
</div>
<div class="pied">RAPPORT N° 1932-04/SAB — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0501 · 17.IV.32</div>
"""

DEC = """
<div class="entete">
  <div class="g">
    <div class="num">RAPPORT DE DÉCÈS N° 1932-05/DEC</div>
    <div class="objet">Décès accidentel par noyade — complexe industriel</div>
  </div>
  <div class="d">
    Agent instructeur : L. Vinogradoff<br>Agent de police, 2<sup>e</sup> classe<br>
    Ouvert le : 30 avril 1932<br>Classé le : 1<sup>er</sup> mai 1932
  </div>
</div>

<!--PHOTO-->
<h2>FICHE D'IDENTITÉ — PERSONNE DÉCÉDÉE</h2>
<div class="fiche">
<span class="k">Nom :</span><b>KURBANOFF, Venyamin Alexeïevitch</b><br>
<span class="k">Date de naissance :</span>3 octobre 1888 — Moscou<br>
<span class="k">Fonction :</span>Cadre supérieur du Parti, service direct du Directeur<br>
<span class="k">Domicile :</span>Berezki — maison individuelle n°4<br>
<span class="k">Date du décès :</span>29 avril 1932 — en soirée<br>
<span class="k">Lieu de découverte :</span>Berge du lac artificiel n°2, station de pompage ouest<br>
<span class="k">Cause du décès :</span><b>Noyade</b> — établie par le rapport médico-légal du
Dr Nesteroff
</div>

<h2>I. CIRCONSTANCES — II. RAPPORT MÉDICO-LÉGAL</h2>
<p>Le corps du camarade Kurbanoff a été découvert en soirée du 29 avril 1932 par des ouvriers de la
station de pompage ouest qui regagnaient leurs baraquements. Le corps gisait sur la berge du lac
artificiel n°2, en contrebas de la rive.</p>
<p>L'examen du corps réalisé par le médecin-chef I. Nesteroff établit que la cause du décès est la
noyade. Des lésions importantes sont constatées à la jambe droite ainsi que des écorchures aux mains
et au visage. Les vêtements sont lacérés. Ces blessures sont compatibles avec une chute le long
d'une berge escarpée et un contact avec le fond rocailleux du lac.</p>

<h2>III. TÉMOIGNAGES</h2>
<div class="temoin"><span class="q">Équipe de la station de pompage</span> — interrogée le 30 avril.
Les ouvriers déclarent n'avoir rien remarqué d'anormal, ni sur la rive ni dans l'eau. Ils indiquent
l'endroit précis de la découverte. L'eau n'y est pas profonde — un homme adulte y a pied.</div>
<div class="temoin"><span class="q">Suspects potentiels</span> — interrogés le 30 avril. Aucun
élément probant.</div>

<!--ANNOT-->

<h2>IV. CONCLUSION</h2>
<div class="cadre"><p>Le décès est dû à un accident. La chute le long de la berge escarpée,
probablement due à un effondrement de la rive ou à une perte d'équilibre lors d'une tournée
d'inspection, a entraîné des blessures et un choc causant la noyade. Aucune preuve d'assassinat n'a
été relevée. L'affaire est classée sans suite.</p></div>

<div class="sign">
  L. VINOGRADOFF — agent de police, 2<sup>e</sup> classe<br>
  Section de police de Magnitogorsk<br>L'an mil neuf cent trente-deux, le premier mai.<br>
  <i>Approuvé</i> — I. PAVLENKO · 1<sup>er</sup> mai 1932
</div>
<div class="pied">RAPPORT N° 1932-05/DEC — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0601 · 30.IV.32</div>
"""

SAB9 = """
<div class="entete">
  <div class="g">
    <div class="num">RAPPORT D'ENQUÊTE N° 1932-09/SAB</div>
    <div class="objet">Série d'incidents sur les voies de transport du minerai</div>
  </div>
  <div class="d">
    Agent instructeur : I. Pavlenko<br>Chef de section<br>
    Ouvert le : 29 avril 1932<br>Enquête en cours
  </div>
</div>

<div class="synthese">
Synthèse établie pour transmission — état du dossier au 2 mai 1932.<br>
Le dossier demeure ouvert. Les pièces originales restent au registre de la section.
</div>
<h2>I. ORIGINE DU SIGNALEMENT</h2>
<p>Le présent dossier fait suite à deux dépositions successives de l'ingénieur F. Nikitine,
responsable de l'acheminement des ressources minières, concernant une série d'incidents survenus
sur les voies de transport entre le mont Magnitnaïa et le complexe industriel. La première, déposée
auprès du palais administratif le 10 avril 1932, signalait deux incidents ; la seconde, déposée le
28 avril, en signalait deux autres. Les deux pièces ne sont parvenues aux services de police que le
29 avril 1932 en raison d'un délai de transmission administratif. L'enquête a été ouverte à cette
date.</p>

<!--ANNOT-->

<h2>II. RÉCAPITULATIF DES INCIDENTS SIGNALÉS</h2>
<table>
<colgroup><col style="width:6%"><col style="width:16%"><col style="width:44%"><col style="width:34%"></colgroup>
<tr><th>N°</th><th>DATE</th><th>DESCRIPTION</th><th>CONSÉQUENCES</th></tr>
<tr><td>1</td><td>2 avril</td><td>Déraillement — défaillance d'un moyeu de wagonnet</td><td>Convoi arrêté deux heures</td></tr>
<tr><td>2</td><td>8 avril</td><td>Déraillement — rupture d'un harnachement de bête de somme</td><td>Wagonnet renversé, chargement perdu</td></tr>
<tr><td>3</td><td>19 avril</td><td>Rupture d'axe d'un wagonnet au départ du hangar</td><td>Convoi immobilisé plusieurs heures</td></tr>
<tr><td>4</td><td>27 avril</td><td>Rail déformé sur la voie principale</td><td><b>Blocage d'une journée complète</b></td></tr>
</table>

<h2>III. ÉTAT DE L'ENQUÊTE</h2>
<p>L'ingénieur Nikitine a indiqué conserver les pièces défectueuses issues des quatre incidents. Ces
pièces n'ont pas encore été examinées par les services de police à la date de rédaction du présent
rapport. L'enquête se concentre à ce stade sur l'identification d'un éventuel saboteur extérieur au
complexe, dont la présence sur le site resterait à établir. <b>Aucun suspect n'a été identifié ni
interrogé à ce jour.</b></p>

<h2>IV. DIRECTIVES EN COURS</h2>
<div class="cadre"><p>Procéder à l'examen des pièces conservées par Nikitine. Interroger les membres
de l'équipe de transport susceptibles d'avoir observé des éléments inhabituels. Déterminer si les
incidents sont le fait d'une négligence répétée ou d'actes volontaires.</p></div>

<div class="sign">
  I. PAVLENKO — chef de section<br>
  Section de police de Magnitogorsk · 2 mai 1932
</div>
<div class="pied">RAPPORT N° 1932-09/SAB — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0590 · 29.IV.32</div>
"""

PLAINTES = [
    ("1", "3 janvier", "n°4 — outillage", "V. Petrov",
     "14 courroies de transmission, 6 boîtes de joints d'étanchéité", "train du 31 décembre"),
    ("2", "18 janvier", "n°7 — consommables électriques", "M. Gordeeva",
     "3 bobines de câble 4 mm², 22 m de gaine isolante", "train du 15 janvier"),
    ("3", "9 février", "n°4 — outillage", "V. Petrov",
     "8 courroies, un lot de 40 joints de robinetterie", "train du 6 février"),
    ("4", "27 février", "n°11 — lubrifiants", "D. Savchenko",
     "18 bidons d'huile 5 L, 4 seaux de graisse", "train du 24 février"),
    ("5", "12 mars", "n°7 — consommables électriques", "M. Gordeeva",
     "2 bobines de câble, un lot d'ampoules industrielles", "train du 10 mars"),
]

ENT = """
<div class="entete">
  <div class="g">
    <div class="num">DOSSIER D'ENQUÊTE N° 1932-03/ENT</div>
    <div class="objet">Disparitions de matériel — entrepôts du complexe industriel</div>
  </div>
  <div class="d">
    Agent instructeur : O. Belousoff<br>Superviseure : Y. Nikitina<br>
    Ouvert le : 14 mars 1932<br>Classé le : 28 mars 1932
  </div>
</div>

<h2>RÉFÉRENCES ADMINISTRATIVES</h2>
<div class="fiche">
<span class="k">Unité concernée :</span>Zone de déchargement ouest — entrepôts n°4, n°7 et n°11<br>
<span class="k">Nature des faits :</span>Disparitions répétées de matériel industriel lors des
déchargements<br>
<span class="k">Période couverte :</span>31 décembre 1931 au 10 mars 1932<br>
<span class="k">Nombre de plaintes :</span>5 plaintes reçues de 3 responsables d'entrepôts distincts<br>
<span class="k">Personnes interrogées :</span>5 personnes auditionnées<br>
<span class="k">Transmission :</span>Dossier soumis à Y. Nikitina le 20 mars — aval reçu le 21 mars
</div>

<h2>I. OBJET DE L'ENQUÊTE</h2>
<p>Suite à la réception de plusieurs plaintes émanant de responsables d'entrepôts du complexe
industriel signalant des écarts répétés entre les stocks attendus et les inventaires réalisés après
déchargement des convois ferroviaires, l'agent soussigné a décidé, avec l'aval de la superviseure
Y. Nikitina, de procéder à un regroupement et à une analyse des faits constatés afin de déterminer
s'il existe un lien entre ces incidents. Le présent dossier constitue le rapport complet de cette
investigation préliminaire, conformément aux procédures en vigueur au sein de la section.</p>

<h2>II. RÉCAPITULATIF DES PLAINTES REÇUES</h2>
<table>
<colgroup><col style="width:4%"><col style="width:13%"><col style="width:22%"><col style="width:15%"><col style="width:30%"><col style="width:16%"></colgroup>
<tr><th>N°</th><th>DATE</th><th>ENTREPÔT</th><th>RESPONSABLE</th><th>ÉCART CONSTATÉ</th><th>CONVOI</th></tr>
<!--LIGNES-->
</table>
<p>Les plaintes n°1 et n°2 ont initialement été déposées auprès de l'administration du complexe —
classées sans suite.</p>

<h2>III. OBSERVATIONS PRÉLIMINAIRES</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<tr><th>CONSTAT</th><th>DÉTAIL</th></tr>
<tr><td>Temporalité</td><td>Dans chaque cas, l'écart est constaté dans les 48 h suivant l'arrivée du convoi. Aucun écart signalé sur des stocks en place depuis plus de trois jours.</td></tr>
<tr><td>Nature des manques</td><td>Exclusivement des consommables à forte valeur d'usage : courroies, joints, câbles, lubrifiants. Aucun équipement lourd ni pièce maîtresse concerné.</td></tr>
<tr><td>Entrepôts touchés</td><td>Trois entrepôts sur seize : n°4, n°7 et n°11. Tous situés dans la zone de déchargement ouest, desservie par le même quai ferroviaire.</td></tr>
<tr><td>Manifestes</td><td>Les articles manquants figuraient bien dans les manifestes d'expédition. Le problème est donc postérieur au départ et antérieur à l'inventaire.</td></tr>
<tr><td>Rotation du personnel</td><td>Rotation anormalement élevée des ouvriers affectés au déchargement de la zone ouest — signalée par M. Gordeeva lors de son audition.</td></tr>
</table>

<h2>IV. PERSONNES INTERROGÉES</h2>
<div class="temoin"><span class="q">V. Petrov</span>, responsable entrepôt n°4 — confirme les deux
plaintes. Précise que les écarts surviennent toujours sur les premiers wagons déchargés. Ne
soupçonne personne nommément.</div>
<div class="temoin"><span class="q">M. Gordeeva</span>, responsable entrepôt n°7 — confirme. Signale
que deux ouvriers affectés au déchargement de la zone ouest ont été remplacés trois fois en six mois
— rotation anormalement élevée pour ce poste.</div>
<div class="temoin"><span class="q">D. Savchenko</span>, responsable entrepôt n°11 — confirme. Ne
peut exclure une erreur de comptage mais juge cela improbable vu les quantités.</div>
<div class="temoin"><span class="q">K. Zykov</span>, chef d'équipe déchargement zone ouest — nie
toute irrégularité. Attitude défensive. Incapable de justifier la rotation élevée dans son
équipe.</div>
<div class="temoin"><span class="q">A. Nikiforov</span>, ouvrier déchargement zone ouest — dit ne
rien avoir remarqué. Regard fuyant lors des questions sur les premiers wagons déchargés.</div>
<div class="temoin"><span class="q">S. Orloff</span>, tenancier — gare de Magnitogorsk —</div>

<!--ANNOT-->

<h2>V. DÉCISION DE CLÔTURE — SIGNÉ I. PAVLENKO, CHEF DE SECTION</h2>
<div class="cadre"><p>Les éléments réunis ne constituent pas des preuves suffisantes de l'existence
d'un lien entre les faits constatés. Les écarts relevés relèvent vraisemblablement d'erreurs de
comptage lors des inventaires ou de problèmes d'organisation imputables aux équipes concernées, ce
qui ne relève pas du champ d'action de la police. L'enquête est close à compter de ce jour. L'agent
Belousoff est réaffecté à la surveillance des mines à compter du 1<sup>er</sup> avril 1932 dans le
cadre du rééquilibrage annuel des effectifs.</p></div>

<div class="sign">
  O. Belousoff — agent instructeur &nbsp;·&nbsp; Y. Nikitina — superviseure<br>
  <i>Approuvé</i> — I. PAVLENKO, chef de section<br>L'an mil neuf cent trente-deux, le vingt-huit mars.
</div>
<div class="pied">DOSSIER N° 1932-03/ENT — ARCHIVES DE LA SECTION DE POLICE — REPRODUCTION INTERDITE</div>
<div class="plume registre">вх. 0287 · 14.III.32</div>
""".replace("<!--LIGNES-->", "\n".join(
    f"<tr><td>{n}</td><td>{d}</td><td>{e}</td><td>{r}</td><td>{c}</td><td>{t}</td></tr>"
    for n, d, e, r, c, t in PLAINTES))



# ══════════════════════════════════════════════════════════════════
#  La pièce manuscrite — les deux dépositions de Faddei Nikitine
# ══════════════════════════════════════════════════════════════════
#
#  Elles s'agrafent au dossier 1932-09/SAB et ce sont les seules
#  pièces de la pile qui ne sortent pas d'une machine à écrire : un
#  ingénieur qui écrit au palais administratif n'a pas de
#  dactylographe.
#
#  **Deux feuillets, pas un.** La lettre du 10 avril porte deux
#  incidents — les deux autres n'avaient pas eu lieu. Elle part le
#  jour même au palais, et elle y reste : Faddei ne l'a plus en main
#  et ne peut rien y ajouter. Le 28 avril il revient en déposer une
#  seconde, qui porte les deux derniers incidents. Le palais transmet
#  le tout à la police **le lendemain** — deux numéros d'arrivée qui
#  se suivent, вх. 0912 et 0913.
#
#  Les dix-neuf jours cessent alors d'être une lenteur abstraite :
#  ce n'est pas l'administration qui a fini par aboutir, c'est un
#  homme qui est revenu.
#
#  Les cachets se posent dans le blanc, sous la signature. Un commis
#  qui tamponne cherche la place libre — et un tampon en travers des
#  lignes se lit comme une maladresse de fabrication, pas comme une
#  trace de greffe.


def cachet(i, couleur, seed, titre, lieu, arrivee, haut, gauche, angle, corps=22):
    """Un cachet d'arrivée : cadre, service, date et numéro d'entrée."""
    return f"""
<svg class="recu" viewBox="0 0 320 124" xmlns="http://www.w3.org/2000/svg"
     style="top:{haut}mm; left:{gauche}mm; transform:rotate({angle}deg)">
 <defs><filter id="r{i}" x="-15%" y="-25%" width="130%" height="150%">
   <feTurbulence type="fractalNoise" baseFrequency="{1.0 + i * .08}" numOctaves="3"
                 seed="{seed}" result="b"/>
   <feDisplacementMap in="SourceGraphic" in2="b" scale="{2.2 + i * .15}"
                      xChannelSelector="R" yChannelSelector="G" result="d"/>
   <feTurbulence type="fractalNoise" baseFrequency="0.085" numOctaves="2"
                 seed="{seed + 23}" result="t"/>
   <feColorMatrix in="t" type="matrix"
     values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.7 0 0 0 -0.3" result="m"/>
   <feComposite in="d" in2="m" operator="out"/>
 </filter></defs>
 <g filter="url(#r{i})" fill="{couleur}">
  <rect x="5" y="5" width="310" height="114" fill="none" stroke="{couleur}" stroke-width="4"/>
  <text x="160" y="40" font-size="{corps}" letter-spacing="3.4" text-anchor="middle"
        font-family="PT" font-weight="bold">{titre}</text>
  <text x="160" y="68" font-size="15" letter-spacing="1.6" text-anchor="middle"
        font-family="PT">{lieu}</text>
  <text x="160" y="100" font-size="20" letter-spacing="2.4" text-anchor="middle"
        font-family="PT" font-weight="bold">{arrivee}</text>
 </g>
</svg>"""


PALAIS = ("#2f3f6b", "ПОЛУЧЕНО", "УПРАВЛЕНИЕ КОМБИНАТА")
POLICE = ("#8c2b22", "МИЛИЦИЯ · ПОЛУЧЕНО", "МАГНИТОГОРСК")


def feuillet(date, corps, cachets, graine):
    """Un feuillet au formulaire russe.

    Pas de « lieu, le date » en tête : cette formule est occidentale.
    Le coin supérieur droit porte la **шапка** — à qui, puis de qui et
    en quelle qualité —, le nom du document vient centré en capitales,
    et la date se pose en pied à gauche, la signature à droite.
    """
    paras = "\n".join(
        f'<p>{ecrire(t, graine=graine + i, encre=True, amplitude=.85)}</p>'
        for i, t in enumerate(corps))
    return f"""
<div class="feuillet">
{cachets}
<div class="shapka">
  <div>{ecrire("À l'administration du combinat", graine=graine + 80,
                encre=True, amplitude=.8)}</div>
  <div>{ecrire("de l'ingénieur F. Nikitine,", graine=graine + 81,
                encre=True, amplitude=.8)}</div>
  <div>{ecrire("responsable du transport du minerai", graine=graine + 82,
                encre=True, amplitude=.8)}</div>
</div>

<div class="titre">{ecrire("RAPPORT", graine=graine + 83, encre=True, amplitude=.75)}</div>

{paras}

<div class="pied">
  <span class="d">{ecrire(date, graine=graine + 90, encre=True, amplitude=.8)}</span>
  <span class="n">{ecrire("F. Nikitine", graine=graine + 91, encre=True, amplitude=.7)}</span>
</div>
</div>"""


PREMIER = [
    """Je porte à votre connaissance les faits suivants, survenus sur la voie de transport du
minerai du mont Magnitnaïa.""",
    """Le 2 avril, au kilomètre 2 de la voie, le moyeu d'une roue de wagonnet s'est désolidarisé
en charge. Le convoi a été arrêté deux heures. J'ai conservé le moyeu et son axe.""",
    """Le 8 avril, à la sortie du hangar, le harnachement d'une bête de somme a cédé. Le wagonnet
s'est renversé et le chargement est perdu. J'ai conservé la lanière.""",
    """Je ne me prononce pas sur les causes, ce n'est pas mon métier. Je dis seulement qu'en quatre
ans sur cette voie je n'ai pas vu deux avaries de cette nature en six jours, et que les deux
pièces sont à la disposition de qui voudra les examiner.""",
    "Je demande qu'un agent se déplace. Je ne demande rien d'autre.",
]

SECOND = [
    """Je complète mon rapport du 10 avril. Personne n'est venu.""",
    """Le 19 avril, au départ du hangar, l'axe d'un wagonnet s'est rompu en charge. Le convoi est
resté immobilisé plusieurs heures.""",
    """Le 27 avril, au virage du kilomètre 3,5, un rail s'est trouvé déformé. La voie a été bloquée
une journée entière. Les deux pièces sont conservées avec les premières.""",
    """Cela fait quatre avaries en vingt-cinq jours. Je redemande qu'un agent se déplace.""",
]


def manuscrit():
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A4; margin: 16mm 20mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Plume, cursive; font-size: 14.6pt; line-height: 1.68;
        color: #1d2430; }}

/* Deux feuilles séparées : la seconde est déposée dix-huit jours plus
   tard, elle n'a jamais été sur la même page que la première. */
.feuillet {{ position: relative; }}
.feuillet + .feuillet {{ break-before: page; }}

/* La « шапка » : un bloc décalé vers la droite, mais ferré à gauche —
   on ne centre pas et on n'aligne pas à droite, on décale. */
.shapka {{ margin-left: 86mm; line-height: 1.42; margin-bottom: 9mm; }}
.titre {{ text-align: center; font-size: 18pt; letter-spacing: .14em;
          margin-bottom: 7mm; }}
p {{ margin: 0 0 3.2mm; text-align: justify; }}
/* La date à gauche, la signature à droite, sur la même ligne. */
.pied {{ display: flex; justify-content: space-between; align-items: baseline;
         margin-top: 9mm; }}
.pied .n {{ font-size: 17pt; }}

/* Les cachets d'arrivée, posés dans le blanc sous la signature. */
svg.recu {{ position: absolute; width: 44mm; height: 17mm;
            opacity: .62; mix-blend-mode: multiply; }}
</style></head><body>
{FILTRES}

{feuillet("Le 10 avril 1932.", PREMIER,
          cachet(1, PALAIS[0], 17, PALAIS[1], PALAIS[2], "10.IV.32 · вх. 318",
                 haut=182, gauche=4, angle=-3.4)
          + cachet(2, POLICE[0], 31, POLICE[1], POLICE[2], "29.IV.32 · вх. 0912",
                   haut=198, gauche=56, angle=2.6, corps=20),
          graine=440)}

{feuillet("Le 28 avril 1932.", SECOND,
          cachet(3, PALAIS[0], 44, PALAIS[1], PALAIS[2], "28.IV.32 · вх. 471",
                 haut=136, gauche=8, angle=2.2)
          + cachet(4, POLICE[0], 58, POLICE[1], POLICE[2], "29.IV.32 · вх. 0913",
                   haut=151, gauche=61, angle=-1.8, corps=20),
          graine=640)}

</body></html>"""


# ══════════════════════════════════════════════════════════════════

DOSSIERS = {
    "mrt": (MRT, "28 avril 1932", "Suffisant. Classer."),
    "dis": (DIS, None, "Les étrangers. Toujours les étrangers."),
    "emp": (EMP, None, "Rien de tout cela ne relève de nos services.<br>"
                       "Constitutions faibles, rien de plus. — I. P."),
    "sab4": (SAB4, "22 avril 1932", "Négligence. Jugement sous quinzaine."),
    "dec": (DEC, "1er mai 1932",
            "Accident. J'ai prévenu le camarade<br>Directeur moi-même."),
    "sab9": (SAB9, None, "Priorité au dossier Tkachenko.<br>Reprendre ensuite."),
    "ent": (ENT, "28 mars 1932", "Belousoff — voir avec Nikitina<br>pour réaffectation."),
}

# Deux inventaires successifs du même fonds : l'un tamponné, l'autre au crayon.
COTES = {"mrt": (112, 87), "dis": (134, 103), "emp": (141, 108), "sab4": (96, 74),
         "dec": (147, 113), "sab9": (151, 116), "ent": (63, 49)}

CLOS = {"mrt", "sab4", "dec", "ent"}  # on les parcourt : la césure y est sans coût

# Igor annote où il trouve de la place, et il va vite : jamais à la même
# hauteur, jamais du même angle, jamais tout à fait de la même taille.
# **Les valeurs sont fixes par dossier** — déterministes, pas tirées au
# sort : deux générations donnent le même document.
MAIN = {
    # code : (x mm, y mm depuis le haut de la zone imprimée, angle, corps en pt)
    "mrt": (100, 30, -3.0, 12.4),
    "dis": (90, 152, 1.3, 13.8),
    "emp": (102, 35, 0.5, 12.4),
    "sab4": (82, 50, 2.4, 13.2),
    "dec": (40, 111, -2.1, 13.0),
    "sab9": (100, 30, -3.6, 11.8),
    "ent": (0, 340, 1.8, 13.6),
}


def main_de(code):
    if code not in MAIN:
        return ""
    x, y, a, t = MAIN[code]
    return (f"left:{x}mm; top:{y}mm; transform:rotate({a}deg); font-size:{t}pt")


def cotes(code):
    t, c = COTES[code]
    return f'<div class="cotes"><span class="tampon">{t}</span>'\
           f'<span class="crayon">{c}</span></div>'


for code, (corps, date, annot) in DOSSIERS.items():
    if ARGS and code not in ARGS:
        continue
    cible = RACINE / "out" / f"rapport-{code}.pdf"
    rendu.pdf(doc(capitales(corps), classe(date) if date else "", annot,
                  cotes=cotes(code), coupures=code in CLOS, portrait=vignette(code),
                  main=main_de(code)),
              cible, RACINE)
    print(f"· {cible.relative_to(RACINE)}")

if not ARGS or "dep" in ARGS:
    cible = RACINE / "out" / "rapport-dep-faddei.pdf"
    rendu.pdf(manuscrit(), cible, RACINE)
    print(f"· {cible.relative_to(RACINE)}")
