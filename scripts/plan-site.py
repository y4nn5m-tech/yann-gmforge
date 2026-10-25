#!/usr/bin/env python3
"""
plan-site.py — la carte de l'auteur, agrandie en A3 et annotée.

    python3 scripts/plan-site.py

Produit out/plan-site.pdf : un A3 à l'italienne, posé sur la table au
briefing et qui y reste tout l'acte 1.

## La base est celle de la source, et c'est voulu

**La source a deux cartes.** Celle du meneur porte les dix-sept lieux
numérotés ; **celle des joueurs ne porte que les zones A à G et les
quatre voies** — pas un seul lieu. C'est cette seconde qu'on reprend.

Un nom écrit sur un plan est une invitation. Un joueur qui lit « Section
D » au premier créneau y va, et la voie des affectations de
l'empoisonnement tombe avec. Les lieux se demandent — c'est le métier de
Kassym, et c'est ce qui le rend utile à la table plutôt que décoratif.

**Une carte recomposée à la main ne valait pas celle-ci.** Le dessin de
l'auteur a été tracé ; un contour obtenu en bruitant une ellipse ne l'est
pas, et l'œil fait la différence sans savoir pourquoi.

## Ce qu'on ajoute, et rien de plus

    les noms        les lettres A à G deviennent les intitulés de la
                    légende, écrits sur place. Plus d'aller-retour entre
                    la carte et une colonne
    les voies       w, x, y, z deviennent leurs noms
    le cartouche    un tirage de la direction des travaux. C'est ce qui
                    fait du document un objet et non une photocopie
    le crayon       ce que Kassym a porté dessus

## Ce que Kassym a écrit

*« chez moi »* · *« vous »* sur leur baraquement · **Guépéou** et
**prison** sur la zone militarisée, que l'imprimé laisse muette · et les
deux trajets qui se paient, **en temps de marche** : un guide compte en
journées, pas en kilomètres.

Ces deux-là sont la raison d'être du document à la table — posé là, il
rappelle la règle des créneaux au moment exact où ils choisissent où
aller, `50-temporalite.md`.

**Le logement de Tkachenko n'y est pas.** Le dossier du déserteur le
nomme ; le plan donnerait son adresse sans qu'ils aient eu à la
demander.

## La dépendance au PDF de la source

L'image vient de `sources/`, qui est ignoré par git : c'est la page 24
des aides officielles, extraite à 300 points par pouce. Le script ne
porte donc qu'un chemin et les surcharges — **rien du dessin de l'auteur
ne part dans le dépôt**. Pour la régénérer :

    pdftoppm -png -r 300 -f 24 -l 24 \\
      sources/magnitogorsk/Magnitogorsk_aides.pdf \\
      sources/magnitogorsk-aides-auteur/plan-joueurs

Fond blanc : l'impression se fait sur papier déjà jauni.
Rendu par Chrome — voir scripts/rendu.py.
"""
import random
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "Le plan du combinat",
     "papier": "papier crème", "grammage": "160 g", "ou": "imprimerie",
     "format": "A3", "feuilles": 1,
     "note": "à l'italienne · **reste sur la table tout l'acte 1** · le jauni du stock n'existe pas en A3, prendre leur crème"},
]
CARTE = RACINE / "sources" / "magnitogorsk-aides-auteur" / "plan-joueurs-24.png"

T = "#1b1d21"   # le trait du tirage
M = "#3b4049"   # le crayon de Kassym

# La carte occupe la hauteur utile ; la colonne de droite porte le titre
# et le cartouche, comme sur tout plan d'exécution.
LARG, HAUT = 275.0, 277.0


def pos(px, py):
    """Un point de la carte, donné en pourcentage de l'image."""
    return px / 100 * LARG, py / 100 * HAUT


# La planche reste **intacte** : aucun texte imprimé par-dessus. Un
# tirage de service n'emporte pas sa légende — elle est sur une autre
# planche, restée au bureau —, alors Kassym l'a recopiée à la main dans
# la marge. C'est ce qui justifie la colonne de droite, et c'est vrai :
# un guide qui donne un plan explique ses lettres.
#
# (lettre, ce qu'elle désigne, ce que le trajet coûte)
LEGENDE = [
    ("A", "tentes et yourtes", None),
    ("B", "Komsomol", None),
    ("C", "gare et entrepôts", None),
    ("D", "zone militarisée", None),
    ("E", "baraquements", None),
    ("F", "l'usine", None),
    ("G", "administration", None),
    (None, None, None),
    ("w", "route de Berezki", "une journée"),
    ("x", "voie ferrée — Tcheliabinsk", None),
    ("y", "voie ferrée du mont", None),
    ("z", "chemin du mont", "une demi-journée"),
]


