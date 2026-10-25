#!/usr/bin/env python3
"""
planches-photos.py — les photographies d'époque, en planches à découper.

    python3 scripts/planches-photos.py

Produit out/planches-photos.pdf : des A4 portrait, **trois images par
feuille, en pleine largeur**. Une photo qu'on fait circuler se tient
dans la main — `15-photographies.md`.

## Ce qui est là, et ce qui n'y est pas

    les dix de lieu   quatre qui disent l'échelle, quatre selon ce
                      qu'ils visitent, deux détails. **Acte 1**
    les six de mine   authentiques, pour la descente. **Acte 2, et à
                      n'utiliser qu'en connaissance de cause** : tous
                      les accessoires quittent la table à ce
                      moment-là, et une image montrée à la frontale
                      défait ce que le noir construit

**Les trois portraits agrafés aux dossiers n'y sont pas** : ils sont
composés dans `rapports-police.py` et sortent avec leur dossier.
**Les cinq portraits de PJ non plus** : ils sont sur les chevalets.
Les doubler serait les affaiblir.

**Les images de l'acte 2 qui sont générées — paysages souterrains,
survivants, la créature — ne s'impriment pas du tout.** Une créature
montrée est une créature qui cesse de faire peur ; elles restent une
référence pour le meneur.

## La règle d'usage, qui prime sur la fabrication

**La photo vient après la description, jamais à la place.** On décrit,
puis on pose l'image — sans quoi la table regarde au lieu d'écouter.

Et la **paire 23 / 28** est la plus utile des dix : les baraquements et
Berezki posés côte à côte disent en une seconde ce qui sépare un ouvrier
d'un étranger. Elles sont voisines sur la planche pour cette raison.

## Les sources

Les images viennent de `sources/`, que git ignore : le script ne porte
que des chemins. Si un fichier manque, sa case reste vide avec son nom —
la planche se fabrique quand même.

Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

ARCH = RACINE / "sources" / "magnitogorsk" / "Archive"

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "Les dix photographies de lieu",
     "papier": "papier photo mat", "grammage": "160 g", "ou": "maison",
     "format": "A4", "feuilles": 4,
     "note": "trois par feuille, à découper · **pas de bleu-gris** : il mangerait "
             "les hautes lumières, et toute la lisibilité tient dans le blanc"},
    {"doc": "Les six photographies de mine",
     "papier": "papier photo mat", "grammage": "160 g", "ou": "maison",
     "format": "A4", "feuilles": 2,
     "note": "pour la descente · **à n'imprimer qu'en connaissance de cause** : "
             "l'acte 2 vide la table"},
]

# (fichier, légende, série)
PHOTOS = [
    # — les quatre qui disent l'échelle —
    ("Site indus 1.jpg", "Le site — cheminées, voies, gazomètres", "lieu"),
    ("sotsgorod 2.png", "Sotsgorod vu du ciel — la ville tracée à la règle", "lieu"),
    ("baraquement.jpg", "Les baraquements — l'alignement bas, la boue", "lieu"),
    ("archives photos/img109.jpg", "Berezki — maisons, jardins, arbres", "lieu"),
    # — les quatre selon ce qu'ils visitent —
    ("archives photos/img255.jpg", "Le palais administratif, de nuit", "lieu"),
    ("Komsomol 1.jpg", "Le bâtiment du Komsomol", "lieu"),
    ("Entrepot 3.jpg", "L'entrepôt — rais de lumière dans la charpente", "lieu"),
    ("archives photos/img170.jpg", "Le dispensaire — deux infirmières, un patient", "lieu"),
    # — les deux détails —
    ("URSS 2.jpg", "Le journal mural — à punaiser dans la pièce", "lieu"),
    ("archives photos/img266.jpg", "Une brigade de choc devant un plan", "lieu"),
    # — la mine, pour la descente —
    ("archives photos/img174.jpg", "Deux piqueurs au front de taille", "mine"),
    ("archives photos/img179.jpg", "Une équipe alignée dans une galerie maçonnée", "mine"),
    ("archives photos/img183.jpg", "Boisage — un mineur couché sous l'étai", "mine"),
    ("archives photos/img191.jpg", "Galerie étayée, wagonnet, éboulis", "mine"),
    ("archives photos/img195.jpg", "Tunnel de roche nue", "mine"),
    ("archives photos/img199.jpg", "Galerie éclairée au fond", "mine"),
]


def case(entree):
    """Une image et sa légende. Un fichier absent laisse la case ouverte."""
    if entree is None:
        return '<div class="v"></div>'
    fichier, legende, _ = entree
    chemin = ARCH / fichier
    if chemin.exists():
        img = f'<img src="{chemin.as_uri()}" alt="">'
    else:
        img = f'<div class="manque">{fichier}</div>'
    return f'<div class="ph">{img}<div class="leg">{legende}</div></div>'


PAR_PAGE = 3


def planches():
    out = []
    for serie, titre in (("lieu", "LES LIEUX — acte 1"), ("mine", "LA MINE — acte 2")):
        lot = [p for p in PHOTOS if p[2] == serie]
        for d in range(0, len(lot), PAR_PAGE):
            page = lot[d:d + PAR_PAGE]
            page += [None] * (PAR_PAGE - len(page))
            out.append(f'<section><div class="ent">{titre}'
                       f'<span>{d // PAR_PAGE + 1}</span></div>'
                       f'<div class="g">{"".join(case(q) for q in page)}</div></section>')
    return "\n".join(out)


HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 10mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: system-ui, -apple-system, sans-serif; color: #23262b; }}

/* 273 et non 277 : à la hauteur exacte de la zone imprimable, un pixel
   d'arrondi suffit à pousser la dernière case sur une page de plus. */
section {{ height: 273mm; display: flex; flex-direction: column;
           overflow: hidden; }}
section + section {{ break-before: page; }}

.ent {{ font-size: 7.6pt; letter-spacing: .22em; color: #6b727a;
        border-bottom: .6px solid #b9bfc6; padding-bottom: 1.4mm; margin-bottom: 3mm;
        display: flex; justify-content: space-between; }}

/* **Trois par feuille, en pleine largeur**, et c'est dicté par les
   images : elles sont presque toutes en format paysage. Dans une case
   portrait — quatre par feuille, deux colonnes — une photo au trois-deux
   perd la moitié de sa case en blanc. En pleine largeur elle fait dans
   les 120 × 80 mm, soit la taille d'une carte postale, qui est ce qu'on
   cherchait. */
.g {{ flex: 1; min-height: 0; display: grid; grid-template-columns: 1fr;
      grid-template-rows: 1fr 1fr 1fr; gap: 5mm; }}

.ph {{ display: flex; flex-direction: column; min-height: 0; }}
/* `contain`, pas `cover` : une photo d'archive ne se recadre pas pour
   remplir une case. On accepte les bandes blanches — à la découpe, on
   coupe au bord de l'image, pas au bord de la case. */
.ph img {{ flex: 1; min-height: 0; width: 100%; object-fit: contain;
           object-position: center; }}
.leg {{ font-size: 7.4pt; color: #4a5059; padding-top: 1.4mm;
        letter-spacing: .02em; }}

.manque {{ flex: 1; border: .8px dashed #b9bfc6; display: flex;
           align-items: center; justify-content: center; font-size: 7pt;
           color: #9aa1a9; padding: 4mm; text-align: center; }}
/* Une case vide ne se dessine pas. En revanche la grille garde ses trois
   rangées : les images doivent toutes sortir à la même taille, sinon la
   découpe n'est plus uniforme. */
.v {{ }}
</style></head><body>
{planches()}
</body></html>"""

cible = RACINE / "out" / "planches-photos.pdf"
rendu.pdf(HTML, cible, RACINE)
manquants = [f for f, _, _ in PHOTOS if not (ARCH / f).exists()]
print(f"· {cible.relative_to(RACINE)} — {len(PHOTOS)} images"
      + (f", {len(manquants)} introuvable(s) : {', '.join(manquants)}" if manquants else ""))
