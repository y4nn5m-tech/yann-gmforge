#!/usr/bin/env python3
"""
revision.py — les pages de révision, à lire sur un téléphone.

    python3 scripts/revision.py            # out/revision-magnitogorsk.html

Ce n'est pas un document de table : c'est un outil pour **apprendre avant**
la séance. Il se consulte dans les transports, debout, une main.

Trois modules, et le découpage vient de ce qu'un MJ doit avoir en tête
parce que ça ne se cherche pas en pleine scène :

    les gens      une trentaine de PNJ — poste, ce qu'ils savent, ce
                  qu'ils cachent, et surtout **ce qu'ils disent des
                  autres**, qui est ce qui se perd le plus vite
    les pistes    pour chacune des dix : la version d'Igor, la vérité,
                  et le point de bascule
    les comptes   le calendrier, les huit créneaux, les distances,
                  les étapes du dé de Torche

Trois manières de s'en servir :

    parcourir     la fiche entière, repliée ; on déplie ce qu'on veut
    réviser       des questions tirées au sort, corrigées sur place.
                  **Une question ratée revient** — dans la même série,
                  puis en priorité à la session suivante
    les schémas   la chronologie et la carte des relations, en SVG

Dans les données, **la bonne réponse s'écrit toujours en premier** : c'est
lisible à la relecture. **La page tire l'ordre au sort à chaque affichage**,
et il change d'une série à l'autre.

**Le JavaScript est écrit à la main, dans la page.** Pas de paquet, pas
de CDN, pas de package.json : la règle du dépôt vise un toolchain Node,
et il n'y en a pas ici. La page fonctionne hors ligne une fois chargée.

La progression vit dans le localStorage du téléphone. Elle n'est jamais
envoyée nulle part, et l'effacer ne casse rien.

La charte vient de web/page.css, copiée dans out/ par scripts/modele.py.
Seul ce qui est propre à la révision est dans la page.
"""
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "scripts"))
from revision_donnees import MODULES, SCHEMAS, TITRE, CHAPEAU  # noqa: E402

OUT = RACINE / "out"

# ══════════════════════════════════════════════════════════════════
#  Ce qui est propre à la révision — le reste est dans page.css
# ══════════════════════════════════════════════════════════════════

