#!/usr/bin/env python3
"""
pieces-de-dossier.py — ce qui garnit les chemises, et qui n'apprend rien.

    python3 scripts/pieces-de-dossier.py

Produit out/pieces-de-dossier.pdf : des A5 à découper, deux par feuille,
à glisser dans les chemises des sept dossiers de police.

**Pourquoi ces pièces existent, et pourquoi elles sont vides.** Un
rapport d'une feuille dans une chemise fait un dossier maigre ; la
tentation est de le remplir. Mais la source est explicite : Igor Pavlenko
et ses hommes font « un travail de piètre qualité », les dossiers sont
« souvent clos de manière prématurée » et les informations consignées
« au mieux parcellaires ». **Un dossier épais de vraies pièces
contredirait la source** — et chaque pièce de contenu est une occasion de
donner une réponse qui doit se chercher en parlant aux gens.

D'où le parti pris : **de la procédure, pas de l'enquête.** Bordereaux,
accusés, fiches à cases, convocations sans suite, demandes restées
lettre morte. Le dossier a l'air sérieux **jusqu'à ce qu'on l'ouvre**.
C'est le portrait d'Igor en objet.

**L'asymétrie est l'information.** Le dossier de la disparition — le seul
qu'il prenne au sérieux, « celui-là est sérieux » — est le seul garni de
pièces qui ont coûté du travail : un sondage de lacs, une réquisition de
moyens. Elles ne disent rien de l'affaire ; elles disent ce qu'il a
dépensé pour elle pendant que le reste dormait.

**Ce qu'aucune pièce ne fait** : nommer un lieu, une personne ou une
procédure que les joueurs n'ont pas encore rencontrés. Une pièce qui
désigne est une pièce qui répond.

Les cases vides sont le cœur du dispositif : **ce qui n'est pas rempli
est ce qui n'a pas été fait**, et personne n'a besoin de le commenter.

Fond blanc : l'impression se fait sur le papier jauni déjà en stock.
Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

# La cote tamponnée de chaque dossier, reprise de `rapports-police.py`.
# Un greffier porte un numéro d'inventaire, pas un code de script : la
# pièce et le rapport qu'elle accompagne doivent donner le même.
COTES = {"mrt": 112, "dis": 134, "emp": 141, "sab4": 96,
         "dec": 147, "sab9": 151, "ent": 63}

PAPIER = [
    {"doc": "Les pièces de procédure des dossiers",
     "papier": "papier jauni", "grammage": "160 g", "ou": "maison", "stock": True,
     "format": "A4", "feuilles": 6,
     "note": "deux A5 par feuille, à découper · **de la procédure, jamais de l'enquête** : "
             "les cases vides sont l'information"},
]

# **La milice, pas l'OGPU** — et la question vaut d'être posée, parce que
# la réponse décide de tout le dossier. Les sept rapports de
# `rapports-police.py` portent РАБОЧЕ-КРЕСТЬЯНСКАЯ МИЛИЦИЯ et un cachet
# МИЛИЦИЯ : une pièce en en-tête OGPU dans la même chemise serait la
# contradiction interne que le modèle désigne comme la faute qui se voit.
#
# Et sur le fond : la source parle du « responsable de la cellule locale
# de la **police** », jamais de la police politique, et ses dossiers le
# confirment — un noyé accidentel, une morte au Komsomol, du matériel
# disparu. L'OGPU traite le politique ; la milice traite ça.
#
# C'est aussi ce qui tient le dispositif du scénario : la milice ouvrière
# et paysanne est sous tutelle de l'OGPU depuis 1931, d'où une enquête de
# la Guépéou moscovite sur la fidélité d'un chef de milice, et une équipe
# venue de Moscou qu'il ne peut pas refuser.
ORGANE = ("RSFSR — MILICE OUVRIÈRE ET PAYSANNE<br>"
          "SECTION DE MAGNITOGORSK")

# (code du dossier, forme, titre, lignes)
#
# Une ligne vaut (intitulé, valeur) :
#   None   le trait reste nu — c'est ce qui n'a pas été rempli
#   "…"    tapé à la machine
#   ("m", "…")  porté à la main
PIECES = [
    ("sab9", "Форма № 4-Б", "BORDEREAU DE TRANSMISSION", [
        ("Service expéditeur", "PALAIS ADMINISTRATIF DU COMBINAT — SECRÉTARIAT GÉNÉRAL"),
        ("Service destinataire", "SECTION DE MAGNITOGORSK"),
        ("Pièce transmise", "Déposition, 1 f., recto"),
        ("Date de la pièce", ("m", "10.IV.32")),
        ("Date d'expédition", ("m", "28.IV.32")),
        ("Date de réception", ("m", "29.IV.32")),
        ("Observations du service expéditeur", None),
    ], "Le retard de dix-neuf jours, en pièce et non en commentaire."),

    ("sab9", "Форма № 9", "FICHE D'INSTRUCTION", [
        ("Objet", "Déraillements de convois — secteur transport"),
        ("Instruit par", None),
        ("Premier acte d'instruction, le", None),
        ("Témoins entendus", None),
        ("Transport sur les lieux, le", None),
        ("Suite donnée", None),
        ("Classé le", None),
    ], "Rien n'est rempli. Rien n'a été fait."),

    ("dis", "Форма № 9", "FICHE D'INSTRUCTION", [
        ("Objet", "Disparition — TKACHENKO, Pavel, urbaniste"),
        ("Instruit par", ("m", "I. Pavlenko")),
        ("Premier acte d'instruction, le", ("m", "28.IV.32")),
        ("Témoins entendus", ("m", "quatre")),
        ("Transport sur les lieux, le", ("m", "29.IV — 30.IV — 1.V")),
        ("Suite donnée", ("m", "recherches en cours")),
        ("Classé le", None),
    ], "Le seul dossier où les lignes sont pleines."),

    ("dis", "Форма № 17", "RAPPORT DE RECHERCHES", [
        ("Nature des opérations", "Sondage de plans d'eau"),
        ("Moyens engagés", "6 hommes, 2 barques, perches"),
        ("Durée", "3 jours"),
        ("Résultat", ("m", "néant")),
        ("Opérations à poursuivre", ("m", "oui")),
    ], "Trois jours, six hommes, néant — et on continue."),

    ("dis", "Форма № 22", "DEMANDE DE MOYENS", [
        ("Service demandeur", "SECTION DE MAGNITOGORSK"),
        ("Objet de la demande", "Maintien de l'équipe de sondage, 5 jours"),
        ("Motif", "Affaire prioritaire"),
        ("Décision", ("m", "accordé")),
    ], "« Affaire prioritaire » — écrit par lui, sur un imprimé."),

    ("emp", "Форма № 31", "DEMANDE DE PIÈCES", [
        ("Service requis", "DISPENSAIRE CENTRAL"),
        ("Pièces demandées", "État des admissions, cadres administratifs, mars-avril"),
        ("Date de la demande", ("m", "19.IV.32")),
        ("Rappel adressé le", None),
        ("Pièces reçues le", None),
    ], "Demandé une fois, jamais relancé."),

    ("emp", "Форма № 9", "FICHE D'INSTRUCTION", [
        ("Objet", "Maladies répétées — cadres administratifs"),
        ("Instruit par", None),
        ("Premier acte d'instruction, le", None),
        ("Témoins entendus", None),
        ("Transport sur les lieux, le", None),
        ("Suite donnée", ("m", "sans objet")),
        ("Classé le", None),
    ], "« Sans objet » est la seule main de la feuille."),

    ("dec", "Форма № 9", "FICHE D'INSTRUCTION", [
        ("Objet", "Décès — KURBANOFF, Venyamin"),
        ("Instruit par", ("m", "I. Pavlenko")),
        ("Premier acte d'instruction, le", ("m", "30.IV.32")),
        ("Témoins entendus", ("m", "deux")),
        ("Transport sur les lieux, le", ("m", "30.IV.32")),
        ("Suite donnée", ("m", "accident — classement")),
        ("Classé le", ("m", "1.V.32")),
    ], "Ouvert et clos en deux jours."),

    ("dec", "Форма № 12", "CONVOCATION", [
        ("Convoqué", "Ouvriers présents sur les lieux, service des eaux"),
        ("À comparaître le", ("m", "2.V.32")),
        ("Motif", "Audition"),
        ("Remise au destinataire, le", None),
        ("Comparution", None),
    ], "Souche non détachée : la convocation n'est jamais partie."),

    ("sab4", "Форма № 9", "FICHE D'INSTRUCTION", [
        ("Objet", "Explosion de machinerie — atelier"),
        ("Instruit par", ("m", "I. Pavlenko")),
        ("Premier acte d'instruction, le", ("m", "17.IV.32")),
        ("Témoins entendus", ("m", "aucun")),
        ("Transport sur les lieux, le", None),
        ("Suite donnée", ("m", "deux inculpations — négligence")),
        ("Classé le", ("m", "22.IV.32")),
    ], "Aucun témoin entendu, aucun transport, deux inculpés."),

    ("mrt", "Форма № 9", "FICHE D'INSTRUCTION", [
        ("Objet", "Décès — jeune femme, cité du Komsomol"),
        ("Instruit par", ("m", "I. Pavlenko")),
        ("Premier acte d'instruction, le", ("m", "27.IV.32")),
        ("Témoins entendus", ("m", "un")),
        ("Transport sur les lieux, le", ("m", "27.IV.32")),
        ("Suite donnée", ("m", "classement")),
        ("Classé le", ("m", "28.IV.32")),
    ], "Un témoin, une journée, classé."),

    ("ent", "Форма № 31", "DEMANDE DE PIÈCES", [
        ("Service requis", "SERVICE DES APPROVISIONNEMENTS"),
        ("Pièces demandées", "Relevé des manquants, trimestre écoulé"),
        ("Date de la demande", ("m", "14.III.32")),
        ("Rappel adressé le", None),
        ("Pièces reçues le", None),
    ], "Six semaines, et rien n'est revenu."),
]


def ligne(i, intitule, valeur, graine):
    """Une ligne de formulaire. Ce qui n'est pas rempli reste nu."""
    if valeur is None:
        contenu = ""
    elif isinstance(valeur, tuple):
        contenu = (f'<span class="plume">'
                   f'{ecrire(valeur[1], graine=graine + i, encre=True, amplitude=1.1)}'
                   f'</span>')
    else:
        contenu = f'<span class="machine">{valeur}</span>'
    return (f'<div class="l"><span class="i">{intitule}</span>'
            f'<span class="v">{contenu}</span></div>')


