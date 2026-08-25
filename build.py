#!/usr/bin/env python3
"""
build.py — une source Markdown, trois sorties.

    python3 build.py note-bun-and-run

Produit dans out/ :
    <doc>.pdf     WeasyPrint, charte d'impression, police embarquée
    <doc>.html    page autonome pour GitHub Pages
    <doc>.epub    liseuse / tablette

Puis lance les contrôles du modèle et sort en code 1 si l'un échoue.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Sans ça, WeasyPrint horodate le PDF et deux compilations identiques donnent
# deux empreintes différentes — la CI ne peut plus rien vérifier.
os.environ.setdefault("SOURCE_DATE_EPOCH", "1700000000")

RACINE = Path(__file__).parent
SRC, OUT, ASSETS, FILTRES = RACINE / "src", RACINE / "out", RACINE / "assets", RACINE / "filters"

PANDOC_COMMUN = [
    "pandoc", "--from", "markdown+grid_tables+fenced_divs+bracketed_spans+definition_lists",
    "--lua-filter", str(FILTRES / "blocks.lua"),
]


def fragments(doc: str):
    d = SRC / doc
    if not d.is_dir():
        sys.exit(f"source introuvable : {d}")
    fs = sorted(d.glob("*.md"))
    if not fs:
        sys.exit(f"aucun fragment dans {d}")
    return fs


def meta(fs):
    """Le premier fragment porte l'en-tête YAML."""
    txt = fs[0].read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    d = {}
    if m:
        for ligne in m.group(1).splitlines():
            if ":" in ligne:
                k, v = ligne.split(":", 1)
                d[k.strip()] = v.strip().strip('"')
    return d


def est_note(m):
    """Le type du document est déclaré, pas deviné.

    Il l'a été un temps : le contrôle de volume reniflait le mot « note » dans
    le pied de page, si bien qu'un pied libellé autrement désactivait l'alarme
    des 15 pages en silence. `type:` tranche ; le reniflage reste en repli pour
    les documents écrits avant.
    """
    t = (m.get("type") or "").strip().lower()
    if t:
        return t.startswith("note")
    return "note" in m.get("pied", "").lower()


def unites(corps_html):
    """Les unités du livret, découpées sur leur div ouvrant."""
    return re.findall(r'<div class="unit">.*?(?=<div class="unit">|\Z)', corps_html, re.S)


def debordements(corps_html):
    """Une unité = une page, et c'est LE contrôle du livret.

    Chaque unité est rendue seule, avec la charte : si elle tient sur deux
    pages, le MJ tourne la page au milieu d'un point de consultation et perd
    le fil devant ses joueurs. On coupe le contenu, ou on scinde l'unité —
    jamais on ne laisse filer.

    Le contrôle vit ici plutôt que dans un script à côté parce qu'il doit
    tourner après *chaque* retouche : quatre lignes ajoutées à une unité qui
    tenait tout juste la font déborder, et le PDF complet ne le montre pas.
    """
    from weasyprint import HTML
    tmp = ASSETS / "_controle.html"
    trouvés = []
    try:
        for i, u in enumerate(unites(corps_html), 1):
            tmp.write_text('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
                           '<link rel="stylesheet" href="print.css"></head><body>'
                           f"{u}</body></html>", encoding="utf-8")
            n = len(HTML(filename=str(tmp)).render().pages)
            if n > 1:
                t = re.search(r"<h2[^>]*>(.*?)</h2>", u, re.S)
                titre = re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else "couverture"
                trouvés.append(f"l'unité {i} « {titre} » déborde sur {n} pages")
    finally:
        tmp.unlink(missing_ok=True)
    return trouvés


def html_fragment(fs):
    return subprocess.run(PANDOC_COMMUN + [*map(str, fs), "--to", "html5"],
                          capture_output=True, text=True, check=True).stdout


def pdf(doc, fs, m):
    from weasyprint import HTML
    corps = html_fragment(fs)
    # Le pied de page est injecté ici plutôt que codé dans la feuille : la
    # charte reste générique, le document apporte son titre.
    pied = m.get("pied", "")
    page = (f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            f'<title>{m.get("title","")}</title>'
            f'<link rel="stylesheet" href="print.css">'
            f'<style>@page {{ @bottom-left {{ content: "{pied}"; }} }}</style>'
            f"</head><body>{corps}</body></html>")
    tmp = ASSETS / "_build.html"
    tmp.write_text(page, encoding="utf-8")
    try:
        rendu = HTML(filename=str(tmp)).render()
        cible = OUT / f"{doc}.pdf"
        rendu.write_pdf(str(cible))
    finally:
        tmp.unlink(missing_ok=True)
    return rendu, cible


def site(doc, fs, m):
    css = OUT / "assets"
    css.mkdir(parents=True, exist_ok=True)
    for f in ("screen.css", "web.css"):
        shutil.copy(ASSETS / f, css / f)
    cible = OUT / f"{doc}.html"
    subprocess.run(PANDOC_COMMUN + [*map(str, fs), "--to", "html5", "--standalone",
                                    "--toc", "--toc-depth=2",
                                    "--css", "assets/screen.css",
                                    "--css", "assets/web.css",
                                    "--metadata", f"pagetitle={m.get('title','')}",
                                    "-o", str(cible)], check=True)
    return cible