CSS = """
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; padding: 0; font-family: var(--texte);
       background: var(--ground); color: var(--corps);
       -webkit-text-size-adjust: 100%; }
.enveloppe { max-width: 40rem; margin: 0 auto; padding: 0 1rem 5rem; }

/* ── la barre du haut, toujours là ──────────────────────────── */
header { position: sticky; top: 0; z-index: 10; background: var(--ground);
         border-bottom: 1px solid var(--filet); padding: .7rem 1rem .6rem;
         display: flex; align-items: baseline; gap: .8rem; }
header .marque { font-family: var(--display); font-size: 1.05rem; color: var(--encre);
                 font-weight: 600; }
header .ou { font-size: .8rem; color: var(--tres-sourd); margin-left: auto; }
header button.retour { font: inherit; font-size: .85rem; background: none; border: none;
                       color: var(--lien); padding: 0; cursor: pointer; }

h1 { font-family: var(--display); font-size: 1.6rem; color: var(--encre);
     margin: 1.4rem 0 .4rem; line-height: 1.2; }
.chapeau { color: var(--sourd); margin: 0 0 1.6rem; font-size: .95rem; line-height: 1.5; }

/* ── les cartes de module, sur l'accueil ────────────────────── */
.module { display: block; width: 100%; text-align: left; font: inherit; cursor: pointer;
          background: var(--surface); border: 1px solid var(--regle); border-radius: 10px;
          padding: 1rem 1.1rem; margin-bottom: .9rem; color: inherit; }
.module:active { background: var(--voile); }
.module .nom { font-family: var(--display); font-size: 1.2rem; color: var(--encre);
               font-weight: 600; }
.module .quoi { font-size: .88rem; color: var(--sourd); margin-top: .25rem; line-height: 1.45; }
.module .jauge { height: 5px; background: var(--voile); border-radius: 3px; margin-top: .8rem;
                 overflow: hidden; }
.module .jauge i { display: block; height: 100%; background: var(--jeu-b); width: 0; }
.module .compte { font-size: .76rem; color: var(--tres-sourd); margin-top: .4rem;
                  font-variant-numeric: tabular-nums; }

/* ── les trois manières de s'en servir ──────────────────────── */
.modes { display: flex; gap: .5rem; margin: 0 0 1.4rem; }
.modes button { flex: 1; font: inherit; font-size: .88rem; padding: .6rem .3rem;
                background: var(--surface); border: 1px solid var(--regle);
                border-radius: 8px; color: var(--sourd); cursor: pointer; }
.modes button[aria-pressed="true"] { background: var(--encre); border-color: var(--encre);
                                     color: #fff; font-weight: 600; }

/* ── parcourir : les fiches ─────────────────────────────────── */
details.fiche { background: var(--surface); border: 1px solid var(--regle);
                border-radius: 9px; margin-bottom: .6rem; overflow: hidden; }
details.fiche > summary { padding: .85rem 1rem; cursor: pointer; list-style: none;
                          display: flex; align-items: baseline; gap: .6rem; }
details.fiche > summary::-webkit-details-marker { display: none; }
details.fiche > summary::after { content: "+"; margin-left: auto; color: var(--tres-sourd);
                                 font-size: 1.1rem; line-height: 1; }
details.fiche[open] > summary::after { content: "–"; }
details.fiche > summary .nom { font-weight: 600; color: var(--encre); }
details.fiche > summary .role { font-size: .82rem; color: var(--tres-sourd); }
.corps { padding: 0 1rem 1rem; font-size: .92rem; line-height: 1.55; }
.corps dl { margin: 0; }
.corps dt { font-size: .74rem; text-transform: uppercase; letter-spacing: .07em;
            color: var(--tres-sourd); margin-top: .85rem; }
.corps dd { margin: .2rem 0 0; }
.corps ul { margin: .2rem 0 0; padding-left: 1.1rem; }
.corps li { margin-bottom: .25rem; }
.corps .dit b { color: var(--encre); }
.replique { font-style: italic; color: var(--dire-t); background: var(--dire-f);
            border-left: 3px solid var(--dire-b); padding: .5rem .7rem; border-radius: 0 5px 5px 0;
            margin-top: .3rem; }
.piege { color: var(--mj-t); background: var(--mj-f); border-left: 3px solid var(--mj-b);
         padding: .5rem .7rem; border-radius: 0 5px 5px 0; margin-top: .3rem; }

/* ── réviser : le quiz ──────────────────────────────────────── */
.quiz { background: var(--surface); border: 1px solid var(--regle); border-radius: 10px;
        padding: 1.1rem; }
.quiz .ou-en { font-size: .78rem; color: var(--tres-sourd); display: flex;
               justify-content: space-between; font-variant-numeric: tabular-nums; }
.quiz .barre { height: 4px; background: var(--voile); border-radius: 2px; margin: .5rem 0 1.1rem;
               overflow: hidden; }
.quiz .barre i { display: block; height: 100%; background: var(--bleu); width: 0;
                 transition: width .25s; }
.quiz .question { font-size: 1.08rem; line-height: 1.4; color: var(--encre);
                  font-weight: 600; margin-bottom: 1rem; }
.quiz .ctx { font-size: .82rem; color: var(--tres-sourd); margin-bottom: .3rem; }
.choix { display: block; width: 100%; text-align: left; font: inherit; font-size: .95rem;
         background: var(--ground); border: 1px solid var(--regle); border-radius: 8px;
         padding: .75rem .9rem; margin-bottom: .5rem; color: inherit; cursor: pointer;
         line-height: 1.4; }
.choix:active { background: var(--voile); }
.choix[data-etat="bon"] { background: var(--jeu-f); border-color: var(--jeu-b);
                          color: var(--jeu-t); font-weight: 600; }
.choix[data-etat="rate"] { background: var(--mj-f); border-color: var(--mj-b);
                           color: var(--mj-t); }
.choix[disabled] { cursor: default; }
.pourquoi { margin-top: .9rem; padding: .8rem .9rem; background: var(--voile);
            border-radius: 8px; font-size: .9rem; line-height: 1.5; }
.pourquoi .ou { display: block; margin-top: .5rem; font-size: .76rem;
                color: var(--tres-sourd); font-family: var(--mono); }
.suite { width: 100%; font: inherit; font-size: .95rem; font-weight: 600; margin-top: .9rem;
         padding: .8rem; background: var(--encre); color: #fff; border: none;
         border-radius: 8px; cursor: pointer; }

/* ── le bilan ───────────────────────────────────────────────── */
.bilan { text-align: center; padding: 1.5rem 1rem; }
.bilan .score { font-family: var(--display); font-size: 3rem; color: var(--encre);
                line-height: 1; font-variant-numeric: tabular-nums; }
.bilan .sur { color: var(--tres-sourd); font-size: 1rem; }
.bilan .mot { margin: .8rem 0 1.4rem; color: var(--sourd); line-height: 1.5; }
.arevoir { text-align: left; margin-top: 1.4rem; }
.arevoir h3 { font-size: .78rem; text-transform: uppercase; letter-spacing: .07em;
              color: var(--tres-sourd); margin: 0 0 .5rem; }
.arevoir li { margin-bottom: .45rem; font-size: .9rem; line-height: 1.4; }

/* ── les schémas ────────────────────────────────────────────── */
.schema { background: var(--surface); border: 1px solid var(--regle); border-radius: 10px;
          padding: 1rem; margin-bottom: 1rem; }
.schema h3 { font-family: var(--display); font-size: 1.1rem; color: var(--encre);
             margin: 0 0 .2rem; }
.schema p.leg { font-size: .85rem; color: var(--sourd); margin: 0 0 .9rem; line-height: 1.45; }
.schema .cadre { overflow-x: auto; -webkit-overflow-scrolling: touch; }
.schema svg { display: block; min-width: 20rem; height: auto; }

.pied { margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--filet);
        font-size: .8rem; color: var(--tres-sourd); line-height: 1.5; }
.pied button { font: inherit; font-size: .8rem; background: none; border: none; padding: 0;
               color: var(--lien); text-decoration: underline; cursor: pointer; }

@media (min-width: 34rem) { .enveloppe { padding-bottom: 3rem; } h1 { font-size: 1.9rem; } }
"""