# (texte, % x, % y, graine, corps en pt, ancrage)
# **Deux annotations seulement**, et c'est tout ce que Kassym a à
# écrire : où il habite, et où ils dorment.
#
# *Guépéou* et *prison* en sont sorties. Le scénario ne connaît pas de
# bureau de la Guépéou — il a **le bureau de police**, celui d'Igor ; le
# mot vient de la légende de la source et ferait croire à une antenne
# locale, alors que les joueurs *sont* les envoyés de la Guépéou. Et la
# prison est le lieu du dossier de la machine : l'écrire donne l'adresse
# sans qu'ils aient eu à la demander. Quant au bureau de police, Kassym
# les y conduit lui-même — il n'a rien à noter.
CRAYON = [
    ("chez moi", 21.5, 25.3, 11, 15, "l"),
    ("vous", 35.4, 49.2, 12, 15, "l"),
]

# Les croix du crayon : ce que Kassym pointe lui-même.
CROIX = [(21.0, 25.0), (34.6, 48.6)]


def legende():
    """La légende recopiée par Kassym, au-dessus du cartouche.

    **Rien n'est aligné.** Une main qui recopie une liste ne tient pas
    une colonne : chaque ligne part un peu plus à droite ou à gauche,
    l'écart entre la lettre et le mot change, et l'interligne respire.
    Les écarts sont tirés d'une graine fixe — le document reste le même
    d'une génération à l'autre.
    """
    r = random.Random(907)
    out = []
    for i, (lettre, quoi, prix) in enumerate(LEGENDE):
        if lettre is None:
            out.append('<div class="vide"></div>')
            continue
        marche = ecrire("— " + prix, graine=60 + i, amplitude=1.05) if prix else ""
        p = f'&nbsp;<span class="pr">{marche}</span>' if prix else ""
        gauche = r.uniform(-0.9, 2.8)
        haut = r.uniform(-0.8, 1.1)
        angle = r.uniform(-1.0, 1.0)
        ecart = r.uniform(5.8, 11.4)
        out.append(f'<div class="li" style="margin-left:{gauche:.1f}mm; '
                   f'margin-top:{haut:.1f}mm; transform:rotate({angle:.2f}deg)">'
                   f'<span class="le" style="margin-right:{ecart:.1f}mm">'
                   f'{ecrire(lettre, graine=40 + i, amplitude=1.1)}</span>'
                   f'<span class="qu">{ecrire(quoi, graine=50 + i, amplitude=1.05)}</span>'
                   f'{p}</div>')
    return "\n    ".join(out)


def croix():
    """Deux traits croisés au crayon.

    Une croix faite de deux segments droits de même longueur se voit
    tout de suite : personne ne croise deux traits à l'équerre. Ici les
    quatre bras ont des longueurs différentes, chaque trait est
    légèrement arqué, l'intersection n'est pas au milieu, et le tout
    passe sous le filtre qui sert à l'écriture.
    """
    r = random.Random(53)
    out = []
    for px, py in CROIX:
        x, y = pos(px, py)
        # l'intersection n'est pas le centre de la croix
        cx, cy = x + r.uniform(-.4, .4), y + r.uniform(-.4, .4)
        a = r.uniform(-18, 18)
        traits = []
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            lg = r.uniform(1.5, 3.1)
            ex, ey = cx + dx * lg, cy + dy * lg
            # le trait s'arque : le point de contrôle sort de l'axe
            ar = r.uniform(-.35, .35)
            qx, qy = (cx + ex) / 2 - dy * ar, (cy + ey) / 2 + dx * ar
            traits.append(f'<path d="M {cx:.2f} {cy:.2f} Q {qx:.2f} {qy:.2f} '
                          f'{ex:.2f} {ey:.2f}" fill="none" stroke="{M}" '
                          f'stroke-width="{r.uniform(.85, 1.25):.2f}" '
                          f'stroke-linecap="round"/>')
        out.append(f'<g filter="url(#plume)" transform="rotate({a:.1f} {x:.1f} {y:.1f})">'
                   + "".join(traits) + "</g>")
    return "\n  ".join(out)


