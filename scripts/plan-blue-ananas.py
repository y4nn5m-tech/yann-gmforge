#!/usr/bin/env python3
"""
plan-blue-ananas.py — le Blue Ananas Burger des scènes 3 et 4, pour le meneur.

    python3 scripts/plan-blue-ananas.py

Produit out/plan-blue-ananas.pdf : une A5 à l'italienne, vue de dessus,
**pour le meneur seul** — comme le plan du Hakuna Burger. Il se
redessine à main levée devant les joueurs quand ils répartissent les
postes de la planque.

**La source décrit le lieu sans le dessiner.** Ce qu'elle pose :

    au coin de la rue       un immeuble de trois étages, propre sans
                            être chic
    l'ananas géant          bleu, en plastique, au-dessus de l'enseigne,
                            visible de loin
    le trottoir             des tables en métal, des clients soda à la
                            main, une circulation dense
    en face                 la banalisée, d'où l'on voit la mascotte sur
                            le trottoir d'en face
    le coupé rouge          se gare « non loin de la planque »
    les fuites              issue de secours, porte de service, accès
                            aux toits · l'auteur : les escaliers de
                            secours en tôle · Leon file vers les rues
                            chic de Feverly Hills
    le zoo                  « un Blue Ananas situé à quelques mètres du
                            zoo » — l'indice de Wells, scène finale

**En rouge, ce qui ne se dessine pas** : le chemin des fuites, et le
zoo. Le premier se joue, le second est l'accroche du scénario suivant.

Le toit est inventé, et c'est le seul ajout : la source y place la
baston d'El Toro sans le décrire.

Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

PAPIER = [
    {"doc": "Le plan du Blue Ananas Burger",
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
.zone {{ position: absolute; font-size: 7.2pt; letter-spacing: .1em; font-weight: bold;
         white-space: nowrap; }}

.route {{ position: absolute; border-top: 1.1px solid #241f1a;
          border-bottom: 1.1px solid #241f1a; }}
.route::after {{ content: ""; position: absolute; left: 0; right: 0; top: 50%;
                 border-top: .8px dashed #8a8276; }}
.routev {{ position: absolute; border-left: 1.1px solid #241f1a;
           border-right: 1.1px solid #241f1a; }}
.routev::after {{ content: ""; position: absolute; top: 0; bottom: 0; left: 50%;
                  border-left: .8px dashed #8a8276; }}

.vitre {{ position: absolute; height: 1.6mm; background: #9fb3c8; }}
.porte {{ position: absolute; background: #241f1a; }}
.comptoir {{ position: absolute; border: 1px solid #241f1a; background:
             repeating-linear-gradient(45deg, #fff 0 2px, #d8d2c6 2px 4px); }}
.escalier {{ position: absolute; border: 1px solid #241f1a; background:
             repeating-linear-gradient(90deg, #fff 0 1.4mm, #241f1a 1.4mm 1.7mm); }}
.table {{ position: absolute; width: 3.4mm; height: 3.4mm; border: .9px solid #6b6356;
          border-radius: 50%; }}
.auto {{ position: absolute; border: .9px solid #241f1a; border-radius: 1mm;
         font-size: 5.8pt; display: flex; align-items: center; justify-content: center; }}
.ananas {{ position: absolute; border-radius: 50% 50% 45% 45%; background: #5a7fb0;
           border: 1px solid #241f1a; }}
.clim {{ position: absolute; border: .9px solid #6b6356; background: #eee9df; }}

.poste {{ position: absolute; width: 6mm; height: 6mm; border: 1.4px solid #2b3a52;
          border-radius: 50%; background: #fff; color: #2b3a52; font-size: 6.6pt;
          font-weight: bold; display: flex; align-items: center; justify-content: center; }}
.pnj {{ position: absolute; width: 5mm; height: 5mm; border-radius: 50%;
        background: #241f1a; color: #fff; font-size: 6.2pt; font-weight: bold;
        display: flex; align-items: center; justify-content: center; }}

.fuite {{ position: absolute; height: 0; border-top: 1.3px dashed #8c2b22; }}
.fuitev {{ position: absolute; width: 0; border-left: 1.3px dashed #8c2b22; }}

.cheminv {{ position: absolute; width: 0; border-left: .9px dotted #8a8276; }}
.lab {{ position: absolute; font-size: 6.6pt; white-space: nowrap; }}
.cote {{ position: absolute; font-size: 6pt; color: #6b6356; white-space: nowrap; }}
.rouge {{ color: #8c2b22; }}
.fleche {{ position: absolute; font-size: 7pt; white-space: nowrap; }}

.encart {{ position: absolute; border: .9px solid #6b6356; background: #faf8f4; }}

.leg {{ position: absolute; left: 143mm; top: 18mm; right: 8mm; font-size: 6.4pt;
        color: #4a443c; line-height: 1.45; }}
.leg h2 {{ font-size: 6.8pt; letter-spacing: .14em; color: #241f1a; margin: 0 0 .8mm; }}
.leg p {{ margin: 0 0 2.4mm; }}
.leg .c {{ color: #2b3a52; font-weight: bold; }}
.leg .r {{ color: #8c2b22; font-weight: bold; }}
.leg .n {{ display: inline-block; width: 3.4mm; height: 3.4mm; border-radius: 50%;
           background: #241f1a; color: #fff; font-size: 5.4pt; font-weight: bold;
           text-align: center; line-height: 3.4mm; }}
</style></head><body>
<div class="p">
  <h1>BLUE ANANAS BURGER — FEVERLY HILLS</h1>
  <div class="sous">pour le meneur · scènes 3 et 4 · nord en haut · au coin de la rue ·
  à redessiner devant eux</div>

  <div class="plan">

    <!-- la rue transversale, à l'ouest -->
    <div class="routev" style="left:0mm; top:0mm; width:12mm; height:84mm"></div>
    <div class="cote" style="left:2.4mm; top:20mm; writing-mode:vertical-rl">rue transversale</div>

    <!-- la ruelle, au nord -->
    <div class="zone" style="left:56mm; top:9mm">RUELLE</div>
    <div class="escalier" style="left:16mm; top:9mm; width:18mm; height:5mm"></div>
    <div class="lab" style="left:15mm; top:0mm">escalier de secours en tôle</div>

    <!-- le bâtiment -->
    <div class="mur" style="left:14mm; top:14mm; width:62mm; height:48mm"></div>
    
    <div class="zone" style="left:18mm; top:19mm; font-weight:normal">CUISINE</div>
    <div class="b" style="left:58mm; top:14mm; width:18mm; height:14mm">bureau<div
         class="pet">manager</div></div>
    <div class="comptoir" style="left:20mm; top:28mm; width:38mm; height:3.4mm"></div>
    <div class="cote" style="left:30mm; top:24.6mm">comptoir</div>
    <div class="b" style="left:64mm; top:31.4mm; width:12mm; height:10mm">WC</div>
    <div class="zone" style="left:17mm; top:34mm">SALLE</div>

    <div class="porte" style="left:44mm; top:13.2mm; width:6mm; height:2.4mm"></div>
    <div class="cote" style="left:38mm; top:16mm">porte de service</div>

    <div class="vitre" style="left:15mm; top:61.2mm; width:24mm"></div>
    <div class="porte" style="left:40mm; top:60.6mm; width:9mm; height:2.6mm"></div>
    <div class="vitre" style="left:50mm; top:61.2mm; width:25mm"></div>

    <!-- le trottoir, les tables, l'ananas -->
    <div class="table" style="left:18mm; top:66mm"></div>
    <div class="table" style="left:25mm; top:69mm"></div>
    <div class="table" style="left:60mm; top:66mm"></div>
    <div class="table" style="left:67mm; top:69mm"></div>
    <div class="cote" style="left:16mm; top:74mm">tables en métal</div>
    <div class="ananas" style="left:42mm; top:65mm; width:5mm; height:6mm"></div>

    <!-- l'avenue -->
    <div class="route" style="left:0mm; top:84mm; width:124mm; height:20mm"></div>
    <div class="zone" style="left:56mm; top:86mm">L'AVENUE</div>
    <div class="cote" style="left:78mm; top:86.6mm">circulation dense · klaxons</div>
    <div class="fleche" style="left:0mm; top:106mm">← Westwood, la frontière</div>
    <div class="fleche" style="left:76mm; top:106mm">les rues chic de Feverly Hills →</div>

    <div class="auto" style="left:36mm; top:97mm; width:17mm; height:6mm">banalisée</div>
    <div class="auto" style="left:60mm; top:79mm; width:14mm; height:4.6mm">coupé rouge</div>
    <div class="cote" style="left:76mm; top:79.4mm">se gare ici, scène 4</div>

    <div class="cheminv" style="left:44.5mm; top:72mm; height:24mm"></div>
    <div class="cote" style="left:46mm; top:76mm">20 m</div>

    <!-- les postes -->
    <div class="poste" style="left:47mm; top:67mm">1</div>
    <div class="poste" style="left:24mm; top:54mm">2</div>
    <div class="poste" style="left:52mm; top:36mm">3</div>
    <div class="poste" style="left:32mm; top:96.5mm">4</div>
    <div class="poste" style="left:54mm; top:96.5mm">5</div>
    <div class="pnj" style="left:56mm; top:21mm">M</div>

    <!-- les fuites, en rouge -->
    <div class="fuitev" style="left:46mm; top:6mm; height:7mm"></div>
    <div class="fuite" style="left:25mm; top:6mm; width:21mm"></div>
    <div class="lab rouge" style="left:48mm; top:3mm">Little Latino, El Toro → le toit</div>
    <div class="fuite" style="left:76mm; top:66mm; width:44mm"></div>
    <div class="lab rouge" style="left:80mm; top:62mm">Leon → Feverly Hills</div>

    <!-- le toit, en encart -->
    <div class="encart" style="left:84mm; top:14mm; width:40mm; height:40mm"></div>
    <div class="zone" style="left:86mm; top:15.5mm">LE TOIT</div>
    <div class="clim" style="left:88mm; top:22mm; width:8mm; height:6mm"></div>
    <div class="clim" style="left:99mm; top:22mm; width:8mm; height:6mm"></div>
    <div class="cote" style="left:88mm; top:28.6mm">climatiseurs</div>
    <div class="clim" style="left:112mm; top:20mm; width:7mm; height:10mm; background:#d8d2c6"></div>
    <div class="cote" style="left:107mm; top:31mm">extraction</div>
    <div class="escalier" style="left:86mm; top:36mm; width:3mm; height:10mm"></div>
    <div class="cote" style="left:90mm; top:39mm">← l'escalier arrive</div>
    <div class="ananas" style="left:99mm; top:43mm; width:10mm; height:9mm"></div>
    <div class="cote" style="left:89mm; top:48.6mm">rebord</div>
    <div class="cote" style="left:111mm; top:46mm">ANANAS</div>
    <div class="cote" style="left:111mm; top:49mm">GÉANT</div>
  </div>

  <div class="leg">
    <h2>LES POSTES, À CINQ</h2>
    <p><span class="c">① l'ananas</span> — sur le trottoir, devant la porte · aucune vision sur
    les côtés · le soleil de face</p>
    <p><span class="c">② la table près de la vitrine</span> — voit le trottoir et l'ananas</p>
    <p><span class="c">③ la table près du comptoir</span> — voit la salle et le manager, pas la
    rue · le Juicy P Suprême</p>
    <p><span class="c">④ ⑤ la banalisée</span> — de l'autre côté de l'avenue · Carl à l'arrière
    · le trafic coupe la vue</p>

    <h2>QUI EST OÙ</h2>
    <p><span class="n">M</span> le manager, entre son bureau et le comptoir</p>

    <h2>LE TOIT</h2>
    <p>par l'escalier de secours, trois étages · l'ananas géant en plastique au bord · les
    climatiseurs pour se cacher</p>

    <h2 class="rouge">NE SE DESSINE PAS</h2>
    <p><span class="r">les fuites</span> — par la porte de service, l'escalier, le toit · Leon
    sur l'avenue, vers l'est</p>
    <p><span class="r">le zoo</span> — à deux pas · c'est là que le fils du procureur disparaît
    pendant la planque</p>

    <p><i>croquis : le dessin n'est pas à l'échelle</i></p>
  </div>
</div>
</body></html>"""

cible = RACINE / "out" / "plan-blue-ananas.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")

image = rendu.png(HTML, RACINE / "out" / "plan-blue-ananas.png", RACINE)
# la feuille de conduite et l'anti-sèche l'embarquent : une image, portée par son propre fragment
for doc in ("feuille-bun-and-run", "antiseche-bun-and-run"):
    fragment = RACINE / "src" / doc / "35-plan-blue-ananas.md"
    rendu.fragment_image(image, fragment, "Plan — le Blue Ananas")
    print(f"· {fragment.relative_to(RACINE)}")