# ══════════════════════════════════════════════════════════════════
#  La mécanique — écrite à la main, sans rien installer
# ══════════════════════════════════════════════════════════════════

JS = r"""
const $ = s => document.querySelector(s);
const CLE = "revision-magnitogorsk-v1";

/* Ce qu'on retient d'une session à l'autre : par question, le nombre de
   réussites d'affilée. Une question ratée repart à zéro et redevient
   prioritaire. Rien ne sort du téléphone. */
let acquis = {};
try { acquis = JSON.parse(localStorage.getItem(CLE) || "{}"); } catch (e) { acquis = {}; }
const garder = () => {
  try { localStorage.setItem(CLE, JSON.stringify(acquis)); } catch (e) {}
};

const questions = m => DONNEES[m].fiches.flatMap(
  f => (f.questions || []).map(q => ({ ...q, ctx: f.nom, id: f.id + "/" + q.q.slice(0, 24) })));

const su = m => questions(m).filter(q => (acquis[q.id] || 0) >= 2).length;

/* Le tirage : les moins sues d'abord, et du hasard à score égal pour que
   deux séries ne se ressemblent pas. */
function serie(m, n) {
  const tout = questions(m).map(q => ({ q, poids: (acquis[q.id] || 0) + Math.random() }));
  tout.sort((a, b) => a.poids - b.poids);
  return tout.slice(0, Math.min(n, tout.length)).map(x => x.q);
}

let vue = { ecran: "accueil", module: null, mode: "reviser" };
let jeu = null;

/* ── l'accueil ─────────────────────────────────────────────── */
function accueil() {
  $("#barre-retour").hidden = true;
  $("#ou").textContent = "";
  const cartes = Object.entries(DONNEES).map(([k, m]) => {
    const tot = questions(k).length, ok = su(k);
    const pct = tot ? Math.round(100 * ok / tot) : 0;
    return `<button class="module" data-module="${k}">
      <span class="nom">${m.titre}</span>
      <span class="quoi">${m.quoi}</span>
      <span class="jauge"><i style="width:${pct}%"></i></span>
      <span class="compte">${ok} sur ${tot} questions sues · ${m.fiches.length} fiches</span>
    </button>`;
  }).join("");
  $("#page").innerHTML = `<h1>${TITRE}</h1><p class="chapeau">${CHAPEAU}</p>${cartes}
    <div class="pied">Une question est « sue » après deux bonnes réponses d'affilée.
    La progression reste sur ce téléphone.
    <button id="oublier">Tout remettre à zéro</button></div>`;
  $("#page").querySelectorAll(".module").forEach(b =>
    b.onclick = () => { vue = { ecran: "module", module: b.dataset.module, mode: "reviser" };
                        rendre(); });
  $("#oublier").onclick = () => {
    if (confirm("Effacer toute la progression ?")) { acquis = {}; garder(); rendre(); }
  };
}

/* ── un module : trois manières ────────────────────────────── */
function module_() {
  const m = DONNEES[vue.module];
  $("#barre-retour").hidden = false;
  $("#ou").textContent = m.titre;
  const onglet = (k, l) =>
    `<button data-mode="${k}" aria-pressed="${vue.mode === k}">${l}</button>`;
  const schemas = (SCHEMAS[vue.module] || []).length
    ? onglet("schemas", "Schémas") : "";
  $("#page").innerHTML = `<h1>${m.titre}</h1><p class="chapeau">${m.quoi}</p>
    <div class="modes">${onglet("reviser", "Réviser")}${onglet("parcourir", "Parcourir")}${schemas}</div>
    <div id="zone"></div>`;
  $("#page").querySelectorAll(".modes button").forEach(b =>
    b.onclick = () => { vue.mode = b.dataset.mode; module_(); });
  if (vue.mode === "parcourir") parcourir(m);
  else if (vue.mode === "schemas") schemasDe(vue.module);
  else demarrer(vue.module);
}

/* ── parcourir ─────────────────────────────────────────────── */
function parcourir(m) {
  $("#zone").innerHTML = m.fiches.map(f => {
    const bloc = (titre, html) => html ? `<dt>${titre}</dt><dd>${html}</dd>` : "";
    const liste = t => Array.isArray(t) ? `<ul>${t.map(x => `<li>${x}</li>`).join("")}</ul>` : t;
    const dits = (f.dit || []).map(d => `<li class="dit"><b>${d.qui}</b> — ${d.quoi}</li>`).join("");
    return `<details class="fiche"><summary>
        <span class="nom">${f.nom}</span><span class="role">${f.role || ""}</span></summary>
      <div class="corps"><dl>
        ${bloc(f.lieuLabel || "Où", f.lieu)}
        ${bloc("Ce qu'il faut savoir", liste(f.sait))}
        ${bloc("Ce qu'il tait", liste(f.cache))}
        ${dits ? `<dt>Ce qu'il dit des autres</dt><dd><ul>${dits}</ul></dd>` : ""}
        ${f.replique ? `<dt>Sa phrase</dt><dd class="replique">${f.replique}</dd>` : ""}
        ${f.piege ? `<dt>À ne pas faire</dt><dd class="piege">${f.piege}</dd>` : ""}
      </dl></div></details>`;
  }).join("");
}

/* ── réviser ───────────────────────────────────────────────── */
function demarrer(m) {
  jeu = { file: serie(m, 10), i: 0, bons: 0, rates: [], repondu: false };
  if (!jeu.file.length) { $("#zone").innerHTML = `<p class="chapeau">Pas encore de question ici.</p>`;
                          return; }
  poser();
}

/* Les choix sont écrits avec la bonne réponse en tête — c'est lisible à
   l'écriture, et illisible à la révision : on coche la première sans lire.
   L'ordre est donc tiré à chaque affichage, et il change d'une série à
   l'autre pour qu'on ne mémorise pas une position. */
function melange(t) {
  for (let i = t.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [t[i], t[j]] = [t[j], t[i]];
  }
  return t;
}

function poser() {
  if (jeu.i >= jeu.file.length) return bilan();
  const q = jeu.file[jeu.i];
  jeu.repondu = false;
  const ordre = melange(q.choix.map((_, i) => i));
  const pct = Math.round(100 * jeu.i / jeu.file.length);
  $("#zone").innerHTML = `<div class="quiz">
    <div class="ou-en"><span>Question ${jeu.i + 1} sur ${jeu.file.length}</span>
      <span>${jeu.bons} bonne${jeu.bons > 1 ? "s" : ""}</span></div>
    <div class="barre"><i style="width:${pct}%"></i></div>
    ${q.ctx ? `<div class="ctx">${q.ctx}</div>` : ""}
    <div class="question">${q.q}</div>
    <div id="choix">${ordre.map(i =>
      `<button class="choix" data-i="${i}">${q.choix[i]}</button>`).join("")}</div>
    <div id="apres"></div></div>`;
  $("#choix").querySelectorAll(".choix").forEach(b => b.onclick = () => repondre(+b.dataset.i));
}

function repondre(choisi) {
  if (jeu.repondu) return;
  jeu.repondu = true;
  const q = jeu.file[jeu.i], juste = choisi === q.bonne;
  $("#choix").querySelectorAll(".choix").forEach(b => {
    b.disabled = true;
    const i = +b.dataset.i;
    if (i === q.bonne) b.dataset.etat = "bon";
    else if (i === choisi) b.dataset.etat = "rate";
  });
  if (juste) { jeu.bons++; acquis[q.id] = (acquis[q.id] || 0) + 1; }
  else { acquis[q.id] = 0; jeu.rates.push(q); }
  garder();
  $("#apres").innerHTML = `<div class="pourquoi">${q.pourquoi}
      ${q.ou ? `<span class="ou">${q.ou}</span>` : ""}</div>
    <button class="suite">${jeu.i + 1 < jeu.file.length ? "Suivante" : "Terminer"}</button>`;
  $("#apres").querySelector(".suite").onclick = () => { jeu.i++; poser(); };
}

function bilan() {
  const n = jeu.file.length, mot =
    jeu.bons === n ? "Rien à revoir." :
    jeu.bons >= n * 0.7 ? "Ce qui a été raté revient à la prochaine série." :
    "Les questions ratées reviendront en priorité.";
  const revoir = jeu.rates.length ? `<div class="arevoir"><h3>À revoir</h3><ul>${
    jeu.rates.map(q => `<li><b>${q.q}</b><br>${q.choix[q.bonne]}</li>`).join("")}</ul></div>` : "";
  $("#zone").innerHTML = `<div class="quiz bilan">
    <div class="score">${jeu.bons}<span class="sur"> / ${n}</span></div>
    <p class="mot">${mot}</p>
    <button class="suite" id="encore">Une autre série</button>${revoir}</div>`;
  $("#encore").onclick = () => demarrer(vue.module);
}

/* ── les schémas ───────────────────────────────────────────── */
function schemasDe(m) {
  $("#zone").innerHTML = (SCHEMAS[m] || []).map(s => `<div class="schema">
    <h3>${s.titre}</h3><p class="leg">${s.leg}</p>
    <div class="cadre">${s.svg}</div></div>`).join("");
}

function rendre() {
  window.scrollTo(0, 0);
  if (vue.ecran === "accueil") accueil(); else module_();
}
$("#barre-retour").onclick = () => { vue = { ecran: "accueil", module: null, mode: "reviser" };
                                     rendre(); };
rendre();
"""