def crayon():
    out = []
    for txt, px, py, g, corps, al in CRAYON:
        x, y = pos(px, py)
        # `right` se compte depuis le bord de la page, pas de la carte
        pos_css = (f"right:{400 - x:.1f}mm; text-align:right;" if al == "r"
                   else f"left:{x:.1f}mm;")
        out.append(f'<div class="k" style="{pos_css} top:{y:.1f}mm; font-size:{corps}pt">'
                   f'{ecrire(txt, graine=g, amplitude=1.05)}</div>')
    return "\n".join(out)


HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A3 landscape; margin: 10mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: {T}; position: relative;
        width: 400mm; height: 277mm; }}

.carte {{ position: absolute; left: 0; top: 0;
          width: {LARG}mm; height: {HAUT}mm; }}
.carte img {{ width: 100%; height: 100%; object-fit: contain; display: block; }}
.carte svg {{ position: absolute; inset: 0; width: 100%; height: 100%; }}

/* La légende, de la main de Kassym. */
.leg {{ position: absolute; left: 9mm; top: 34mm; width: 117mm;
        font-family: Plume, cursive; color: {M}; font-size: 15pt; }}
.leg .li {{ display: flex; align-items: baseline; margin-bottom: 2.2mm; }}
.leg .vide {{ height: 5mm; }}
.leg .le {{ flex: none; font-size: 17pt; }}
.leg .pr {{ font-size: 13pt; color: #5a616b; white-space: nowrap; }}

.k {{ position: absolute; font-family: Plume, cursive; color: {M};
      line-height: 1.1; white-space: nowrap; }}

/* La colonne de droite : titre en haut, cartouche en bas. */
.col {{ position: absolute; left: 283mm; top: 0; width: 117mm; height: 277mm; }}
.col h1 {{ font-size: 14pt; letter-spacing: .1em; margin: 2mm 0 1mm;
           font-weight: bold; }}
.col .sous {{ font-size: 9pt; letter-spacing: .12em; color: #555b63;
              margin-bottom: 3mm; }}
.col .filet {{ border-top: 1.1px solid {T}; }}

.cart {{ position: absolute; left: 0; bottom: 0; width: 117mm;
         border: 1.1px solid {T}; }}
.cart .l {{ display: flex; border-bottom: .5px solid {T}; }}
.cart .l:last-child {{ border-bottom: none; }}
.cart .c {{ padding: 2.2mm 3mm; font-size: 8.4pt; letter-spacing: .07em; }}
.cart .c + .c {{ border-left: .5px solid {T}; }}
.cart .g {{ flex: 1; }}
.cart .p {{ font-size: 7.2pt; color: #555b63; letter-spacing: .06em; }}
.ech {{ display: flex; height: 2.6mm; width: 46mm; border: .7px solid {T};
        margin: 1.4mm 0 .8mm; }}
.ech i {{ flex: 1; }}
.ech i:nth-child(odd) {{ background: {T}; }}
</style></head><body>
{FILTRES}

<div class="carte">
  <img src="{CARTE.as_uri()}" alt="">
  <svg viewBox="0 0 {LARG} {HAUT}" xmlns="http://www.w3.org/2000/svg">
    {croix()}
  </svg>
</div>

{crayon()}

<div class="col">
  <h1>МАГНИТОГОРСКИЙ КОМБИНАТ</h1>
  <div class="sous">PLAN GÉNÉRAL DU SITE ET DES QUARTIERS</div>
  <div class="filet"></div>

  <div class="leg">
    {legende()}
  </div>

  <div class="cart">
    <div class="l">
      <div class="c g">DIRECTION DES TRAVAUX<br>
        <span class="p">УПРАВЛЕНИЕ СТРОИТЕЛЬСТВА</span></div>
      <div class="c">ÉCH. 1:10 000</div>
    </div>
    <div class="l">
      <div class="c g">TIRAGE N° 214 — II.1932<br>
        <span class="p">EXEMPLAIRE DE SERVICE</span></div>
      <div class="c">VOIR ÉCHELLE<br><span class="p">EN BAS DE PLANCHE</span></div>
    </div>
  </div>
</div>

</body></html>"""

cible = RACINE / "out" / "plan-site.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
