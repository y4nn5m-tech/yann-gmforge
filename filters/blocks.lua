-- blocks.lua — filtre pandoc commun aux trois sorties.
--
-- 1. Un bloc coloré s'écrit :        ::: {.dire lab="Ambiance — à piocher"}
--    Le filtre transforme l'attribut `lab` en <span class="lab">…</span> réel,
--    ce qui marche identiquement en HTML, en EPUB et en PDF — contrairement à
--    `content: attr(data-lab)`, dont le support est inégal chez les liseuses.
--
-- 2. Une micro-grille s'écrit :      ::: {.loc}
--                                    - [Décor —]{.g .d} …
--    Le filtre habille chaque puce en <div class="ln">, pour retrouver les
--    filets horizontaux sans écrire de HTML à la main.
--
-- 2 bis. Un bloc de lignes à dire :  ::: {.say}
--                                    - Une idée par ligne.
--                                    - [« Une réplique. »]{.q}
--    Même mécanique, mais chaque puce devient un <div> nu : la feuille cible
--    `.say div` pour l'indentation négative. C'est ce qui distingue une pile
--    de lignes qu'on pioche d'un paragraphe qu'on lit.
--
-- 3. Les paliers de test s'écrivent : ::: {.pal}
--                                     Échec :   …    (liste de définitions)

local BLOCS = { dire = true, jeu = true, mj = true, obj = true, warn = true }

local function a_classe(el, nom)
  for _, c in ipairs(el.classes) do if c == nom then return true end end
  return false
end

-- 1 — l'étiquette
local function etiquette(div)
  local lab = div.attributes["lab"]
  if not lab then return nil end
  local span = pandoc.Span(pandoc.Str(lab), pandoc.Attr("", {"lab"}, {}))
  div.attributes["lab"] = nil
  if div.content[1] and div.content[1].t == "Para" then
    table.insert(div.content[1].content, 1, pandoc.LineBreak())
    table.insert(div.content[1].content, 1, span)
  else
    table.insert(div.content, 1, pandoc.Plain({span}))
  end
  return div
end

-- 2 — chaque item de liste devient une ligne : .ln pour la micro-grille,
--     un div nu pour les lignes à dire.
local function enveloppe_items(div, classe)
  local lignes = {}
  for _, bloc in ipairs(div.content) do
    if bloc.t == "BulletList" then
      for _, item in ipairs(bloc.content) do
        local classes = classe and {classe} or {}
        table.insert(lignes, pandoc.Div(item, pandoc.Attr("", classes, {})))
      end
    else
      table.insert(lignes, bloc)
    end
  end
  div.content = lignes
  return div
end

-- 4 — largeurs de colonnes déclarées, et non déduites du dessin ASCII.
--     ::: {.tight widths="26,18,56"}
--     Sans ça, la largeur des colonnes dépend du nombre de tirets qu'on a
--     tapés — une fragilité invisible qui décale la pagination.
local function largeurs(div)
  local spec = div.attributes["widths"]
  if not spec then return div end
  local parts, total = {}, 0
  for n in spec:gmatch("[^,%s]+") do
    local v = tonumber(n)
    if v then table.insert(parts, v); total = total + v end
  end
  if total == 0 then return div end
  div.attributes["widths"] = nil
  for _, bloc in ipairs(div.content) do
    if bloc.t == "Table" then
      for i, cs in ipairs(bloc.colspecs) do
        if parts[i] then cs[2] = parts[i] / total end
      end
    end
  end
  return div
end

function Div(el)
  for classe, _ in pairs(BLOCS) do
    if a_classe(el, classe) then return etiquette(el) or el end
  end
  if a_classe(el, "loc") then
    return enveloppe_items(etiquette(el) or el, "ln")
  end
  if a_classe(el, "say") then
    return enveloppe_items(etiquette(el) or el, nil)
  end
  if a_classe(el, "head") then return etiquette(el) or el end
  if el.attributes["widths"] then return largeurs(el) end
  return el
end

-- 3 — pandoc pose un width sur les tableaux de grille ; on le neutralise,
--     la feuille de style impose 100 % et table-layout: fixed.
function Table(el)
  for i, spec in ipairs(el.colspecs) do
    -- on conserve les largeurs relatives (elles deviennent le colgroup)
    -- mais on laisse la CSS décider de la largeur totale
  end
  return el
end
