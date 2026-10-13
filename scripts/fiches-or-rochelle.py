#!/usr/bin/env python3
"""
fiches-or-rochelle.py — les six prétirés sur la fiche alternative de
Cthulhu Hack VF, remplie.

    python3 scripts/fiches-or-rochelle.py

Produit out/fiches-or-rochelle.pdf : six pages A4 paysage, une par
personnage, le texte calé sur le scan de la fiche vierge.

Hors de build.py à dessein, comme cartes-sorts.py : ce n'est pas un
document de la collection (ni couverture, ni charte, ni contrôles),
c'est un accessoire de table.

La fiche vierge est celle de Jean-Baptiste 'jbfr' Fylicz, éditée par les
XII Singes. Elle vit dans sources/, que git ignore, comme le texte du
scénario : le script est versionné, sa matière non.

    sources/cthulhu-hack/fiche-vierge.jpg

D'OÙ VIENNENT LES CHIFFRES, et la distinction a coûté un passage entier.
Les six Sauvegardes et les trois dés d'usage viennent de la conversion
faite dans src/annote-or-rochelle ; ils sont cités tels quels dans le
livret et la feuille, et ne bougent pas. Tout le reste vient du livre
de base, archétype par archétype :

- Points de Vie = Dé de Vie + 8 ;
- la Richesse est un dé, pas un compte de pièces ;
- les dégâts appartiennent au personnage et non à l'arme — « d6 armé,
  d4 sans arme » est une propriété de l'archétype ;
- l'équipement, c'est deux objets notables, pas un inventaire ;
- les points d'Armure : 1 (légère) · 2 (renforcée) · 3 (lourde) ;
- un personnage de one-shot porte trois Capacités spéciales : celle de
  son archétype, plus deux de ses trois secondaires.

Les trois règles propres au scénario — traits, métier, coup du sort —
ne sont pas des Capacités spéciales du jeu : elles sont en Notes.
"""
import os
import sys
from pathlib import Path

os.environ.setdefault("SOURCE_DATE_EPOCH", "1700000000")

RACINE = Path(__file__).resolve().parent.parent
ASSETS = RACINE / "assets"
OUT = RACINE / "out"
FICHE = RACINE / "sources" / "cthulhu-hack" / "fiche-vierge.jpg"

# Positions, en pourcentage de la page, relevées sur le scan.
CHAMPS = {
    "nom":         (13.0, 7.0, 13.0),
    "metier":      (27.0, 7.0, 12.5),
    "archetype":   (12.6, 11.1, 13.6),
    "description": (26.8, 11.1, 13.0),
    "pv":          (5.0, 66.8, 6.0),
    "de_vie":      (20.9, 70.7, 5.0),
    "arme":        (31.5, 66.5, 6.0),
    "mains_nues":  (40.2, 66.5, 6.0),
    "richesse":    (25.3, 76.0, 5.9),
    "equipement":  (6.0, 83.6, 39.0),
    "capacites":   (56.0, 8.5, 38.2),
    "notes":       (56.0, 46.6, 38.2),
}

# Les six couronnes de laurier : centre du creux où va le chiffre.
CARACS = {
    "FOR": (7.7, 26.6), "DEX": (17.4, 26.6),
    "INT": (7.7, 38.1), "CON": (17.4, 38.1),
    "SAG": (7.7, 49.6), "CHA": (17.4, 49.6),
}

# Les trois rangées de dés d'usage, et l'abscisse de chaque dé.
RESSOURCES = {"Torche": 26.4, "Bagou": 38.0, "Santé mentale": 49.8}
DES = {"d12": 30.4, "d10": 33.9, "d8": 37.4, "d6": 40.9, "d4": 44.4}

