#!/usr/bin/env python3
"""
cartes-sorts.py — les sorts des prétirés, en cartes à découper.

    python3 scripts/cartes-sorts.py

Produit out/cartes-sorts.pdf : une carte par sort, six par page A4, avec
le texte complet du Guide du joueur. Les fiches de prétirés ne donnent
qu'un résumé d'une ligne ; il fallait ouvrir le livre à chaque fois.

Hors de build.py à dessein : ce n'est pas un document de la collection
(ni couverture, ni charte, ni contrôles), c'est un accessoire de table.
La police embarquée et SOURCE_DATE_EPOCH sont repris de la chaîne, pour
que le PDF reste reproductible au bit près.
"""
import os
import sys
from pathlib import Path

os.environ.setdefault("SOURCE_DATE_EPOCH", "1700000000")

RACINE = Path(__file__).resolve().parent.parent
ASSETS = RACINE / "assets"
OUT = RACINE / "out"

# Les dix sorts des huit prétirés du quickstart, texte du Guide du joueur V5.
SORTS = [
    ("Armure de mage", "Rang 1, magicien", "10 rounds", "personnelle", "Creeg",
     "Une force magique invisible protège vos organes vitaux. Votre classe d'armure "
     "passe à <b>14</b> (ou à <b>18</b> en cas de réussite critique au test d'incantation) "
     "pendant la durée du sort."),
    ("Projectile magique", "Rang 1, magicien", "instantanée", "longue", "Creeg · Zaldini",
     "Vous bénéficiez de <b>l'avantage</b> à votre test d'incantation de ce sort.<br>"
     "Un rayon de force lumineux jaillit de votre main ouverte et inflige "
     "<b>1d4 dégâts</b> à une cible."),
    ("Détection de la magie", "Rang 1, magicien", "concentration", "intermédiaire", "Creeg",
     "Vous sentez la présence de la magie à portée intermédiaire pendant la durée du sort. "
     "Si vous vous concentrez pendant <b>deux rounds</b>, vous en discernez les propriétés "
     "générales. Les barrières pleines bloquent l'effet du sort."),
    ("Sommeil", "Rang 1, magicien", "instantanée", "intermédiaire", "Creeg",
     "Vous déployez une aura de léthargie qui remplit un cube de taille intermédiaire "
     "s'étendant à partir de vous. Les créatures vivantes situées à l'intérieur tombent "
     "dans un profond sommeil <b>si elles sont de niveau 2 ou moins</b>.<br>"
     "Les secouer vigoureusement ou les blesser permet de les réveiller."),
    ("Mains brûlantes", "Rang 1, magicien", "instantanée", "courte", "Zaldini",
     "Vous écartez les doigts en mettant vos pouces en contact pour libérer un cercle de "
     "flammes qui se répandent en rugissant à portée courte tout autour de vous.<br>"
     "Les créatures situées à portée subissent <b>1d6 dégâts</b>, et les objets "
     "combustibles prennent feu."),
    ("Charme-personne", "Rang 1, magicien", "1d8 jours", "intermédiaire", "Zaldini",
     "Vous séduisez par magie un humanoïde <b>de niveau 2 ou moins</b> situé à portée, "
     "et qui vous considère comme un ami pendant la durée du sort.<br>"
     "Le sort s'achève si vous ou vos alliés faites quoi que ce soit pour lui nuire et "
     "qu'il le remarque. Quand l'effet s'achève, <b>la cible sait que vous l'avez "
     "ensorcelée</b>."),
    ("Guérison des blessures", "Rang 1, prêtre", "instantanée", "courte", "Elbin · Iraga",
     "Votre contact restaure le flux vital. Lancez un nombre de <b>d6</b> égal à "
     "<b>1 + la moitié de votre niveau</b> (arrondie à l'inférieur). Une cible que vous "
     "touchez regagne un nombre de PV équivalent."),
    ("Bouclier de la foi", "Rang 1, prêtre", "5 rounds", "personnelle", "Elbin",
     "Une force protectrice issue de votre conviction religieuse vous entoure. Vous recevez "
     "un bonus de <b>+2 à la classe d'armure</b> pour toute la durée."),
    ("Arme sacrée", "Rang 1, prêtre", "5 rounds", "courte", "Iraga",
     "Vous transmettez une bénédiction à une arme que vous touchez. Celle-ci devient "
     "magique et bénéficie d'un bonus de <b>+1 aux jets d'attaque et de dégâts</b> "
     "pendant la durée."),
    ("Renvoi des morts-vivants", "Rang 1, prêtre", "instantanée", "intermédiaire",
     "Elbin · Iraga",
     "Vous repoussez les morts-vivants et les forcez à fuir. <b>Vous devez brandir un "
     "symbole sacré</b> pour lancer ce sort.<br>"
     "Les morts-vivants à portée intermédiaire effectuent un test de <b>CHA</b> contre le "
     "résultat de votre test d'incantation. En cas d'échec, ils vous fuient pendant "
     "<b>5 rounds</b>. Si l'échec est de <b>10 points ou plus</b> et que la créature est "
     "de niveau inférieur ou égal au vôtre, elle est <b>détruite</b>."),
]

