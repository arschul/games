#!/usr/bin/env python3
"""Regenerate Game Hub cover art.

  cd covers/tools && npm install            # local copies of the games' Google Fonts (@fontsource)
  pip install playwright pillow && playwright install chromium
  python3 build.py                          # every cover
  python3 build.py beam-of-ra jeopardy      # just these

Writes covers/src/<id>.svg (source) and covers/<id>.webp (what the hub shows, 720x960).
Each game's cover is a function in covers_*.py; add a new game by adding a function + COVERS entry.
"""
import os, sys, importlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "src"))
OUT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
os.makedirs(SRC, exist_ok=True)
only = set(sys.argv[1:])
paths = []
for m in ["covers_a", "covers_b", "covers_c", "covers_d", "covers_e", "covers_f"]:
    for gid, fn in importlib.import_module(m).COVERS.items():
        if only and gid not in only:
            continue
        p = os.path.join(SRC, gid + ".svg")
        open(p, "w", encoding="utf-8").write(fn())
        paths.append(p)
subprocess.run([sys.executable, os.path.join(HERE, "render.py"), OUT] + paths, check=True)
