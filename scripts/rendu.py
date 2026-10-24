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


def pdf(html, cible, racine=None):
    """Écrit `html` dans un fichier temporaire et le rend en PDF."""
    cible = Path(cible)
    cible.parent.mkdir(parents=True, exist_ok=True)
    racine = Path(racine or Path.cwd())

    # le HTML vit dans la racine : les url(assets/...) doivent résoudre
    with tempfile.NamedTemporaryFile("w", suffix=".html", dir=racine,
                                     encoding="utf-8", delete=False) as f:
        f.write(html)
        tmp = Path(f.name)
    try:
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=4000",
            f"--print-to-pdf={cible}", tmp.as_uri(),
        ], check=True, capture_output=True, timeout=90)
    finally:
        tmp.unlink(missing_ok=True)
    return cible
