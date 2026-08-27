#!/usr/bin/env python3
"""
modele.py — met le modèle à disposition, et publie la page qui le présente.

    python3 scripts/modele.py

Écrit dans out/ :

    demarche.html        la page de présentation, copiée de web/
    modele-complet.md    les chapitres concaténés dans l'ordre de chargement
    modele.zip           les mêmes chapitres, séparés

Deux formes parce qu'il y a deux façons de travailler. Dans une conversation,
tout est chargé d'un coup et le chargement conditionnel du socle n'a plus
d'objet : le fichier unique suffit. Avec un assistant qui ouvre les fichiers, le
découpage se paie en place — on ne charge le chapitre d'un système que si on
joue ce système.

**Rien n'est transformé.** `modele/` n'est pas du code : les fichiers sont
concaténés tels quels, sans reformatage ni linter, et l'archive les reprend
octet pour octet. Le seul ajout est un séparateur entre deux chapitres du
fichier unique.

Le journal des passages est laissé de côté : c'est le retour d'expérience de ce
dépôt, scénario par scénario, pas une règle applicable ailleurs.
"""
import os
import sys
import time
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
MODELE = RACINE / "modele"
WEB = RACINE / "web"
OUT = RACINE / "out"

# L'ordre de chargement réel, celui que CLAUDE.md fait suivre : les
# instructions priment, le socle indique la suite, l'analyse sert dès la
# première étape, puis les livrables, puis ce qui dépend du scénario et du jeu.
ORDRE = [
    "instructions-projet.md",
    "MODELE-socle.md",
    "MODELE-analyse.md",
    "MODELE-livrable-dossier-prep.md",
    "MODELE-livrable-annote.md",
    "MODELE-livrable-aide-de-jeu.md",
    "MODELE-formes.md",
    "MODELE-systemes.md",
]

# Le retour d'expérience du dépôt : daté, nominatif, sans portée générale.
EXCLUS = {"JOURNAL-passages.md", "README.md"}

EN_TETE = """<!--
Le modèle éditorial — {n} chapitres, concaténés dans l'ordre de chargement.

Déposez ce fichier dans une conversation avec votre scénario. Les chapitres
sont séparés par une ligne « ─── ». Le premier, les instructions, prime sur
tous les autres.

Les chapitres séparés, la chaîne de fabrication et la marche à suivre :
https://github.com/y4nn5m-tech/yann-gmforge
-->

"""

SEP = "\n\n───────────────────────────────────────────────────────────────────────────────\n\n"


def chapitres():
    """Les chapitres dans l'ordre, en vérifiant qu'aucun n'a été oublié."""
    presents = {f.name for f in MODELE.glob("*.md")} - EXCLUS
    manquants = presents - set(ORDRE)
    if manquants:
        # un chapitre ajouté à modele/ sans être rangé ici sortirait du modèle
        # publié sans que personne le voie : c'est un échec, pas un détail
        print(f"  ÉCHEC chapitre(s) hors de l'ordre de chargement : "
              f"{', '.join(sorted(manquants))}", file=sys.stderr)
        raise SystemExit(1)
    absents = [n for n in ORDRE if not (MODELE / n).is_file()]
    if absents:
        print(f"  ÉCHEC chapitre(s) introuvable(s) : {', '.join(absents)}",
              file=sys.stderr)
        raise SystemExit(1)
    return [MODELE / n for n in ORDRE]


def fichier_unique(fs):
    corps = SEP.join(f.read_text(encoding="utf-8").rstrip() for f in fs)
    cible = OUT / "modele-complet.md"
    cible.write_text(EN_TETE.format(n=len(fs)) + corps + "\n", encoding="utf-8")
    return cible


def archive(fs):
    """Les chapitres séparés, horodatés à SOURCE_DATE_EPOCH.

    Sans date fixe, deux exécutions donnent deux archives différentes — et le
    dépôt tient à ce que deux fabrications d'une même source se ressemblent.
    """
    epoch = int(os.environ.get("SOURCE_DATE_EPOCH", "1700000000"))
    horodatage = time.gmtime(epoch)[:6]
    cible = OUT / "modele.zip"
    with zipfile.ZipFile(cible, "w", zipfile.ZIP_DEFLATED) as z:
        for f in fs:
            info = zipfile.ZipInfo(f"modele/{f.name}", date_time=horodatage)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, f.read_bytes())
    return cible


def page():
    src = WEB / "demarche.html"
    if not src.is_file():
        print(f"  ÉCHEC page introuvable : {src}", file=sys.stderr)
        raise SystemExit(1)
    cible = OUT / "demarche.html"
    cible.write_bytes(src.read_bytes())
    return cible


def main():
    OUT.mkdir(exist_ok=True)
    fs = chapitres()
    lignes = sum(f.read_text(encoding="utf-8").count("\n") for f in fs)

    u, a, p = fichier_unique(fs), archive(fs), page()
    print(f"· modèle — {len(fs)} chapitres, {lignes} lignes")
    for f in (p, u, a):
        print(f"  {f.name:<20} {f.stat().st_size // 1024:4d} Ko")
    return 0


if __name__ == "__main__":
    sys.exit(main())