# Les Capacités spéciales employées, résumées d'après le livre de base.
CAPACITES = {
    "Agile": "Avantage aux Sauvegardes qui demandent un effort physique : grimper, "
             "sauter, courir.",
    "Main sûre": "Une fois par heure de jeu, réussir automatiquement un test "
                 "d'attaque à distance.",
    "Profiteur": "Annuler la perte d'un équipement après un test de Matériel raté, "
                 "en perdant un niveau de Torche ou de Bagou à la place.",
    "Fuyant comme une anguille": "Une fois par session, répercuter sur quelqu'un "
                                 "d'autre les conséquences d'une Sauvegarde "
                                 "d'Intelligence ou de Sagesse ratée.",
    "Indomptable": "Avantage aux Sauvegardes contre la tromperie, le contrôle mental, "
                   "et lorsqu'il tente lui-même de tromper son interlocuteur.",
    "Médecin de terrain": "Une fois par heure de jeu, hors combat, soigner "
                          "<b>1d6 Points de Vie</b> perdus.",
    "Force de caractère": "Une fois par session, relancer les dés d'un test de Hors Jeu "
                          "ou de Folie passagère, et garder le résultat de son choix.",
    "Musclé": "Avantage aux Sauvegardes qui emploient la force : soulever, déplacer, "
              "lutter.",
    "Tactique": "Une fois par combat, après son action, faire une attaque "
                "supplémentaire — même cible ou une autre.",
    "Échappée belle": "Une fois par session, casser un équipement, en racontant "
                      "comment, pour éviter les dégâts d'une Sauvegarde de Force ou de "
                      "Dextérité ratée.",
    "Artiste": "Avantage lorsqu'il divertit un auditoire.",
    "Réseau": "Une fois par session, éviter les conséquences d'une Sauvegarde de "
              "Charisme ou de Sagesse ratée, en tirant parti d'un réseau d'amis, "
              "d'associés ou de faveurs dues.",
    "Ce ne sont pas vos affaires": "Une fois par session, baisser son Bagou d'un niveau "
                                   "pour mettre hors jeu un adversaire qui n'est pas du "
                                   "Mythe et qui a <b>15 Points de Vie ou moins</b>.",
    "Mental d'acier": "Avantage aux Sauvegardes qui résistent à la magie, aux rituels "
                      "occultes, aux malédictions et à la possession.",
    "Érudit": "Une fois par heure de jeu, réussir automatiquement une Sauvegarde "
              "d'Intelligence ou de Sagesse.",
    "Déduction": "Une fois par session, réclamer au MJ un indice sur la prochaine "
                 "étape de l'enquête.",
}

