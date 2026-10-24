#!/usr/bin/env python3
"""Render cover SVGs (600x800 viewBox) to WebP with locally installed @fontsource fonts.

usage: python3 render.py <out_dir> <svg> [<svg> ...]
"""
import os, re, sys, glob, io
from PIL import Image
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FS = os.path.join(HERE, "node_modules", "@fontsource")
W, H = 720, 960


def font_faces():
    rules = []
    for pkg in sorted(os.listdir(FS)):
        files = os.path.join(FS, pkg, "files")
        css = os.path.join(FS, pkg, "index.css")
        family = pkg.replace("-", " ").title()
        if os.path.exists(css):
            m = re.search(r"font-family:\s*'([^']+)'", open(css).read())
            if m:
                family = m.group(1)
        for f in glob.glob(os.path.join(files, "*-latin-*.woff2")):
            m = re.search(r"-latin-(\d+)-(normal|italic)\.woff2$", f)
            if not m:
                continue
            rules.append(
                f"@font-face{{font-family:'{family}';font-weight:{m.group(1)};"
                f"font-style:{m.group(2)};src:url('file://{f}') format('woff2');}}"
            )
    return "\n".join(rules)


def main():
    out_dir, svgs = sys.argv[1], sys.argv[2:]
    os.makedirs(out_dir, exist_ok=True)
    faces = font_faces()
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        for path in svgs:
            svg = open(path, encoding="utf-8").read()
            html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{faces}"
                    f"html,body{{margin:0;background:#000}}svg{{display:block;width:{W}px;height:{H}px}}"
                    f"</style></head><body>{svg}</body></html>")
            tmp = os.path.join(HERE, "_page.html")
            open(tmp, "w", encoding="utf-8").write(html)
            pg.goto("file://" + tmp)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(250)
            png = pg.locator("svg").first.screenshot()
            name = os.path.splitext(os.path.basename(path))[0]
            im = Image.open(io.BytesIO(png)).convert("RGB")
            dest = os.path.join(out_dir, name + ".webp")
            im.save(dest, "WEBP", quality=84, method=6)
            print(f"{name}: {os.path.getsize(dest)//1024} KB")
        b.close()


if __name__ == "__main__":
    main()
