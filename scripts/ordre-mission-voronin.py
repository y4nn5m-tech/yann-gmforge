#!/usr/bin/env python3
"""
ordre-mission-voronin.py — l'ordre de détachement n° 112 / DMM.

    python3 scripts/ordre-mission-voronin.py              # Voronin, capitaine
    python3 scripts/ordre-mission-voronin.py --feminin    # Voronina, sans grade

Produit out/ordre-mission-voronin[-feminin].pdf : une page A4, remise
**en mains propres par le commandant Tikhonoff**, qui sert aussi de
laissez-passer.

Deux versions, parce que le genre du militaire change le document en
profondeur et non à la marge :

    masculin   capitaine, garnison de Reoutov. **Il commande le groupe**,
               et le document le dit noir sur blanc.
    féminin    ni grade, ni garnison, ni supérieur militaire. Le
               paragraphe d'autorité disparaît — **personne ne commande**,
               et c'est l'absence de cette phrase qui le produit.

Tikhonoff remet le document dans les deux cas : il a fait la guerre
civile avec elle comme avec lui.

Les trois accompagnateurs peuvent être féminins indépendamment :
--petrenko-f, --krasnova, --guseva.

Rendu par Chrome et non par WeasyPrint (voir scripts/rendu.py) : le
tampon a besoin de textPath pour que son texte suive l'arc, et de
feTurbulence pour que son encre soit inégale. WeasyPrint ignore les
deux en silence.

Ce qui fait qu'un document d'époque a l'air vrai, et qui est ici :

    trois mains     l'imprimeur (PT Serif, le formulaire), la
                    dactylographe (Special Elite, le texte), le
                    fonctionnaire (Caveat, ce qui est ajouté au stylo)
    le tampon mord  apposé de travers par-dessus la signature, encre
                    pâle et irrégulière
    le registre     un numéro d'arrivée porté à la main en haut, comme
                    sur tout document qui a traversé un service
"""
import os
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

A = sys.argv[1:]
F_VOR = "--feminin" in A or "--voronina" in A
F_PET = "--petrenko-f" in A
F_KRA = "--krasnova" in A
F_GUS = "--guseva" in A

vor_nom = "VORONINA, Maria Andreïevna" if F_VOR else "VORONIN, Mikhaïl Andreïevitch"
vor_qual = ("Instructrice de culture physique — Institut central, Moscou"
            if F_VOR else "Capitaine, garnison de Reoutov")
camarade = "À la camarade" if F_VOR else "Au camarade"
appel = "Camarade instructrice," if F_VOR else "Camarade capitaine,"
detache = "détachée" if F_VOR else "détaché"
affecte = "affectée" if F_VOR else "affecté"

pet = "PETRENKO, Bogdana" if F_PET else "PETRENKO, Borislav"
kra = "KRASNOVA, Svetlana" if F_KRA else "KRASNOFF, Sergeï"
gus = "GUSEVA, Alina" if F_GUS else "GUSEV, Alekseï"

AUTORITE = ("""<p>Vous veillerez à la bonne tenue du groupe, à la sécurité des personnes et à la
transmission du rapport final à Moscou.</p>""" if F_VOR else """<p>En qualité d'officier de l'Armée
Rouge, vous exercez sur cette équipe <b>l'autorité hiérarchique</b>. Vous portez la responsabilité
de la discipline du groupe, de la sécurité des personnes, et de la transmission du rapport final à
Moscou.</p>""")

# ── le cachet : textPath pour l'arc, feTurbulence pour l'encre ──────
TAMPON = """
<svg class="tampon" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <path id="haut" d="M 18,100 A 82,82 0 0 1 182,100"/>
  <path id="bas"  d="M 24,100 A 76,76 0 0 0 176,100"/>
  <filter id="encre" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="7" result="b"/>
    <feDisplacementMap in="SourceGraphic" in2="b" scale="2.1"
                       xChannelSelector="R" yChannelSelector="G" result="d"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.055" numOctaves="2" seed="19" result="t"/>
    <feColorMatrix in="t" type="matrix"
      values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.6 0 0 0 -0.28" result="m"/>
    <feComposite in="d" in2="m" operator="out"/>
  </filter>
 </defs>
 <g filter="url(#encre)" fill="#2b4a8c">
  <g fill="none" stroke="#2b4a8c">
    <circle cx="100" cy="100" r="92" stroke-width="4.6"/>
    <circle cx="100" cy="100" r="80" stroke-width="1.7"/>
  </g>
  <text font-size="12.4" letter-spacing="1.7" font-family="PT">
    <textPath href="#haut" startOffset="50%" text-anchor="middle">
      ОБЪЕДИНЁННОЕ ГОСУДАРСТВЕННОЕ
    </textPath>
  </text>
  <text font-size="11.4" letter-spacing="2.4" font-family="PT">
    <textPath href="#bas" startOffset="50%" text-anchor="middle">
      ★ МОСКВА ★ 1932 ★
    </textPath>
  </text>
  <text x="100" y="97" font-size="30" letter-spacing="3" text-anchor="middle"
        font-family="PT" font-weight="bold">ОГПУ</text>
  <text x="100" y="117" font-size="10.5" letter-spacing="2.4" text-anchor="middle"
        font-family="PT">СЕКРЕТНО</text>
 </g>
</svg>"""

