#!/usr/bin/env python3
"""
carte-parti.py — le партбилет, modèle 1926.

    python3 scripts/carte-parti.py                 # Petrenko
    python3 scripts/carte-parti.py krasnov         # Krasnov (masculin seul : Svetlana n'est pas du Parti)
    python3 scripts/carte-parti.py voronin         # Voronin·

Produit out/carte-parti-<nom>.pdf : une page A4 portant la couverture
et la double page intérieure, à découper et plier.

**Le modèle 1926 est le bon.** Échangé en mars-mai 1927, remplacé
seulement en 1936 : un membre du Parti en mai 1932 porte celui-là.
Référence : travail/magnitogorsk/15-iconographie-papiers.md.

Ce que le document porte, et pourquoi il vaut la peine :

    la page gauche    état civil, date d'entrée au Parti, l'organisation
                      qui a délivré le billet, deux signatures, un cachet
    la page droite    УПЛАТА ЧЛЕНСКИХ ВЗНОСОВ — douze lignes, et la
                      colonne **месячный заработок**

**La carte du Parti dit ce que son porteur gagne, mois par mois.** C'est
le détail qui fait l'accessoire : dans un scénario dont le ressort est
une enquête de fiabilité, un écart entre le salaire et le train de vie
est une pièce à charge toute prête.

**Mai est vide, et avril est la dernière ligne signée.** Ils sont partis
de Moscou le 26 avril : la cotisation de mai se paiera au retour, si
retour il y a.

Le taux de cotisation retenu — 2 % du salaire — est une estimation
d'ordre de grandeur, pas une valeur sourcée.

Rendu par Chrome : WeasyPrint ignore les motifs SVG et mix-blend-mode.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
import rendu  # noqa: E402

F = (RACINE / "assets" / "fonts").as_uri()

# ══════════════════════════════════════════════════════════════════
#  Les porteurs
# ══════════════════════════════════════════════════════════════════

PORTEURS = {
    # clé        n°         nom            prénom + patronyme     né    entré  organisation
    "petrenko": ("0624817", "ПЕТРЕНКО", "Борислав Петрович", "1906", "1926",
                 "Краснопресненский РК<br>ВКП(б) гор. Москвы", "Б. Петренко", 285),
    "krasnov": ("0318402", "КРАСНОВ", "Сергей Ильич", "1889", "1924",
                "Выборгский РК ВКП(б)<br>гор. Ленинграда", "С. Краснов", 410),
    "voronin": ("0547193", "ВОРОНИН", "Михаил Андреевич", "1896", "1919",
                "Политотдел гарнизона<br>гор. Москвы", "М. Воронин", 330),
}

CLE = next((a for a in sys.argv[1:] if not a.startswith("-")), "petrenko")
if CLE not in PORTEURS:
    sys.exit(f"porteur inconnu : {CLE} — choisir parmi {', '.join(PORTEURS)}")
NUM, NOM, PRENOM, NE, ENTRE, ORG, SIGNE, SALAIRE = PORTEURS[CLE]

MOIS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

# Quatre mois payés, puis plus rien : ils sont partis le 26 avril.
SECRETAIRES = ["Ильин", "Ильин", "Ильин", "Ильин"]


def cotisation(salaire):
    """2 % du salaire, arrondi au kopeck — estimation d'ordre de grandeur."""
    k = round(salaire * 0.02 * 100)
    return f"{k // 100} р. {k % 100:02d} к."


def lignes():
    out = []
    for i, m in enumerate(MOIS):
        if i < len(SECRETAIRES):
            out.append(f"""<tr><td class="m">{m}</td>
 <td class="p">{SALAIRE} р.</td><td class="p">{cotisation(SALAIRE)}</td>
 <td class="p sec">{SECRETAIRES[i]}</td></tr>""")
        else:
            out.append(f'<tr><td class="m">{m}</td><td></td><td></td><td></td></tr>')
    return "\n".join(out)


HTML = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><style>
@font-face {{ font-family: PT; src: url({F}/PTSerif-Regular.ttf); }}
@font-face {{ font-family: PT; src: url({F}/PTSerif-Bold.ttf); font-weight: bold; }}
@font-face {{ font-family: Plume; src: url({F}/Caveat.ttf); }}

