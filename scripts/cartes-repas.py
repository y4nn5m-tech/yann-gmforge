#!/usr/bin/env python3
"""
cartes-repas.py — les cinq cartes que Kassym leur remet le premier jour.

    python3 scripts/cartes-repas.py

Produit out/cartes-repas.pdf : une A4, six cartons de 90 × 64 mm à
découper — cinq pour les joueurs, un de rechange.

## Ce qu'elles font, et elles font deux choses

**Elles créent un choix social qui se repose chaque jour.** Ce n'est pas
la carte de tout le monde : c'est une carte de cadres en mission, et
elle porte `SERVICE HORS FILE`. Passer devant trois cents ouvriers qui
attendent, ou faire la queue avec eux. **Personne ne commente, dans les
deux cas** — mais la salle commune du soir s'en souvient.

**Et elles rendent le temps volé matériel.** Elles portent *valable du 3
au 10 mai 1932*. Au premier repas d'après la mine, ils la tendent,
l'agent la regarde et **il la refuse** : il la repousse du doigt et
appelle le suivant. Rien à expliquer — `50-temporalite.md`.

C'est Kassym qui les remet, avec les clés des chambres : on les lui a
confiées pour eux. *« Vous, vous n'attendez pas. »*

## Ce qui n'y figure pas

**Aucun réfectoire nommé.** Le rapport de l'empoisonnement parle des
réfectoires B et C, et les victimes y sont reliées à tort : une carte
qui en désignerait un enverrait les joueurs sur la fausse piste que le
dossier construit déjà. Une carte de cadre vaut partout, ce qui est à la
fois vrai et neutre.

**Et le nom reste à écrire.** Un bureau d'approvisionnement remplit ses
cartes à la main, et une ligne portée au stylo vaut mieux qu'un champ
composé. La qualité est pour la même raison *« en mission — Moscou »* et
non *« envoyé en mission »* : le genre des personnages se choisit à la
table, et un participe accordé d'avance en condamne la moitié.

> **Un repas par jour**, et c'est la règle commune — la carte ne donne
> pas plus à manger, elle donne de ne pas attendre.

**Pas le papier jauni des dossiers.** Les rapports ont vieilli en
archive ; cette carte a été délivrée il y a deux jours, elle vit dans
une poche et se tend chaque jour. Sur le même papier que la pile, elle
cesse d'être un objet distinct. Et la teinte dit la catégorie : les
cartes de rationnement se distinguaient couramment par la couleur selon
le groupe d'ayants droit. Le papier est déclaré dans `PAPIER` ci-dessus
— `python3 scripts/papiers.py` en fait la liste de courses.

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
    {"doc": "Les cartes de repas",
     "papier": "bristol vert pâle", "grammage": "250 g", "ou": "imprimerie",
     "format": "A4", "feuilles": 1,
     "note": "six cartons à découper · **la teinte dit la catégorie**, c'est le seul document où la couleur porte du sens"},
]

T = "#23252a"
R = "#8c2b22"   # le filet de priorité, et le cachet

NOMBRE = 6      # cinq joueurs, un de rechange


def cachet(i):
    """Le cachet du service, mal appuyé comme tous les cachets."""
    return f"""
