#!/usr/bin/env python3
"""
carnet-du-temps.py — le calendrier de mai 1932, qui se coche à la table.

    python3 scripts/carnet-du-temps.py

Produit out/carnet-du-temps.pdf : une page A4 à l'italienne, posée au
centre de la table pendant tout l'acte 1.

**Ce n'est pas une aide du MJ, c'est un objet des joueurs.** Le rituel de
fin de créneau se termine par *« Qui coche ? »*, et on attend que
quelqu'un le fasse : une case cochée par le MJ est une annonce, une case
cochée par un joueur est une décision.

**Un seul papier, qui est à la fois l'outil et un objet d'époque.** La
version précédente ne montrait que les huit jours du séjour : c'était
lisible, et ça ne ressemblait à aucun calendrier — or un calendrier se
présente par mois.

**Le mois est en six-jours, et c'est exact.** Depuis fin 1931, l'URSS vit
sous la *chestidnevka* : cinq jours de travail, un de repos, et les jours
chômés tombent aux **6, 12, 18, 24 et 30** de chaque mois. Plus de
dimanche, plus de semaine de sept jours. Un calendrier imprimé en 1932 a
donc six colonnes, pas sept, et les jours du six-jours n'ont pas de nom :
on dit le premier, le deuxième… Le 31 est hors cycle, travaillé.

    Le 6 mai tombe donc en jour de repos, au milieu de leur séjour.
    **Ça ne coûte aucun créneau** : le combinat tourne en continu, les
    équipes se relaient, les hauts-fourneaux ne s'arrêtent pas. C'est de
    la couleur — bureaux en effectif réduit, réfectoire plein à une autre
    heure, du monde dehors — et jamais une porte fermée.

**Les deux cases sont sur les trente et un jours**, pas seulement sur les
huit. N'en mettre que sur le séjour annoncerait qu'il s'arrête le 10, et
une feuille qui annonce quelque chose cesse d'être leur objet.

**Aucun mode d'emploi sur la feuille.** Ni sous-titre qui dit à quoi
servent les cases, ni légende « matin · après-midi » : un calendrier
d'époque n'explique pas comment on l'utilise, et le meneur le dit une
fois à la table. Il ne reste que le mois, le lieu et les jours.

**Et pas de bandeau d'échéance en pied.** Il portait le départ du train
et la date de remise du rapport : un calendrier de bureau ne dit pas ce
qui attend celui qui le regarde, et deux dates imprimées annoncent la fin
du séjour avant qu'elle arrive. Les deux se savent — elles sont sur leurs
ordres de mission — et se redisent en jeu.

**Rien n'y est coché d'avance, pas même le 3 mai.** La feuille arrive
vierge et le premier jour se barre à la table, avec eux, comme tous les
autres.

**Et pas de bande de déblaiement.** Elle nommait un chantier dont ils
n'ont pas encore entendu parler. Le déblaiement se dit en jeu, quand il
les concerne. Les 8 et 9 mai ne sont pas grisés non plus : les griser
annoncerait que ces jours sont déjà pris, or descendre doit rester leur
décision.

Deux contraintes de fabrication, parce qu'elle vit au centre d'une table :

    on écrit dessus        deux cases de 17 × 11 mm par jour, papier mat
                           et épais : la croix se trace au crayon et elle
                           reste cinq séances
    aucune information     rien que le MJ saurait et qu'eux ignorent
    du meneur

La répétition des en-têtes en haut et en bas, qui servait à ceux d'en
face, n'a plus lieu d'être : le quantième est écrit dans chaque case et
un chiffre se lit de tous les côtés.

Fond blanc : l'impression se fait sur papier déjà jauni.
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
    {"doc": "Le calendrier de mai 1932",
     "papier": "papier jauni", "grammage": "160 g", "ou": "maison", "stock": True,
     "format": "A4", "feuilles": 1,
     "note": "à l'italienne · **coché au crayon cinq séances**, d'où le grammage"},
]

REPOS = {6, 12, 18, 24, 30}
COLONNES = ["PREMIER", "DEUXIÈME", "TROISIÈME", "QUATRIÈME", "CINQUIÈME", "REPOS"]


def case(q):
    """Un jour : son quantième, et deux cases à cocher."""
    cls = " repos" if q in REPOS else ""
    mention = '<span class="mention">repos</span>' if q in REPOS else ""
    return (f'<div class="jour{cls}"><span class="q">{q}</span>{mention}'
            f'<div class="demis"><div class="d"></div><div class="d"></div></div></div>')


grille = "".join(
    f'<div class="rang">{"".join(case(q) for q in range(d, d + 6))}</div>'
    for d in range(1, 31, 6))

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}

@page {{ size: A4 landscape; margin: 10mm 14mm; }}
*, *::before, *::after {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: #241f1a; }}

h1 {{ font-size: 17pt; font-weight: bold; letter-spacing: .3em; text-align: center;
      margin: 0; }}
.sous {{ text-align: center; font-size: 8.4pt; color: #6b6356; letter-spacing: .14em;
         margin: .8mm 0 3.4mm; }}

/* ── en-tête des six colonnes : les jours du six-jours n'ont pas de nom ── */
.tete {{ display: flex; border-bottom: 1px solid #4a443c; padding-bottom: 1.4mm;
         margin-bottom: 1.8mm; }}
.tete div {{ flex: 1; text-align: center; font-size: 6.6pt; letter-spacing: .16em;
             color: #8a8276; }}
.tete div:last-child {{ color: #4a443c; }}

.rang {{ display: flex; }}
.jour {{ flex: 1; margin: 0 1mm 2mm; padding: 1.2mm 1.4mm 1.4mm;
         border: .9px solid #4a443c; background: #fff; }}
.jour .q {{ font-size: 13pt; font-weight: bold; line-height: 1; }}
.jour .mention {{ font-size: 5.8pt; letter-spacing: .12em; color: #8a8276;
                  margin-left: 1.6mm; }}
.jour.repos {{ border-style: dashed; }}

.demis {{ display: flex; gap: 1.4mm; margin-top: 1.4mm; }}
.demis .d {{ flex: 1; height: 11mm; border: .7px solid #8a8276; }}

</style></head><body>

<h1>МАЙ 1932</h1>
<div class="sous">MAGNITOGORSK</div>

<div class="tete">{"".join(f"<div>{c}</div>" for c in COLONNES)}</div>
{grille}
<div class="rang">{case(31)}<div class="jour vide" style="border:none"></div>
<div class="jour vide" style="border:none"></div><div class="jour vide" style="border:none"></div>
<div class="jour vide" style="border:none"></div><div class="jour vide" style="border:none"></div></div>

</body></html>"""

cible = RACINE / "out" / "carnet-du-temps.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
