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
import logging
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


def type_doc(m):
    """`note` · `aide` · `annote` — déclaré, jamais deviné.

    Il l'a été un temps : le contrôle de volume reniflait le mot « note » dans
    le pied de page, si bien qu'un pied libellé autrement désactivait l'alarme
    des 15 pages en silence. `type:` tranche ; le reniflage reste en repli pour
    les documents écrits avant.
    """
    t = (m.get("type") or "").strip().lower()
    if t.startswith("annot"):
        return "annote"
    if t.startswith("note"):
        return "note"
    if t.startswith("aide"):
        return "aide"
    return "note" if "note" in m.get("pied", "").lower() else "aide"


def est_note(m):
    return type_doc(m) == "note"


def coule(m):
    """Les documents dont les sections coulent, par opposition au livret.

    La note et le scénario annoté partagent le même régime de mise en page —
    `h2.sec` et `.card` — donc les mêmes contrôles de remplissage et de renvois.
    Ce qui les sépare est le volume : la note complète la source en huit à douze
    pages, l'annoté la **remplace** et pèse forcément davantage.
    """
    return type_doc(m) in ("note", "annote")


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
                trouvés.append(f"l'unité {i} « {titre} » tient sur {n} pages — elle a enflé")
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
    AVERTISSEMENTS.messages.clear()
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
    # Pas de `--toc` : le panneau de navigation est construit par `sommaire()`,
    # et le sommaire de pandoc ferait doublon en tête de document. Il ne se
    # voyait pas tant que les seuls documents concernés étaient des livrets —
    # pandoc ne remonte pas leurs titres, imbriqués à deux niveaux — mais la
    # note et l'annoté ont leurs `h2` à la racine, et il s'y affichait.
    # `title` vidé : le document porte déjà son titre dans le premier fragment
    # (c'est lui que le PDF compose). Sans ça, pandoc ajoute son propre
    # title-block et le titre apparaît deux fois sur le site. Le `<title>` de
    # l'onglet vient de `pagetitle`, qui n'alimente pas ce bloc.
    subprocess.run(PANDOC_COMMUN + [*map(str, fs), "--to", "html5", "--standalone",
                                    "--css", "assets/screen.css",
                                    "--css", "assets/web.css",
                                    "--metadata", "title=",
                                    "--metadata", f"pagetitle={m.get('title','')}",
                                    "-o", str(cible)], check=True)
    page = tableaux_defilants(cible.read_text(encoding="utf-8"))
    cible.write_text(sommaire(page, not coule(m)), encoding="utf-8")
    return cible


def tableaux_defilants(html):
    """Chaque tableau du site devient défilant sur petit écran.

    `web.css` définit `.table-scroll` depuis toujours — et rien ne la posait
    jamais sur un tableau. Sur un téléphone, une note d'arbitrage à dix-sept
    tableaux, dont un à cinq colonnes, débordait donc de la fenêtre.

    L'enveloppe se pose ici et non dans le filtre Lua : le PDF est composé
    depuis le même HTML, et une div de plus dans son flux est un risque de
    pagination pour un gain nul. `.table-scroll` n'existe que pour le site.
    """
    return re.sub(r"<table>(.*?)</table>",
                  lambda m: f'<div class="table-scroll"><table>{m.group(1)}</table></div>',
                  html, flags=re.S)


