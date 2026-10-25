#!/usr/bin/env python3
"""
chevalets-magnitogorsk.py — les cinq prétirées en cartons nom + photo.

    python3 scripts/chevalets-magnitogorsk.py

Produit out/chevalets-magnitogorsk-feminins.pdf : trois pages A4 paysage,
deux cartons par page, le dernier seul. Découper sur le trait, poser sur
le chevalet à la place du joueur.

L'auteur a doublé chaque prétiré masculin d'une version féminine, pour
que la table choisisse. Les chevalets masculins existaient déjà — trois
PDF produits à la main depuis un HTML qui n'a pas été gardé. Ce script
refait **le même carton**, mesuré dans ces PDF-là et non redessiné :

    carton          300 × 527 px, filet 1 px noir, à x = 232 et 591, y = 133
    bandeau de nom  39 px, fond blanc, **filet 1 px compris** — pas en plus
    le nom          Special Elite 22 px, letter-spacing 0.08 em, centré
    fenêtre photo   300 × 488 px, image calée en haut et rognée

La page fait 1123 × 794 px, soit A4 paysage à 96 dpi — l'original venait
d'une impression Chrome, et ces pixels-là sont ses unités.

Hors de build.py à dessein, comme cartes-sorts.py et chevalets-or-rochelle.py :
ce n'est pas un document de la collection (ni couverture, ni charte, ni
contrôles), c'est un accessoire de table.

Les portraits viennent du PDF du commerce et vivent dans sources/, que git
ignore — comme le texte du scénario. Le script est donc versionné, sa matière
non : il ne tourne que sur une machine où le scénario a été dépouillé.
"""
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image

os.environ.setdefault("SOURCE_DATE_EPOCH", "1700000000")

from weasyprint import HTML  # noqa: E402  (après SOURCE_DATE_EPOCH)

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "Les cinq chevalets de prétirés",
     "papier": "bristol blanc", "grammage": "250 g", "ou": "imprimerie",
     "format": "A4", "feuilles": 3,
     "note": "à l'italienne · à découper et plier, ils tiennent debout"},
]

RACINE = Path(__file__).resolve().parent.parent
ASSETS = RACINE / "assets"
OUT = RACINE / "out"
BACKGROUND = RACINE / "sources" / "magnitogorsk-pretires" / "Prétirés - Background.pdf"
RECADRES = OUT / "_chevalets-magnitogorsk"

PAGE = (1123, 794)         # px — A4 paysage à 96 dpi, les unités de l'original
CARTON = (300, 527)        # px — hors filet
BANDEAU = 39               # px — hauteur du bandeau de nom
# L'original trace son filet centré sur la demi-unité — 231,5 et 132,5 —, si
# bien que le contenu commence à 232 et 133. En CSS, `left` pose le bord
# extérieur du filet : ce sont donc 231 et 132 qu'il faut écrire pour retomber
# sur le même pixel.
COLONNES = (231, 590)      # px — bord extérieur du filet des deux cartons
HAUT = 132                 # px — bord extérieur du filet, en haut

# Une page du background par prétirée, et la photo en est la seule image.
# Les pages impaires portent les versions masculines, déjà sur chevalet.
#
# Le cadrage ne se centre pas : la fenêtre est verticale et les photos sont
# larges. La fraction dit où prendre la bande, 0 = tout à gauche, 1 = tout à
# droite. Centrer Maria ramène la seconde gymnaste, Alina les hommes derrière
# elle, et coupe Kira en deux. Maria n'est pas tout à fait à zéro : son visage
# s'y collait au bord droit du carton, et 0,13 le recentre sans faire revenir
# l'épaule de sa voisine.
PRETIREES = [
    ("BOGDANA PETRENKO", 2, 0.5),
    ("SVETLANA KRASNOVA", 4, 0.5),
    ("MARIA VORONINA", 6, 0.13),
    ("ALINA GUSEVA", 8, 0.0),
    ("KIRA VOLKOVA", 10, 0.0),
]

CSS = f"""
@font-face {{ font-family: "SpecialElite"; src: url("fonts/SpecialElite-Regular.ttf"); }}
@page {{ size: {PAGE[0]}px {PAGE[1]}px; margin: 0; }}
body {{ margin: 0; }}
.page {{ position: relative; width: {PAGE[0]}px; height: {PAGE[1]}px;
         page-break-after: always; }}
.page:last-child {{ page-break-after: auto; }}
.carton {{ position: absolute; top: {HAUT}px; width: {CARTON[0]}px; height: {CARTON[1]}px;
           border: 1px solid #000; box-sizing: content-box; }}
.nom {{ height: {BANDEAU - 1}px; line-height: {BANDEAU - 3}px; text-align: center;
        background: #fff; border-bottom: 1px solid #000;
        font-family: "SpecialElite"; font-size: 22px; letter-spacing: 0.08em; }}
.photo {{ width: {CARTON[0]}px; height: {CARTON[1] - BANDEAU}px; display: block; }}
"""


def portraits():
    """Un PNG recadré par prétirée, au format de la fenêtre photo."""
    if not BACKGROUND.is_file():
        sys.exit(f"source absente : {BACKGROUND}\n"
                 "Déposer le PDF du commerce dans sources/magnitogorsk-pretires/.")
    RECADRES.mkdir(parents=True, exist_ok=True)
    fenetre = CARTON[0] / (CARTON[1] - BANDEAU)
    faits = []
    for nom, page, fraction in PRETIREES:
        brut = RECADRES / f"p{page:02d}"
        subprocess.run(["pdfimages", "-png", "-f", str(page), "-l", str(page),
                        str(BACKGROUND), str(brut)], check=True)
        source = sorted(RECADRES.glob(f"p{page:02d}-*.png"))[0]
        im = Image.open(source).convert("RGB")
        w, h = im.size
        largeur = min(w, int(round(h * fenetre)))
        x = int(round((w - largeur) * fraction))
        cible = RECADRES / f"{page:02d}.png"
        im.crop((x, 0, x + largeur, h)).save(cible)
        faits.append((nom, cible))
    return faits


def main():
    OUT.mkdir(exist_ok=True)
    cartons = portraits()

    pages = []
    for i in range(0, len(cartons), 2):
        corps = "".join(
            f'<div class="carton" style="left:{COLONNES[j]}px">'
            f'<div class="nom">{nom}</div>'
            f'<img class="photo" src="{f.as_uri()}">'
            f"</div>"
            for j, (nom, f) in enumerate(cartons[i:i + 2]))
        pages.append(f'<div class="page">{corps}</div>')

    html = ('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            f"<style>{CSS}</style></head><body>{''.join(pages)}</body></html>")

    cible = OUT / "chevalets-magnitogorsk-feminins.pdf"
    doc = HTML(string=html, base_url=str(ASSETS)).render()
    doc.write_pdf(cible)
    print(f"· chevalets-magnitogorsk — {len(cartons)} cartons, {len(doc.pages)} page(s)")
    print(f"  {cible}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
