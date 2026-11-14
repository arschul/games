"""Batch G covers."""
from kit import *


def peel():
    d = (lin("wood", [(0, "#d9a45f"), (.5, "#c48a45"), (1, "#a8702f")])
         + lin("tile", [(0, "#fff0a8"), (1, "#f1c24a")])
         + lin("mat", [(0, "#e8d3a6"), (1, "#d2b67f")])
         + '<pattern id="grain" width="600" height="14" patternUnits="userSpaceOnUse"><rect width="600" height="1.6" y="6" fill="#000" opacity=".08"/></pattern>')
    b = [rect(0, 0, 600, 800, "url(#wood)"), rect(0, 0, 600, 800, "url(#grain)")]
    # striped awning
    for i in range(8):
        b.append(rect(i * 75, 0, 75, 150, "#d63b2f" if i % 2 == 0 else "#fbf1d8"))
    b.append(f'<path d="M0 150 ' + "".join(f"Q{37.5 + i*75} 196 {75 + i*75} 150 " for i in range(8)) + 'L600 0 L0 0Z" fill="none"/>')
    for i in range(8):
        b.append(f'<path d="M{i*75} 150 Q{i*75+37.5} 198 {i*75+75} 150Z" fill="{"#d63b2f" if i % 2 == 0 else "#fbf1d8"}" filter="url(#k-drop-s)"/>')
    # title
    b.append(text(300, 318, "Peel!", "Alfa Slab One", 150, "#2a1a0c", extra='stroke="#fff3cf" stroke-width="10" paint-order="stroke" filter="url(#k-drop)"'))
    b.append(text(300, 366, "Race to build the grid", "Figtree", 28, "#3b2713", 800))
    # kraft mat with a crossword of tiles
    b.append(rect(60, 410, 480, 300, "url(#mat)", 14, 'stroke="#7a5527" stroke-width="5" filter="url(#k-drop)"'))
    cs, g = 64, 6
    def tile(c, r, ch, rot=0):
        x, y = 130 + c * (cs + g), 458 + r * (cs + g)
        return (f'<g transform="rotate({rot} {x+cs/2} {y+cs/2})">' + rect(x, y + 5, cs, cs, "#9a6f1d", 10)
                + rect(x, y, cs, cs, "url(#tile)", 10, 'stroke="#fff6cf" stroke-width="2"')
                + text(x + cs / 2, y + cs / 2 + 18, ch, "Alfa Slab One", 48, "#2a1a0c") + "</g>")
    cells = [(0, 0, "P"), (1, 0, "E"), (2, 0, "E"), (3, 0, "L"), (3, 1, "A"), (1, 2, "N"), (2, 2, "A"), (3, 2, "P")]
    for i, (c, r, ch) in enumerate(cells):
        b.append(tile(c, r, ch, (-2, 1.5, -1, 2)[i % 4]))
    # banana hint: loose tile in hand rack
    b.append(rect(60, 736, 480, 44, "#5a3718", 10))
    for i, ch in enumerate("BANANAS"):
        x = 78 + i * 66
        b.append(rect(x, 742, 54, 32, "url(#tile)", 6) + text(x + 27, 766, ch, "Alfa Slab One", 24, "#2a1a0c"))
    return svg(d, "".join(b))


COVERS = {"peel": peel}
