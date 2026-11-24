#!/bin/bash
set -e
cd /home/user/Fac-app/livre-treso
python3 build/build_docx.py >/dev/null && (zip -d livrables/LA_TRESO_SOUS_CONTROLE.docx "*/" >/dev/null 2>&1 || true)
cd livrables && timeout 300 soffice --headless --convert-to pdf LA_TRESO_SOUS_CONTROLE.docx >/dev/null 2>&1
pdfinfo LA_TRESO_SOUS_CONTROLE.pdf | grep Pages