PERSONNAGES = [
    {
        "nom": "Thibault Deschamps",
        "metier": "Archéologue",
        "archetype": "Aventurier",
        "description": "Barbe fournie, yeux perçants",
        "caracs": {"FOR": 9, "DEX": 13, "CON": 10, "INT": 15, "SAG": 14, "CHA": 12},
        "des": {"Torche": "d8", "Bagou": "d6", "Santé mentale": "d8"},
        "de_vie": "d8", "pv": 12, "richesse": "d8",
        "degats": ("d6", "d4"),
        "equipement": [
            "<b>Le miroir à signaux</b> — il voit les rondes de loin et donne le départ",
            "<b>Le kit de crochetage</b>",
        ],
        "porte": "Tenue de noble · <b>armure de cuir, 1 point d'Armure</b> · épée-canne · "
                 "sac de parchemins et matériel d'écriture · une bourse de figues séchées "
                 "et de noix, à partager",
        "capacites": ["Agile", "Profiteur", "Fuyant comme une anguille"],
        "traits": "Érudit · Solitaire · Passionné",
        "sait": "Bibliothèque, histoire, droit, écriture, arabe. Lire les textes de l'Ordre.",
        "notes": [
            "D'une famille cathare éduquée, il a grandi en lisant les anciens manuscrits "
            "de l'Ordre des Croisés du Parchemin. Porte toujours un vieux sac à dos.",
        ],
    },
    {
        "nom": "Evrard Duprave",
        "metier": "Docteur",
        "archetype": "Philanthrope",
        "description": "Cheveux gris, lunettes rondes",
        "caracs": {"FOR": 10, "DEX": 12, "CON": 14, "INT": 15, "SAG": 14, "CHA": 9},
        "des": {"Torche": "d6", "Bagou": "d6", "Santé mentale": "d8"},
        "de_vie": "d6", "pv": 13, "richesse": "d10",
        "degats": ("d4", "1"),
        "equipement": [
            "<b>La torche avec huile</b> — la seule flamme du groupe, et c'est elle qui "
            "brûle le livre",
            "<b>La fiole de chloroforme</b> — elle prend un homme sans le tuer",
        ],
        "porte": "<b>Déguisement de moine</b> · armure légère, <b>1 point d'Armure</b> · "
                 "trousse médicale · dague · une ration de pain et de fromage",
        "capacites": ["Indomptable", "Médecin de terrain", "Force de caractère"],
        "traits": "Empathique · Curieux · Rigoureux",
        "sait": "Premiers soins, médecine, pharmacie, latin, occultisme.",
        "notes": [
            "Descendant d'une lignée de guérisseurs cathares, il est attiré par les "
            "mystères de l'esprit et du corps, et espère trouver un moyen de guérir "
            "l'âme humaine.",
        ],
    },
    {
        "nom": "Guillaume de Montfaucon",
        "metier": "Soldat",
        "archetype": "Brute",
        "description": "Grande stature, cicatrices",
        "caracs": {"FOR": 15, "DEX": 14, "CON": 14, "INT": 14, "SAG": 12, "CHA": 11},
        "des": {"Torche": "d6", "Bagou": "d6", "Santé mentale": "d6"},
        "de_vie": "d10", "pv": 16, "richesse": "d4",
        "degats": ("d8", "d6"),
        "equipement": [
            "<b>La corde avec crochet</b> — il monte le premier et assure les autres",
            "<b>L'épée et le bouclier</b> — seul à tenir une créature au contact",
        ],
        "porte": "Uniforme de soldat · armure de cuir et bouclier, <b>2 points "
                 "d'Armure</b> · poignards · une ration de viande séchée",
        "capacites": ["Musclé", "Tactique", "Échappée belle"],
        "traits": "Loyal · Courageux · Silencieux",
        "sait": "Épée, bouclier, équitation, tactique, latin.",
        "notes": [
            "Héritier d'une lignée cathare de chevaliers, il est dévoué à son ordre et à "
            "la protection des innocents.",
            "<b>Bagou à Désavantage, toujours</b> — il ne sait pas négocier, et il le sait.",
        ],
    },
    {
        "nom": "Geoffroy Leblanc",
        "metier": "Officier",
        "archetype": "Aventurier",
        "description": "Moustache soignée, regard sévère",
        "caracs": {"FOR": 14, "DEX": 15, "CON": 14, "INT": 14, "SAG": 13, "CHA": 13},
        "des": {"Torche": "d8", "Bagou": "d8", "Santé mentale": "d8"},
        "de_vie": "d8", "pv": 15, "richesse": "d8",
        "degats": ("d6", "d4"),
        "equipement": [
            "<b>Les papiers falsifiés</b>, signés de Richelieu — ils ouvrent la Porte Royale",
            "<b>L'uniforme d'officier</b> — il parle aux royalistes d'égal à égal",
        ],
        "porte": "Armure de mailles, <b>2 points d'Armure</b> · rapière · arquebuse · "
                 "sifflet · corde avec crochet · un morceau de fromage et des biscuits",
        "capacites": ["Agile", "Main sûre", "Fuyant comme une anguille"],
        "traits": "Stratège · Déterminé · Imperturbable",
        "sait": "Commandement, arquebuse, stratégie, équitation. Parler à un officier "
                "d'égal à égal.",
        "notes": [
            "Élevé dans la foi cathare, il a rejoint l'armée pour servir Dieu et son "
            "peuple. Déserteur de l'armée de Gascogne.",
        ],
    },
    {
        "nom": "Remy Thibodeau",
        "metier": "Escroc",
        "archetype": "Artiste",
        "description": "Œil de verre, tatouages marins",
        "caracs": {"FOR": 14, "DEX": 15, "CON": 14, "INT": 12, "SAG": 13, "CHA": 10},
        "des": {"Torche": "d8", "Bagou": "d10", "Santé mentale": "d8"},
        "de_vie": "d6", "pv": 14, "richesse": "d6",
        "degats": ("d4", "d4"),
        "equipement": [
            "<b>La lanterne sourde</b> — il ouvre la marche sous terre",
            "<b>L'assortiment de clés</b> et le grappin avec corde",
        ],
        "porte": "Costume de soldat · armure de cuir, <b>1 point d'Armure</b> · couteau "
                 "de marin · une ration de fruits séchés et une miche de pain du marin",
        "capacites": ["Artiste", "Réseau", "Ce ne sont pas vos affaires"],
        "traits": "Rusé · Indépendant · Charismatique",
        "sait": "Navigation, furtivité, arme de poing, marchandage, connaissance des "
                "rues. Circuler sous une ville par l'eau. Faire parler un quai.",
        "notes": [
            "Issu d'une famille chargée des transports par voie d'eau par les templiers, "
            "il a choisi la contrebande pour lutter contre l'oppression et protéger "
            "les siens.",
        ],
    },
    {
        "nom": "Élise de Bellevue",
        "metier": "Bibliothécaire",
        "archetype": "Savant",
        "description": "Auburn grisonnant, lunettes",
        "caracs": {"FOR": 9, "DEX": 11, "CON": 11, "INT": 15, "SAG": 14, "CHA": 12},
        "des": {"Torche": "d10", "Bagou": "d8", "Santé mentale": "d10"},
        "de_vie": "d4", "pv": 11, "richesse": "d6",
        "degats": ("1", "1"),
        "equipement": [
            "<b>Le déguisement de nonne</b> — les soldats laissent passer un religieux",
            "<b>La loupe</b>, les parchemins et l'encrier",
        ],
        "porte": "<b>Aucune armure, aucune arme</b> · quelques livres rares · matériel "
                 "d'écriture",
        "capacites": ["Mental d'acier", "Érudit", "Déduction"],
        "traits": "Érudite · Curieuse · Perspicace",
        "sait": "Bibliothèque, érudition, latin, histoire, calligraphie, psychologie, "
                "médecine, religion. Lire les textes de l'Ordre.",
        "notes": [
            "Née dans la bourgeoisie de Bordeaux, elle a voyagé à travers l'Europe pour "
            "apprendre auprès des plus grands érudits, puis s'est établie à La Rochelle "
            "pour la richesse de ses bibliothèques.",
            "<b>Elle est déjà dans la ville</b> au début de la partie : elle n'entre pas "
            "par les souterrains.",
        ],
    },
]

