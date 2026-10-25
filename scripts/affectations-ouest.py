#!/usr/bin/env python3
"""
affectations-ouest.py — les deux pièces qui ouvrent les disparitions
par les papiers.

    python3 scripts/affectations-ouest.py

Produit deux fichiers :

    out/affectations-ouest.pdf   le tableau des affectations, A4 à l'italienne
    out/carnet-gordeeva.pdf      son carnet d'écarts, A5

**Les deux se trouvent dans le bureau à cloison de Gordeeva**, aux
entrepôts. Elle a les affectations parce qu'elle réclame du monde chaque
semaine — mais *« Gordeeva ne propose jamais rien »* : il faut les lui
demander. Le carnet, elle le sort de son propre chef l'après-midi, quand
elle est assise ; le matin elle compte des bobines et répond entre deux
chiffres.

## Le tableau

**Ce n'est pas un imprimé du service du personnel, c'est son registre à
elle.** Gordeeva réclame du monde chaque semaine : elle tient un tableau
pour savoir qui elle a eu, et pour argumenter quand elle redemande. Même
tiroir, même encre que son carnet d'écarts.

**On n'imprime donc que la grille**, tracée à la règle au crayon — ni
bandeau, ni numéro de formulaire, ni intitulés. Les en-têtes de colonnes,
les semaines et les noms se portent à la main. Une ou deux ratures, une
encre qui change en cours de route, et c'est elle qui l'a tenu.

**La forme du tableau n'est pas négociable**, en revanche. Le document
n'existe que pour permettre un recoupement : voir d'un coup que deux
colonnes ne bougent jamais pendant que les autres tournent. Sur dix-neuf
pages séparées, personne ne le verrait — et la note demande que ce soit
trouvable **en deux minutes** par qui le cherche.

Le retournement du dossier tient là : dans une équipe où tout le monde
tourne, **Zykov et Nikiforov n'ont jamais bougé** — et sur les cinq dates
de plainte, Nikiforov est le seul nom présent à chaque fois. **Rien sur
la feuille ne le souligne** : les joueurs croisent eux-mêmes avec les
dates du dossier `1932-03/ENT`.

`--rempli` sort la version de référence, celle qui dit quoi écrire dans
chaque case. À garder sous la main en remplissant, pas à poser sur la
table.

## Le carnet

Quatre lignes, et **deux sont postérieures au classement du 28 mars** —
dont un écart sur le convoi du 24 avril. C'est ce qui prouve que le
trafic continue et désamorce le « tout ça est vieux ».

Fond blanc : l'impression se fait sur papier déjà jauni.
Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

REMPLI = "--rempli" in sys.argv
F = (RACINE / "assets" / "fonts").as_uri()

# ══════════════════════════════════════════════════════════════════
#  Le tableau
# ══════════════════════════════════════════════════════════════════

_T = "Tarassov"; _G = "Goloubev"; _P = "Panfilov"; _Y = "Yegorov"; _L = "Loukine"
_R = "Romanenko"; _S = "Chiriaev"; _B = "Borodine"; _C = "Tchernov"; _I = "Ivatchenko"
_D = "Doubov"; _O = "Rogov"; _V = "Sytchev"; _F = "Fomine"; _Z = "Zotov"
_K = "Kalinine"; _H = "Prokhorov"; _N = "Nazarenko"; _M = "Mikhaïlov"; _A = "Avdeïev"
X = None  # poste non pourvu cette semaine


def R(barre, final):
    """Remplacé en cours de semaine : on barre et on réécrit à côté."""
    return (barre, final)


# (semaine, encre, les cinq postes qui tournent)
SEMAINES = [
    ("1ᵉʳ janv.", "a", [_P, _Y, _L, _R, _S]),
    ("8 janv.", "a", [_P, _Y, _L, _R, _S]),
    ("15 janv.", "a", [X, _Y, _R, _B, _S]),
    ("22 janv.", "a", [_B, _Y, _R, R(_B, _C), _S]),
    ("29 janv.", "a", [_B, X, _R, _I, _C]),
    ("5 févr.", "b", [_B, _I, _D, _I, _L]),
    ("12 févr.", "b", [_B, _I, _D, _K, _L]),
    ("19 févr.", "b", [X, _I, _D, _K, _Z]),
    ("26 févr.", "b", [_F, _I, _Z, _K, _Z]),
    ("5 mars", "b", [_F, _K, _Z, _H, _T]),
    ("9 mars", "c", [_K, _K, _Z, _H, _T]),
    ("16 mars", "c", [_K, X, _M, _N, _T]),
    ("23 mars", "c", [_A, _T, _M, _N, _G]),
    ("30 mars", "c", [_A, _T, _M, R(_N, _D), _G]),
    ("6 avril", "c", [_L, _T, _R, _D, _P]),
    ("13 avril", "d", [_L, _S, _R, _O, _P]),
    ("20 avril", "d", [X, _S, _R, _O, _Y]),
    ("27 avril", "d", [_B, _S, _D, _V, _Y]),
    ("4 mai", "d", [_B, _C, _D, _V, _F]),
]


def case(v, encre):
    if v is None:
        return "<td></td>"
    if isinstance(v, tuple):
        barre, final = v
        return f'<td class="m {encre}"><s>{barre}</s> {final}</td>'
    return f'<td class="m {encre}">{v}</td>'


def lignes():
    """Vierge par défaut : seules les semaines sont imprimées.

    `--rempli` sort la version de référence, celle qui dit quoi écrire
    dans chaque case — à garder sous la main en remplissant, pas à poser
    sur la table.
    """
    out = []
    for sem, encre, postes in SEMAINES:
        c = [f'<td class="sem">{sem}</td>']
        if REMPLI:
            c += [f'<td class="m {encre}">Zykov</td>',
                  f'<td class="m {encre}">Nikiforov</td>']
            c += [case(v, encre) for v in postes]
        else:
            c += ["<td></td>"] * 7
        out.append(f"<tr>{''.join(c)}</tr>")
    return "\n".join(out)


_VIDE = "".join("<td></td>" for _ in range(8))
GRILLE = (f'<tr class="tete">{_VIDE}</tr>'
          + "".join(f"<tr>{_VIDE}</tr>" for _ in range(19)))

TABLEAU = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4 landscape; margin: 13mm 14mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Plume, cursive; color: #1f2c3d; position: relative; }}

/* La grille qu'elle a tirée à la règle : un trait de crayon, rien
   d'autre. Pas de bandeau, pas de numéro de formulaire — ce n'est pas
   un imprimé du service du personnel, c'est son registre à elle, du
   même tiroir que son carnet d'écarts. */
table {{ width: 100%; border-collapse: collapse; table-layout: fixed; }}
td {{ border: .55px solid #9aa4b0; height: 8.1mm; padding: 0 1.6mm;
      vertical-align: middle; }}
/* Le trait du haut et celui de gauche sont appuyés : c'est par là
   qu'on commence quand on trace. */
tr:first-child td {{ border-top-width: 1.1px; }}
td:first-child {{ border-left-width: 1.1px; }}
/* La ligne d'en-tête, laissée vide : elle y écrit ses intitulés. */
tr.tete td {{ height: 10.5mm; border-bottom-width: 1.1px; }}

</style></head><body>

<table>
<colgroup><col style="width:11%"><col style="width:12.7%"><col style="width:12.7%">
<col style="width:12.7%"><col style="width:12.7%"><col style="width:12.7%">
<col style="width:12.7%"><col style="width:12.8%"></colgroup>
{GRILLE}
</table>

</body></html>"""

