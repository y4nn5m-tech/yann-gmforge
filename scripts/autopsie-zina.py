#!/usr/bin/env python3
"""
autopsie-zina.py — la copie du rapport d'autopsie de Zina Krylova.

    python3 scripts/autopsie-zina.py
    python3 scripts/autopsie-zina.py --grille   # la règle, pour régler la main

Produit out/autopsie-zina.pdf : une page, format médical.

**C'est le document qui détruit l'enquête de Vinogradoff**, et il dort
dans un tiroir à deux cents mètres de lui. La page manque au dossier
1932-06/MRT, qui en porte le renvoi ; la copie est au dispensaire, et
Nesteroff la sort en râlant, au deuxième passage.

Ce qui le distingue des sept rapports de police, et c'est volontaire :

    l'en-tête     un dispensaire, pas la milice
    la forme      des constats numérotés, pas des sections romaines
    la main       un médecin qui dicte, pas un dactylographe de bureau
    rien d'autre  **pas de photo, pas de pièce à conviction** — la
                  cordelette et la mèche se décrivent, elles ne se
                  montrent pas : ce sont les preuves de l'autre, et les
                  manipuler leur donnerait du poids

**Le soupçon du complice est une réserve professionnelle, pas une
conclusion.** Un légiste de 1932 n'accuse pas : il note ce qui lui
paraît difficilement compatible, et il laisse l'enquêteur conclure.
C'est ce qui rend la pièce crédible — et c'est aussi pourquoi
Vinogradoff a pu ne pas la lire sans être un monstre.

Forme reprise de l'acte d'autopsie de 1934 relevé en archive :
`sources/magnitogorsk-iconographie/rapports-archives/autopsie-borisov-1934.pdf`
— titre espacé et souligné, formule de date en toutes lettres, pas de
bandeau d'organisme, noms propres en capitales, cotes d'archive au coin.

Textes dans preparation/magnitogorsk/89-komsomol.md.
Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

GRILLE = "--grille" in sys.argv
MANUSCRIT = "--sans-annotations" not in sys.argv
F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "La copie de l'autopsie de Zina",
     "papier": "papier jauni", "grammage": "160 g", "ou": "maison", "stock": True,
     "format": "A4", "feuilles": 1,
     "note": "recto seul"},
]

# La main de Nesteroff, pas celle d'Igor : il annote sa propre copie,
# en bas, là où il reste de la place. Position fixe — voir rapports-police.py.
#
# **Le document n'a jamais quitté le dispensaire.** Nesteroff a prévenu la
# section, et personne n'est venu — c'est sa réplique mot pour mot
# (89-komsomol.md). Écrire « remis au bureau de police » le ferait partir,
# et il n'aurait plus rien à sortir aux joueurs. C'est aussi ce qui donne
# son sens à « exemplaire de service n° 2 » : on tape en deux exemplaires,
# et **celui destiné au destinataire est encore sur l'étagère**.
#
# Et « personne n'est venu » ne peut pas s'écrire le 7 avril : c'est une
# annotation portée des semaines plus tard, ce qu'une écriture manuscrite
# dit toute seule.
MAIN = (16, 184, -1.4, 12.8)
ANNOT = "Section de police prévenue le 7.IV.<br>Personne n'est venu le chercher."


def regle():
    if not GRILLE:
        return ""
    e = []
    for x in range(0, 180, 20):
        e.append(f'<b style="left:{x}mm; top:0; width:.25mm; height:100%"></b>')
        e.append(f'<i style="left:{x + .6}mm; top:.5mm">{x}</i>')
    for y in range(0, 280, 20):
        e.append(f'<b class="v" style="left:0; top:{y}mm; height:.25mm; width:100%"></b>')
        e.append(f'<i class="v" style="left:.6mm; top:{y + .6}mm">{y}</i>')
    return f'<div class="regle">{"".join(e)}</div>'


x, y, a, t = MAIN
note = (f'<div class="plume annot" style="left:{x}mm; top:{y}mm; '
        f'transform:rotate({a}deg); font-size:{t}pt">'
        f'{ecrire(ANNOT, graine=61, encre=True, amplitude=.95)}</div>' if MANUSCRIT else "")

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Machine; src: url({F}/SpecialElite-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4; margin: 13mm 16mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Machine, serif; font-size: 8.4pt; line-height: 1.5;
        color: #1a1713; position: relative; }}
.frappe {{ filter: url(#frappe); }}

/* ── l'en-tête : un dispensaire, et il tient en trois lignes ──── */
.service {{ font-family: PT, serif; font-size: 6.8pt; letter-spacing: .1em;
            line-height: 1.6; margin-bottom: 7mm; }}
.service .ru {{ letter-spacing: .16em; }}

h1 {{ font-size: 11pt; font-weight: normal; letter-spacing: .5em; text-align: center;
      text-decoration: underline; text-underline-offset: 2.4px;
      text-decoration-thickness: .6px; margin: 0 0 5mm; }}

.ouverture {{ text-align: justify; margin: 0 0 5mm; }}

h2 {{ font-size: 8.4pt; font-weight: normal; letter-spacing: .22em;
      text-decoration: underline; text-underline-offset: 1.8px;
      text-decoration-thickness: .6px; margin: 5mm 0 2.2mm; }}

ol {{ margin: 0; padding-left: 7mm; }}
li {{ margin-bottom: 2.6mm; text-align: justify; padding-left: 1.5mm; }}
p {{ margin: 0 0 2.4mm; text-align: justify; }}

.reserve {{ border: .9px solid #1a1713; padding: 2.6mm 3.4mm; margin: 4mm 0 0; }}

.sign {{ margin-top: 7mm; text-align: right; line-height: 1.75; }}
.pied {{ margin-top: 6mm; border-top: .7px solid #1a1713; padding-top: 1.4mm;
         font-family: PT, serif; font-size: 6.4pt; letter-spacing: .07em; text-align: center; }}

.plume {{ font-family: Plume, cursive; color: #233a66; }}
.annot {{ position: absolute; z-index: 9; line-height: 1.25;
          transform-origin: left center; white-space: nowrap; }}
.cotes {{ position: absolute; right: 0; top: 0; text-align: right; line-height: 1; }}
.cotes .tampon {{ font-family: PT, serif; font-size: 13pt; font-weight: bold; color: #2a2724; }}
.cotes .crayon {{ font-family: Plume, cursive; font-size: 13pt; color: #6b6356;
                  display: block; margin: .4mm -1.5mm 0 0; transform: rotate(-3deg); }}

/* ── le cachet du dispensaire, pâle : une copie de service ───── */
svg.copie {{ position: absolute; width: 34mm; height: 34mm;
             right: 2mm; bottom: 46mm; transform: rotate(5deg);
             opacity: .55; mix-blend-mode: multiply; }}

.regle {{ position: absolute; inset: 0; pointer-events: none; }}
.regle b {{ position: absolute; background: #d33; opacity: .33; }}
.regle b.v {{ background: #39c; }}
.regle i {{ position: absolute; font-family: PT, serif; font-size: 5.2pt; color: #d33;
            font-style: normal; }}
.regle i.v {{ color: #2a7fa8; }}
</style></head><body>

<svg width="0" height="0" style="position:absolute">
 <filter id="frappe">
   <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" seed="3" result="n"/>
   <feDisplacementMap in="SourceGraphic" in2="n" scale="0.55"
                      xChannelSelector="R" yChannelSelector="G"/>
 </filter>
</svg>
{regle()}
{FILTRES}

<div class="cotes"><span class="tampon">31</span><span class="crayon">{ecrire("24", graine=62, amplitude=1.3)}</span></div>

<div class="frappe">
<div class="service">
  <div class="ru">ЦЕНТРАЛЬНЫЙ ДИСПАНСЕР — МАГНИТОГОРСК</div>
  <div>DISPENSAIRE CENTRAL DU COMPLEXE INDUSTRIEL</div>
  <div>Cabinet du médecin-chef — exemplaire de service n° 2</div>
</div>

<h1>A C T E</h1>

<p class="ouverture">1932 г. апреля 6 дня — l'an mil neuf cent trente-deux, le six avril, sur
réquisition de la section de police de Magnitogorsk, le soussigné I. NESTEROFF, médecin-chef du
dispensaire central, a procédé à l'examen médico-légal du corps de la citoyenne KRYLOVA, Zinaïda
Pavlovna, née en 1912 à Leningrad, découverte sans vie aux abords du gymnase du quartier du
Komsomol dans la matinée du 5 avril.</p>

<h2>CONSTATATIONS</h2>

<ol>
<li><b>Du moment du décès.</b> Le corps a séjourné à l'air libre par température négative et sous
chute de neige continue. Le refroidissement et la rigidité ne permettent <b>aucune estimation de
l'heure du décès</b>. Le soussigné s'en tient à la nuit du 4 au 5 avril, sans davantage de
précision, et appelle l'attention sur ce point.</li>

<li><b>De la cause du décès.</b> Asphyxie mécanique par strangulation au lien. Sillon cervical
unique, oblique ascendant, continu sur la face antérieure et les faces latérales du cou.
Congestion de la face, piqueté hémorragique des conjonctives.</li>

<li><b>De l'instrument.</b> Le sillon mesure entre quatre et six millimètres de large. Quelques
fibres végétales torsadées ont été recueillies au fond du sillon et sur le col du vêtement.
La largeur et la texture correspondent à une cordelette tressée de faible diamètre, <b>du type
employé couramment pour le maintien d'un vêtement de travail</b>.</li>

<li><b>Des traces de lutte.</b> Excoriations récentes aux deux avant-bras. Deux ongles de la main
droite rompus. Ecchymoses en nappe à la face interne des deux poignets, de forme ovalaire,
<b>symétriques et de dimensions concordantes</b>, sans correspondance avec les lésions du cou.</li>

<li><b>Du reste.</b> Aucune autre violence. Aucune trace de rapport. L'examen des organes ne révèle
ni maladie ni intoxication. Sujet jeune, de bonne constitution, parfaitement entraîné.</li>
</ol>

<h2>OBSERVATION DU SOUSSIGNÉ</h2>

<div class="reserve"><p>Il n'appartient pas au soussigné de conclure sur les circonstances. Il est
cependant de son devoir de signaler que <b>la tenue simultanée des deux poignets paraît
difficilement compatible avec une strangulation effectuée par un seul opérateur</b>, l'instrument
exigeant l'emploi des deux mains. Le soussigné se borne à ce constat et le soumet à l'appréciation
du service instructeur.</p></div>

<div class="sign">
  I. NESTEROFF — médecin-chef<br>
  Dispensaire central de Magnitogorsk<br>
  L'an mil neuf cent trente-deux, le six avril.
</div>

<div class="pied">EXAMEN MÉDICO-LÉGAL — KRYLOVA Z. P. — COPIE DE SERVICE — NE PAS DÉTRUIRE</div>
</div>
{note}

<svg class="copie" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
 <defs>
  <path id="dh" d="M 22,100 A 78,78 0 0 1 178,100"/>
  <path id="db" d="M 32,100 A 68,68 0 0 0 168,100"/>
  <filter id="encre" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="3" seed="29" result="b"/>
    <feDisplacementMap in="SourceGraphic" in2="b" scale="2.2"
                       xChannelSelector="R" yChannelSelector="G" result="d"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.08" numOctaves="2" seed="13" result="t"/>
    <feColorMatrix in="t" type="matrix"
      values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.6 0 0 0 -0.3" result="m"/>
    <feComposite in="d" in2="m" operator="out"/>
  </filter>
 </defs>
 <g filter="url(#encre)" fill="#2f5c46">
  <g fill="none" stroke="#2f5c46">
    <circle cx="100" cy="100" r="88" stroke-width="3"/>
    <circle cx="100" cy="100" r="77" stroke-width="1.2"/>
  </g>
  <text font-size="12" letter-spacing="1" font-family="PT">
    <textPath href="#dh" startOffset="50%" text-anchor="middle">
      ЦЕНТРАЛЬНЫЙ ДИСПАНСЕР
    </textPath>
  </text>
  <text font-size="11" letter-spacing="1.8" font-family="PT">
    <textPath href="#db" startOffset="50%" text-anchor="middle">
      ★ МАГНИТОГОРСК ★
    </textPath>
  </text>
  <text x="100" y="96" font-size="19" letter-spacing="2" text-anchor="middle"
        font-family="PT" font-weight="bold">КОПИЯ</text>
  <text x="100" y="116" font-size="10" letter-spacing="1.4" text-anchor="middle"
        font-family="PT">6.IV.32</text>
 </g>
</svg>

</body></html>"""

cible = RACINE / "out" / "autopsie-zina.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
