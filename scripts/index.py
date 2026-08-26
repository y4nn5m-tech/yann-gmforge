#!/usr/bin/env python3
"""
index.py — la page d'accueil du site, reconstruite à chaque passage de la CI.

    python3 scripts/index.py

Lit les métadonnées de chaque document dans src/, regarde ce qui existe
réellement dans out/, et écrit out/index.html : un scénario par bloc, ses
documents en dessous, chacun avec ses trois formats.

Rien à tenir à jour à la main. Ajouter un scénario, c'est ajouter un
répertoire dans src/ ; la page suit au prochain build.
"""
import json
import sys
from html import escape
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
from build import SRC, OUT, ASSETS, meta  # noqa: E402

TITRE = "Documents de table"
CHAPEAU = ("Scénarios du commerce transformés en documents menables : un livret de table "
           "et une note d'arbitrage.")

LIBELLES = {"annote": "Le scénario annoté", "note": "Note d'arbitrage",
            "aide": "Aide de jeu"}
FORMATS = [("pdf", "PDF"), ("html", "Lire en ligne"), ("epub", "EPUB")]

STYLE = """
.chapeau { font-size: 1.05rem; color: #46555f; margin: 0 0 2.2rem 0; max-width: 34rem; }
.scenario { border-top: 1px solid #c3cfd7; padding-top: 1.1rem; margin-top: 2rem; }
.scenario h2 { background: none; border: none; padding: 0; margin: 0 0 0.1rem 0;
               font-size: 1.45rem; }
.scenario .jeu-src { font-size: 0.78rem; text-transform: uppercase;
                     letter-spacing: 0.09em; color: #8aa4b2; margin: 0 0 0.9rem 0; }
.doc { display: flex; flex-wrap: wrap; align-items: baseline; gap: 0.5rem 0.9rem;
       padding: 0.6rem 0; border-bottom: 1px solid #eef2f5; }
.doc .quoi { font-weight: bold; color: #132c3c; min-width: 11rem; }
.doc .vol { font-size: 0.82rem; color: #8aa4b2; }
.doc .liens { margin-left: auto; font-size: 0.88rem; }
.doc .liens a { margin-left: 0.7rem; }
.vide { color: #8aa4b2; font-style: italic; }
.doc .liens a { color: #2d5f80; text-decoration: none;
                border-bottom: 1px solid #c3cfd7; padding-bottom: 1px; }
.doc .liens a:hover { color: #132c3c; border-bottom-color: #34566b; }
@media (prefers-color-scheme: dark) {
  .chapeau { color: #9fb0bb; }
  .scenario { border-top-color: #2c3a44; }
  .doc { border-bottom-color: #1d262c; }
  .doc .quoi { color: #cfe0ec; }
  .doc .liens a { color: #8fc4e8; border-bottom-color: #2c3a44; }
  .doc .liens a:hover { color: #cfe0ec; border-bottom-color: #4a6a80; }
}
"""


def documents():
    """Un dict par répertoire de src/, métadonnées + sorties réellement présentes."""
    trouves = []
    for d in sorted(SRC.glob("*/")):
        fs = sorted(d.glob("*.md"))
        if not fs:
            continue
        m = meta(fs)
        nom = d.name
        side = OUT / f"{nom}.meta.json"
        pages = None
        if side.is_file():
            try:
                pages = json.loads(side.read_text(encoding="utf-8")).get("pages")
            except (ValueError, OSError):
                pass
        sorties = [(ext, lib) for ext, lib in FORMATS if (OUT / f"{nom}.{ext}").is_file()]
        trouves.append({
            "nom": nom,
            "titre": m.get("title", nom),
            "soustitre": m.get("subtitle", ""),
            # `scenario` groupe les documents ; à défaut le titre fait l'affaire,
            # ce qui est juste tant qu'un scénario n'a qu'un document.
            "scenario": m.get("scenario") or m.get("title") or nom,
            "jeu": m.get("jeu", ""),
            "type": (m.get("type") or "").strip().lower(),
            "pages": pages,
            "sorties": sorties,
        })
    return trouves


def grouper(docs):
    groupes = {}
    for d in docs:
        groupes.setdefault(d["scenario"], []).append(d)
    # Les documents d'un scénario dans un ordre stable : la note se lit avant.
    ordre = {"annote": 0, "note": 1, "aide": 2}   # l'ordre de lecture réel
    for v in groupes.values():
        v.sort(key=lambda d: (ordre.get(d["type"], 9), d["titre"]))
    return sorted(groupes.items(), key=lambda kv: kv[0].lower())


def rendre(groupes):
    h = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f"<title>{escape(TITRE)}</title>",
         '<link rel="stylesheet" href="assets/screen.css">',
         '<link rel="stylesheet" href="assets/web.css">',
         f"<style>{STYLE}</style></head><body>",
         f"<h1>{escape(TITRE)}</h1>", '<div class="rule"></div>',
         f'<p class="chapeau">{escape(CHAPEAU)}</p>']

    if not groupes:
        h.append('<p class="vide">Aucun document publié pour l\'instant.</p>')

    for scenario, docs in groupes:
        jeu = next((d["jeu"] for d in docs if d["jeu"]), "")
        h.append('<div class="scenario">')
        h.append(f"<h2>{escape(scenario)}</h2>")
        if jeu:
            h.append(f'<p class="jeu-src">{escape(jeu)}</p>')
        for d in docs:
            quoi = LIBELLES.get(d["type"]) or d["soustitre"] or d["titre"]
            h.append('<div class="doc">')
            h.append(f'<span class="quoi">{escape(quoi)}</span>')
            if d["pages"]:
                h.append(f'<span class="vol">{d["pages"]} pages</span>')
            if d["sorties"]:
                liens = "".join(
                    f'<a href="{escape(d["nom"])}.{ext}">{escape(lib)}</a>'
                    for ext, lib in d["sorties"])
                h.append(f'<span class="liens">{liens}</span>')
            else:
                h.append('<span class="liens vide">pas encore compilé</span>')
            h.append("</div>")
        h.append("</div>")

    h.append("</body></html>")
    return "\n".join(h)


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    for f in ("screen.css", "web.css"):
        (OUT / "assets" / f).write_bytes((ASSETS / f).read_bytes())

    docs = documents()
    groupes = grouper(docs)
    (OUT / "index.html").write_text(rendre(groupes), encoding="utf-8")

    compiles = sum(1 for d in docs if d["sorties"])
    print(f"· index — {len(groupes)} scénario(s), {len(docs)} document(s), "
          f"{compiles} compilé(s)")
    for scenario, ds in groupes:
        for d in ds:
            etat = "/".join(e for e, _ in d["sorties"]) or "—"
            print(f"  {scenario} · {LIBELLES.get(d['type'], d['type'] or '?')} [{etat}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