def epub(doc, fs, m):
    cible = OUT / f"{doc}.epub"
    subprocess.run(PANDOC_COMMUN + [*map(str, fs), "--to", "epub3",
                                    "--css", str(ASSETS / "screen.css"),
                                    "--epub-chapter-level=2",
                                    "--metadata", f"title={m.get('title','')}",
                                    "--metadata", f"lang={m.get('lang','fr')}",
                                    "-o", str(cible)], check=True)
    return cible


# ------------------------------------------------------------------ contrôles

def bas_de_texte(page):
    """Bas de la dernière ligne de texte, en mm — hors boîtes de marge."""
    fonds = []

    def marche(b):
        if "Margin" in type(b).__name__:
            return
        if type(b).__name__ == "LineBox":
            fonds.append(b.position_y + b.height)
        for c in getattr(b, "children", []) or []:
            marche(c)

    for enfant in page._page_box.children:
        marche(enfant)
    return max(fonds) * 25.4 / 96 if fonds else None


def controles(rendu, corps_html, m):
    échecs, avertis = [], []
    pages = rendu.pages

    # 1 — volume (règle du chapitre de la note)
    if est_note(m) and len(pages) > 15:
        échecs.append(f"la note fait {len(pages)} pages : au-delà de 15, il y a de la recopie")

    # 2 — pages presque vides. Seulement pour la note : dans le livret, une
    #     unité qui remplit la moitié de sa page est normale et souvent
    #     souhaitable (mesuré de 49 % à 87 % sur un livret validé). Ce qui s'y
    #     mesure, c'est le débordement — contrôle 5.
    if est_note(m):
        for i, p in enumerate(pages, 1):
            b = bas_de_texte(p)
            if b is None:
                continue
            taux = (b - 12) / (284 - 12) * 100
            if taux < 20:
                échecs.append(f"p.{i} ne porte qu'une ou deux lignes ({taux:.0f} %)")
            elif taux < 62 and i not in (1, len(pages)):
                avertis.append(f"p.{i} remplie à {taux:.0f} % — fin de section ?")

    # 3 — renvois d'arbitrage dans le vide. Le livret, lui, renvoie à la note
    #     par un tiret (« on retient Y — A4 ») : ces numéros-là sont définis
    #     dans l'autre document, et les vérifier ici n'aurait aucun sens.
    définis = set(re.findall(r'class="lab">([ABC]\d)\s*—', corps_html))
    définis |= set(re.findall(r"<strong>([ABC]\d)</strong>", corps_html))
    définis |= set(re.findall(r"\b([ABC]\d) ·", corps_html))
    cités = set(re.findall(r"\(([ABC]\d)\)", corps_html))
    orphelins = (cités - définis) if est_note(m) else set()
    if orphelins:
        échecs.append(f"renvois vers un arbitrage inexistant : {', '.join(sorted(orphelins))}")

    # 4 — renvois à un numéro de page (interdit par le socle)
    if re.search(r"\bvoir (la )?page \d+", corps_html, re.I):
        échecs.append("renvoi à un numéro de page dans le corps du texte")

    # 5 — une unité = une page (livret seulement)
    if not est_note(m):
        n_unités = len(unites(corps_html))
        échecs += debordements(corps_html)
        if n_unités and n_unités != len(pages):
            avertis.append(f"{n_unités} unités pour {len(pages)} pages")

    return échecs, avertis


def main():
    doc = sys.argv[1] if len(sys.argv) > 1 else "note-bun-and-run"
    OUT.mkdir(exist_ok=True)
    fs = fragments(doc)
    m = meta(fs)
    print(f"· {doc} — {len(fs)} fragments")

    rendu, f_pdf = pdf(doc, fs, m)
    f_html = site(doc, fs, m)
    f_epub = epub(doc, fs, m)

    corps = html_fragment(fs)
    échecs, avertis = controles(rendu, corps, m)

    # Le nombre de pages ne se relit pas d'un PDF sans outil supplémentaire ;
    # on le dépose ici pour que scripts/index.py l'affiche sans dépendance.
    (OUT / f"{doc}.meta.json").write_text(json.dumps({
        "titre": m.get("title", ""), "type": m.get("type", ""),
        "scenario": m.get("scenario", ""), "pages": len(rendu.pages),
    }, ensure_ascii=False), encoding="utf-8")

    empreinte = hashlib.sha256(f_pdf.read_bytes()).hexdigest()[:16]
    print(f"  PDF   {len(rendu.pages):2d} p.  {f_pdf.stat().st_size // 1024:4d} Ko  sha {empreinte}")
    print(f"  HTML          {f_html.stat().st_size // 1024:4d} Ko")
    print(f"  EPUB          {f_epub.stat().st_size // 1024:4d} Ko")
    for a in avertis:
        print(f"  · {a}")
    for e in échecs:
        print(f"  ÉCHEC {e}")
    return 1 if échecs else 0


if __name__ == "__main__":
    sys.exit(main())