def piece(n, code, forme, titre, lignes, _note):
    corps = "".join(ligne(i, a, b, 400 + n * 37) for i, (a, b) in enumerate(lignes))
    return f"""<div class="piece">
  <div class="organe">{ORGANE}</div>
  <div class="forme">{forme}</div>
  <h2>{titre}</h2>
  <div class="dossier">Dossier&nbsp;n<sup>o</sup> <span class="plume">
    {ecrire(str(COTES[code]), graine=900 + n, encre=True, amplitude=0.9)}</span></div>
  {corps}
  <div class="pied">Тип. № 2 · Магнитогорск · 1931 г.</div>
</div>"""


pages = "".join(
    f'<div class="feuille">{piece(n, *PIECES[n])}'
    f'{piece(n + 1, *PIECES[n + 1]) if n + 1 < len(PIECES) else ""}</div>'
    for n in range(0, len(PIECES), 2))

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Mono; src: url({F}/CourierPrime-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4; margin: 0; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Mono, monospace; color: #241f1a; }}

.feuille {{ height: 297mm; display: flex; flex-direction: column;
            page-break-after: always; }}
.feuille > .piece:first-child {{ border-bottom: .6px dashed #b9b0a2; }}

.piece {{ flex: 1; padding: 13mm 15mm 9mm; position: relative; }}

.organe {{ font-family: PT, serif; font-size: 6.8pt; letter-spacing: .14em;
           line-height: 1.6; color: #4a443c; }}
.forme {{ position: absolute; right: 15mm; top: 13mm; font-size: 6.4pt;
          letter-spacing: .08em; color: #6b6356; }}

h2 {{ font-family: PT, serif; font-size: 11.4pt; font-weight: bold;
      letter-spacing: .2em; text-align: center; margin: 7mm 0 1.4mm; }}
.dossier {{ text-align: center; font-size: 7.2pt; color: #6b6356;
            margin-bottom: 6mm; }}
.dossier .plume {{ font-size: 11pt; }}

.l {{ display: flex; align-items: flex-end; gap: 2.6mm; margin-bottom: 4.6mm; }}
.l .i {{ font-size: 7pt; letter-spacing: .04em; color: #4a443c; white-space: nowrap; }}
.l .v {{ flex: 1; border-bottom: .7px solid #8a8276; min-height: 6.4mm;
         padding: 0 1.6mm .8mm; }}
.machine {{ font-size: 7.6pt; letter-spacing: .02em; }}
.plume {{ font-family: Plume, cursive; font-size: 12.6pt; color: #2b3a52;
          line-height: 1; }}

.pied {{ position: absolute; left: 15mm; bottom: 7mm; font-size: 5.8pt;
         letter-spacing: .1em; color: #a9a194; }}
</style></head><body>
{FILTRES}
{pages}
</body></html>"""

cible = RACINE / "out" / "pieces-de-dossier.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
for n, (code, _f, titre, _l, note) in enumerate(PIECES):
    print(f"  {code:5s} {titre:24s} {note}")
