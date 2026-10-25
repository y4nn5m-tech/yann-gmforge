#!/usr/bin/env python3
"""
aides-acte2.py — les cinq cartons qu'on lit à la bougie.

    python3 scripts/aides-acte2.py

Produit out/aides-acte2.pdf : cinq pages A5 à l'italienne, à découper et
**poser à plat** côte à côte. Trois feuilles A4 à l'imposition deux par
page, ou cinq A4 si tu les veux plus grandes.

## Pourquoi un accessoire et pas un livrable

**L'acte 2 se joue dans le noir, à la bougie** — `100-acte2-cadrage.md`
—, et c'est le moment où tous les accessoires quittent la table :
rapports, plan, carnet, cartes de repas sont illisibles et appartiennent
tous à l'acte 1. **Ce qui reste doit se lire sans être feuilleté.**

La charte du dépôt est réglée pour une lecture normale : son corps de
texte est juste à la bougie, et `assets/print.css` ne se modifie pas
pour un cas particulier. D'où le régime accessoire — corps de 13 à 26
points, noir pur sur blanc, aucun filet fin, aucun gris sous 40 %.

> **Tester la lisibilité à la bougie avant d'imprimer les cinq.** Une
> seule page, la vraie bougie, la vraie distance. Cinq minutes.

## Ce que chaque carton porte, et pourquoi lui

    les onze disparus   **quatre sont la famille de Kassym**, et il en
                        perd six en tout. C'est le seul carton qu'on
                        consulte pour un nom, en plein milieu d'une
                        scène
    le fil              la descente est linéaire et la mémoire ne l'est
                        pas. Les deux branches de la strate 1, les sept
                        temps de la strate 2, l'enchaînement de la 3
    les effets          **ils se saupoudrent, donc ils s'oublient.**
                        Avec des cases, parce que ce qui compte est de
                        ne pas répéter le même
    la créature         trois comportements et trois issues, à trancher
                        en une seconde pendant que la table attend
    l'horreur           **trois jets dans toute la campagne**, et le
                        troisième est dans l'acte 3. Les avoir sous les
                        yeux évite d'en inventer un quatrième

Fond blanc : l'impression se fait sur du blanc ordinaire.
Rendu par Chrome — voir scripts/rendu.py.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

# Sur quoi ça s'imprime, et où. `python3 scripts/papiers.py` en fait la
# liste de courses — il lit cette constante sans exécuter le script.
PAPIER = [
    {"doc": "Les cinq aides MJ de l'acte 2",
     "papier": "papier blanc", "grammage": "80 g", "ou": "maison",
     "format": "A4", "feuilles": 3,
     "note": "cinq A5 à l'italienne, deux par feuille · **le blanc est le bon "
             "choix** : elles se lisent à la bougie"},
]

N = "#000"

# **Le réglage à toucher après l'essai à la bougie**, et le seul : tous
# les autres corps en découlent. 13.4 pt sur A5 équivaut à 19 pt sur une
# A4 — si c'est encore trop petit, monter ici et vérifier qu'aucun
# carton ne passe à deux pages.
CORPS = 13.4


def carton(titre, corps, numero):
    return f"""
<div class="c">
  <div class="t">{titre}<span class="n">{numero}/5</span></div>
  {corps}
</div>"""


# ══════════════════════════════════════════════════════════════════
#  1 — les onze disparus
# ══════════════════════════════════════════════════════════════════

DISPARUS = [
    ("1", "Yaroslava Ibragimova", "", "morte de ses blessures, au campement"),
    ("2", "Baris Volkoff", "père", "mort, éboulement — sous les débris, La corde"),
    ("3", "Andreï Volkoff", "oncle", "mort, éboulement — plus profond, La corde"),
    ("4", "Vassilisa Korolyova", "", "morte, chute — au fond du puits"),
    ("5", "Akim Korolyoff", "", "VIVANT, jambe cassée, fou de douleur"),
    ("6", "Dorofei Sokoloff", "", "infarctus en voyant la créature"),
    ("7", "Anatoli Polyakoff", "", "pris par la larve — le corps à la corniche"),
    ("8", "Sacha Savchenko", "", "chute, six mètres sous la corniche"),
    ("9", "Anushka Alekseeva", "", "tranchée en deux par un tube"),
    ("10", "Aksinia Volkova", "sœur", "dupliquée — elle s'assassine elle-même"),
    ("11", "Dmitri Volkoff", "frère", "VIVANT, fou, connecté aux créatures"),
]


def disparus():
    lignes = "".join(
        f'<tr class="{"k" if lien else ""}"><td class="num">{n}</td>'
        f'<td class="nom">{nom}</td><td class="lien">{lien}</td>'
        f'<td class="sort">{sort}</td></tr>'
        for n, nom, lien, sort in DISPARUS)
    return f"""