REGLE = """<div class="carte regle">
<div class="titre">Lancer un sort</div>
<div class="meta">Le rappel, pour tout le monde</div>
<div class="corps">
<b>Test d'incantation :</b> 1d20 + modificateur, contre un <b>ND de 10 + le rang du sort</b>.<br>
Magicien : <b>INT</b> · Prêtre : <b>SAG</b>.<br><br>
<b>Réussite</b> — le sort agit, <b>et tu le gardes</b>. Tu pourras le relancer.<br>
<b>Échec</b> — rien ne se passe, et <b>tu perds ce sort jusqu'au prochain repos complet</b>.
Tes autres sorts restent.<br>
<b>20 naturel</b> — tu doubles l'un des effets chiffrés du sort.<br>
<b>1 naturel</b> — magicien : table des catastrophes magiques. Prêtre : ta divinité te retire
le sort jusqu'à une <b>pénitence</b>.
</div>
</div>"""

CSS = """
@font-face { font-family:"DejaVuVendored"; font-weight:normal; font-style:normal;
             src:url("fonts/DejaVuSans.ttf") format("truetype"); }
@font-face { font-family:"DejaVuVendored"; font-weight:bold; font-style:normal;
             src:url("fonts/DejaVuSans-Bold.ttf") format("truetype"); }
@font-face { font-family:"DejaVuVendored"; font-weight:normal; font-style:italic;
             src:url("fonts/DejaVuSans-Oblique.ttf") format("truetype"); }
@page { size: A4; margin: 10mm; }
body { font-family:"DejaVuVendored"; margin:0; color:#1a2227; }
.grille { display:flex; flex-wrap:wrap; }
.carte { width:92mm; height:86mm; box-sizing:border-box;
         border:1px dashed #9aa8b0; padding:5mm 5mm 4mm 5mm; margin:0;
         page-break-inside:avoid; overflow:hidden; }
.titre { font-size:12pt; font-weight:bold; color:#14507c; line-height:1.15; }
.meta  { font-size:7pt; text-transform:uppercase; letter-spacing:0.8pt;
         color:#7d8f9a; margin:1.5mm 0 0 0; }
.ligne { font-size:7.6pt; color:#2e3d46; margin:2.5mm 0 2mm 0;
         border-top:1px solid #d8e0e5; border-bottom:1px solid #d8e0e5;
         padding:1.4mm 0; }
.corps { font-size:8.4pt; line-height:1.36; }
.qui   { font-size:7pt; color:#7d8f9a; margin-top:2.5mm; font-style:italic; }
.regle .titre { color:#1e5c30; }
.regle .corps { font-size:8pt; }
"""


def carte(nom, rang, duree, portee, qui, texte):
    return (f'<div class="carte"><div class="titre">{nom}</div>'
            f'<div class="meta">{rang}</div>'
            f'<div class="ligne"><b>Durée</b> {duree} &nbsp;·&nbsp; '
            f'<b>Portée</b> {portee}</div>'
            f'<div class="corps">{texte}</div>'
            f'<div class="qui">{qui}</div></div>')


def main():
    try:
        from weasyprint import HTML
    except ImportError:
        print("weasyprint manquant : pip install weasyprint --break-system-packages")
        return 1
    cartes = REGLE + "".join(carte(*s) for s in SORTS)
    html = (f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            f"<style>{CSS}</style></head><body>"
            f'<div class="grille">{cartes}</div></body></html>')
    OUT.mkdir(exist_ok=True)
    cible = OUT / "cartes-sorts.pdf"
    doc = HTML(string=html, base_url=str(ASSETS)).render()
    doc.write_pdf(cible)
    print(f"· cartes-sorts — {len(SORTS) + 1} cartes, {len(doc.pages)} page(s)")
    print(f"  {cible}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
