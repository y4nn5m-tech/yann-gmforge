#!/usr/bin/env python3
"""
dossier-gusev.py — la note de l'officier traitant.

    python3 scripts/dossier-gusev.py              # Gusev, Alekseï
    python3 scripts/dossier-gusev.py --feminin    # Guseva, Alina

Produit out/dossier-gusev[-feminin].pdf : une page A4 dont on découpe
la note, **à ne remettre qu'au joueur de Gusev·**, en aparté.

**L'ordre de mission n'est plus ici.** Ce script en portait un second,
au même numéro 0447 / L.I. que celui de `ordres-mission.py`, et les deux
avaient divergé : celui-ci envoyait Gusev· « aux fins de coordination
logistique », l'autre le met à la disposition d'une commission sur
réquisition — ce qui est la seule version qui explique pourquoi il ne
quitte pas trois enquêteurs pendant trois semaines. Deux papiers au même
numéro disant deux choses, c'est la contradiction interne que le modèle
des accessoires désigne comme la faute qui se voit à la table.

Les quatre ordres se fabriquent donc en un seul endroit, avec le même
gabarit pour les quatre personnages :

    python3 scripts/ordres-mission.py

Ce qui reste ici est ce qui n'a pas d'équivalent ailleurs : la note ne
porte **ni en-tête, ni numéro, ni tampon, ni signature** — un document
qu'on demande de brûler n'a pas de cartouche administratif, et c'est ce
qui le rend crédible.

Rendu par Chrome : WeasyPrint ignore feTurbulence.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F_GUS = "--feminin" in sys.argv

nom = "GUSEVA, Alina" if F_GUS else "GUSEV, Alekseï"
court = "Guseva" if F_GUS else "Gusev"

pet = "Petrenko"
kra = "Krasnova" if "--krasnova" in sys.argv else "Krasnoff"
vor = "Voronina" if "--voronina" in sys.argv else "Voronin"
vor_f = "--voronina" in sys.argv

F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "La note de l'officier traitant de Gusev·",
     "papier": "papier blanc", "grammage": "100 g", "ou": "maison",
     "format": "A4", "feuilles": 1,
     "note": "se découpe et se remet **en aparté** · **pas de jauni** · "
             "une seule des deux variantes s'imprime"},
]

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Mono; src: url({F}/CourierPrime-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A4; margin: 9mm 13mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Mono, monospace; font-size: 8pt; line-height: 1.5;
        color: #241f1a; }}

.consigne {{ font-family: PT, serif; font-size: 7.2pt; color: #7a736a; text-align: center;
             font-style: italic; margin-bottom: 3mm; line-height: 1.5; }}
.consigne.bas {{ text-align: left; margin: 2.5mm 0 0; }}

.bloc {{ border: .8px solid #b9b0a2; padding: 4.4mm 6mm; position: relative; }}
.remettre {{ font-family: PT, serif; font-size: 7.4pt; font-weight: bold; color: #7d2b2b;
             letter-spacing: .1em; text-align: center; margin: 2.4mm 0; }}

/* ── la note, et elle ne porte rien ──────────────────────────── */
.note {{ font-family: PT, serif; font-size: 9.4pt; font-style: italic; color: #2b3a52;
         line-height: 1.52; padding: 5mm 7mm; }}
.note p {{ margin: 0 0 2.8mm; text-align: left; }}
.note ul {{ list-style: none; margin: 0 0 2.8mm; padding-left: 7mm; }}
.note li {{ margin-bottom: 2mm; text-indent: -4mm; }}
.note b {{ font-weight: bold; font-style: italic; }}
.brule {{ text-align: right; margin-top: 3.5mm; }}
.brule .maj {{ color: #8a2222; font-size: 11.4pt; letter-spacing: .04em; }}
</style></head><body>

<div class="consigne">
À imprimer et découper. L'ordre de mission n° 0447 / L.I. se fabrique à part
(<b>scripts/ordres-mission.py</b>) et se remet devant toute la table ;
la note pliée ne se donne qu'au joueur de {court}, en aparté.
</div>

<div class="remettre">— À NE REMETTRE QU'AU JOUEUR DE {nom.split(',')[0]} —</div>

<div class="bloc note">
  <p>{court} —</p>

  <p>Ta mission de coordination est une couverture. Tiens-la sans faille.</p>

  <p>On attend de toi un <b>contre-rapport</b>. Tu voyages avec trois personnes. Juge-les, et ne
  rends ton jugement qu'à moi.</p>

  <ul>
    <li>— <b>{pet}</b> · postule chez nous. Parents monarchistes. Des nôtres, ou un rôle ?</li>
    <li>— <b>{kra}</b> · cercle de savants d'avant la Révolution. Garder, ou remercier ?</li>
    <li>— <b>{vor}</b> · {'montée' if vor_f else 'monté'} trop vite. N'aime pas la Guépéou, et
        l'a montré.</li>
  </ul>

  <p>N'entrave pas leur travail. Reste le fonctionnaire qu'ils croient voir.</p>

  <div class="brule">Mémorise. <span class="maj">BRÛLE CE BILLET.</span></div>
</div>

<div class="consigne bas">
Les annotations manuscrites — s'il y en a — se portent au stylo après impression.
</div>

</body></html>"""

cible = RACINE / "out" / f"dossier-gusev{'-feminin' if F_GUS else ''}.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