<svg class="cachet" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
 <defs><filter id="c{i}" x="-20%" y="-20%" width="140%" height="140%">
   <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3"
                 seed="{7 + i * 5}" result="b"/>
   <feDisplacementMap in="SourceGraphic" in2="b" scale="1.1"
                      xChannelSelector="R" yChannelSelector="G" result="d"/>
   <feTurbulence type="fractalNoise" baseFrequency="0.1" numOctaves="2"
                 seed="{31 + i * 3}" result="t"/>
   <feColorMatrix in="t" type="matrix"
     values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.7 0 0 0 -0.32" result="m"/>
   <feComposite in="d" in2="m" operator="out"/>
 </filter>
 <path id="arc{i}" d="M 16 60 A 44 44 0 0 1 104 60" fill="none"/>
 <path id="bas{i}" d="M 20 60 A 40 40 0 0 0 100 60" fill="none"/>
 </defs>
 <g filter="url(#c{i})" fill="{R}">
  <circle cx="60" cy="60" r="52" fill="none" stroke="{R}" stroke-width="3.4"/>
  <circle cx="60" cy="60" r="44" fill="none" stroke="{R}" stroke-width="1.4"/>
  <text font-size="13" letter-spacing="1.1" font-family="PT" font-weight="bold">
    <textPath href="#arc{i}" startOffset="50%" text-anchor="middle">ОТДЕЛ СНАБЖЕНИЯ</textPath>
  </text>
  <text font-size="10.5" letter-spacing="1.2" font-family="PT">
    <textPath href="#bas{i}" startOffset="50%" text-anchor="middle">МАГНИТОГОРСК</textPath>
  </text>
  <text x="60" y="66" font-size="15" letter-spacing="1" text-anchor="middle"
        font-family="PT" font-weight="bold">№ 4</text>
 </g>
</svg>"""


def carte(i):
    return f"""
<div class="c">
  <div class="tete">
    <div class="org">УПРАВЛЕНИЕ МАГНИТОГОРСКОГО КОМБИНАТА</div>
    <div class="serv">ОТДЕЛ СНАБЖЕНИЯ · SERVICE DE L'APPROVISIONNEMENT</div>
  </div>

  <div class="titre">CARTE DE REPAS</div>

  <div class="ligne"><span class="lb">N°</span><span class="tr"></span></div>
  <div class="ligne"><span class="lb">Délivrée à</span><span class="tr"></span></div>
  <div class="ligne qual"><span class="lb">Qualité</span>
    <span class="va">en mission — Moscou</span></div>

  <div class="prio">SERVICE HORS FILE</div>

  <div class="val">VALABLE DU 3 AU 10 MAI 1932</div>

  <div class="pied">Un repas par jour. Non cessible.<br>
    À présenter à chaque service.</div>
  {cachet(i)}
</div>"""


HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A4; margin: 12mm 10mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: {T};
        display: flex; flex-wrap: wrap; gap: 6mm 8mm; }}

.c {{ width: 90mm; height: 64mm; border: .8px solid {T}; padding: 3.4mm 4mm;
      position: relative; overflow: hidden; }}

.tete {{ text-align: center; border-bottom: .5px solid #9aa0a8; padding-bottom: 1.4mm; }}
.org {{ font-size: 6.4pt; font-weight: bold; letter-spacing: .09em; }}
.serv {{ font-size: 5.4pt; letter-spacing: .07em; color: #5c626a; margin-top: .4mm; }}

.titre {{ text-align: center; font-size: 11.5pt; font-weight: bold;
          letter-spacing: .22em; margin: 2.4mm 0 2.6mm; }}

.ligne {{ display: flex; align-items: baseline; font-size: 7.2pt; margin-bottom: 2.4mm;
          letter-spacing: .04em; }}
.lb {{ flex: none; color: #5c626a; margin-right: 2mm; }}
.tr {{ flex: 1; border-bottom: .5px solid #7e858d; height: 3.4mm; }}
.qual .va {{ font-size: 7pt; }}

/* La mention qui fait tout le choix social de la file. */
.prio {{ display: inline-block; border: 1.1px solid {R}; color: {R};
         font-size: 7.4pt; font-weight: bold; letter-spacing: .16em;
         padding: .8mm 2.4mm; margin-top: .6mm; }}

.val {{ font-size: 8.6pt; font-weight: bold; letter-spacing: .1em;
        margin-top: 2.6mm; }}

.pied {{ position: absolute; left: 4mm; bottom: 3mm; width: 54mm; font-size: 5.6pt;
         line-height: 1.35; color: #5c626a; letter-spacing: .04em; }}

svg.cachet {{ position: absolute; right: 3.4mm; bottom: 2.4mm;
              width: 24mm; height: 24mm; opacity: .78;
              mix-blend-mode: multiply; transform: rotate(-7deg); }}
</style></head><body>
{"".join(carte(i) for i in range(NOMBRE))}
</body></html>"""

cible = RACINE / "out" / "cartes-repas.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
