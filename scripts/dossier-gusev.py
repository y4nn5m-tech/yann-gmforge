#!/usr/bin/env python3
"""
dossier-gusev.py — les deux pièces du camarade Gusev·.

    python3 scripts/dossier-gusev.py              # Gusev, Alekseï
    python3 scripts/dossier-gusev.py --feminin    # Guseva, Alina

Produit out/dossier-gusev[-feminin].pdf : une page A4 à découper.

    en haut    l'ordre de mission n° 0447 / L.I. — la couverture,
               **remise devant toute la table**
    en bas     la note de l'officier traitant
               — **à ne remettre qu'au joueur de Gusev·**

Le billet de train a été retiré : il ne portait rien que l'ordre de
mission ne dise déjà — date, gare, train de nuit.

Composition reprise de la page 11 des aides non officielles, qui la
réussit : en-tête centré sur quatre lignes, titre espacé, sous-titre
cyrillique, corps monospace justifié, bloc de découpe, note en italique.

Deux écarts volontaires :

    fond blanc    les leurs sont crème. L'impression se fait sur du
                  papier déjà jauni, et deux teintes superposées font
                  de la boue
    le tampon     chevauche la signature, encre inégale, mêlée au
                  papier — voir scripts/rendu.py

La note ne porte **ni en-tête, ni numéro, ni tampon, ni signature** :
un document qu'on demande de brûler n'a pas de cartouche
administratif, et c'est ce qui le rend crédible.

Rendu par Chrome : WeasyPrint ignore textPath et feTurbulence.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F_GUS = "--feminin" in sys.argv

nom = "GUSEVA, Alina" if F_GUS else "GUSEV, Alekseï"
court = "Guseva" if F_GUS else "Gusev"
rep = "représentante" if F_GUS else "représentant"
det = "détachée" if F_GUS else "détaché"
camarade = "La camarade" if F_GUS else "Le camarade"
son = "son"

pet = "Petrenko"
kra = "Krasnova" if "--krasnova" in sys.argv else "Krasnoff"
vor = "Voronina" if "--voronina" in sys.argv else "Voronin"
vor_f = "--voronina" in sys.argv
pet_f = "--petrenko-f" in sys.argv

F = (RACINE / "assets" / "fonts").as_uri()

HTML = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Mono; src: url({F}/CourierPrime-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4; margin: 9mm 13mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: Mono, monospace; font-size: 8pt; line-height: 1.5;
        color: #241f1a; }}

.consigne {{ font-family: PT, serif; font-size: 7.2pt; color: #7a736a; text-align: center;
             font-style: italic; margin-bottom: 3mm; line-height: 1.5; }}
.consigne.bas {{ text-align: left; margin: 2.5mm 0 0; }}

.bloc {{ border: .8px solid #b9b0a2; padding: 4.4mm 6mm; position: relative; }}
.coupe {{ border-top: 1px dashed #b9b0a2; margin: 2.6mm 0; }}
.remettre {{ font-family: PT, serif; font-size: 7.4pt; font-weight: bold; color: #7d2b2b;
             letter-spacing: .1em; text-align: center; margin: 2.4mm 0; }}

/* ── l'ordre de mission ──────────────────────────────────────── */
.organe {{ text-align: center; line-height: 1.6; }}
.organe .ru {{ letter-spacing: .14em; }}
.organe .fr {{ letter-spacing: .07em; }}
.organe .gras {{ font-weight: bold; }}
.organe .bureau {{ font-weight: bold; font-size: 9.8pt; letter-spacing: .14em;
                   margin-top: .8mm; }}
.trait {{ border-top: .9px solid #241f1a; margin: 2.6mm auto 2.2mm; width: 86%; }}

h1 {{ font-size: 12pt; font-weight: bold; letter-spacing: .2em; text-align: center;
      margin: 0; }}
.sous {{ text-align: center; font-size: 7.4pt; letter-spacing: .06em; color: #4a443c;
         margin: .5mm 0 3.6mm; }}

p {{ margin: 0 0 2.6mm; text-align: justify; }}
.sign {{ display: flex; justify-content: space-between; margin-top: 5mm; line-height: 1.6; }}
.sign .d {{ text-align: right; }}

/* ── la note, et elle ne porte rien ──────────────────────────── */
.note {{ font-family: PT, serif; font-size: 9.4pt; font-style: italic; color: #2b3a52;
         line-height: 1.52; padding: 5mm 7mm; }}
.note p {{ margin: 0 0 2.8mm; text-align: left; }}
.note ul {{ list-style: none; margin: 0 0 2.8mm; padding-left: 7mm; }}
.note li {{ margin-bottom: 2mm; text-indent: -4mm; }}
.note b {{ font-weight: bold; font-style: italic; }}
.brule {{ text-align: right; margin-top: 3.5mm; }}
.brule .maj {{ color: #8a2222; font-size: 11.4pt; letter-spacing: .04em; }}

svg.tampon {{ position: absolute; width: 31mm; height: 31mm;
              right: 12mm; bottom: 6mm; transform: rotate(-7deg);
              opacity: .58; mix-blend-mode: multiply; }}
</style></head><body>

<div class="consigne">
À imprimer et découper. L'ordre de mission va dans l'enveloppe remise devant toute la table ;
la note pliée ne se donne qu'au joueur de {court} (ou se lit en aparté).
</div>

<div class="bloc">
  <div class="organe">
    <div class="ru">СОЮЗ СОВЕТСКИХ СОЦИАЛИСТИЧЕСКИХ РЕСПУБЛИК</div>
    <div class="fr">Union des Républiques Socialistes Soviétiques</div>
    <div class="fr gras">Commissariat du Peuple à l'Industrie Lourde — Наркомтяжпром</div>
    <div class="bureau">BUREAU DE LA LOGISTIQUE INDUSTRIELLE · MOSCOU</div>
  </div>
  <div class="trait"></div>

  <h1>ORDRE DE MISSION N° 0447 / L.I.</h1>
  <div class="sous">командировочное удостоверение</div>

  <p>{camarade} <b>{nom}</b>, {rep} du Bureau de la Logistique Industrielle, est
  <b>{det} pour trois (3) semaines</b> auprès du complexe métallurgique de Magnitogorsk (région de
  Tcheliabinsk), aux fins de <b>coordination logistique</b> et de vérification des approvisionnements
  du chantier.</p>

  <p>Départ : Moscou, gare de Iaroslavski, le <b>26 avril 1932</b>, train de nuit. Retour attendu
  sous trois semaines.</p>

  <p>Toutes les autorités civiles, administratives et ferroviaires sont requises de faciliter
  {son} déplacement et de lui prêter, en tant que de besoin, assistance et concours.</p>

  <div class="sign">
    <div class="g">Fait à Moscou,<br>le 24 avril 1932.</div>
    <div class="d">Le Directeur adjoint du Bureau<br><b>I. LÉVINE</b></div>
  </div>

  <svg class="tampon" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
   <defs>
    <path id="gh" d="M 20,100 A 80,80 0 0 1 180,100"/>
    <path id="gb" d="M 27,100 A 73,73 0 0 0 173,100"/>
    <filter id="gencre" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.95" numOctaves="3" seed="11" result="b"/>
      <feDisplacementMap in="SourceGraphic" in2="b" scale="1.9"
                         xChannelSelector="R" yChannelSelector="G" result="d"/>
      <feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="5" result="t"/>
      <feColorMatrix in="t" type="matrix"
        values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.5 0 0 0 -0.3" result="m"/>
      <feComposite in="d" in2="m" operator="out"/>
    </filter>
   </defs>
   <g filter="url(#gencre)" fill="#6b4a7a">
    <g fill="none" stroke="#6b4a7a">
      <circle cx="100" cy="100" r="90" stroke-width="3.4"/>
      <circle cx="100" cy="100" r="79" stroke-width="1.4"/>
    </g>
    <text font-size="11.6" letter-spacing="1.4" font-family="PT">
      <textPath href="#gh" startOffset="50%" text-anchor="middle">
        БЮРО ПРОМЫШЛЕННОЙ ЛОГИСТИКИ
      </textPath>
    </text>
    <text font-size="11" letter-spacing="2.2" font-family="PT">
      <textPath href="#gb" startOffset="50%" text-anchor="middle">
        ★ МОСКВА ★ 1932 ★
      </textPath>
    </text>
    <text x="100" y="98" font-size="22" letter-spacing="2" text-anchor="middle"
          font-family="PT" font-weight="bold">НКТП</text>
    <text x="100" y="116" font-size="9" letter-spacing="1.8" text-anchor="middle"
          font-family="PT">Н.К.Т.П.</text>
   </g>
  </svg>
</div>

<div class="remettre">— À NE REMETTRE QU'AU JOUEUR DE {nom.split(',')[0]} —</div>

<div class="bloc note">
  <p>{court} —</p>

  <p>Ta mission de coordination est une couverture. Tiens-la sans faille.</p>

  <p>On attend de toi un <b>contre-rapport</b>. Tu voyages avec trois personnes. Juge-les, et ne
  rends ton jugement qu'à moi.</p>

  <ul>
    <li>— <b>{pet}</b> · postule chez nous. Parents monarchistes. Des nôtres, ou un rôle ?</li>
    <li>— <b>{kra}</b> · cercle de savants d'avant la Révolution. Garder, ou remercier ?</li>
    <li>— <b>{vor}</b> · {'montée' if vor_f else 'monté'} trop vite. N'aime pas la Guépéou, et
        l'a montré.</li>
  </ul>

  <p>N'entrave pas leur travail. Reste le fonctionnaire qu'ils croient voir.</p>

  <div class="brule">Mémorise. <span class="maj">BRÛLE CE BILLET.</span></div>
</div>

<div class="consigne bas">
Les annotations manuscrites — s'il y en a — se portent au stylo après impression.
</div>

</body></html>"""

cible = RACINE / "out" / f"dossier-gusev{'-feminin' if F_GUS else ''}.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