# ══════════════════════════════════════════════════════════════════
#  Le carnet d'écarts
# ══════════════════════════════════════════════════════════════════

ECARTS = [
    ("14.I", "n°7", "2 bobines de câble", "tr. du 11"),
    ("23.III", "n°7", "1 lot d'ampoules, 6 m de gaine", "tr. du 20"),
    ("11.IV", "n°7", "4 bobines, 1 boîte de fusibles", "tr. du 8"),
    ("27.IV", "n°7", "9 m de gaine, 2 lots d'ampoules", "tr. du 24"),
]

CARNET = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A5; margin: 14mm 15mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Plume, cursive; font-size: 14.5pt; line-height: 9mm;
        color: #1f2c3d; position: relative; }}

/* Pas de réglure : calée au millimètre elle dérive quand même sous le
   rendu, et une ligne qui ne tombe pas sous le texte se voit plus
   qu'elle ne sert. Reste le filet de marge, qui dit « carnet ». */
.marge {{ position: absolute; left: 11mm; top: 0; bottom: 0; width: .3mm;
          background: #d9b7b7; opacity: .8; }}

.dedans {{ position: relative; padding-left: 4mm; }}
.titre {{ font-size: 16pt; margin-bottom: 9mm; display: inline-block;
          border-bottom: .7px solid #41536b; padding-bottom: .6mm; }}
.l {{ margin-bottom: 0; white-space: nowrap; }}
.l .d {{ display: inline-block; width: 14mm; }}
.l .o {{ display: inline-block; width: 10mm; }}
.trait {{ border-top: .5px solid #93a3b5; width: 58%; margin: 9mm 0 0; }}
.fin {{ font-size: 14pt; padding-top: 4mm; }}
</style></head><body>

{FILTRES}
<div class="marge"></div>

<div class="dedans">
  <div class="titre">{ecrire("Manques constatés — entrepôt 7", graine=71,
                             amplitude=1.1)}</div>

  {"".join(f'<div class="l"><span class="d">{ecrire(d, graine=80 + i)}</span>'
           f'<span class="o">{ecrire(o, graine=90 + i)}</span>'
           f'{ecrire(q, graine=100 + i, amplitude=1.1)} '
           f'<i>{ecrire("(" + c + ")", graine=110 + i)}</i></div>'
           for i, (d, o, q, c) in enumerate(ECARTS))}

  <div class="trait"></div>
  <div class="fin">{ecrire("Plus rien transmis depuis mars.", graine=72, amplitude=1.2)}<br>
  {ecrire("Je note, c'est tout.", graine=73, amplitude=1.2)}</div>
</div>

</body></html>"""


def main():
    for nom, html in (("affectations-ouest", TABLEAU), ("carnet-gordeeva", CARNET)):
        suffixe = "-rempli" if (REMPLI and nom == "affectations-ouest") else ""
        cible = RACINE / "out" / f"{nom}{suffixe}.pdf"
        rendu.pdf(html, cible, RACINE)
        print(f"· {cible.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