@page {{ size: A4; margin: 14mm 15mm; }}
html, body {{ margin: 0; padding: 0; }}
body {{ font-family: PT, serif; color: #23272e; }}

.consigne {{ font-size: 7.4pt; color: #7a736a; font-style: italic; text-align: center;
             margin-bottom: 5mm; line-height: 1.5; }}

/* ── le papier : bleu-gris très pâle, guilloché ─────────────── */
.feuillet {{ position: relative; background: #e8eaec; border: .6px solid #a9aeb4;
             overflow: hidden; }}
.guilloche {{ position: absolute; inset: 0; opacity: .5; }}
.contenu {{ position: relative; padding: 6mm 7mm; }}

/* ── la couverture ──────────────────────────────────────────── */
.couv {{ width: 74mm; height: 108mm; background: #e8eaec; margin-bottom: 7mm; }}
.couv .contenu {{ height: 100%; box-sizing: border-box; padding: 4mm; }}
.cadre {{ height: 100%; box-sizing: border-box;
          border: 2.4px solid #2c3138; padding: 7mm 5mm;
          display: flex; flex-direction: column; align-items: center; text-align: center; }}
.cadre .devise {{ font-size: 6.2pt; letter-spacing: .07em; margin-bottom: 14mm; }}
.cadre .org {{ font-size: 13pt; font-weight: bold; letter-spacing: .07em; line-height: 1.5; }}
.cadre .sec {{ font-size: 7.6pt; letter-spacing: .08em; margin-top: 9mm; line-height: 1.6; }}
.cadre .ck {{ font-size: 9.4pt; letter-spacing: .14em; margin-top: auto; }}

/* ── la double page ─────────────────────────────────────────── */
.double {{ display: flex; width: 148mm; height: 108mm; }}
.page {{ width: 50%; box-sizing: border-box; }}
.page.g {{ border-right: .5px dashed #9aa0a6; }}
.page .contenu {{ height: 100%; box-sizing: border-box; padding: 5mm 7mm 4.5mm; }}

.titre {{ text-align: center; font-size: 6pt; letter-spacing: .06em; line-height: 1.45; }}
.titre b {{ font-size: 7.4pt; letter-spacing: .04em; }}
h1 {{ text-align: center; font-size: 10.6pt; font-weight: bold; letter-spacing: .1em;
      margin: 3mm 0 1.2mm; }}
.num {{ text-align: center; font-family: PT, serif; font-size: 13pt; font-weight: bold;
        color: #93352c; letter-spacing: .1em; margin-bottom: 4mm; }}

.champ {{ font-size: 6.6pt; margin-bottom: 2.6mm; }}
.champ .lab {{ letter-spacing: .02em; }}
.champ .val {{ font-family: Plume, cursive; font-size: 11.6pt; color: #1e2f55;
               border-bottom: .5px solid #8d949b; display: block; margin-top: .4mm;
               padding: 0 1mm .2mm; min-height: 5.2mm; line-height: 1.25; }}
.champ .val.deux {{ min-height: 9.4mm; }}

.signes {{ display: flex; justify-content: space-between; align-items: flex-end;
           margin-top: 4mm; }}
.signes div {{ font-size: 6pt; text-align: center; }}
.signes .plume {{ font-family: Plume, cursive; font-size: 12pt; color: #1e2f55;
                  display: block; border-bottom: .5px solid #8d949b; padding: 0 3mm;
                  min-width: 22mm; }}

/* ── le tableau des cotisations ─────────────────────────────── */
.page.d h2 {{ text-align: center; font-size: 8.4pt; font-weight: bold; letter-spacing: .05em;
              margin: 0 0 2.4mm; }}
table {{ width: 100%; border-collapse: collapse; }}
th, td {{ border: .5px solid #7e858c; padding: .55mm .8mm; }}
th {{ font-size: 5.3pt; font-weight: bold; line-height: 1.25; text-align: center; }}
td.m {{ font-size: 6.2pt; width: 26%; }}
td.p {{ font-family: Plume, cursive; font-size: 10.4pt; color: #1e2f55; text-align: center;
        line-height: 1.1; }}
td.p.sec {{ font-size: 10.8pt; }}
td:not(.m) {{ height: 5.4mm; }}

/* ── le cachet du raïkom ────────────────────────────────────── */
svg.cachet {{ position: absolute; width: 27mm; height: 27mm;
              left: 17mm; bottom: 5mm; transform: rotate(-9deg);
              opacity: .5; mix-blend-mode: multiply; }}
</style></head><body>

<svg width="0" height="0" style="position:absolute">
 <defs>
  <pattern id="gu" width="18" height="12" patternUnits="userSpaceOnUse">
    <path d="M0 6 Q 4.5 0 9 6 T 18 6" fill="none" stroke="#9fb0c4" stroke-width=".45"/>
    <path d="M0 12 Q 4.5 6 9 12 T 18 12" fill="none" stroke="#b9c3cf" stroke-width=".35"/>
  </pattern>
  <filter id="encre" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="1.05" numOctaves="3" seed="19" result="b"/>
    <feDisplacementMap in="SourceGraphic" in2="b" scale="2.1"
                       xChannelSelector="R" yChannelSelector="G" result="d"/>
    <feTurbulence type="fractalNoise" baseFrequency="0.07" numOctaves="2" seed="7" result="t"/>
    <feColorMatrix in="t" type="matrix"
      values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.6 0 0 0 -0.3" result="m"/>
    <feComposite in="d" in2="m" operator="out"/>
  </filter>
 </defs>
</svg>

<div class="consigne">
À imprimer, découper et plier en deux. La couverture se colle dos à dos avec la double page,
ou se garde séparée.
</div>

<!-- ── la couverture ─────────────────────────────────────────── -->
<div class="feuillet couv">
  <svg class="guilloche"><rect width="100%" height="100%" fill="url(#gu)"/></svg>
  <div class="contenu">
    <div class="cadre">
      <div class="devise">ПРОЛЕТАРИИ ВСЕХ СТРАН, СОЕДИНЯЙТЕСЬ!</div>
      <div class="org">ВСЕСОЮЗНАЯ<br>КОММУНИСТИЧЕСКАЯ<br>ПАРТИЯ (б)</div>
      <div class="sec">СЕКЦИЯ КОММУНИСТИЧЕСКОГО<br>ИНТЕРНАЦИОНАЛА</div>
      <div class="ck">ЦК ВКП (б)</div>
    </div>
  </div>
</div>

<!-- ── la double page ────────────────────────────────────────── -->
<div class="feuillet double">
  <svg class="guilloche"><rect width="100%" height="100%" fill="url(#gu)"/></svg>

  <div class="page g"><div class="contenu">
    <div class="titre">
      ВСЕСОЮЗНАЯ КОММУНИСТИЧЕСКАЯ<br><b>ПАРТИЯ (большевиков)</b>
    </div>
    <h1>ПАРТИЙНЫЙ БИЛЕТ</h1>
    <div class="num">№ {NUM}</div>

    <div class="champ"><span class="lab">Фамилия</span>
      <span class="val">{NOM}</span></div>
    <div class="champ"><span class="lab">Имя и отчество</span>
      <span class="val">{PRENOM}</span></div>
    <div class="champ"><span class="lab">Год рождения</span>
      <span class="val">{NE}</span></div>
    <div class="champ"><span class="lab">Время вступления в партию</span>
      <span class="val">{ENTRE}</span></div>
    <div class="champ"><span class="lab">Наименование организации, выдавшей билет</span>
      <span class="val deux">{ORG}</span></div>

    <div class="signes">
      <div><span class="plume">{SIGNE}</span>личная подпись</div>
      <div><span class="plume">Ильин</span>Секретарь Райкома</div>
    </div>
  </div></div>

  <div class="page d"><div class="contenu">
    <h2>УПЛАТА ЧЛЕНСКИХ ВЗНОСОВ ЗА 1932 г.</h2>
    <table>
      <tr><th>Месяц</th><th>Месячный<br>заработок</th><th>Членский<br>взнос</th>
          <th>Подпись<br>секретаря</th></tr>
      {lignes()}
    </table>
  </div></div>

  <svg class="cachet" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
   <defs>
    <path id="ch" d="M 22,100 A 78,78 0 0 1 178,100"/>
    <path id="cb" d="M 30,100 A 70,70 0 0 0 170,100"/>
   </defs>
   <g filter="url(#encre)" fill="#93352c">
    <g fill="none" stroke="#93352c">
      <circle cx="100" cy="100" r="88" stroke-width="3.2"/>
      <circle cx="100" cy="100" r="76" stroke-width="1.3"/>
    </g>
    <text font-size="12.4" letter-spacing="1.1" font-family="PT">
      <textPath href="#ch" startOffset="50%" text-anchor="middle">
        ВСЕСОЮЗНАЯ КОММУНИСТИЧЕСКАЯ ПАРТИЯ
      </textPath>
    </text>
    <text font-size="11.4" letter-spacing="2" font-family="PT">
      <textPath href="#cb" startOffset="50%" text-anchor="middle">
        ★ РАЙОННЫЙ КОМИТЕТ ★
      </textPath>
    </text>
    <text x="100" y="97" font-size="20" letter-spacing="2.4" text-anchor="middle"
          font-family="PT" font-weight="bold">ВКП(б)</text>
    <text x="100" y="117" font-size="10.4" letter-spacing="1.6" text-anchor="middle"
          font-family="PT">★ 1932 ★</text>
   </g>
  </svg>
</div>

</body></html>"""

cible = RACINE / "out" / f"carte-parti-{CLE}.pdf"
rendu.pdf(HTML, cible, RACINE)
print(f"· {cible.relative_to(RACINE)}")