CSS = """
@font-face { font-family:"DejaVuVendored"; font-weight:normal; font-style:normal;
             src:url("fonts/DejaVuSans.ttf") format("truetype"); }
@font-face { font-family:"DejaVuVendored"; font-weight:bold; font-style:normal;
             src:url("fonts/DejaVuSans-Bold.ttf") format("truetype"); }
@font-face { font-family:"DejaVuVendored"; font-weight:normal; font-style:italic;
             src:url("fonts/DejaVuSans-Oblique.ttf") format("truetype"); }
@page { size: A4 landscape; margin: 0; }
body { font-family:"DejaVuVendored"; margin:0; color:#1a2227; }
.fiche { position:relative; width:297mm; height:210mm; overflow:hidden;
         page-break-after:always; }
.fiche:last-child { page-break-after:auto; }
.fond { position:absolute; left:0; top:0; width:297mm; height:210mm; }
.ch { position:absolute; font-size:8.2pt; line-height:1.26; }
.ch.c { text-align:center; }
.petit { font-size:6.4pt; line-height:1.15; }
.sous { font-size:6.4pt; line-height:1.1; }
.cartouche { font-size:9pt; }
.carac { position:absolute; width:4%; text-align:center; font-size:15pt;
         font-weight:bold; }
.cercle { position:absolute; width:10mm; height:10mm; margin-left:-5mm;
          margin-top:-5mm; border:1.6pt solid #a2272f; border-radius:50%; }
.gros { font-size:14pt; font-weight:bold; }
.liste { margin:0; padding:0; list-style:none; }
.liste li { margin:0 0 1.5mm 0; }
.bloc-t { font-size:7.2pt; text-transform:uppercase; letter-spacing:1pt;
          color:#7d8f9a; margin:0 0 1.1mm 0; }
.bloc-t:not(:first-child) { margin-top:3mm; }
.cap { margin:0 0 2.2mm 0; }
.ital { font-style:italic; }
.menu { font-size:7pt; color:#44555f; margin-top:1.6mm; }
"""


