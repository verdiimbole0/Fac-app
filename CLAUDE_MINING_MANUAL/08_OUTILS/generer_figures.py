# -*- coding: utf-8 -*-
"""Régénère toutes les figures du manuel (PNG 200 dpi + SVG) dans 02_ILLUSTRATIONS/."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fig_parties_1_2, fig_partie_3, fig_parties_4_6

for module in (fig_parties_1_2, fig_partie_3, fig_parties_4_6):
    for f in module.ALL:
        print(f())
