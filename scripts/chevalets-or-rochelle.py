#!/usr/bin/env python3
"""
chevalets-or-rochelle.py — les six prétirés en cartons à poser sur un chevalet.

    python3 scripts/chevalets-or-rochelle.py

Produit out/chevalets-or-rochelle.pdf : deux pages, le même jeu de six
cartons dans deux formats — paysage 85 × 55 mm en page 1, portrait
55 × 85 mm en page 2. Découper celui qui entre dans le chevalet, jeter
l'autre page. Les deux formats existent parce qu'un porte-carte en bois
n'a pas de dimension standard ; CARTE_PAYSAGE et CARTE_PORTRAIT se
règlent en tête de fichier si aucun des deux ne tombe juste.

Hors de build.py à dessein, comme cartes-sorts.py : ce n'est pas un
document de la collection (ni couverture, ni charte, ni contrôles),
c'est un accessoire de table.

Les portraits viennent du PDF du commerce et vivent dans sources/, que
git ignore — comme le texte du scénario. Le script est donc versionné,
sa matière non : il ne tourne que sur une machine où le scénario a été
dépouillé. Les extraire :

    pdfimages -png -f 22 -l 24 "L'Or de la Rochelle.pdf" prefixe

puis renommer dans l'ordre du flux : deschamps, duprave, montfaucon,
leblanc, remy, elise.
"""
import os
import sys
from pathlib import Path

os.environ.setdefault("SOURCE_DATE_EPOCH", "1700000000")

RACINE = Path(__file__).resolve().parent.parent
ASSETS = RACINE / "assets"
OUT = RACINE / "out"
PORTRAITS = RACINE / "sources" / "or-rochelle" / "portraits"

CARTE_PAYSAGE = (85, 55)   # mm — format carte de visite
CARTE_PORTRAIT = (55, 85)  # mm — le même, debout

# Le cadrage d'un portrait ne se centre pas : le visage est en haut sur
# les images verticales de la source, au milieu sur les deux horizontales.
# La fraction dit où prendre le carré, 0 = tout en haut, 1 = tout en bas.
PERSONNAGES = [
    ("deschamps",  "Thibault Deschamps",   "Ingénieur",      0.00),
    ("duprave",    "Evrard Duprave",       "Médecin",        0.05),
    ("montfaucon", "Guillaume de Montfaucon", "Chevalier",   0.00),
    ("leblanc",    "Geoffroy Leblanc",     "Capitaine",      0.35),
    ("remy",       "Remy Thibodeau",       "Contrebandier",  0.10),
    ("elise",      "Élise de Bellevue",    "Femme de lettres", 0.00),
]

CSS = """
@font-face { font-family:"DejaVuVendored"; font-weight:normal; font-style:normal;
             src:url("fonts/DejaVuSans.ttf") format("truetype"); }
@font-face { font-family:"DejaVuVendored"; font-weight:bold; font-style:normal;
             src:url("fonts/DejaVuSans-Bold.ttf") format("truetype"); }
@font-face { font-family:"DejaVuVendored"; font-weight:normal; font-style:italic;
             src:url("fonts/DejaVuSans-Oblique.ttf") format("truetype"); }
@page { size: A4; margin: 12mm 10mm; }
body { font-family:"DejaVuVendored"; margin:0; color:#1a2227; }
.page { page-break-after:always; }
.page:last-child { page-break-after:auto; }
.titre-page { font-size:8pt; text-transform:uppercase; letter-spacing:1.6pt;
              color:#7d8f9a; margin:0 0 4mm 0; }
.grille { display:flex; flex-wrap:wrap; gap:4mm; }

.carte { box-sizing:border-box; border:1px dashed #9aa8b0;
         page-break-inside:avoid; overflow:hidden; background:#fff; }

/* paysage — le portrait tient la hauteur, le nom occupe le reste.
   table-cell et non flex : WeasyPrint empile les deux lignes du nom
   l'une sur l'autre dans une colonne flex centrée. */
.pays { width:%(pl)dmm; height:%(ph)dmm; display:table; }
.pays .vignette { display:table-cell; width:%(ph)dmm; height:%(ph)dmm; }
.pays .nom { display:table-cell; vertical-align:middle; padding:0 3mm 0 3.5mm; }

/* portrait — le portrait en haut, le nom dessous */
.port { width:%(ql)dmm; height:%(qh)dmm; }
.port .vignette { width:%(ql)dmm; height:%(ql)dmm; }
.port .nom { padding:2.5mm 2mm 0 2mm; text-align:center; }

.vignette img { width:100%%; height:100%%; display:block; }
.n1 { font-size:10.5pt; font-weight:bold; line-height:1.15; color:#14507c;
      margin:0; }
.n2 { font-size:7.5pt; font-style:italic; color:#5a6b75; line-height:1.2;
      margin:1.4mm 0 0 0; }
.port .n1 { font-size:8.6pt; }
"""


