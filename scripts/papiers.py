#!/usr/bin/env python3
"""
papiers.py — la liste de courses des accessoires.

    python3 scripts/papiers.py

**Il n'y a aucune liste à tenir à jour.** Chaque script d'accessoire
déclare sur quoi il s'imprime, dans une constante `PAPIER` posée près de
ses imports ; celui-ci les lit toutes et regroupe par papier.

    PAPIER = [
        {"doc": "Les cartes de repas",
         "papier": "bristol vert pâle", "grammage": "250 g",
         "ou": "imprimerie", "format": "A4", "feuilles": 1,
         "note": "six cartons à découper"},
    ]

## Ce qui sort de la maison, et ce qui n'en sort pas

La **Brother HL-L3240CDW** plafonne à **163 g/m²**, bac et fente manuelle
comprise — la fente n'apporte rien, contrairement à l'usage —, et son
**recto-verso automatique s'arrête à 105 g**. Son chemin papier sort par
le dessus, donc il est courbé : forcer un grammage supérieur ne se solde
pas par un refus poli mais par un bourrage.

D'où la répartition que `"ou"` porte :

    maison       tout ce qui tient sous 163 g — les archives et la
                 feuille du temps sur le jauni 160 g **déjà en stock**,
                 les documents de Moscou sur du blanc. Le rapport de
                 mission est à 100 g **exprès** : il est recto-verso, et
                 le duplex automatique plafonne à 105
    imprimerie   ce qui doit être rigide ou grand — les cartes, les
                 chevalets, le plan A3. Six feuilles, et c'est là qu'on
                 peut demander du 250 g sans se poser de question

**Le jauni 160 g passe en laser**, vérifié à l'usage — ce n'est pas
acquis d'avance : un papier à dessin teinté est souvent texturé, et le
toner accroche mal sur le grain.

**Mais feuille à feuille.** Il est à trois grammes du
plafond : le bac l'empile mal et finit par en prendre deux. La fente
manuelle a la même limite annoncée, mais une feuille à la fois, et
quatorze feuilles se posent en deux minutes.

La clé `"stock"` marque ce qu'on possède déjà : ces feuilles comptent
dans le total à imprimer, pas dans celui à acheter.

**La constante se lit sans exécuter le script.** Un import lancerait la
génération du PDF — plusieurs accessoires rendent au chargement du
module —, donc on analyse l'arbre syntaxique et on n'évalue que les
littéraux.

## Pourquoi plusieurs papiers, et pas un seul

Les trois familles ne sont pas une coquetterie : **l'œil classe les
documents à la table sans qu'on explique rien.**

    jauni        ce qui a vieilli en archive — les dossiers de police,
                 les dépositions, l'autopsie
    blanc cassé  ce qui vient de Moscou et a neuf jours — l'ordre de
                 détachement, les formulaires de l'épilogue
    bristol      ce qui se manipule tous les jours, ou se découpe — les
                 cartes de repas, la carte du Parti, les chevalets

Un document posé sur le mauvais papier se fond dans la pile voisine et
cesse d'être un objet.
"""
import ast
import sys
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent


def declaration(fichier):
    """La constante PAPIER d'un script, lue sans l'exécuter."""
    arbre = ast.parse(fichier.read_text(), filename=str(fichier))
    for noeud in arbre.body:
        if not isinstance(noeud, ast.Assign):
            continue
        cibles = [c.id for c in noeud.targets if isinstance(c, ast.Name)]
        if "PAPIER" in cibles:
            return ast.literal_eval(noeud.value)
    return []


TITRES = {"maison": "CHEZ SOI — la Brother plafonne à 163 g, duplex à 105",
          "imprimerie": "À L'IMPRIMERIE — rigide ou grand format",
          "papeterie": "EN PAPETERIE — ce qui ne s'imprime pas"}

# Le troisième groupe ne compte pas dans le total de feuilles : des
# chemises cartonnées ne sont pas du papier d'impression, et les
# mélanger fausserait les deux chiffres qui servent — ce qui passe dans
# la Brother, et ce qu'il faut acheter en ramette.
HORS_RAME = {"papeterie"}


def main():
    lots = defaultdict(lambda: defaultdict(list))
    for f in sorted((RACINE / "scripts").glob("*.py")):
        if f.name == "papiers.py":
            continue
        for d in declaration(f):
            cle = (d["papier"], d["grammage"], d["format"])
            lots[d.get("ou", "maison")][cle].append((f.name, d))

    if not lots:
        print("Aucun accessoire ne déclare son papier.")
        return 1

    total = 0
    print("\nLISTE DE COURSES — les accessoires")
    for ou in ("maison", "imprimerie", "papeterie"):
        if ou not in lots:
            continue
        sous = sum(d["feuilles"] for g in lots[ou].values() for _, d in g)
        if ou not in HORS_RAME:
            total += sous
        unite = "pièces" if ou in HORS_RAME else "feuilles"
        print(f"\n{TITRES[ou]}  ({sous} {unite})\n")
        for (papier, grammage, fmt), docs in sorted(lots[ou].items()):
            n = sum(d["feuilles"] for _, d in docs)
            stock = " — DÉJÀ EN STOCK" if all(d.get("stock") for _, d in docs) else ""
            mot = "pièce" if ou in HORS_RAME else "feuille"
            print(f"  ▸ {papier}, {grammage} — {fmt} — {n} {mot}"
                  f"{'s' if n > 1 else ''}{stock}")
            for script, d in docs:
                print(f"      {d['feuilles']}×  {d['doc']}")
                if d.get("note"):
                    print(f"          {d['note']}")
                print(f"          scripts/{script}")
            print()
    acheter = sum(d["feuilles"] for ou, g in lots.items() if ou not in HORS_RAME
                  for c in g.values() for _, d in c if not d.get("stock"))
    print(f"  {total} feuilles en tout, dont {acheter} à se procurer. "
          f"Sans compter les ratés.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