F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "L'ordre de détachement",
     "papier": "papier blanc", "grammage": "100 g", "ou": "maison",
     "format": "A4", "feuilles": 1,
     "note": "**pas de jauni** : délivré le 24 avril, il a neuf jours"},
]

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Machine; src: url({F}/SpecialElite-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4; margin: 13mm 17mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Machine, serif; font-size: 8.2pt; line-height: 1.42;
        color: #1a1713; position: relative; }}

/* la frappe d'une machine n'est jamais parfaitement régulière */
.frappe {{ filter: url(#frappe); }}

/* ── la main de l'imprimeur ──────────────────────────────────── */
.haut {{ display: flex; justify-content: space-between; align-items: flex-start; }}
.organe {{ width: 76%; font-family: PT, serif; font-size: 7.4pt; line-height: 1.6;
           letter-spacing: .08em; }}
.organe .sec {{ margin-top: 1.4mm; font-size: 6.9pt; letter-spacing: .12em; }}
.secret {{ font-family: PT, serif; border: 1.5px solid #1a1713; padding: 1mm 3mm;
           font-size: 8.2pt; letter-spacing: .3em; transform: rotate(1.4deg); }}
.filet {{ border-top: 2.4px solid #1a1713; border-bottom: .7px solid #1a1713;
          height: 1.3mm; margin: 3mm 0 4mm; }}
h1 {{ font-family: PT, serif; font-size: 12.6pt; font-weight: normal; letter-spacing: .18em;
      text-align: center; margin: 0 0 4.5mm; }}
h2 {{ font-family: PT, serif; font-size: 7.4pt; font-weight: bold; letter-spacing: .17em;
      border-bottom: .7px solid #1a1713; padding-bottom: .7mm; margin: 4mm 0 2.2mm; }}

/* ── la main de la dactylographe ─────────────────────────────── */
.ref {{ font-size: 8pt; line-height: 1.5; margin-bottom: 4mm; }}
.dest {{ margin-bottom: 4mm; line-height: 1.65; }}
.dest .remis {{ font-size: 8pt; }}
p {{ margin: 0 0 2.2mm; text-align: justify; }}
ol {{ margin: 0 0 2.2mm; padding-left: 6mm; }}
li {{ margin-bottom: 1.5mm; }}
.equipe {{ margin: 1.8mm 0 2.2mm 8mm; line-height: 1.6; }}
.equipe .n {{ display: inline-block; width: 50mm; }}
.echeance {{ margin-left: 8mm; line-height: 1.65; }}

/* ── la main du fonctionnaire ────────────────────────────────── */
.plume {{ font-family: Plume, cursive; color: #233a66; }}
.registre {{ position: absolute; right: 1mm; top: 23mm; font-size: 13pt;
             transform: rotate(-4deg); line-height: 1.15; text-align: right; }}
.registre small {{ font-size: 9pt; }}
.paraphe {{ font-size: 24pt; line-height: 1; margin-top: 1mm;
            transform: rotate(-5deg); display: inline-block; }}
.remisle {{ position: absolute; left: 1mm; bottom: 3mm; font-size: 11pt;
            transform: rotate(-1.8deg); }}

.bas {{ display: flex; justify-content: space-between; align-items: flex-start;
        margin-top: 4mm; gap: 8mm; }}
.bas .laissez {{ width: 52%; text-align: justify; }}
.sign {{ width: 44%; text-align: center; font-size: 8.3pt; line-height: 1.6; }}

svg.tampon {{ position: absolute; width: 40mm; height: 40mm;
              right: 6mm; bottom: 11mm; transform: rotate(-12deg);
              opacity: .58; mix-blend-mode: multiply; }}

.pied {{ margin-top: 5mm; border-top: .7px solid #1a1713; padding-top: 1.3mm;
         font-family: PT, serif; font-size: 6.6pt; letter-spacing: .08em; text-align: right; }}
</style></head><body>
{FILTRES}

<svg width="0" height="0" style="position:absolute">
 <filter id="frappe">
   <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" seed="3" result="n"/>
   <feDisplacementMap in="SourceGraphic" in2="n" scale="0.55"
                      xChannelSelector="R" yChannelSelector="G"/>
 </filter>
</svg>

<div class="frappe">

<div class="haut">
  <div class="organe">
    DIRECTION POLITIQUE D'ÉTAT UNIFIÉE (OGPU)<br>
    AUPRÈS DU CONSEIL DES COMMISSAIRES DU PEUPLE
    <div class="sec">SECTION SPÉCIALE — AFFAIRES INDUSTRIELLES</div>
  </div>
  <div class="secret">SECRET</div>
</div>
<div class="filet"></div>

<div class="ref">
  Moscou, le 24 avril 1932<br>
  Mission n° 112 / DMM<br>
  Exemplaire personnel
</div>

<h1>ORDRE DE DÉTACHEMENT</h1>

<div class="dest">
  {camarade} <b>{vor_nom}</b><br>
  {vor_qual}<br>
  <span class="remis">— remis en mains propres par le commandant TIKHONOFF —</span>
</div>

<p>{appel}</p>

<p>En vertu de la décision conjointe du Commissariat du Peuple à la Défense et de la Direction
Politique d'État Unifiée (OGPU), vous êtes par la présente {detache} de votre poste pour une durée
de <b>trois (3) semaines</b>, à compter du 26 avril 1932.</p>

<h2>OBJET DU DÉTACHEMENT</h2>

<p>Vous êtes {affecte} à une mission conjointe sur le complexe métallurgique de Magnitogorsk
(district de Tcheliabinsk), dans le cadre d'une enquête portant sur des faits présumés de
<b>sabotage et de haute trahison</b>.</p>

<p>Une équipe interdisciplinaire vous accompagnera. Sa composition est la suivante :</p>

<div class="equipe">
  <span class="n">— {pet}</span> bureaucrate (Leningrad)<br>
  <span class="n">— {kra}</span> universitaire, génie mécanique (Leningrad)<br>
  <span class="n">— {gus}</span> Bureau de la Logistique Industrielle (Moscou)
</div>

{AUTORITE}

<h2>VOS INSTRUCTIONS</h2>

<ol>
<li><b>Conduite de la mission.</b> Vous accompagnerez l'équipe jusqu'à Magnitogorsk et veillerez au
bon déroulement de l'enquête sur place.</li>
<li><b>Coordination locale.</b> Un guide vous attendra en gare de Magnitogorsk. Il vous mettra en
relation avec les organes compétents de la police politique locale, placés sous l'autorité du
camarade Igor PAVLENKO.</li>
<li><b>Rapport.</b> Un rapport final sera remis à votre retour, dans un délai de
<b>quarante-huit (48) heures</b>.</li>
<li><b>Discipline.</b> Toute initiative dépassant le cadre des présentes instructions devra faire
l'objet d'une demande préalable. Aucun engagement ni promesse ne pourra être fait au nom de l'État
sans autorisation expresse.</li>
</ol>

<h2>DURÉE ET ÉCHÉANCE</h2>

<div class="echeance">
  <b>Départ :</b> 26 avril 1932, gare de Iaroslavski, train n° 47, compartiment 4.<br>
  <b>Retour :</b> au plus tard le <b>17 mai 1932</b>.
</div>

<div class="bas">
  <div class="laissez">Vous présenterez le présent document à toute autorité militaire ou
  administrative qui en ferait la demande, en guise de laissez-passer.</div>
  <div class="sign">
    Pour la Direction Politique<br>d'État Unifiée,<br>
    <b>G. G. IAGODA</b><br>
    Chef adjoint de l'OGPU
    <div class="plume paraphe">{ecrire("Ягода", graine=201, encre=True, amplitude=1.4)}</div>
  </div>
</div>

<div class="pied">Mission n° 112 / DMM</div>

</div>

<div class="plume registre">{ecrire("вх. 1147", graine=202, amplitude=1.2)}<br><small>{ecrire("24.IV.32", graine=203, amplitude=1.2)}</small></div>
<div class="plume remisle">{ecrire("Remis le 24.IV.32 —", graine=204)} <i>{ecrire("Тихонов", graine=205, encre=True, amplitude=1.3)}</i></div>

{TAMPON}

</body></html>"""

cible = RACINE / "out" / f"ordre-mission-voronin{'-feminin' if F_VOR else ''}.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