def vignette(nom_fichier, ancrage, cote_px=620):
    """Recadre le portrait en carré et le dépose dans out/. PIL plutôt que
    object-fit : le cadrage se décide image par image, pas en CSS."""
    from PIL import Image

    src = PORTRAITS / f"{nom_fichier}.png"
    im = Image.open(src).convert("RGB")
    c = min(im.size)
    x = (im.width - c) // 2
    y = int((im.height - c) * ancrage)
    im = im.crop((x, y, x + c, y + c)).resize((cote_px, cote_px), Image.LANCZOS)
    cible = OUT / "_chevalets" / f"{nom_fichier}.png"
    cible.parent.mkdir(parents=True, exist_ok=True)
    im.save(cible, optimize=True)
    return cible


def carte(classe, chemin, nom, metier):
    return (f'<div class="carte {classe}">'
            f'<div class="vignette"><img src="file://{chemin}"></div>'
            f'<div class="nom"><div class="n1">{nom}</div>'
            f'<div class="n2">{metier}</div></div></div>')


def main():
    try:
        from weasyprint import HTML
    except ImportError:
        print("weasyprint manquant : pip install weasyprint --break-system-packages")
        return 1
    if not PORTRAITS.is_dir():
        print(f"portraits absents : {PORTRAITS}")
        print("les extraire du PDF du commerce — voir l'en-tête du script")
        return 1

    OUT.mkdir(exist_ok=True)
    vignettes = {c[0]: vignette(c[0], c[3]) for c in PERSONNAGES}

    pays = "".join(carte("pays", vignettes[c[0]], c[1], c[2]) for c in PERSONNAGES)
    port = "".join(carte("port", vignettes[c[0]], c[1], c[2]) for c in PERSONNAGES)
    css = CSS % {"pl": CARTE_PAYSAGE[0], "ph": CARTE_PAYSAGE[1],
                 "ql": CARTE_PORTRAIT[0], "qh": CARTE_PORTRAIT[1]}
    html = (f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            f"<style>{css}</style></head><body>"
            f'<div class="page"><div class="titre-page">'
            f'Chevalets — format paysage {CARTE_PAYSAGE[0]} × {CARTE_PAYSAGE[1]} mm</div>'
            f'<div class="grille">{pays}</div></div>'
            f'<div class="page"><div class="titre-page">'
            f'Chevalets — format portrait {CARTE_PORTRAIT[0]} × {CARTE_PORTRAIT[1]} mm</div>'
            f'<div class="grille">{port}</div></div>'
            f"</body></html>")

    cible = OUT / "chevalets-or-rochelle.pdf"
    doc = HTML(string=html, base_url=str(ASSETS)).render()
    doc.write_pdf(cible)
    print(f"· chevalets-or-rochelle — {len(PERSONNAGES)} cartons × 2 formats, "
          f"{len(doc.pages)} page(s)")
    print(f"  {cible}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
