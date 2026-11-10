#!/usr/bin/env python3
"""
rendu.py — HTML → PDF par Chrome, pour les accessoires.

Les documents de la collection passent par WeasyPrint et `build.py`, et
**ça ne change pas** : le CLAUDE.md du dépôt fait de la reproductibilité
au bit près une règle qui prime sur tout, parce qu'elle seule révèle
qu'une modification de contenu a déplacé la pagination d'un livret.

Les accessoires n'ont pas cette contrainte — ils tiennent sur une page,
et un débordement se voit à l'œil. Ils gagnent en échange ce que
WeasyPrint ne sait pas faire :

    textPath          le texte d'un tampon qui suit l'arc du cercle.
                      WeasyPrint l'ignore en silence
    filtres SVG       feTurbulence et feDisplacementMap, soit l'encre
                      irrégulière d'un cachet mal appuyé
    mix-blend-mode    l'encre qui se mêle au papier au lieu de le couvrir
    masques           les manques d'encre

**La variation reste déterministe.** Un document régénéré deux fois est
identique : les irrégularités viennent de graines fixes, jamais d'un
tirage. Sans quoi on ne pourrait plus comparer un avant et un après.
"""
import subprocess
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def _chrome(html, racine, options):
    racine = Path(racine or Path.cwd())
    # le HTML vit dans la racine : les url(assets/...) doivent résoudre
    with tempfile.NamedTemporaryFile("w", suffix=".html", dir=racine,
                                     encoding="utf-8", delete=False) as f:
        f.write(html)
        tmp = Path(f.name)
    try:
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--run-all-compositor-stages-before-draw", "--virtual-time-budget=4000",
            *options, tmp.as_uri(),
        ], check=True, capture_output=True, timeout=90)
    finally:
        tmp.unlink(missing_ok=True)


def pdf(html, cible, racine=None):
    """Écrit `html` dans un fichier temporaire et le rend en PDF."""
    cible = Path(cible)
    cible.parent.mkdir(parents=True, exist_ok=True)
    _chrome(html, racine, ["--no-pdf-header-footer", f"--print-to-pdf={cible}"])
    return cible


def png(html, cible, racine=None, largeur=794, hauteur=560, echelle=2.5):
    """Capture `html` en PNG — une A5 à l'italienne par défaut, à 96 dpi × `echelle`.

    Sert aux plans que la feuille de conduite embarque : la chaîne des
    documents ne sait pas lire un accessoire, elle lit une image."""
    cible = Path(cible)
    cible.parent.mkdir(parents=True, exist_ok=True)
    _chrome(html, racine, ["--hide-scrollbars", f"--window-size={largeur},{hauteur}",
                           f"--force-device-scale-factor={echelle}",
                           f"--screenshot={cible}"])
    return cible


def fragment_image(png_path, fragment, titre):
    """Écrit un fragment Markdown qui porte l'image en data URI.

    Le PDF se compose depuis assets/, le site depuis out/, l'EPUB depuis la
    racine : un chemin relatif ne résout pas partout. Une data URI, si — sans
    toucher à build.py."""
    import base64
    donnees = base64.b64encode(Path(png_path).read_bytes()).decode("ascii")
    Path(fragment).write_text(
        f"## {titre} {{.sec}}\n\n"
        f"![](data:image/png;base64,{donnees}){{width=100%}}\n",
        encoding="utf-8")
    return fragment
