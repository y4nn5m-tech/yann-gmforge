#!/usr/bin/env python3
"""
carnet-nesteroff.py — la feuille de carnet du médecin-chef.

    python3 scripts/carnet-nesteroff.py

Produit out/carnet-nesteroff.pdf : une A5 manuscrite, à découper dans
une A4.

**Ce n'est pas un rapport, et c'est tout l'intérêt.** Le rapport
officiel est au dossier de police (`1932-08/EMP`) : il porte les noms,
les fonctions, l'état — et **le réfectoire**, colonne remplie pour
prouver la contamination alimentaire et qui prouve le contraire.

Cette feuille-ci est ce que Nesteroff note pour lui depuis le deuxième
mort. **Elle porte les dates, et les dates ne sont nulle part ailleurs.**

Ce qu'elle donne et que la lecture à voix haute perdrait : **le rythme**.
Six jours entre les deux premiers cas, puis sept, puis sept, puis six,
puis cinq, puis trois. Ça s'accélère, et ça se voit d'un coup d'œil sur
une colonne — jamais dans une phrase.

**Pas de réglure** : un interligne imprimé qui ne tombe pas exactement sur
les lignes d'écriture les barre à mi-hauteur, et c'est pire que rien. Le
papier jauni fait le travail.

**Pas de colonne d'affectation, jamais.** La question *« où
travaillaient-ils ? »* doit se poser et non se lire : c'est la règle qui
prime du chapitre des accessoires. Nesteroff, d'ailleurs, ne l'a pas
notée — il pense alimentation, pas lieu de travail.

Il la sort quand on la lui demande, ou quand quelqu'un a tenu sa cuvette.

**La ligne sur le registre d'entrées appelle un objet** que les joueurs
demanderont aussitôt : ce qu'il est, ce qu'il coûte et ce qu'il donne est
tranché dans `preparation/magnitogorsk/88-empoisonnement.md`, *le registre
des entrées*.

Rendu par Chrome — WeasyPrint ignore feTurbulence.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402
from plume import FILTRES, ecrire  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

PAPIER = [
    {"doc": "La feuille de carnet de Nesteroff",
     "papier": "papier jauni", "grammage": "160 g", "ou": "maison", "stock": True,
     "format": "A4", "feuilles": 1,
     "note": "une A5 à découper · **les dates sont l'information** · "
             "pas de colonne d'affectation"},
]

# nom, fonction, premiers symptômes, entrée, état
#
# Les écarts entre deux premiers symptômes : 6, 7, 7, 6, 5, 3 jours.
# **Ça s'accélère**, et c'est la seule chose que cette feuille apprend
# que le rapport de police n'apprend pas.
CAS = [
    ("Lebedev K.", "ing. en chef fonderie", "29.III", "31.III", "† 1.IV"),
    ("Ignatieva N.", "comptable principale", "4.IV", "6.IV", "† 8.IV"),
    ("Blokhin F.", "contremaître fonderie", "11.IV", "13.IV", "† 16.IV"),
    ("Gratchev S.", "ing. adj. tuyauterie", "18.IV", "20.IV", "† 2.V"),
    ("Maltseva I.", "techn. contrôle", "24.IV", "26.IV", "coma"),
    ("Rjevski R.", "ouvrier moulage", "29.IV", "1.V", "inconscient"),
    ("Koulikova A.", "ouvr. entretien", "2.V", "3.V", "inconsciente"),
]

NOTES = [
    ("Pas une épidémie. Rien ne se transmet.", False),
    ("Eau analysée le 21.IV — propre.", False),
    ("Demandé autopsie Blokhin. Refusé.", True),
    ("Ouvriers venus pour le ventre ce mois-ci : voir registre d'entrées.", False),
    ("Ils partagent quelque chose. Quoi ?", False),
]


def m(texte, graine, taille=1.0):
    return (f'<span class="pl" style="font-size:{12.4 * taille:.1f}pt">'
            f'{ecrire(texte, graine=graine, encre=True, amplitude=1.15)}</span>')


lignes = "".join(
    f'<tr><td>{m(n, 300 + i)}</td><td class="f">{m(f, 340 + i)}</td>'
    f'<td class="d">{m(s, 380 + i)}</td><td class="d">{m(e, 420 + i)}</td>'
    f'<td class="d">{m(t, 460 + i)}</td></tr>'
    for i, (n, f, s, e, t) in enumerate(CAS))

notes = "".join(
    f'<div class="note"><span class="{"raye" if barre else ""}">'
    f'{m(t, 600 + i, .92)}</span></div>'
    for i, (t, barre) in enumerate(NOTES))

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}

@page {{ size: A4; margin: 0; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: #241f1a; }}

.feuille {{ width: 210mm; height: 148mm; padding: 13mm 14mm 10mm;
            border-bottom: .6px dashed #b9b0a2; position: relative; }}

.pl {{ font-family: Plume, cursive; color: #2b3a52; line-height: 1; }}

.titre {{ position: relative; margin-bottom: 4mm; }}
.titre .pl {{ font-size: 15pt; }}

table {{ position: relative; width: 100%; border-collapse: collapse; }}
td {{ padding: .8mm 2mm 1.6mm 0; vertical-align: bottom; }}
td.f {{ opacity: .9; }}
td.d {{ text-align: left; white-space: nowrap; padding-left: 3mm; }}

.notes {{ position: relative; margin-top: 6mm; }}
.note {{ margin-bottom: 2.4mm; }}
.raye {{ position: relative; display: inline-block; }}
.raye::after {{ content: ""; position: absolute; left: -1.5mm; right: -1.5mm;
                top: 54%; height: .45mm; background: #2b3a52; opacity: .7;
                transform: rotate(-.6deg); }}
</style></head><body>
{FILTRES}
<div class="feuille">
  <div class="titre">{m("Cas — mars/mai 32", 200, 1.2)}</div>
  <table>{lignes}</table>
  <div class="notes">{notes}</div>
</div>
</body></html>"""

cible = RACINE / "out" / "carnet-nesteroff.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
