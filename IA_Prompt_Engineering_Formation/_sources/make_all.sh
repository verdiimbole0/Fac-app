#!/bin/bash
# Régénère tous les livrables. Prérequis : python3 (python-pptx, cairosvg, pypdf), node + playwright (Chromium).
set -e
cd "$(dirname "$0")"
python3 build_pptx.py
python3 build_syllabus.py
python3 build_kit.py
python3 build_guide.py
