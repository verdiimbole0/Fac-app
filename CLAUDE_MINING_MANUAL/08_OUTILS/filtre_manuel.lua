-- Filtre pandoc pour le manuel : encadrés, sauts de page, carnets, ouvertures de partie.
local ENCADRES = {
  retenir     = {"Retenir",     "À retenir"},
  terrain     = {"Terrain",     "Conseil de terrain"},
  attention   = {"Attention",   "Attention"},
  erreur      = {"Erreur",      "Erreur fréquente"},
  application = {"Application", "Application professionnelle"},
  defi        = {"Defi",        "Défi pratique"},
  setrompe    = {"Setrompe",    "Quand Claude se trompe"},
  controle    = {"Controle",    "Contrôle qualité"},
}

local PAGEBREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

local function styled(style, blocks)
  return pandoc.Div(blocks, pandoc.Attr("", {}, {["custom-style"] = style}))
end

local function para_text(style, text)
  return styled(style, {pandoc.Para({pandoc.Str(text)})})
end

-- Aplatit listes et sous-blocs pour que chaque paragraphe reçoive le style de l'encadré
local function flatten(blocks)
  local out = {}
  for _, b in ipairs(blocks) do
    if b.t == "BulletList" or b.t == "OrderedList" then
      for i, item in ipairs(b.content) do
        local mark = (b.t == "BulletList") and "•  " or (tostring((b.start or 1) + i - 1) .. ".  ")
        for j, ib in ipairs(item) do
          if (ib.t == "Plain" or ib.t == "Para") then
            local inl = {}
            if j == 1 then table.insert(inl, pandoc.Str(mark)) end
            for _, x in ipairs(ib.content) do table.insert(inl, x) end
            table.insert(out, pandoc.Para(inl))
          else
            for _, y in ipairs(flatten({ib})) do table.insert(out, y) end
          end
        end
      end
    elseif b.t == "Plain" then
      table.insert(out, pandoc.Para(b.content))
    else
      table.insert(out, b)
    end
  end
  return out
end

function Div(el)
  for _, cls in ipairs(el.classes) do
    local e = ENCADRES[cls]
    if e then
      local titre = el.attributes["titre"]
      local label = e[2] .. (titre and (" : " .. titre) or "")
      local blocks = { para_text("Encadre " .. e[1] .. " Titre", label) }
      table.insert(blocks, styled("Encadre " .. e[1], flatten(el.content)))
      table.insert(blocks, pandoc.Para({}))  -- séparateur (casse le regroupement des bordures)
      return blocks
    end
    if cls == "partie" then
      local out = {}
      local n = 0
      for _, b in ipairs(el.content) do if b.t == "BulletList" then n = n + #b.content end end
      local suf = (n > 10) and " Serre" or ""
      for _, b in ipairs(el.content) do
        if b.t == "Header" then table.insert(out, b)
        elseif b.t == "BulletList" then
          for _, item in ipairs(b.content) do
            table.insert(out, styled("Partie Chapitres" .. suf, {pandoc.Para(pandoc.utils.blocks_to_inlines(item))}))
          end
        else table.insert(out, styled("Partie Intro" .. suf, {b})) end
      end
      return out
    end
    if cls == "titrelivre" then
      local out = {}
      local styles = {"Titre Livre", "Sous-titre Livre"}
      for i, b in ipairs(el.content) do
        table.insert(out, styled(styles[i] or "Mention Livre", {b}))
      end
      return out
    end
    if cls == "carnet" then
      -- <div class="carnet" titre="Chapitre 3"> : page(s) de réflexion
      local chap = el.attributes["titre"] or ""
      local out = { para_text("Carnet Titre", "Mon carnet d'application et de réflexion") }
      table.insert(out, styled("Mention Livre", {pandoc.Para({pandoc.Emph({pandoc.Str(chap)})})}))
      local rubriques = {
        "Ce que je viens d'apprendre", "Ce que je comprends mieux maintenant",
        "Les applications possibles dans mon métier", "Les idées que ce chapitre m'a inspirées",
        "Les prompts que je pourrais construire", "Les données et documents nécessaires",
        "Les précautions à prendre", "Les actions que je souhaite mettre en œuvre",
      }
      for _, r in ipairs(rubriques) do
        table.insert(out, para_text("Carnet Rubrique", r))
        for _ = 1, 2 do table.insert(out, para_text("Carnet Ligne", "\u{00A0}")) end
      end
      table.insert(out, pandoc.RawBlock("openxml", PAGEBREAK))
      table.insert(out, para_text("Carnet Rubrique", "Espace libre : réflexions, schémas, brainstorming"))
      for _ = 1, 30 do table.insert(out, para_text("Carnet Cadre", "\u{00A0}")) end
      return out
    end
  end
end

local TOC = '<w:sdt><w:sdtPr><w:docPartObj><w:docPartGallery w:val="Table of Contents" /><w:docPartUnique /></w:docPartObj></w:sdtPr><w:sdtContent>'
  .. '<w:p><w:pPr><w:pStyle w:val="TOCHeading" /></w:pPr><w:r><w:t xml:space="preserve">Sommaire</w:t></w:r></w:p>'
  .. '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true" /><w:instrText xml:space="preserve">TOC \\o &quot;1-2&quot; \\h \\z \\u</w:instrText>'
  .. '<w:fldChar w:fldCharType="separate" /><w:fldChar w:fldCharType="end" /></w:r></w:p></w:sdtContent></w:sdt>'

function Para(el)
  if #el.content == 1 and el.content[1].t == "Str" and el.content[1].text == "\\sommaire" then
    return pandoc.RawBlock("openxml", TOC)
  end
  if #el.content == 1 and el.content[1].t == "Str" and el.content[1].text == "\\newpage" then
    return pandoc.RawBlock("openxml", PAGEBREAK)
  end
  if #el.content == 1 and el.content[1].t == "RawInline" and el.content[1].text:match("\\sommaire") then
    return pandoc.RawBlock("openxml", TOC)
  end
  if #el.content == 1 and el.content[1].t == "RawInline" and el.content[1].text:match("\\newpage") then
    return pandoc.RawBlock("openxml", PAGEBREAK)
  end
end

function RawBlock(el)
  if el.format == "tex" and el.text:match("\\sommaire") then
    return pandoc.RawBlock("openxml", TOC)
  end
  if el.format == "tex" and el.text:match("\\newpage") then
    return pandoc.RawBlock("openxml", PAGEBREAK)
  end
end