def sommaire(html, est_livret):
    """Le panneau de navigation du site — la seule façon d'atteindre une unité.

    Il n'existe pas sans nous : `--toc` est bien passé à pandoc, mais les titres
    d'unité sont imbriqués à deux niveaux (`.unit` > `.head`) et pandoc ne
    remonte pas des titres si profonds. Plutôt que de sortir le `<h2>` de son
    bandeau — ce qui casserait la charte d'impression pour un gain identique —
    la liste se construit ici, à partir du rendu.

    **Un panneau, et non un sommaire en tête de document.** Un sommaire en tête
    oblige à remonter tout le document à chaque changement d'unité : ce n'est
    pas de la navigation, c'est un aller-retour. Le panneau reste joignable d'un
    geste depuis n'importe quel point du document.

    Le mécanisme est `:target`, donc du CSS pur — pas une ligne de JavaScript.
    Le bouton flottant ouvre le panneau ; cliquer une entrée déplace la cible
    vers l'unité, ce qui le referme tout seul. Sur grand écran il est épinglé
    ouvert en colonne, et le bouton disparaît.

    C'est la contrepartie écran de « une unité = une page » : sur le papier, le
    MJ atteint son point de consultation en tournant une page ; sur un écran, il
    l'atteint ici.
    """
    entrées = []
    if est_livret:
        for u in unites(html):
            t = (re.search(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', u, re.S)
                 or re.search(r'<h1 id="([^"]+)"[^>]*>(.*?)</h1>', u, re.S))
            if not t:
                continue
            usage = re.search(r'<span class="use([^"]*)">(.*?)</span>', u, re.S)
            # une espace, pas rien : sinon « <span class="num">2</span>Lundi »
            # devient « 2Lundi »
            titre = " ".join(re.sub(r"<[^>]+>", " ", t.group(2)).split())
            cls = "use" + usage.group(1) if usage else ""
            lab = " ".join(re.sub(r"<[^>]+>", "", usage.group(2)).split()) if usage else ""
            # la couverture n'a pas d'étiquette d'usage : on lui donne quand
            # même un marqueur, sinon elle se désaligne de toutes les autres
            puce = f'<span class="{cls}">{lab}</span>' if lab else '<span class="use nul"></span>'
            entrées.append(f'<li><a href="#{t.group(1)}">{puce}{titre}</a></li>')
    else:
        # la note n'a pas d'unités : ses sections coulent, marquées par h2.sec
        # une entrée vers le haut du document : la note et l'annoté n'ont pas
        # d'unité de couverture qui la fournirait toute seule
        tête = re.search(r'<h1 id="([^"]+)"[^>]*>(.*?)</h1>', html, re.S)
        if tête:
            entrées.append(f'<li><a href="#{tête.group(1)}"><span class="use"></span>'
                           + " ".join(re.sub(r"<[^>]+>", " ", tête.group(2)).split())
                           + "</a></li>")
        # les attributs se lisent séparément : pandoc coupe la ligne entre eux
        # quand elle est longue, et « class="sec" id="…" » n'est alors plus
        # séparé par une simple espace
        for m in re.finditer(r"<h2\b([^>]*)>(.*?)</h2>", html, re.S):
            attrs, titre = m.group(1), m.group(2)
            ident = re.search(r'id="([^"]+)"', attrs)
            if "sec" not in attrs or not ident:
                continue
            entrées.append(f'<li><a href="#{ident.group(1)}"><span class="use"></span>'
                           + " ".join(re.sub(r"<[^>]+>", " ", titre).split()) + "</a></li>")
    if len(entrées) < 3:
        return html
    panneau = (
        '<a class="toc-open" href="#sommaire" aria-label="Ouvrir le sommaire">'
        "\u2630<span> Sommaire</span></a>"
        '<nav id="sommaire" class="toc" aria-label="Sommaire">'
        '<p class="toc-head">'
        '<a class="toc-home" href="index.html">\u2190 Tous les documents</a>'
        '<a class="toc-close" href="#_" aria-label="Fermer le sommaire">\u00d7</a></p>'
        "<ol>" + "".join(entrées) + "</ol></nav>")
    return html.replace("<body>", "<body>\n" + panneau, 1)


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

class _Avertissements(logging.Handler):
    """WeasyPrint signale les défauts de feuille de style en WARNING, et continue.

    Un sélecteur invalide, une propriété inconnue, une police introuvable : le
    PDF sort quand même, silencieusement dégradé. C'est ainsi qu'un commentaire
    CSS imbriqué a fait tomber le `@font-face` de la police régulière sans que
    personne le voie — le texte passait sur une police système, plus large, et
    les unités débordaient d'une ligne. Trois pages de trop sur un livret, et un
    rendu qui dépendait de la machine de build.

    Ici, un avertissement est un échec : c'est le seul contrôle qui protège la
    reproductibilité en amont du diff d'empreintes.
    """

    def __init__(self):
        super().__init__(level=logging.WARNING)
        self.messages = []

    def emit(self, record):
        self.messages.append(" ".join(record.getMessage().split())[:150])


AVERTISSEMENTS = _Avertissements()
logging.getLogger("weasyprint").addHandler(AVERTISSEMENTS)


def grappes_d_encarts(corps_html):
    """Les encarts se posent où ils servent, pas en pile à la fin de l'unité.

    Une unité se lit comme la scène se joue : ce qu'on doit savoir avant de
    parler, puis la descente par paliers avec chaque encart au point où sa
    matière tombe, puis la sortie. Une grappe de quatre encarts en pied de page
    est le signe qu'on a rédigé la description d'abord et rangé le reste après —
    à table, le MJ cherche alors le jet trois écrans plus bas que la phrase qui
    le déclenche.

    Le contrôle ne vaut que pour les unités qui **descendent par paliers** :
    une page de référence (la conclusion, un profil, une table de mécanique)
    n'a pas de progression, donc pas d'alternance à respecter.
    """
    trouvés = []
    for i, u in enumerate(unites(corps_html), 1):
        jalons = re.findall(r'<h3[^>]*>|<div class="(?:dire|jeu|mj|obj|warn)\b', u)
        if sum(1 for j in jalons if j.startswith("<h3")) < 2:
            continue
        seq = "".join("T" if j.startswith("<h3") else "E" for j in jalons)
        tête, pied = len(seq) - len(seq.lstrip("E")), len(seq) - len(seq.rstrip("E"))
        if tête > 2 or pied > 2:
            t = re.search(r"<h2[^>]*>(.*?)</h2>", u, re.S)
            titre = " ".join(re.sub(r"<[^>]+>", "", t.group(1)).split()) if t else f"unité {i}"
            trouvés.append(f"« {titre} » : {tête} encart(s) avant le premier palier, "
                           f"{pied} en pied — les poser où ils servent")
    return trouvés


PLAFOND_EXPLICATION = 3000  # signes — l'explication de texte tient sur une page, pas deux
PLAFOND_LIGNE = 110         # caractères — au-delà, la ligne est rédigée, pas notée
PLAFOND_REPLIQUE = 190      # une réplique se prononce telle quelle : plus de marge
MEDIANE_MAX = 60            # caractères — repère de facture, signalé sans faire échouer

# Marqueurs de phrase construite. Volontairement courts et sans ambiguïté :
# ce sont les tournures qui transforment une notation en récit rédigé. Les
# impératifs adressés au MJ (« Comptez-les devant eux ») n'en font pas partie,
# et c'est voulu — ce sont des consignes, pas de la narration.



def _divs(html, ouvrant):
    """Contenu de chaque div ouvert par ce motif, imbrication comptée."""
    res = []
    for m in re.finditer(ouvrant, html):
        prof = 1
        for t in re.finditer(r"</?div\b[^>]*>", html[m.end():]):
            prof += 1 if t.group(0).startswith("<div") else -1
            if prof == 0:
                res.append(html[m.end():m.end() + t.start()])
                break
    return res


def lignes_a_dire(corps_html):
    """Les lignes des blocs bleus, en (nombre de signes, réplique ?, texte)."""
    lignes = []
    for bloc in _divs(corps_html, r'<div class="say">'):
        for texte in re.findall(r"<div>\n(.*?)\n</div>", bloc, re.S):
            nu = " ".join(re.sub(r"<[^>]+>", " ", texte).split())
            if nu:
                # la réplique porte .q sur un span, à l'intérieur de la ligne
                lignes.append((len(nu), 'class="q"' in texte, nu))
    return lignes


def lignes_a_piocher(corps_html):
    """Une ligne à dire se note, elle ne se rédige pas.

    Le MJ pioche dans une pile de fragments et **fabrique** sa phrase ; il ne
    récite pas la nôtre. La forme qui le permet est nominale — un sujet, des
    adjectifs, une matière : « Terre battue, tassée, balayée de frais. » La
    forme qui l'en empêche est la phrase construite, avec son verbe conjugué
    et sa subordonnée : « Le sol est en terre battue, qui a été balayée
    récemment. » La seconde se lit à voix haute telle quelle, et c'est
    exactement le moment où le livret cesse de servir.

    **Le vrai critère est le style, pas la longueur** — une ligne courte mais
    rédigée est déjà de la narration prête à réciter. La longueur reste
    mesurée parce qu'elle attrape les débordements francs, mais c'est le taux
    de phrases construites qui fait échouer.

    Les répliques sont hors mesure : entre guillemets, elles sont faites pour
    être prononcées mot pour mot, et un PNJ parle avec des verbes. Les
    consignes adressées au MJ à l'impératif non plus ne sont pas visées.
    """
    lignes = lignes_a_dire(corps_html)
    if not lignes:
        return [], []
    échecs, avertis = [], []
    for n, repl, texte in lignes:
        if n > (PLAFOND_REPLIQUE if repl else PLAFOND_LIGNE):
            échecs.append(f"ligne à dire de {n} signes : « {texte[:60]}… »")
    ns = sorted(n for n, repl, _ in lignes if not repl)
    if ns:
        med = ns[len(ns) // 2] if len(ns) % 2 else (ns[len(ns) // 2 - 1] + ns[len(ns) // 2]) / 2
        if med > MEDIANE_MAX:
            avertis.append(f"médiane des lignes à dire : {med:.0f} signes "
                           f"(repère de facture : {MEDIANE_MAX})")
    return échecs, avertis


def explication(corps_html):
    """L'explication de texte en tête de note — sa longueur, et rien d'autre.

    Elle répond à la question qu'on se pose en refermant la source : *et
    maintenant, comment je mène ça ?* Elle ne redit donc rien de ce qu'on vient
    de lire — elle nomme l'espèce du scénario, le verbe des joueurs, les
    compteurs à tenir, et les points de rupture.

    **Le seul garde-fou automatisable est la longueur**, et il n'est pas
    décoratif : c'est exactement ce bloc qui, laissé libre, a produit une note
    de 37 pages sur « Bun & Run » en racontant l'intrigue au lieu de l'exposer.
    On ne raconte pas une histoire en une page ; on ne peut qu'en exposer la
    charpente. Le reste — ne rien redire de la source — se relit à la main.

    Mesuré : tout ce qui précède la première section, hors titre, sous-titre et
    table de routage.
    """
    i, j = corps_html.find("<body>"), corps_html.find('<h2 class="sec"')
    tete = corps_html[:j] if j > 0 else ""
    if i >= 0:
        tete = tete[i:]
    for cls in ("eyebrow", "subtitle", "rule"):
        tete = re.sub(rf'<div class="{cls}">.*?</div>', "", tete, flags=re.S)
    tete = re.sub(r"<h1.*?</h1>", "", tete, flags=re.S)
    tete = re.sub(r"<table>.*?</table>", "", tete, flags=re.S)
    n = len(" ".join(re.sub(r"<[^>]+>", " ", tete).split()))
    if n > PLAFOND_EXPLICATION:
        return [f"l'explication de texte fait {n} signes (max {PLAFOND_EXPLICATION}) — "
                "elle raconte au lieu d'exposer"]
    return []


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
    if type_doc(m) == "annote" and len(pages) > 24:
        échecs.append(f"le scénario annoté fait {len(pages)} pages : au-delà de 24, il ne remplace "
                      "plus la source, il la double")

    # 2 — pages presque vides. Seulement pour la note : dans le livret, une
    #     unité qui remplit la moitié de sa page est normale et souvent
    #     souhaitable (mesuré de 49 % à 87 % sur un livret validé). Ce qui s'y
    #     mesure, c'est le débordement — contrôle 5.
    if coule(m):
        for i, p in enumerate(pages, 1):
            b = bas_de_texte(p)
            if b is None:
                continue
            taux = (b - 12) / (284 - 12) * 100
            if taux < 20:
                échecs.append(f"p.{i} ne porte qu'une ou deux lignes ({taux:.0f} %)")
            elif taux < 62 and i not in (1, len(pages)):
                avertis.append(f"p.{i} remplie à {taux:.0f} % — fin de section ?")

    # 2 bis — l'explication de texte tient sur une page (note seulement)
    if est_note(m):
        échecs += explication(corps_html)

    # 3 — renvois d'arbitrage dans le vide. Le livret, lui, renvoie à la note
    #     par un tiret (« on retient Y — A4 ») : ces numéros-là sont définis
    #     dans l'autre document, et les vérifier ici n'aurait aucun sens.
    définis = set(re.findall(r'class="lab">([ABC]\d)\s*—', corps_html))
    définis |= set(re.findall(r"<strong>([ABC]\d)</strong>", corps_html))
    # les arbitrages de table sont groupés dans un seul bloc, chacun ouvert par
    # « **B1 — titre** » : c'est la forme que prescrit le chapitre de la note
    définis |= set(re.findall(r"<strong>([ABC]\d)\s*—", corps_html))
    définis |= set(re.findall(r"\b([ABC]\d) ·", corps_html))
    cités = set(re.findall(r"\(([ABC]\d)\)", corps_html))
    orphelins = (cités - définis) if coule(m) else set()
    if orphelins:
        échecs.append(f"renvois vers un arbitrage inexistant : {', '.join(sorted(orphelins))}")

    # 4 — renvois à un numéro de page (interdit par le socle)
    if re.search(r"\bvoir (la )?page \d+", corps_html, re.I):
        échecs.append("renvoi à un numéro de page dans le corps du texte")

    # 5 — la charte d'impression parse-t-elle sans faute ?
    #     Ne porte que sur print.css, la seule feuille que WeasyPrint rende :
    #     screen.css et web.css visent un navigateur et utilisent légitimement
    #     des règles qu'il ne connaît pas (@media, overflow-x).
    for a in dict.fromkeys(AVERTISSEMENTS.messages):
        échecs.append(f"charte d'impression : {a}")

    # 6 — les encarts se posent où ils servent (livret seulement)
    if not coule(m):
        avertis += grappes_d_encarts(corps_html)

    # 7 — les lignes à dire restent de la matière à piocher (livret seulement)
    if not coule(m):
        e, a = lignes_a_piocher(corps_html)
        échecs += e
        avertis += a

    # 8 — le budget de densité d'une unité (livret seulement).
    #     Avertissement, et non échec : les documents se mènent sur écran, où
    #     l'unité est une section et non une page. Ce qui reste dur, c'est
    #     « une unité = un point de consultation » ; la page A4 n'en est plus
    #     que la mesure — le seul budget automatique qui signale qu'une unité
    #     a enflé.
    if not coule(m):
        n_unités = len(unites(corps_html))
        avertis += debordements(corps_html)
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
