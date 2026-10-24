#!/usr/bin/env python3
"""
carnet-du-temps.py — la feuille qui se coche à la table.

    python3 scripts/carnet-du-temps.py

Produit out/carnet-du-temps.pdf : une page A4 à l'italienne, posée au
centre de la table pendant tout l'acte 1.

**Ce n'est pas une aide du MJ, c'est un objet des joueurs.** Le rituel de
fin de créneau se termine par *« Qui coche ? »*, et on attend que
quelqu'un le fasse : une case cochée par le MJ est une annonce, une case
cochée par un joueur est une décision.

Ce qu'elle montre, et rien d'autre (`50-temporalite.md`) :

    les huit jours     du 3 au 10 mai, chacun coupé en matin et après-midi
                       — **sauf le 10, qui n'a que sa matinée** : le train
                       part le soir, et l'après-midi se passe à rejoindre
                       la gare
    le retour          départ le 10 au soir, échéance le 17

**Rien n'y est coché d'avance, pas même le 3 mai.** La feuille arrive
vierge et le premier jour se barre à la table, avec eux, comme tous les
autres : une case cochée d'avance est une annonce du meneur.

**Et pas de bande de déblaiement.** Elle nommait un chantier dont ils
n'ont pas encore entendu parler, et une feuille qui annonce quelque chose
cesse d'être leur objet. Le déblaiement se dit en jeu, quand il les
concerne.

Ce qu'elle ne montre pas, et c'est aussi important : **ni la descente, ni
le 13, ni le 20 mai.** Les cinq jours volés ne doivent pas être
prévisibles.

**Les cases des 8 et 9 mai restent vides.** Les griser annoncerait que ces
jours sont déjà pris, donc qu'il va se passer quelque chose — or descendre
doit rester leur décision. Ils croient disposer de douze demi-journées, ils
en ont huit, et la bande de déblaiement les rattrape tard.

Trois contraintes de fabrication, parce qu'elle vit au centre d'une table :

    dans les quatre sens   les jours sont répétés en haut et en bas,
                           pour ceux d'en face
    on écrit dessus        cases de 20 mm, papier mat et épais : la croix
                           se trace au crayon et elle reste cinq séances
    aucune information     rien que le MJ saurait et qu'eux ignorent
    du meneur

Fond blanc : l'impression se fait sur papier déjà jauni.
Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

# (quantième, jour de la semaine, demi-journées disponibles)
#
# Le 10 n'a que sa matinée : le train part le soir, et l'après-midi se
# passe à rejoindre la gare et à charger. On ne part pas en expédition
# le jour du départ — mais on a bien cette dernière demi-journée, et
# c'est un choix serré de plus.
JOURS = [("3", "mardi", 2), ("4", "mercredi", 2), ("5", "jeudi", 2),
         ("6", "vendredi", 2), ("7", "samedi", 2), ("8", "dimanche", 2),
         ("9", "lundi", 2), ("10", "mardi", 1)]



def entetes(bas=False):
    cls = " bas" if bas else ""
    return "".join(
        f'<div class="jour{cls}">'
        f'<span class="q">{q}</span><span class="s">{sem}</span></div>'
        for q, sem, _ in JOURS)


def cases(rang, moment):
    """Une rangée. Le 10 mai n'a pas d'après-midi : le train part le soir."""
    out = []
    for i, (q, _, demis) in enumerate(JOURS):
        if rang >= demis:
            out.append('<div class="case absente"></div>')
        elif i == 0:
            out.append(f'<div class="case"><span class="moment">{moment}</span></div>')
        else:
            out.append('<div class="case"></div>')
    return f'<div class="bande"><div class="quand"></div>{"".join(out)}</div>'


HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A4 landscape; margin: 14mm 16mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: #241f1a; }}

h1 {{ font-size: 13pt; font-weight: bold; letter-spacing: .26em; text-align: center;
      margin: 0 0 1mm; }}
.sous {{ text-align: center; font-size: 8pt; color: #6b6356; letter-spacing: .08em;
         margin: 0 0 6mm; }}

/* ── la grille : une colonne de libellé, sept colonnes de jours ── */
.bande {{ display: flex; align-items: stretch; }}
.quand {{ width: 4mm; flex: none; }}
/* Le moment se dit une fois, dans la première case, et pas en colonne :
   il compte — Gordeeva ne parle que l'après-midi, Nesteroff aussi — mais
   une colonne de libellés faisait grille administrative. */
.case .moment {{ position: absolute; left: 1.6mm; top: 1.2mm; font-size: 6.4pt;
                 letter-spacing: .1em; color: #a9a194; }}
.jour, .case {{ flex: 1; }}

.jour {{ text-align: center; padding: 0 0 1.6mm; }}
.jour.bas {{ padding: 1.6mm 0 0; }}
.jour .q {{ display: block; font-size: 15pt; font-weight: bold; line-height: 1; }}
.jour .s {{ display: block; font-size: 7pt; letter-spacing: .1em; color: #8a8276;
            margin-top: .6mm; }}
.jour.barre .q, .jour.barre .s {{ color: #a9a194; }}

.case {{ height: 20mm; border: .9px solid #4a443c; margin: 0 1mm 2mm;
         background: #fff; position: relative; }}
.case.absente {{ border: none; background: none; }}


/* ── le retour, en pied ───────────────────────────────────────── */
.retour {{ display: flex; align-items: baseline; gap: 4mm; margin-top: 10mm;
           border-top: 1px solid #4a443c; padding-top: 2.4mm;
           font-size: 9pt; letter-spacing: .04em; }}
.retour b {{ letter-spacing: .1em; }}
.retour .pointille {{ flex: 1; border-bottom: .7px dotted #a9a194; }}
</style></head><body>

<h1>MAGNITOGORSK — MAI 1932</h1>
<div class="sous">une croix par demi-journée employée</div>

<div class="bande"><div class="quand"></div>{entetes()}</div>
{cases(0, "matin")}
{cases(1, "après-midi")}
<div class="bande"><div class="quand"></div>{entetes(bas=True)}</div>


<div class="retour">
  <span><b>LE TRAIN</b> — 10 mai au soir</span>
  <span class="pointille"></span>
  <span><b>MOSCOU</b> — 17 mai</span>
</div>

</body></html>"""

cible = RACINE / "out" / "carnet-du-temps.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