def page():
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>{TITRE} — révision</title>
<link rel="stylesheet" href="page.css">
<style>{CSS}</style>
</head>
<body>
<header>
  <button class="retour" id="barre-retour" hidden>‹ Les modules</button>
  <span class="marque">Magnitogorsk</span>
  <span class="ou" id="ou"></span>
</header>
<main class="enveloppe" id="page"></main>
<script>
const TITRE = {json.dumps(TITRE)};
const CHAPEAU = {json.dumps(CHAPEAU)};
const DONNEES = {json.dumps(MODULES, ensure_ascii=False)};
const SCHEMAS = {json.dumps(SCHEMAS, ensure_ascii=False)};
{JS}
</script>
</body>
</html>"""


def main():
    OUT.mkdir(exist_ok=True)
    cible = OUT / "revision-magnitogorsk.html"
    cible.write_text(page(), encoding="utf-8")
    n_f = sum(len(m["fiches"]) for m in MODULES.values())
    n_q = sum(len(f.get("questions", [])) for m in MODULES.values() for f in m["fiches"])
    print(f"· {cible.relative_to(RACINE)} — {len(MODULES)} modules, "
          f"{n_f} fiches, {n_q} questions, {cible.stat().st_size // 1024} Ko")


if __name__ == "__main__":
    main()