def bloc(cle, contenu, classe=""):
    x, y, l = CHAMPS[cle]
    return (f'<div class="ch {classe}" style="left:{x}%;top:{y}%;width:{l}%">'
            f"{contenu}</div>")


def page(p):
    out = [f'<img class="fond" src="file://{FICHE}">']

    out.append(bloc("nom", f'<b>{p["nom"]}</b>', "cartouche c"))
    out.append(bloc("metier", p["metier"], "cartouche c"))
    out.append(bloc("archetype", p["archetype"], "c petit"))
    out.append(bloc("description", p["description"], "c petit"))

    for nom, valeur in p["caracs"].items():
        x, y = CARACS[nom]
        out.append(f'<div class="carac" style="left:{x - 2}%;top:{y - 1.8}%">'
                   f"{valeur}</div>")

    for ressource, y in RESSOURCES.items():
        x = DES[p["des"][ressource]]
        out.append(f'<div class="cercle" style="left:{x}%;top:{y}%"></div>')

    arme, nu = p["degats"]
    out.append(bloc("pv", f'<span class="gros">{p["pv"]}</span>', "c"))
    out.append(bloc("de_vie", f'<span class="gros">{p["de_vie"]}</span>', "c"))
    out.append(bloc("arme", f'<span class="gros">{arme}</span>', "c"))
    out.append(bloc("mains_nues", f'<span class="gros">{nu}</span>', "c"))
    out.append(bloc("richesse", f'<b>{p["richesse"]}</b>', "sous"))

    equip = "".join(f"<li>{l}</li>" for l in p["equipement"])
    out.append(bloc("equipement",
                    f'<ul class="liste">{equip}</ul>'
                    f'<div class="menu">{p["porte"]}</div>'))

    caps = "".join(
        f'<div class="cap"><b>{c}</b> — {CAPACITES[c]}</div>' for c in p["capacites"])
    out.append(bloc("capacites",
                    f'<div class="bloc-t">Trois capacités, pour toute la partie</div>'
                    f'{caps}'))

    notes = "".join(f"<li>{n}</li>" for n in p["notes"])
    regles = (f'<div class="bloc-t">Les trois traits — Avantage, une fois par scène</div>'
              f'<div><b>{p["traits"]}</b> · nommer le trait avant le jet, et dire '
              f"comment il s'applique.</div>"
              f'<div class="bloc-t">Le métier — {p["metier"].lower()}, réussit sans '
              f'jet</div><div>{p["sait"]}</div>'
              f'<div class="bloc-t">Le coup du sort — une fois par partie</div>'
              f"<div>Dépenser <b>un cran de Santé mentale</b> pour qu'un imprévu tourne "
              f'bien. Aucun jet — le prix <span class="ital">est</span> le jet.</div>'
              f'<div class="bloc-t">Qui tu es</div><ul class="liste">{notes}</ul>')
    out.append(bloc("notes", regles))

    return f'<div class="fiche">{"".join(out)}</div>'


def main():
    try:
        from weasyprint import HTML
    except ImportError:
        print("weasyprint manquant : pip install weasyprint --break-system-packages")
        return 1
    if not FICHE.is_file():
        print(f"fiche vierge absente : {FICHE}")
        return 1

    html = (f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            f"<style>{CSS}</style></head><body>"
            f'{"".join(page(p) for p in PERSONNAGES)}</body></html>')

    OUT.mkdir(exist_ok=True)
    cible = OUT / "fiches-or-rochelle.pdf"
    doc = HTML(string=html, base_url=str(ASSETS)).render()
    doc.write_pdf(cible)
    for p in PERSONNAGES:
        if p["pv"] > 8 + int(p["de_vie"][1:]):
            print(f"  INCOHÉRENT {p['nom']} : {p['pv']} PV > 8 + {p['de_vie']}")
    print(f"· fiches-or-rochelle — {len(PERSONNAGES)} fiches, {len(doc.pages)} page(s)")
    print(f"  {cible}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