<table class="disp">
  <colgroup><col style="width:6%"><col style="width:30%">
  <col style="width:13%"><col style="width:51%"></colgroup>
  {lignes}
</table>
<div class="pied"><b>Plus deux</b> — sa mère et un frère, morts dans l'effondrement.
Corps non identifiables. <b>Kassym perd six personnes dans cet acte.</b></div>"""


# ══════════════════════════════════════════════════════════════════
#  2 — le fil de la descente
# ══════════════════════════════════════════════════════════════════

FIL = """
<div class="st">STRATE 1 — bougie 1</div>
<div class="bl"><b>Le campement</b> — deux morts, la traînée de sang, les affaires.
<b>Deux tunnels. Ne pas orienter.</b></div>
<div class="br">
  <div><b>A · pas de sang</b> — La corde <i>(Baris, Andreï)</i> → Akim vivant.
    <b>Cul-de-sac</b>, mais tout l'enjeu humain</div>
  <div><b>B · la traînée</b> — La peinture → La corniche <i>(Anatoli)</i> →
    La porte → Le conduit</div>
</div>

<div class="st">STRATE 2 — bougie 2 · intercaler, jamais enchaîner</div>
<div class="sept">
  <span>1 · Tubes — l'ouïe</span><span>2 · Le bassin, Aksinia</span>
  <span>3 · Mœbius, <b>dont le duplicata</b></span><span>4 · Tubes — la vue</span>
  <span>5 · Un effet de plus</span><span>6 · Tubes — le toucher <i>(Anushka)</i></span>
  <span>7 · <b>L'attaque du double</b></span>
</div>

<div class="st">STRATE 3 — bougie 3</div>
<div class="bl">La Grande Galerie → <b>point de non-retour</b>, il ne s'annonce pas →
Dmitri → la première larve → le Nexus → <b>l'alerte, inévitable</b> → acte 3</div>"""


# ══════════════════════════════════════════════════════════════════
#  3 — les effets à saupoudrer
# ══════════════════════════════════════════════════════════════════

EFFETS = [
    ("Tubes 1 — l'ouïe", "vrombissement dans la paroi. <b>Leur couper la parole</b>, "
     "pour de vrai, quelques secondes"),
    ("Tubes 2 — la vue", "un tuyau de pierre noire apparaît <b>par segments d'un mètre</b>, "
     "traverse, disparaît de même"),
    ("Tubes 3 — le toucher", "le corps d'Anushka, tranché net. S'ils s'attardent : "
     "<b>la seule mort possible de la strate</b>"),
    ("Déphasage", "<b>dire à un joueur de changer de place</b> sans prévenir les autres. "
     "Il ne s'en aperçoit pas"),
    ("Limite invisible", "<b>faire éteindre une frontale.</b> La lumière est stoppée net, "
     "il faut contourner"),
    ("Écho temporel", "<b>reprendre mot pour mot</b> une réplique dite une heure plus tôt"),
    ("Duplicata", "une lanterne identique à la leur, chocs compris, <b>réservoir plein</b>. "
     "<b>Avant l'attaque</b>"),
]


def effets():
    return "".join(
        f'<div class="ef"><span class="box"></span>'
        f'<span class="q"><b>{t}</b> — {d}</span></div>' for t, d in EFFETS)


# ══════════════════════════════════════════════════════════════════
#  4 — la créature
# ══════════════════════════════════════════════════════════════════

CREATURE = """
<div class="bl grand"><b>Ils ne sont pas des ennemis. Ils ne sont rien du tout.</b></div>

<div class="cas"><b>ELLE IGNORE</b> — elle vient réparer la rigole et repart.
<b>Elle passe au travers</b> de qui reste sur son chemin. Rien ne se passe,
et c'est la scène la plus inquiétante de l'acte</div>

<div class="cas"><b>ELLE NETTOIE</b> — couverts de substance, ils se font nettoyer
au pseudopode : <b>sans danger</b>. Dmitri, lui, y passe — pseudopode dans la gorge,
mort en dix secondes <b>devant son frère</b></div>

<div class="cas av"><b>ILS AGRESSENT</b> — un pseudopode les projette en l'air,
<b>figés, muscles bloqués</b>. Puis, au choix :</div>
<div class="iss">
  <div><b>projeté à cent mètres</b> — gravement blessé ou tué</div>
  <div><b>démembré</b> par des effets gravitationnels — lent, atroce,
    <b>les autres figés et impuissants</b></div>
  <div><b>tout le monde figé</b>, elle s'éloigne. <b>Le choix qui sert
    quand le groupe tient à Kassym</b></div>
</div>"""


# ══════════════════════════════════════════════════════════════════
#  5 — les jets d'horreur
# ══════════════════════════════════════════════════════════════════

