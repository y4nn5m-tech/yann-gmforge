#!/usr/bin/env python3
"""
plan-hakuna-burger.py — le Hakuna Burger de la scène 2, pour le meneur.

    python3 scripts/plan-hakuna-burger.py

Produit out/plan-hakuna-burger.pdf : une A5 à l'italienne, vue de
dessus, **pour le meneur seul** — comme le plan du secteur transport de
Magnitogorsk. Il se redessine à main levée devant les joueurs quand ils
montent leur plan.

**La source n'a pas de plan**, et l'auteur le dit dans sa vidéo : « si
vous voulez faire un petit plan avant, allez-y ». Tout ce qui est ici
est donc inventé, sauf ce que la source pose :

    114 Jefferson Avenue    frontière Westwood / Feverly Hills
    le parking              Harvey a vu la patrouille dessus, et s'est
                            replié à l'intérieur
    onze otages             sept employés, quatre clients — un enfant et
                            son père, une vieille dame, Carl
    un accès secondaire     *Fast-Food Queen* de Mei Davis sert à
                            « repérer une faille logistique ou un accès
                            secondaire » : il faut qu'il en existe un, et
                            qu'il ne se voie pas de la rue
    le périmètre            trois pas au-delà, il tire — l'auteur
    les médias              N64 sur place, un PJ doit parler à la caméra

**En rouge, ce qui ne se dessine que s'ils le trouvent.** Le plan ne
doit pas porter la réponse (MODELE-accessoires) : la porte de service
calée ouverte se découvre en parlant au personnel, pas en lisant le
croquis.

Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

PAPIER = [
    {"doc": "Le plan du Hakuna Burger",
     "papier": "papier blanc", "grammage": "80 g", "ou": "maison",
     "format": "A4", "feuilles": 1,
     "note": "**pour le meneur seul** · se redessine à main levée devant les joueurs"},
]

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A5 landscape; margin: 0; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: #241f1a; }}

.p {{ position: relative; width: 210mm; height: 148mm; padding: 8mm 10mm; }}
h1 {{ font-size: 10pt; letter-spacing: .22em; margin: 0 0 1mm; }}
.sous {{ font-size: 7pt; color: #6b6356; letter-spacing: .06em; margin: 0 0 3mm; }}

.plan {{ position: absolute; left: 10mm; top: 18mm; width: 128mm; bottom: 8mm; }}

.b {{ position: absolute; border: 1.1px solid #241f1a; background: #fff;
      font-size: 7.2pt; display: flex; flex-direction: column; align-items: center;
      justify-content: center; text-align: center; line-height: 1.2; }}
.b .pet {{ font-size: 6pt; color: #6b6356; }}
.mur {{ position: absolute; border: 1.8px solid #241f1a; }}
.zone {{ position: absolute; font-size: 7.2pt; letter-spacing: .1em; font-weight: bold; }}

.route {{ position: absolute; border-top: 1.1px solid #241f1a;
          border-bottom: 1.1px solid #241f1a; }}
.route::after {{ content: ""; position: absolute; left: 0; right: 0; top: 50%;
                 border-top: .8px dashed #8a8276; }}

.vitre {{ position: absolute; height: 1.6mm; background: #9fb3c8; }}
.vitrev {{ position: absolute; width: 1.6mm; background: #9fb3c8; }}
.porte {{ position: absolute; background: #241f1a; }}
.secret {{ position: absolute; background: #8c2b22; }}
.ruban {{ position: absolute; height: 0; border-top: 1.4px dashed #b8860b; }}
.comptoir {{ position: absolute; border: 1px solid #241f1a; background:
             repeating-linear-gradient(45deg, #fff 0 2px, #d8d2c6 2px 4px); }}
.tas {{ position: absolute; border: 1px solid #241f1a; background:
        repeating-linear-gradient(-45deg, #fff 0 2px, #d8d2c6 2px 4px); }}
.auto {{ position: absolute; border: .9px solid #6b6356; border-radius: 1mm;
         font-size: 5.6pt; color: #6b6356; display: flex; align-items: center;
         justify-content: center; }}
.groupe {{ position: absolute; border: .9px dotted #241f1a; border-radius: 50%;
           font-size: 6.4pt; display: flex; flex-direction: column; align-items: center;
           justify-content: center; text-align: center; line-height: 1.2; }}

.pnj {{ position: absolute; width: 5mm; height: 5mm; border-radius: 50%;
        background: #241f1a; color: #fff; font-size: 6.2pt; font-weight: bold;
        display: flex; align-items: center; justify-content: center; }}
.acc {{ position: absolute; width: 6mm; height: 6mm; border: 1.4px solid #2b3a52;
        border-radius: 50%; background: #fff; color: #2b3a52; font-size: 6.6pt;
        font-weight: bold; display: flex; align-items: center; justify-content: center; }}
.acc.r {{ border-color: #8c2b22; color: #8c2b22; }}

.cheminv {{ position: absolute; width: 0; border-left: .9px dotted #8a8276; }}
.lab {{ position: absolute; font-size: 6.6pt; white-space: nowrap; }}
.cote {{ position: absolute; font-size: 6pt; color: #6b6356; white-space: nowrap; }}
.rouge {{ color: #8c2b22; }}
.fleche {{ position: absolute; font-size: 7pt; white-space: nowrap; }}

.leg {{ position: absolute; left: 143mm; top: 18mm; right: 8mm; font-size: 6.4pt;
        color: #4a443c; line-height: 1.45; }}
.leg h2 {{ font-size: 6.8pt; letter-spacing: .14em; color: #241f1a; margin: 0 0 .8mm; }}
.leg p {{ margin: 0 0 2.6mm; }}
.leg .c {{ color: #2b3a52; font-weight: bold; }}
.leg .r {{ color: #8c2b22; font-weight: bold; }}
.leg .n {{ display: inline-block; width: 3.4mm; height: 3.4mm; border-radius: 50%;
           background: #241f1a; color: #fff; font-size: 5.4pt; font-weight: bold;
           text-align: center; line-height: 3.4mm; }}
</style></head><body>
<div class="p">
  <h1>HAKUNA BURGER — 114 JEFFERSON AVENUE</h1>
  <div class="sous">pour le meneur · scène 2 · nord en haut · frontière Westwood / Feverly Hills ·
  à redessiner devant eux</div>

  <div class="plan">

    <!-- la ruelle de service, au nord -->
    <div class="zone" style="left:42mm; top:1mm">RUELLE DE SERVICE</div>
    <div class="tas" style="left:12mm; top:2mm; width:12mm; height:6mm"></div>
    <div class="cote" style="left:12mm; top:8.4mm">bennes</div>
    <div class="cote" style="left:84mm; top:1.5mm">← rejoint la rue latérale</div>

    <!-- le bâtiment -->
    <div class="mur" style="left:6mm; top:12mm; width:102mm; height:50mm"></div>

    <!-- cuisine, réserve, bureau, poste du drive -->
    <div class="b" style="left:6mm; top:12mm; width:68mm; height:21mm; border:none;
         background:none">CUISINE<div class="pet">grill · friteuses · bac à frites</div></div>
    <div class="b" style="left:74mm; top:12mm; width:34mm; height:11mm">RÉSERVE<div
         class="pet">chambre froide · échelle</div></div>
    <div class="b" style="left:74mm; top:23mm; width:16mm; height:10mm">bureau<div
         class="pet">gérant</div></div>
    <div class="b" style="left:90mm; top:23mm; width:18mm; height:10mm">poste<div
         class="pet">du drive</div></div>

    <!-- le comptoir, qui coupe la salle de la cuisine -->
    <div class="comptoir" style="left:14mm; top:33mm; width:60mm; height:3.4mm"></div>
    <div class="cote" style="left:76mm; top:33.4mm">comptoir · caisses · <b>téléphone</b></div>

    <!-- la salle -->
    <div class="zone" style="left:9mm; top:56mm">SALLE</div>
    <div class="b" style="left:94mm; top:36.4mm; width:14mm; height:10mm">WC</div>
    <div class="groupe" style="left:22mm; top:41mm; width:58mm; height:16mm">onze otages au sol<br>
      <span style="color:#6b6356">mains sur la tête · l'enfant et son père</span></div>
    <div class="cote" style="left:78mm; top:50mm">banquettes · palmiers</div>
    <div class="cote" style="left:78mm; top:53mm">en plastique</div>

    <!-- vitrines et porte d'entrée, au sud -->
    <div class="vitre" style="left:7mm; top:61.2mm; width:30mm"></div>
    <div class="porte" style="left:39mm; top:60.6mm; width:12mm; height:2.6mm"></div>
    <div class="vitre" style="left:53mm; top:61.2mm; width:54mm"></div>
    <div class="vitrev" style="left:5.2mm; top:40mm; width:1.6mm; height:21mm"></div>

    <!-- les accès cachés -->
    <div class="secret" style="left:28mm; top:11.2mm; width:7mm; height:2.4mm"></div>
    <div class="secret" style="left:107.2mm; top:25mm; width:2.4mm; height:6mm"></div>
    <div class="secret" style="left:101mm; top:14mm; width:4mm; height:4mm"></div>

    <!-- les gens -->
    <div class="pnj" style="left:38mm; top:27mm">H</div>
    <div class="pnj" style="left:44mm; top:27mm">V</div>
    <div class="pnj" style="left:17mm; top:39mm">C</div>

    <!-- les accès, numérotés -->
    <div class="acc" style="left:42mm; top:64mm">1</div>
    <div class="acc" style="left:111mm; top:25mm">2</div>
    <div class="acc r" style="left:29mm; top:4mm">3</div>
    <div class="acc r" style="left:100mm; top:4mm">4</div>

    <!-- la voie du drive, à l'est -->
    <div class="cheminv" style="left:118mm; top:6mm; height:90mm"></div>
    <div class="cote" style="left:111mm; top:40mm">voie</div>
    <div class="cote" style="left:111mm; top:43mm">du drive</div>
    <div class="cote" style="left:113mm; top:47mm">↑</div>

    <!-- le parking -->
    <div class="zone" style="left:8mm; top:66mm">PARKING</div>
    <div class="auto" style="left:60mm; top:67mm; width:9mm; height:4.5mm">auto</div>
    <div class="auto" style="left:72mm; top:67mm; width:9mm; height:4.5mm">auto</div>

    <!-- le périmètre -->
    <div class="ruban" style="left:0mm; top:76mm; width:124mm"></div>
    <div class="lab" style="left:2mm; top:71.5mm; color:#b8860b">rubalise — <b>14 m de la porte ·
      trois pas de plus : il tire</b></div>

    <div class="auto" style="left:14mm; top:80mm; width:16mm; height:6mm;
         border-color:#241f1a; color:#241f1a">patrouille</div>
    <div class="auto" style="left:36mm; top:80mm; width:16mm; height:6mm;
         border-color:#241f1a; color:#241f1a">patrouille</div>
    <div class="auto" style="left:90mm; top:79mm; width:20mm; height:8mm;
         border-color:#241f1a; color:#241f1a">camion N64</div>
    <div class="cote" style="left:56mm; top:82mm">collègues · gyrophares</div>
    <div class="cote" style="left:58mm; top:90mm">badauds tenus à distance</div>

    <!-- l'avenue -->
    <div class="route" style="left:0mm; top:96mm; width:124mm; height:14mm"></div>
    <div class="zone" style="left:34mm; top:98mm">JEFFERSON AVENUE</div>
    <div class="fleche" style="left:0mm; top:112mm">← Westwood</div>
    <div class="fleche" style="left:96mm; top:112mm">Feverly Hills →</div>
  </div>

  <div class="leg">
    <h2>QUI EST OÙ</h2>
    <p><span class="n">H</span> <b>Harvey</b>, derrière la caisse · il voit la porte et toute la
    salle · <b>la cuisine est dans son dos</b><br>
    <span class="n">V</span> la vieille dame, contre lui<br>
    <span class="n">C</span> Carl, à une table couverte de burgers</p>

    <h2>LES ACCÈS</h2>
    <p><span class="c">① porte vitrée</span> — barricadée, tables et chaises · face à Harvey, à
    8 m · il voit tout venir</p>
    <p><span class="c">② guichet du drive</span> — étroit, un adulte mince · donne dans le poste du
    drive, à 10 m de son dos</p>
    <p><span class="r">③ porte de service</span> — sur la ruelle · <b>calée par un seau : le
    personnel sort fumer</b> · Mei le sait, un employé le dira</p>
    <p><span class="r">④ trappe du toit</span> — dans la réserve, par l'échelle · se trouve par
    le toit, si quelqu'un y grimpe</p>

    <h2>PARLER</h2>
    <p>le téléphone du comptoir · le mégaphone · un appareil glissé sous la porte</p>

    <p class="rouge"><b>en rouge : ne se dessine que s'ils le trouvent</b></p>
    <p><i>croquis : les distances sont écrites, le dessin n'est pas à l'échelle</i></p>
  </div>
</div>
</body></html>"""

cible = RACINE / "out" / "plan-hakuna-burger.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")

image = rendu.png(HTML, RACINE / "out" / "plan-hakuna-burger.png", RACINE)
# la feuille de conduite et l'anti-sèche l'embarquent : une image, portée par son propre fragment
for doc in ("feuille-bun-and-run", "antiseche-bun-and-run"):
    fragment = RACINE / "src" / doc / "25-plan-hakuna-burger.md"
    rendu.fragment_image(image, fragment, "Plan — le Hakuna Burger")
    print(f"· {fragment.relative_to(RACINE)}")
