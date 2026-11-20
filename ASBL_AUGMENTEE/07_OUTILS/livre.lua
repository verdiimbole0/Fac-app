-- Filtre Pandoc de l'ouvrage : sauts de page, table des matières, styles personnalisés (DOCX).
local function is_docx() return FORMAT:match('docx') ~= nil end

local TOC_XML = [[
<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>Table des matières</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \o "1-1" \h \z \u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Cliquez avec le bouton droit puis « Mettre à jour le champ » pour afficher la table des matières.</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
]]

function Div(el)
  if el.classes:includes('saut') then
    if is_docx() then
      return pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
    end
    return el
  end
  if el.classes:includes('tdm') then
    if is_docx() then return pandoc.RawBlock('openxml', TOC_XML) end
    return el
  end
  if is_docx() then
    if el.classes:includes('fauxtitre') then el.attributes['custom-style'] = 'Faux titre' end
    if el.classes:includes('pagetitre') then el.attributes['custom-style'] = 'Page de titre' end
  end
  return el
end

function Span(el)
  if is_docx() and el.classes:includes('titrelivre') then
    el.attributes['custom-style'] = 'Titre du livre'
  end
  return el
end