HORREUR = """
<div class="bl grand"><b>Trois dans toute la campagne.</b> Ne pas en inventer un quatrième.</div>

<div class="jet"><span class="num">1</span><span class="q"><b>La peinture</b>
<i>— strate 1, branche B</i><br>Plane, et pourtant en trois dimensions ou plus.
<b>Facultatif : il faut choisir de la regarder vraiment.</b><br>
Échec → troubles de l'équilibre, le monde paraît plat</span></div>

<div class="jet"><span class="num">2</span><span class="q"><b>Le corps d'Anatoli</b>
<i>— strate 1, la corniche</i><br>Os broyés, peau corrodée, le sang sorti par tous les
orifices <b>comme s'il avait été pressé</b>.<br>
<b>Immédiat, rien à chercher.</b> Ausculter le corps = un jet de plus</span></div>

<div class="jet"><span class="num">3</span><span class="q"><b>La vision</b>
<i>— acte 3, pas ici</i><br>Salle à la Escher. Leur peau devient chitineuse, ils voient
dans toutes les directions.<br>
Échec → ils s'arrachent la peau des bras</span></div>"""


HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A5 landscape; margin: 8mm 9mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
/* Tout est noir pur : à la bougie, un gris à 60 % disparaît. */
body {{ font-family: PT, serif; color: {N}; font-size: {CORPS}pt; line-height: 1.38; }}

.c {{ height: 100%; }}
.c + .c {{ break-before: page; }}
.t {{ font-size: {CORPS * 1.34:.1f}pt; font-weight: bold; letter-spacing: .1em;
      border-bottom: 2px solid {N}; padding-bottom: 1.4mm; margin-bottom: 3mm;
      display: flex; justify-content: space-between; align-items: baseline; }}
.t .n {{ font-size: 10pt; letter-spacing: .06em; font-weight: normal; }}

.bl {{ margin-bottom: 2.6mm; }}
.bl.grand {{ font-size: {CORPS * 1.16:.1f}pt; text-align: center; margin-bottom: 3.4mm; }}
.st {{ font-size: {CORPS * .9:.1f}pt; font-weight: bold; letter-spacing: .14em;
       border-bottom: 1px solid {N}; margin: 3mm 0 1.8mm; padding-bottom: .8mm; }}
.st:first-child {{ margin-top: 0; }}

/* ── 1 · les disparus ──────────────────────────────────────── */
table.disp {{ width: 100%; border-collapse: collapse; font-size: {CORPS * .93:.1f}pt; }}
table.disp td {{ padding: 1.1mm 1.4mm; border-bottom: .7px solid #000; }}
table.disp .num {{ text-align: right; }}
table.disp .nom {{ font-weight: bold; }}
table.disp .lien {{ font-style: italic; }}
table.disp tr.k td {{ background: #e4e4e4; }}
table.disp tr.k .nom::after {{ content: " ●"; }}
.pied {{ margin-top: 3mm; font-size: {CORPS * .9:.1f}pt; }}

/* ── 2 · le fil ────────────────────────────────────────────── */
.br {{ display: flex; gap: 3mm; }}
.br > div {{ flex: 1; border: 1.2px solid {N}; padding: 1.8mm 2.2mm; }}
.sept {{ display: flex; flex-wrap: wrap; gap: 1.4mm 2mm; }}
.sept span {{ border: 1px solid {N}; padding: 1mm 2mm; }}

/* ── 3 · les effets ────────────────────────────────────────── */
.ef {{ display: flex; align-items: flex-start; gap: 2.6mm; margin-bottom: 2.4mm; }}
.ef .box {{ flex: none; width: 5mm; height: 5mm; border: 1.6px solid {N};
            margin-top: .4mm; }}
.ef .q {{ flex: 1; }}

/* ── 4 · la créature ───────────────────────────────────────── */
.cas {{ border-left: 3px solid {N}; padding: 1.4mm 0 1.4mm 2.6mm;
        margin-bottom: 2.4mm; }}
.cas.av {{ margin-bottom: 1.4mm; }}
.iss {{ margin-left: 5mm; }}
.iss > div {{ border: 1px solid {N}; padding: 1.2mm 2.2mm; margin-bottom: 1.4mm; }}

/* ── 5 · l'horreur ─────────────────────────────────────────── */
.jet {{ display: flex; gap: 3mm; align-items: flex-start; margin-bottom: 3mm;
        border-top: 1px solid {N}; padding-top: 2mm; }}
.jet .num {{ flex: none; font-size: {CORPS * 1.94:.1f}pt; font-weight: bold; line-height: 1;
             width: 9mm; }}
.jet .q {{ flex: 1; }}
</style></head><body>
{carton("LES ONZE DISPARUS", disparus(), 1)}
{carton("LE FIL DE LA DESCENTE", FIL, 2)}
{carton("LES EFFETS À SAUPOUDRER", effets(), 3)}
{carton("LA CRÉATURE", CREATURE, 4)}
{carton("LES JETS D'HORREUR", HORREUR, 5)}
</body></html>"""

cible = RACINE / "out" / "aides-acte2.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
