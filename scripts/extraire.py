#!/usr/bin/env python3
"""
extraire.py — l'étape mécanique : un PDF source entre, du texte greppable sort.

    python3 scripts/extraire.py ~/scenarios/grand-froid.pdf
    python3 scripts/extraire.py ~/scenarios/grand-froid.pdf --nom grand-froid

Produit dans sources/<nom>/ :
    texte.txt        pdftotext -layout, une page par form feed
    manifeste.md     ce que l'extraction a réussi, et surtout ce qu'elle a raté
    pages/p-NN.png   les seules pages à regarder en image (--rendre)

Cette passe ne se pose aucune question et ne juge rien. Son seul travail
intelligent est de SIGNALER CE QU'ELLE N'A PAS SU EXTRAIRE : une page dont la
densité de texte s'effondre porte le plan ou une pleine page illustrée, et le
modèle est formel — un plan est un document de règles, pas une illustration.

Le manifeste n'est donc pas un rapport, c'est une liste de travail : après lui,
on rend trois à six pages en image au lieu de quarante.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SOURCES = RACINE / "sources"

# Une page sous ce pourcentage de la densité médiane est tenue pour illisible :
# c'est presque toujours une carte, un plan ou une pleine page illustrée.
SEUIL_CREUX = 0.35
# Et une page franchement vide en texte, quelle que soit la médiane.
PLANCHER_ABSOLU = 250


def outil(nom):
    if not shutil.which(nom):
        sys.exit(f"{nom} est absent — installer poppler-utils")
    return nom


def pages_texte(pdf: Path):
    """Le texte page par page. pdftotext sépare les pages par un form feed."""
    txt = subprocess.run([outil("pdftotext"), "-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    pages = txt.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def images(pdf: Path):
    """Inventaire des images embarquées, par page."""
    try:
        sortie = subprocess.run([outil("pdfimages"), "-list", str(pdf)],
                                capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return {}
    par_page = {}
    for ligne in sortie.splitlines()[2:]:
        champs = ligne.split()
        if len(champs) > 3 and champs[0].isdigit():
            page = int(champs[0])
            largeur, hauteur = int(champs[3]), int(champs[4])
            par_page.setdefault(page, []).append(largeur * hauteur)
    return par_page


def mediane(valeurs):
    v = sorted(valeurs)
    n = len(v)
    if not n:
        return 0
    return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2


def rendre(pdf: Path, numeros, dossier: Path, dpi=110):
    dossier.mkdir(parents=True, exist_ok=True)
    for n in numeros:
        subprocess.run([outil("pdftoppm"), "-png", "-r", str(dpi),
                        "-f", str(n), "-l", str(n), str(pdf),
                        str(dossier / "p")], check=True)


def main():
    ap = argparse.ArgumentParser(description="Extraction mécanique d'un scénario PDF.")
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--nom", help="nom du dossier dans sources/ (défaut : celui du PDF)")
    ap.add_argument("--rendre", action="store_true",
                    help="rendre en PNG les pages signalées comme illisibles")
    args = ap.parse_args()

    if not args.pdf.is_file():
        sys.exit(f"introuvable : {args.pdf}")

    nom = args.nom or re.sub(r"[^a-z0-9]+", "-", args.pdf.stem.lower()).strip("-")
    dossier = SOURCES / nom
    dossier.mkdir(parents=True, exist_ok=True)

    pages = pages_texte(args.pdf)
    if not pages:
        sys.exit("aucun texte extrait — le PDF est probablement un scan ; il faudra l'OCR")

    (dossier / "texte.txt").write_text("\f".join(pages), encoding="utf-8")

    densites = [len(p.strip()) for p in pages]
    med = mediane([d for d in densites if d > 0]) or 1
    imgs = images(args.pdf)

    creuses = [i for i, d in enumerate(densites, 1)
               if d < PLANCHER_ABSOLU or d < med * SEUIL_CREUX]

    # ------------------------------------------------------------- manifeste
    m = [f"# {nom} — manifeste d'extraction", "",
         f"Source : `{args.pdf.name}`  ·  {len(pages)} pages  ·  "
         f"{sum(densites)} caractères  ·  médiane {int(med)} car./page", ""]

    if creuses:
        m += ["## Pages à regarder en image", "",
              "L'extraction n'en a presque rien tiré. C'est là que se trouvent le plan, les",
              "pleines pages illustrées et les tableaux dessinés — autant de **documents de",
              "règles** dont la légende porte des valeurs absentes du texte.", "",
              "| Page | Caractères | Images | Ce que c'est probablement |",
              "|---:|---:|---:|---|"]
        for n in creuses:
            surfaces = imgs.get(n, [])
            grande = max(surfaces) if surfaces else 0
            if grande > 1_000_000:
                pari = "pleine page illustrée, ou plan"
            elif surfaces:
                pari = "illustration avec légende"
            else:
                pari = "page de titre, ou dessin vectoriel — un plan tracé au trait"
            m.append(f"| {n} | {densites[n-1]} | {len(surfaces)} | {pari} |")
        m.append("")
    else:
        m += ["## Pages à regarder en image", "",
              "Aucune. Toutes les pages ont rendu du texte en quantité comparable.",
              "**Vérifier tout de même qu'il existe un plan** : s'il n'y en a pas et que le",
              "scénario se déroule dans un site, c'est une pièce à réclamer avant d'analyser.",
              ""]

    m += ["## Ce que cette extraction ne dit pas", "",
          "À ne pas trancher depuis `texte.txt` seul :", "",
          "- **le niveau typographique** — encadrés, texte à lire à voix haute, apartés MJ.",
          "  Le test « la source est-elle lisible ? » porte précisément là-dessus, et le texte",
          "  à plat détruit le signal qu'il mesure ;",
          "- **les légendes d'illustration**, qui portent parfois un fait unique ;",
          "- **les tableaux et profils**, que `-layout` approxime et parfois emmêle ;",
          "- **les colonnes**, quand la mise en page en compte plus d'une.", ""]

    (dossier / "manifeste.md").write_text("\n".join(m), encoding="utf-8")

    if args.rendre and creuses:
        rendre(args.pdf, creuses, dossier / "pages")

    print(f"· {nom} — {len(pages)} pages, {sum(densites)} caractères")
    print(f"  sources/{nom}/texte.txt")
    print(f"  sources/{nom}/manifeste.md")
    if creuses:
        print(f"  {len(creuses)} page(s) à regarder en image : {', '.join(map(str, creuses))}")
        if args.rendre:
            print(f"  sources/{nom}/pages/ — rendues à 110 dpi")
        else:
            print("  (relancer avec --rendre pour les produire)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
