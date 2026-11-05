"""Batch B covers."""
import math, random
from kit import *


def alphabet():
    d = rad("bg", [(0, "#16244a"), (1, "#0a1020")], cy="30%") + lin("gold", [(0, "#fde68a"), (1, "#f59e0b")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 120, 'Alphabet <tspan fill="url(#gold)">Grab</tspan>', "Lilita One", 78, "#f8fafc",
                  extra='stroke="#050a16" stroke-width="6" paint-order="stroke"'))
    b.append(text(300, 166, "SAY IT · GRAB THE LETTER", "Nunito", 17, "#93a4c6", 900, ls=4))
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    owner = {"B": "r", "C": "b", "F": "r", "H": "b", "M": "r", "P": "b", "S": "r", "T": "b", "W": "b", "D": "r", "L": "b"}
    hard = {"Q": 3, "X": 3, "Z": 3, "J": 2, "K": 2, "V": 2, "Y": 2}
    cs, gap, cols = 78, 12, 6
    x0 = (600 - cols * cs - (cols - 1) * gap) / 2
    y0 = 210
    for k, ch in enumerate(letters):
        r, c = divmod(k, cols)
        if r == 4:
            c += 2  # center the last two
        x, y = x0 + c * (cs + gap), y0 + r * (cs + gap)
        o = owner.get(ch)
        fill = {"r": "#ef4444", "b": "#3b82f6"}.get(o, "#162038")
        stroke = {"r": "#fca5a5", "b": "#93c5fd"}.get(o, "#2a3a64")
        b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, cs, cs, fill, 14, f"stroke=\"{stroke}\" stroke-width=\"2.5\"")}</g>')
        b.append(text(x + cs/2, y + cs/2 + 17, ch, "Lilita One", 48, "#fff" if o else "#e2e8f0"))
        if ch in hard:
            b.append(f'<circle cx="{x+cs-6}" cy="{y+6}" r="15" fill="#fbbf24" stroke="#0a1020" stroke-width="3"/>'
                     + text(x + cs - 6, y + 12, f"+{hard[ch]}", "Nunito", 15, "#1a1203", 900))
    # grabbing hand cursor over "G"
    gx, gy = 470, 640
    b.append(f'<g transform="translate({gx} {gy}) rotate(-15)">' + emoji(0, 0, "👆", 58) + "</g>")
    b.append(footer("TEAMS · A1–B1 · 16 WORD LISTS", "Nunito", "#fbbf24", 15, 3, 772, 900))
    return svg(d, "".join(b))


def back_to_board():
    d = (lin("wall", [(0, "#1a0b19"), (1, "#2c0e1d")])
         + lin("brass", [(0, "#ffe7a6"), (.35, "#dca545"), (.8, "#94661b"), (1, "#6b4712")])
         + rad("panel", [(0, "#fffaf0"), (.6, "#f8f0dd"), (1, "#e9dcbf")], cy="30%")
         + lin("cur", [(0, "#3e0510"), (.3, "#7d1222"), (.55, "#b8263b"), (.8, "#7d1222"), (1, "#5a0a18")], x2=1, y2=0)
         + lin("floor", [(0, "#6b4325"), (1, "#3e2412")])
         + rad("p1", [(0, "#5fe0d2"), (.5, "#17b8a6"), (1, "#0a6a60")], cy="25%")
         + rad("p2", [(0, "#cf9bff"), (.5, "#a24dff"), (1, "#541c9a")], cy="25%")
         + rad("bulb", [(0, "#fffbe6"), (.55, "#ffd36a"), (1, "#e89a20")], cy="40%", r="60%"))
    b = [rect(0, 0, 600, 800, "url(#wall)")]
    b.append('<polygon points="150,0 200,0 330,760 20,760" fill="#ffecbe" opacity=".10"/>'
             '<polygon points="400,0 450,0 580,760 270,760" fill="#ffecbe" opacity=".10"/>')
    b.append(rect(0, 690, 600, 110, "url(#floor)"))
    b.append("".join(f'<rect x="{x}" y="690" width="2" height="110" fill="#000" opacity=".35"/>' for x in range(30, 600, 70)))
    b.append(rect(0, 684, 600, 8, "#120804"))
    # curtains + valance
    for x0, flip in ((0, 1), (600, -1)):
        b.append(f'<g transform="translate({x0} 0) scale({flip} 1)">'
                 '<path d="M0 0 H70 Q 64 400 40 690 H0 Z" fill="url(#cur)"/>'
                 '<rect x="26" y="420" width="44" height="14" rx="7" fill="url(#brass)"/></g>')
    b.append(''.join(f'<ellipse cx="{x}" cy="34" rx="34" ry="24" fill="#8f1527"/>' for x in range(0, 640, 60)))
    b.append(rect(0, 0, 600, 34, "#5a0a18") + rect(0, 34, 600, 4, "#dca545"))
    # marquee sign
    sx, sy, sw, sh = 54, 92, 492, 300
    b.append(f'<g filter="url(#k-drop)">{rect(sx, sy, sw, sh, "url(#brass)", 22)}</g>')
    b.append(rect(sx + 34, sy + 34, sw - 68, sh - 68, "url(#panel)", 8, 'stroke="#5e3f0e" stroke-opacity=".5" stroke-width="2"'))
    pts = []
    n_x, n_y, ins = 13, 7, 17
    for i in range(n_x): pts.append((sx + ins + i * (sw - 2 * ins) / n_x, sy + ins))
    for i in range(n_y): pts.append((sx + sw - ins, sy + ins + i * (sh - 2 * ins) / n_y))
    for i in range(n_x): pts.append((sx + sw - ins - i * (sw - 2 * ins) / n_x, sy + sh - ins))
    for i in range(n_y): pts.append((sx + ins, sy + sh - ins - i * (sh - 2 * ins) / n_y))
    for k, (x, y) in enumerate(pts):
        lit = k < len(pts) * .72
        if lit:
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#ffc64a" opacity=".45" filter="url(#k-glow-s)"/>')
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="{"url(#bulb)" if lit else "#3a2b1a"}" stroke="#7a5418" stroke-width="2.5"/>')
    b.append(text(300, sy + 92, "Back to", "Figtree", 30, "#6e5a50", 800))
    b.append(text(300, sy + 200, "the Board", "Anton", 98, "#24161f"))
    b.append(chip(222, sy + 220, 156, 30, "100 categories", "Figtree", 16, "url(#brass)", "#2b1a05", weight=800))
    # timer LED
    b.append(rect(250, sy + sh - 16, 100, 40, "#0a0505", 8, 'stroke="#94661b" stroke-width="4"'))
    b.append(glow_text(300, sy + sh + 16, "0:12", "Anton", 30, "#ffb84a", "#ff9a20"))
    # podiums
    for px, col, em, sc in ((40, "p1", "🦊", "4"), (330, "p2", "🦉", "3")):
        b.append(f'<g filter="url(#k-drop)">'
                 f'<ellipse cx="{px+80}" cy="{532}" rx="46" ry="26" fill="url(#{col})" stroke="#b98a2f" stroke-width="4"/>'
                 f'{rect(px, 536, 230, 24, "#3a2830", 10)}'
                 f'{rect(px + 10, 556, 210, 120, "url(#" + col + ")", 10)}</g>')
        b.append(f'<circle cx="{px+52}" cy="600" r="30" fill="#f4ead6"/>' + emoji(px + 52, 612, em, 34))
        b.append(rect(px + 140, 576, 64, 54, "#0a0505", 8) + glow_text(px + 172, 618, sc, "Anton", 40, "#ffcf6b", "#ffa030"))
        b.append(rect(px + 22, 640, 186, 24, "#000", 12, 'opacity=".35"'))
        b.append("".join(f'<circle cx="{px + 38 + i*22}" cy="652" r="8" fill="{"#fff" if i < int(sc) else "#000"}" opacity="{.85 if i < int(sc) else .45}"/>' for i in range(8)))
    # center button
    b.append(rect(272, 580, 56, 80, "url(#brass)", 10))
    b.append(footer("TEAMS · A1–B2 · SPEAKING", "Figtree", "#f2dcb6", 14, 4, 760, 800))
    return svg(d, "".join(b))


def bear_park():
    d = (lin("sky", [(0, "#0d1a2b"), (.6, "#2a3555"), (1, "#a8573a")])
         + rad("orb", [(0, "#fbe7b5"), (1, "#fbe7b5")], r="50%")
         + rad("felt", [(0, "#86a67c"), (.5, "#6a8a63"), (1, "#4a6847")], cy="45%")
         + lin("cedar", [(0, "#b27c4b"), (.5, "#8a5a33"), (1, "#55331b")])
         + lin("brass", [(0, "#fbe7a6"), (.55, "#c99a3e"), (1, "#8a6418")])
         + lin("grass", [(0, "#a6dc86"), (1, "#6fae5a")]))
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(21, 60, y1=300)]
    b.append('<circle cx="470" cy="120" r="90" fill="#fbe7b5" opacity=".18"/><circle cx="470" cy="120" r="30" fill="#fbe7b5"/>')
    def ridge(base, amp, tree, step, fill, seed):
        r = random.Random(seed); y = base; dd = f"M0 800 L0 {base}"
        for x in range(0, 600 + step, step):
            y = max(base - amp * 2, min(base + amp, y + (r.random() - .5) * amp))
            if tree:
                h = tree * (.6 + r.random() * .7); w = step * .55
                dd += f" L{x-w:.0f} {y:.0f} L{x} {y-h:.0f} L{x+w:.0f} {y:.0f}"
            else:
                dd += f" L{x} {y:.0f}"
        return f'<path d="{dd} L{600+step} 800 Z" fill="{fill}"/>'
    b.append(ridge(250, 30, 0, 40, "#2a3b3a", 3) + ridge(300, 14, 30, 22, "#1b2a24", 5))
    # felt table with cedar rim
    b.append(f'<g filter="url(#k-drop)">{rect(24, 300, 552, 470, "url(#cedar)", 26)}</g>' + rect(40, 316, 520, 438, "url(#felt)", 18))
    # park board: cedar plate + cardboard grass cells
    cs, x0, y0 = 92, 116, 356
    b.append(f'<g filter="url(#k-drop)">{rect(x0-16, y0-16, 4*cs+32, 4*cs+32, "url(#cedar)", 24)}</g>')
    for r in range(4):
        for c in range(4):
            if (r, c) == (2, 1):
                b.append(rect(x0+c*cs+4, y0+r*cs+4, cs-8, cs-8, "#f5c518", 10))
                for k in range(-2, 6):
                    b.append(f'<path d="M{x0+c*cs+4+k*16} {y0+r*cs+cs-4} l{cs-8} {-(cs-8)}" stroke="#1a1a1a" stroke-width="7" clip-path="url(#pitc)"/>')
                b.append(f'<clipPath id="pitc">{rect(x0+c*cs+4, y0+r*cs+4, cs-8, cs-8, "#000", 10)}</clipPath>')
                b.append(rect(x0+c*cs+20, y0+r*cs+20, cs-40, cs-40, "#2a1d12", 6))
            else:
                b.append(rect(x0+c*cs+4, y0+r*cs+4, cs-8, cs-8, "url(#grass)", 10, 'stroke="#2f6b2a" stroke-opacity=".5" stroke-width="2"'))
                b.append(rect(x0+c*cs+10, y0+r*cs+9, cs-20, 6, "#fff", 3, 'opacity=".3"'))
    def tile(cells, fill, edge):
        g = ""
        for (r, c) in cells:
            g += rect(x0+c*cs+3, y0+r*cs+3, cs-6, cs-6, fill, 12, f'stroke="{edge}" stroke-width="3"')
            g += rect(x0+c*cs+10, y0+r*cs+9, cs-20, 7, "#fff", 3, 'opacity=".4"')
        return f'<g filter="url(#k-drop-s)">{g}</g>'
    b.append(tile([(0, 0), (0, 1), (1, 0)], "#a8dcf7", "#2c6c90"))
    b.append(tile([(0, 3), (1, 3), (2, 3), (1, 2)], "#e6b45c", "#7a4f12"))
    b.append(tile([(3, 0), (3, 1)], "#cfe57f", "#56701b"))
    b.append(emoji(x0+0.5*cs, y0+0.5*cs+20, "🐻‍❄️", 50) + emoji(x0+3.5*cs, y0+1.5*cs+20, "🐻", 50)
             + emoji(x0+2.5*cs, y0+3.5*cs+18, "🌲", 44) + emoji(x0+0.5*cs+46, y0+3.5*cs+18, "🛝", 40))
    # brass bear statue rising from the pit
    sx, sy = x0+1.5*cs, y0+2.5*cs - 26
    b.append(f'<g filter="url(#k-drop)"><circle cx="{sx-26}" cy="{sy-26}" r="16" fill="url(#brass)"/><circle cx="{sx+26}" cy="{sy-26}" r="16" fill="url(#brass)"/>'
             f'<circle cx="{sx}" cy="{sy}" r="40" fill="url(#brass)" stroke="#6e4f12" stroke-width="4"/>'
             f'<circle cx="{sx}" cy="{sy}" r="32" fill="none" stroke="#fff0c8" stroke-opacity=".55" stroke-width="2"/></g>'
             + text(sx, sy + 14, "16", "Bevan", 36, "#3a2805"))
    # routed cedar title sign
    b.append(f'<g filter="url(#k-drop)">{rect(140, 166, 14, 150, "#4a2c12")}{rect(446, 166, 14, 150, "#4a2c12")}'
             + rect(36, 40, 528, 170, "url(#cedar)", 20, 'stroke="#2e1a08" stroke-width="4"') + '</g>')
    b.append(rect(48, 52, 504, 146, "none", 14, 'stroke="#fbeed3" stroke-opacity=".3" stroke-width="2"'))
    b.append(text(300, 142, "Bear Park", "Bevan", 78, "#2a1606") + text(300, 138, "Bear Park", "Bevan", 78, "#fbeed3"))
    b.append(text(300, 180, "Build the best bear park", "Rethink Sans", 22, "#f3dcb8", 700))
    b.append(rect(0, 760, 600, 40, "#14231c", 0, 'opacity=".9"') + footer("TILE PUZZLE · 2–4 TEAMS", "Rethink Sans", "#e8c46c", 14, 4, 786, 800))
    return svg(d, "".join(b))


def bingo():
    d = (lin("sky", [(0, "#05000f"), (.6, "#1a0033"), (1, "#3b0050")])
         + lin("sun", [(0, "#ffe14a"), (.5, "#ff00cc"), (1, "#b300ff")]))
    b = [rect(0, 0, 600, 800, "url(#sky)")]
    # synth sun
    b.append('<clipPath id="sunclip"><rect x="0" y="0" width="600" height="420"/></clipPath>')
    b.append('<g clip-path="url(#sunclip)" opacity=".85"><circle cx="300" cy="420" r="170" fill="url(#sun)"/>'
             + "".join(rect(100, 300 + k*26, 400, 4 + k*2, "#1a0033") for k in range(5)) + "</g>")
    # neon grid floor
    g = ['<g stroke="#ff00cc" stroke-opacity=".55" stroke-width="2">']
    for k in range(9):
        y = 420 + (k ** 1.7) * 9
        g.append(f'<line x1="0" y1="{y:.0f}" x2="600" y2="{y:.0f}"/>')
    for k in range(-12, 13):
        g.append(f'<line x1="{300 + k*12}" y1="420" x2="{300 + k*110}" y2="800"/>')
    g.append("</g>")
    b.append("".join(g))
    b.append(text(300, 108, "CYBER", "Orbitron", 36, "#00ffe7", 900, ls=14, extra='filter="url(#k-glow-s)"'))
    b.append(text(300, 108, "CYBER", "Orbitron", 36, "#d9fffb", 900, ls=14))
    b.append(glow_text(300, 200, "BINGO", "Orbitron", 104, "#ffd6f5", "#ff00cc", 900, ls=6))
    b.append(text(300, 240, "// EFL VOCABULARY DRAW SYSTEM //", "Share Tech Mono", 17, "#e8d4ff", ls=3))
    # card
    words = ["cat", "rain", "jump", "blue", "shoe", "milk", "door", "sing", "FREE", "tree", "fast", "moon", "bread", "swim", "cold", "fish"]
    cx0, cy0, cs = 156, 470, 72
    b.append(f'<g filter="url(#k-drop)">{rect(cx0 - 14, cy0 - 14, 4*cs + 28, 4*cs + 28, "#0d0020", 14, "stroke=\"#00ffe7\" stroke-width=\"3\"")}</g>')
    marked = {0, 5, 8, 10, 15}
    for k, w in enumerate(words[:16]):
        r, c = divmod(k, 4)
        x, y = cx0 + c*cs, cy0 + r*cs
        b.append(rect(x + 3, y + 3, cs - 6, cs - 6, "#1a0033", 6, 'stroke="#7a5a9a" stroke-width="1.5"'))
        b.append(text(x + cs/2, y + cs/2 + 6, w, "Share Tech Mono", 17, "#e8d4ff"))
        if k in marked:
            b.append(f'<circle cx="{x+cs/2}" cy="{y+cs/2}" r="26" fill="none" stroke="#39ff14" stroke-width="4" filter="url(#k-glow-s)"/>'
                     f'<circle cx="{x+cs/2}" cy="{y+cs/2}" r="26" fill="#39ff14" fill-opacity=".14" stroke="#b6ffa3" stroke-width="2.5"/>')
    b.append(footer("WHOLE CLASS · LISTEN & MARK", "Orbitron", "#00ffe7", 13, 4, 786))
    return svg(d, "".join(b))


def bluff():
    d = rad("felt", [(0, "#4a1d2a"), (1, "#1c0a10")], cy="40%")
    b = [rect(0, 0, 600, 800, "url(#felt)")]
    b.append(text(300, 104, "WORD", "Playfair Display", 40, "#e8c98a", 700, ls=16))
    b.append(text(300, 204, "Bluff", "Playfair Display", 120, "#f6ead2", 900, italic=True,
                  extra='stroke="#1c0a10" stroke-width="4" paint-order="stroke"'))
    b.append(text(300, 246, "IF YOU DON'T KNOW, MAKE IT UP", "Lato", 15, "#c9a36a", 700, ls=4))
    defs_ = [("snollygoster", "n. a clever, dishonest person", -10, 150, 360),
             ("snollygoster", "n. a small snow-covered hill", 3, 300, 330),
             ("snollygoster", "n. a ghost that eats socks", 12, 450, 360)]
    for k, (w, df, rot, x, y) in enumerate(defs_):
        b.append(f'<g transform="translate({x} {y+180}) rotate({rot})" filter="url(#k-drop)">'
                 + rect(-110, -150, 220, 300, "#fbf6ea", 14, 'stroke="#c9a36a" stroke-width="2"')
                 + text(0, -112, ["A", "B", "C"][k], "Playfair Display", 34, "#8e2a3a", 900)
                 + text(0, -62, w, "Playfair Display", 19, "#2a1a10", 700, italic=True)
                 + '<line x1="-80" y1="-44" x2="80" y2="-44" stroke="#c9a36a" stroke-width="1.5"/>'
                 + "".join(text(-86, -10 + i*26, line, "Lato", 16, "#3b2a1e", 400, "start") for i, line in enumerate(_wrap(df, 20)))
                 + "</g>")
    # stamp
    b.append('<g transform="translate(330 700) rotate(-12)" opacity=".9">'
             + rect(-110, -34, 220, 68, "none", 8, 'stroke="#d0342c" stroke-width="5"')
             + text(0, 14, "BLUFF?", "Playfair Display", 42, "#d0342c", 900, ls=4) + "</g>")
    return svg(d, "".join(b))


def _wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + 1 > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    return out + [cur]


def cant_stop():
    d = (rad("felt", [(0, "#2a6b52"), (1, "#0f3326")], cy="45%")
         + lin("brass", [(0, "#f6d37a"), (.5, "#d1a03f"), (1, "#7d5717")])
         + lin("ember", [(0, "#ffb27a"), (1, "#e4692b")]))
    b = [rect(0, 0, 600, 800, "url(#felt)")]
    # topo lines
    r = random.Random(4)
    for k in range(9):
        b.append(f'<path d="M-20 {120+k*80} C 150 {80+k*80+r.randint(-30,30)}, 400 {160+k*80+r.randint(-30,30)}, 620 {110+k*80}" '
                 'fill="none" stroke="#f7eedb" stroke-opacity=".06" stroke-width="2"/>')
    # mountain icon + title
    b.append('<path d="M60 150 L110 70 L135 105 L150 85 L195 150 Z" fill="url(#brass)"/><path d="M110 70 L122 90 L98 90 Z" fill="#fff6d8"/>')
    b.append(text(210, 112, "Can't", "Big Shoulders Display", 72, "#f7eedb", 900, "start"))
    b.append(text(60, 214, "Stop", "Big Shoulders Display", 120, "#f7eedb", 900, "start", ls=2))
    b.append(text(64, 250, "PUSH YOUR LUCK · CLIMB THE COLUMNS", "Bricolage Grotesque", 15, "#cdbd9f", 800, "start", ls=2))
    # columns 2..12
    heights = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
    prog = {4: (5, "#ff9e57"), 7: (9, "#43b878"), 9: (4, "#ff9e57"), 6: (7, "#5aa9e6"), 11: (5, "#43b878")}
    x0, base, step, gap = 52, 700, 26, 50
    for i, n in enumerate(range(2, 13)):
        x = x0 + i * gap
        hgt = heights[n]
        for s in range(hgt):
            y = base - s * step
            b.append(f'<circle cx="{x}" cy="{y}" r="9" fill="#0f2731" stroke="#d1a03f" stroke-opacity=".55" stroke-width="2"/>')
        b.append(f'<circle cx="{x}" cy="{base + 36}" r="17" fill="url(#brass)"/>' + text(x, base + 43, n, "Big Shoulders Display", 20, "#2a1d06", 900))
        if n in prog:
            s, col = prog[n]
            y = base - (s - 1) * step
            b.append(f'<g filter="url(#k-drop-s)"><circle cx="{x}" cy="{y}" r="13" fill="{col}" stroke="#fff6d8" stroke-width="3"/></g>')
        if n == 7:
            y = base - 11 * step
            b.append(f'<circle cx="{x}" cy="{y}" r="13" fill="#fff6d8" stroke="#f2843f" stroke-width="4" filter="url(#k-drop-s)"/>')
    # dice
    def die(x, y, rot, pips, col="#f7eedb"):
        pos = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
               5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}[pips]
        return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop)">' + rect(-30, -30, 60, 60, col, 12)
                + "".join(f'<circle cx="{px*15}" cy="{py*15}" r="6" fill="#1b2a22"/>' for px, py in pos) + "</g>")
    b.append(die(420, 330, -12, 3) + die(500, 300, 14, 4) + die(445, 410, 22, 5) + die(530, 395, -6, 2, "#ffd9b8"))
    return svg(d, "".join(b))


def cefr_quest():
    d = rad("bg", [(0, "#1b2033"), (1, "#0f1117")], cy="30%") + lin("gold", [(0, "#fde9a0"), (1, "#f5c842")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(emoji(300, 118, "⚔️", 72))
    b.append(text(300, 216, "CEFR Quest", "Instrument Serif", 104, "url(#gold)", 400, italic=True))
    b.append(text(300, 254, "GRAMMAR BOARD GAME", "Sora", 15, "#8a93b0", 700, ls=6))
    # snaking path
    cols = ["#34d98b", "#4ea8f5", "#a78bfa", "#fb923c"]
    path = []
    for r in range(5):
        row = list(range(6)) if r % 2 == 0 else list(range(5, -1, -1))
        for c in row:
            path.append((90 + c * 84, 320 + r * 88))
    b.append('<polyline points="' + " ".join(f"{x},{y}" for x, y in path) + '" fill="none" stroke="#2a3250" stroke-width="40" stroke-linejoin="round"/>')
    special = {5: "🎲", 11: "⚡", 17: "🏆", 22: "💎", 3: "❓", 14: "❓"}
    for k, (x, y) in enumerate(path):
        col = cols[(k // 6) % 4]
        b.append(rect(x - 30, y - 30, 60, 60, "#161b2a", 12, f'stroke="{col}" stroke-width="3"'))
        if k in special:
            b.append(emoji(x, y + 11, special[k], 30))
        else:
            b.append(text(x, y + 7, k + 1, "JetBrains Mono", 18, col, 700))
    # team pawns
    for (k, col) in [(8, "#f25c6e"), (13, "#4ea8f5"), (19, "#34d98b")]:
        x, y = path[k]
        b.append(f'<g transform="translate({x+14} {y-16})" filter="url(#k-drop-s)"><circle cx="0" cy="-10" r="10" fill="{col}" stroke="#fff" stroke-width="2.5"/>'
                 f'<path d="M-12 14 Q 0 -6 12 14 Z" fill="{col}" stroke="#fff" stroke-width="2.5"/></g>')
    # level tokens
    for i, (lv, col) in enumerate(zip(["A1", "A2", "B1", "B2"], cols)):
        x = 120 + i * 120
        b.append(f'<circle cx="{x}" cy="760" r="24" fill="{col}22" stroke="{col}" stroke-width="3"/>' + text(x, 767, lv, "Sora", 18, col, 800))
    return svg(d, "".join(b))


def chain():
    d = ""
    b = [rect(0, 0, 600, 800, "#fff9f0")]
    b.append('<circle cx="80" cy="90" r="160" fill="#ffd6dc" opacity=".55"/><circle cx="560" cy="760" r="200" fill="#d6ecff" opacity=".6"/>')
    b.append(rect(160, 52, 280, 40, "#1a1a2e", 20) + text(300, 79, "★ PARTY EDITION", "Nunito", 18, "#fff", 900, ls=3))
    b.append(text(300, 196, "Word Chain", "Fredoka One", 92, "#1a1a2e"))
    b.append(text(300, 240, "LAST ONE STANDING WINS", "Nunito", 17, "#555", 900, ls=4))
    words = [("APPLE", "#ff4757"), ("EGG", "#2ed573"), ("GIRAFFE", "#1e90ff"), ("ELEPHANT", "#ffa502"), ("TIGER", "#ff4757")]
    y = 300
    for k, (w, col) in enumerate(words):
        wd = 90 + len(w) * 30
        x = 60 if k % 2 == 0 else 540 - wd
        b.append(rect(x + 7, y + 7, wd, 78, "#1a1a2e", 14) + rect(x, y, wd, 78, "#fff", 14, f'stroke="#1a1a2e" stroke-width="4"'))
        b.append(rect(x + 10, y + 12, 54, 54, col, 10, 'stroke="#1a1a2e" stroke-width="3"') + text(x + 37, y + 52, w[0], "Fredoka One", 34, "#fff"))
        nxt = words[(k + 1) % len(words)][1]
        b.append(text(x + 76, y + 53, f'{w[1:-1]}<tspan fill="{nxt}">{w[-1]}</tspan>', "Fredoka One", 34, "#1a1a2e", anchor="start"))
        # chain link to next
        if k < len(words) - 1:
            nx = 300
            b.append(f'<g transform="translate({nx} {y+88})"><ellipse cx="0" cy="0" rx="14" ry="22" fill="none" stroke="#1a1a2e" stroke-width="6"/>'
                     f'<ellipse cx="0" cy="18" rx="22" ry="14" fill="none" stroke="#1a1a2e" stroke-width="6"/></g>')
        y += 94
    return svg(d, "".join(b))


def city():
    d = rad("bg", [(0, "#1a2622"), (1, "#0e1614")], cy="40%") + lin("brass", [(0, "#e3c273"), (1, "#a8791f")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    # city blocks
    x0, y0 = 30, 250
    bw, st = 110, 34
    blk_cols = ["#3a6635", "#4a5a52", "#5b4a3a", "#3e4b5e", "#4a5a52", "#3a6635"]
    for r in range(4):
        for c in range(4):
            x, y = x0 + c * (bw + st) + st, y0 + r * (bw + st) + st/2
            if y > 760:
                continue
            col = blk_cols[(r * 3 + c) % 6]
            b.append(rect(x, y, bw, bw, col, 8))
            rr = random.Random(r * 7 + c)
            for _ in range(3):
                bx, by = x + rr.randint(8, 60), y + rr.randint(8, 60)
                b.append(rect(bx, by, rr.randint(24, 40), rr.randint(24, 40), "#000", 3, 'opacity=".22"'))
    # street names
    b.append(text(48, 300, "OAK ST", "Manrope", 11, "#9fb3a9", 800, "start", 2, 'transform="rotate(-90 48 300)"'))
    # route
    pts = [(x0 + st/2, 760), (x0 + st/2, y0 + 2*(bw+st)), (x0 + st/2 + 2*(bw+st), y0 + 2*(bw+st)),
           (x0 + st/2 + 2*(bw+st), y0 + (bw+st)), (x0 + st/2 + 3*(bw+st), y0 + (bw+st))]
    pl = " ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    b.append(f'<polyline points="{pl}" fill="none" stroke="#e3c273" stroke-width="12" stroke-linejoin="round" opacity=".35" filter="url(#k-glow-s)"/>')
    b.append(f'<polyline points="{pl}" fill="none" stroke="#e3c273" stroke-width="5" stroke-dasharray="14 9" stroke-linejoin="round"/>')
    # arrows at turns
    for (x, y), rot in zip(pts[1:4], [0, -90, 0]):
        pass
    px, py = pts[-1]
    b.append(f'<g transform="translate({px} {py-12})" filter="url(#k-drop)"><path d="M0 0 C -24 -30 -24 -60 0 -60 C 24 -60 24 -30 0 0 Z" fill="#e2665a" stroke="#fff" stroke-width="3"/>'
             '<circle cx="0" cy="-40" r="9" fill="#fff"/></g>')
    b.append(f'<circle cx="{pts[0][0]}" cy="742" r="12" fill="#fff" stroke="#2b3733" stroke-width="4"/>')
    # title
    b.append(rect(0, 0, 600, 230, "#0e1614", 0, 'opacity=".9"'))
    b.append(emoji(300, 84, "🏙️", 56))
    b.append(text(300, 162, "City Directions", "Cinzel", 56, "url(#brass)", 700))
    b.append(text(300, 204, "“Turn left on Oak Street…”", "Manrope", 21, "#c2cbc6", 600, italic=True))
    return svg(d, "".join(b))


def classroom_auction():
    """Velvet-curtain auction house: marquee bulbs, lot card on a brass easel, gavel, team paddles."""
    d = (lin("vel", [(0, "#22060b"), (.35, "#7d1d2b"), (.55, "#5c1420"), (1, "#22060b")], x2=1, y2=0)
         + rad("wall", [(0, "#40121b"), (1, "#0d0406")], cy="45%", r="70%")
         + lin("gilt", [(0, "#f3cf7a"), (.5, "#d9a441"), (1, "#8a6420")])
         + lin("wood", [(0, "#86442a"), (1, "#3f1c10")])
         + lin("paper", [(0, "#fbf4e2"), (1, "#ead9b2")])
         + lin("cone", [(0, "#ffecbe"), (1, "#ffecbe00")]))
    b = [rect(0, 0, 600, 800, "url(#wall)")]
    b.append('<polygon points="270,90 330,90 520,700 80,700" fill="url(#cone)" opacity=".28"/>')
    b.append('<ellipse cx="300" cy="690" rx="250" ry="40" fill="#ffe2a0" opacity=".16"/>')
    # floor + curtains
    b.append(rect(0, 650, 600, 150, "url(#wood)"))
    for k in range(0, 600, 34):
        b.append(f'<line x1="0" y1="{650+k*0.25:.0f}" x2="600" y2="{650+k*0.25:.0f}" stroke="#000" stroke-opacity=".25"/>')
    def curtain(x, flip):
        pts = "0,0 110,0 70,360 46,430 30,800 0,800" if not flip else "600,0 490,0 530,360 554,430 570,800 600,800"
        stripes = "".join(f'<rect x="{x0}" y="0" width="22" height="800" fill="url(#vel)"/>' for x0 in range(x, x + 120, 22))
        cid = "cl" if not flip else "cr"
        return f'<clipPath id="{cid}"><polygon points="{pts}"/></clipPath><g clip-path="url(#{cid})">{stripes}</g>'
    b.append(curtain(0, False) + curtain(490, True))
    b.append('<rect x="22" y="404" width="64" height="14" rx="7" fill="url(#gilt)" transform="rotate(-14 54 411)"/>'
             '<rect x="514" y="404" width="64" height="14" rx="7" fill="url(#gilt)" transform="rotate(14 546 411)"/>')
    # valance with scallops and bulbs
    b.append(rect(0, 0, 600, 70, "#5c1420") + rect(0, 66, 600, 5, "#8a6420"))
    b.append("".join(f'<circle cx="{x}" cy="70" r="20" fill="#d9a441"/><circle cx="{x}" cy="68" r="18" fill="#5c1420"/>' for x in range(20, 620, 40)))
    b.append("".join(f'<circle cx="{x}" cy="52" r="5.5" fill="#ffd98a"/><circle cx="{x}" cy="52" r="10" fill="#ffd98a" opacity=".25"/>' for x in range(18, 600, 28)))
    # title
    b.append(text(300, 168, "AUCTION", "Bungee", 92, "#3a0d14", extra='transform="translate(0 5)"'))
    b.append(glow_text(300, 168, "AUCTION", "Bungee", 92, "#f3cf7a", "#ffb84d"))
    b.append(text(300, 222, "STUNT SHOW", "Bungee", 46, "#fbf4e2", extra='filter="url(#k-drop-s)"'))
    # easel + lot card
    b.append('<g filter="url(#k-drop)"><polygon points="250,300 262,300 196,690 182,690" fill="#6b3a1c"/>'
             '<polygon points="338,300 350,300 418,690 404,690" fill="#6b3a1c"/></g>')
    b.append('<g filter="url(#k-drop)">' + rect(150, 262, 300, 210, "url(#paper)", 6)
             + rect(160, 272, 280, 190, "none", 4, 'stroke="#d9a441" stroke-width="3"') + "</g>")
    b.append(rect(130, 470, 340, 14, "url(#gilt)", 5))
    b.append(text(176, 304, "LOT 7", "Bungee", 20, "#8a6420", anchor="start"))
    b.append(chip(338, 286, 92, 26, "Stunt", "Figtree", 15, "#16856b", "#fff", weight=800, rx=4))
    b.append(text(300, 370, "BOOK FLIPS", "Bungee", 40, "#2b1a10"))
    b.append(text(300, 404, "10 times. Lowest bid wins.", "Figtree", 18, "#5a4330", 600))
    b.append('<g transform="translate(372 452) rotate(-9)">' + rect(-74, -38, 148, 54, "none", 8, 'stroke="#e0342b" stroke-width="4"')
             + text(0, 4, "SOLD", "Bungee", 34, "#e0342b") + "</g>")
    # gavel on block
    b.append('<ellipse cx="500" cy="660" rx="54" ry="14" fill="#3f1c10"/><g transform="translate(470 610) rotate(18)" filter="url(#k-drop-s)">'
             '<rect x="0" y="-6" width="110" height="12" rx="6" fill="#8a4a2c"/><rect x="-26" y="-36" width="40" height="66" rx="9" fill="#9a5a34"/>'
             '<rect x="-26" y="-26" width="40" height="6" fill="#d9a441"/><rect x="-26" y="14" width="40" height="6" fill="#d9a441"/></g>')
    # paddles
    def paddle(x, y, rot, e, col):
        return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop-s)">'
                '<rect x="-7" y="30" width="14" height="96" rx="6" fill="#8a4a2c"/>'
                f'<circle cx="0" cy="0" r="44" fill="{col}" stroke="#fff" stroke-opacity=".35" stroke-width="4"/>'
                f'<circle cx="-12" cy="-14" r="14" fill="#fff" opacity=".35"/>' + emoji(0, 17, e, 44) + "</g>")
    b.append(paddle(110, 610, -10, "🦊", "#e4572e") + paddle(225, 560, -3, "🦈", "#2f6fde")
             + paddle(345, 620, 4, "🦁", "#f2c230"))
    b.append(rect(0, 730, 600, 70, "url(#wood)") + rect(0, 726, 600, 5, "#d9a441"))
    b.append(text(300, 772, "Bid it. Do it. Take a bow.", "Figtree", 24, "#f3cf7a", 800))
    return svg(d, "".join(b))

def connect():
    """Letterpress print shop: inked metal type on a steel stone in a maple chase, broadside title, Ultra."""
    d = (rad("wbLamp", [(0, "#ffd9a0"), (1, "#15120f")], cx="50%", cy="0%", r="85%")
         + lin("wbDrawer", [(0, "#5a3c22"), (.3, "#4a321d"), (1, "#2b1d12")])
         + lin("wbMaple", [(0, "#c9965c"), (.55, "#ab7841"), (1, "#8f6234")])
         + lin("wbStone", [(0, "#4a515a"), (1, "#30363c")])
         + lin("wbMetal", [(0, "#eef1f4"), (.45, "#aab2ba"), (1, "#6b737b")], x2=.5, y2=1)
         + lin("wbBrass", [(0, "#f3dc93"), (.55, "#c9a24a"), (1, "#8d6a22")])
         + lin("wbPaper", [(0, "#f7f0e0"), (1, "#e4d7bb")]))
    b = [rect(0, 0, 600, 800, "#15120f")]
    # type-case drawers behind
    for r_ in range(9):
        for c in range(3):
            x, y = 14 + c * 196, -10 + r_ * 92
            b.append(rect(x, y, 182, 80, "url(#wbDrawer)", 5) + rect(x + 66, y + 16, 50, 18, "#a38135", 2)
                     + rect(x + 70, y + 19, 42, 12, "#efe6d2", 1, 'opacity=".5"')
                     + f'<path d="M{x+73} {y+52}a18 12 0 0 0 36 0z" fill="#a38135"/>')
    b.append(rect(0, 0, 600, 800, "url(#wbLamp)", 0, 'opacity=".55"'))
    # broadside title sheet
    b.append(f'<g filter="url(#k-drop)"><path d="M40 34 L560 30 L566 92 L558 212 L44 218 L34 120 Z" fill="url(#wbPaper)"/></g>')
    b.append('<path d="M58 48 L544 45 L548 200 L60 203 Z" fill="none" stroke="#b23a1e" stroke-width="3"/>')
    b.append('<path d="M66 54 L538 52 L541 194 L68 196 Z" fill="none" stroke="#1f3f78" stroke-width="1.5"/>')
    for txt, y, size in (("Word Battle", 120, 64), ("Arena", 188, 76)):
        b.append(text(303, y + 3, txt, "Ultra", size, "#1f3f78", extra='opacity=".55"'))
        b.append(text(300, y, txt, "Ultra", size, "#b23a1e"))
    # chase + stone
    b.append(f'<g filter="url(#k-drop)">{rect(44, 246, 512, 470, "url(#wbMaple)", 16)}</g>')
    b.append(rect(62, 264, 476, 434, "url(#wbStone)", 8, 'stroke="#14171a" stroke-width="2"'))
    letters = {(0, 0): ("W", "r"), (0, 1): ("O", "r"), (0, 2): ("R", "r"), (0, 3): ("D", "r"),
               (1, 1): ("A", "s"), (2, 0): ("S", "b"), (2, 1): ("H", "b"), (2, 2): ("I", "b"), (2, 3): ("P", "b"),
               (3, 1): ("N", "s"), (3, 3): ("E", "f"), (1, 3): ("T", "s"), (4, 3): ("N", "b")}
    cols = {"r": "#e23b3b", "b": "#2f6fe0"}
    cs, x0, y0 = 88, 80, 282
    for r_ in range(5):
        for c in range(5):
            x, y = x0 + c * cs, y0 + r_ * 80
            b.append(rect(x + 5, y + 5, cs - 10, 70, "#1b1e22", 9, 'stroke="#0d0f11" stroke-width="2"'))
            if (r_, c) not in letters:
                continue
            ch, k = letters[(r_, c)]
            sx, sy, sw, sh = x + 9, y + 6, cs - 18, 66
            g = [rect(sx, sy + 6, sw, sh, "#3a4046", 8), rect(sx, sy, sw, sh, "url(#wbMetal)", 8)]
            face = cols.get(k, "#b9c0c7")
            ink = "#ffffff" if k in cols else "#15181b"
            g.append(rect(sx + 7, sy + 5, sw - 14, sh - 16, face, 6))
            g.append(rect(sx + 7, sy + 5, sw - 14, 16, "#ffffff", 6, 'opacity=".22"'))
            g.append(text(sx + sw / 2, sy + 46, ch, "Ultra", 36, ink))
            if k == "f":
                g.insert(0, rect(sx - 4, sy - 4, sw + 8, sh + 8, "#e23b3b", 10, 'opacity=".55" filter="url(#k-glow-s)"'))
            if k in cols:
                em = "🦊" if k == "r" else "🐳"
                g.append(f'<circle cx="{sx+sw-4}" cy="{sy+sh-2}" r="13" fill="{cols[k]}" stroke="#c9a24a" stroke-width="2.5"/>' + emoji(sx + sw - 4, sy + sh + 4, em, 15))
            b.append(f'<g filter="url(#k-drop-s)">{"".join(g)}</g>')
    # shield quoin on an empty square
    qx, qy = x0 + 4 * cs, y0 + 2 * 80
    b.append(rect(qx + 2, qy + 2, cs - 4, 76, "none", 11, 'stroke="url(#wbBrass)" stroke-width="7"'))
    b.append(f'<g>{rect(qx + cs - 26, qy + 54, 28, 28, "url(#wbBrass)", 6)}<rect x="{qx+cs-19}" y="{qy+66}" width="14" height="10" rx="2" fill="#2a1a06"/>'
             f'<path d="M{qx+cs-16} {qy+66}v-4a4 4 0 0 1 8 0v4" fill="none" stroke="#2a1a06" stroke-width="2.5"/></g>')
    # ink brayer rolling across WORD
    b.append('<g filter="url(#k-drop)" transform="rotate(-6 470 300)"><rect x="440" y="276" width="18" height="70" rx="4" fill="url(#wbBrass)"/>'
             '<rect x="404" y="330" width="96" height="40" rx="20" fill="#e23b3b"/><rect x="404" y="330" width="96" height="12" rx="6" fill="#ffffff" opacity=".25"/>'
             '<rect x="398" y="342" width="10" height="16" rx="3" fill="#2a1a06"/><rect x="496" y="342" width="10" height="16" rx="3" fill="#2a1a06"/></g>')
    # proof strip
    b.append('<g filter="url(#k-drop-s)" transform="rotate(-4 300 742)">' + rect(196, 722, 208, 46, "#f3ecdc", 3)
             + rect(196, 722, 7, 46, "#e23b3b") + text(282, 756, "WORD", "Ultra", 28, "#1d1a16")
             + rect(352, 732, 36, 26, "#1d1a16", 5) + text(370, 751, "5", "Schibsted Grotesk", 18, "#efe6d2", 800) + "</g>")
    return svg(d, "".join(b))


def control_deck():
    # matches the 2026-11 rebuild: gunmetal rack, amber VT323 screens, ivory keycaps, Dymo labels, Oxanium title
    d = (lin("wall", [(0, "#080c10"), (.6, "#111a22"), (1, "#1b2a35")]) + lin("plate", [(0, "#4a555e"), (.6, "#30393f"), (1, "#283035")])
         + lin("rackg", [(0, "#252d33"), (1, "#14191d")]) + rad("key", [(0, "#fffaf0"), (.6, "#ece3cf"), (1, "#b9ad93")], cy="20%")
         + rad("knob", [(0, "#7d8a93"), (.62, "#2a3237"), (1, "#161b1f")], cx="36%", cy="30%") + rad("lcd", [(0, "#251a08"), (1, "#170f04")])
         + rad("glo", [(0, "#2a5f6e"), (1, "#111a22")]))
    b = [rect(0, 0, 600, 800, "url(#wall)"), '<ellipse cx="300" cy="520" rx="420" ry="300" fill="url(#glo)" opacity=".5"/>',
         stars(77, 40, "#34e0cf", op=(.15, .6))]
    b.append(text(40, 112, "Control", "Oxanium", 96, "#e8eef1", 800, "start"))
    b.append(text(40, 206, "Deck", "Oxanium", 96, "#ffb547", 800, "start"))
    # voice readout
    b.append(rect(40, 236, 520, 72, "url(#lcd)", 10))
    b.append(glow_text(300, 284, "Turn the dial to: begun", "VT323", 38, "#ffb547", "#ffb547", 400))
    # rack
    b.append(f'<g filter="url(#k-drop)">{rect(28, 330, 544, 440, "url(#rackg)", 20, "stroke=\"#46525b\" stroke-width=\"2\"")}</g>')
    def module(x, y, label, acc, screen):
        g = rect(x, y, 248, 198, "url(#plate)", 10, 'stroke="#66727b" stroke-width="1.5"') + rect(x, y, 248, 5, acc, 2)
        for sx, sy in ((x + 9, y + 14), (x + 239, y + 14), (x + 9, y + 189), (x + 239, y + 189)):
            g += f'<circle cx="{sx}" cy="{sy}" r="5" fill="#b9c2c7"/>'
        w = len(label) * 10.5 + 16
        g += rect(x + 18, y + 14, w, 26, "#141414", 3) + text(x + 18 + w / 2, y + 33, label, "Barlow Semi Condensed", 18, "#f4f4f0", 700)
        g += rect(x + 14, y + 48, 220, 46, "url(#lcd)", 6) + glow_text(x + 124, y + 81, screen, "VT323", 32, "#ffb547", "#ffb547")
        return g
    ox, oy = 46, 350
    # module 1: word class keys
    m = module(ox, oy, "Word Class Keys", "#ffb547", "pick one")
    for i, w in enumerate(["river", "slowly", "angry", "write"]):
        kx, ky = ox + 16 + (i % 2) * 112, oy + 106 + (i // 2) * 44
        down = i == 0
        m += rect(kx, ky + (4 if down else 0), 104, 36, "#857a63", 8) if not down else ""
        m += rect(kx, ky + (3 if down else 0), 104, 34, "url(#key)", 8, 'stroke="#ffb547" stroke-width="3"' if down else "")
        m += text(kx + 52, ky + 27 + (3 if down else 0), w, "Barlow Semi Condensed", 22, "#0d1114", 700)
    b.append(m)
    # module 2: verb form dial
    x2 = ox + 260
    m = module(x2, oy, "Verb Form Dial", "#34e0cf", "verb: begin")
    cx, cy = x2 + 124, oy + 160
    for i, lab in enumerate(["off", "V1", "V2", "V3"]):
        a = math.radians(-90 + 60 * i)
        lx, ly = cx + 84 * math.sin(a + math.pi / 2 - math.pi / 2), cy - 52 * math.cos(a)
        lx = cx + 86 * math.sin(a)
        sel = lab == "V3"
        if sel:
            m += rect(lx - 20, ly - 15, 40, 26, "#34e0cf", 5)
        m += text(f"{lx:.1f}", f"{ly + 5:.1f}", lab, "Barlow Semi Condensed", 20, "#0d1114" if sel else "#cfd8dd", 700)
    m += f'<circle cx="{cx}" cy="{cy}" r="30" fill="url(#knob)" stroke="#0d1012" stroke-width="3"/>'
    m += f'<line x1="{cx}" y1="{cy}" x2="{cx+24}" y2="{cy}" stroke="#34e0cf" stroke-width="6" stroke-linecap="round"/>'
    b.append(m)
    # module 3: verb switches
    y3 = oy + 212
    m = module(ox, y3, "Verb Switches", "#ff4b3e", "4 verbs")
    for i, (w, on) in enumerate([("went", 1), ("eats", 0), ("saw", 1), ("play", 0)]):
        sx = ox + 22 + i * 54
        m += f'<circle cx="{sx+18}" cy="{y3+110}" r="5" fill="{"#4fe08a" if on else "#2a2020"}"/>'
        m += rect(sx + 6, y3 + 120, 24, 44, "#0c0f11", 6)
        m += rect(sx + 9, y3 + (123 if on else 141), 18, 20, "#ff4b3e" if on else "#c4ccd1", 4)
        m += rect(sx - 2, y3 + 170, 40, 20, "#141414", 3) + text(sx + 18, y3 + 185, w, "Barlow Semi Condensed", 15, "#f4f4f0", 700)
    b.append(m)
    # module 4: quantity lever
    m = module(x2, y3, "Quantity Lever", "#4fe08a", "How ___ water?")
    ly = y3 + 150
    m += rect(x2 + 12, ly - 16, 66, 32, "#4fe08a", 6) + text(x2 + 45, ly + 8, "much", "Oxanium", 22, "#0d1114", 800)
    m += rect(x2 + 88, ly - 8, 76, 16, "#07090a", 8) + f'<circle cx="{x2+98}" cy="{ly}" r="17" fill="#4fe08a" stroke="#1f5c38" stroke-width="3"/>'
    m += f'<circle cx="{x2+93}" cy="{ly-5}" r="5" fill="#fff" opacity=".55"/>' + text(x2 + 202, ly + 8, "many", "Oxanium", 22, "#cfd8dd", 800)
    b.append(m)
    return svg(d, "".join(b))


def crown_lands():
    # matches the game: dusk hills with a castle, an oak tray of cardboard tiles, gilt Grenze title
    d = (lin("sky", [(0, "#0d1324"), (.75, "#2a1f3d")]) + lin("gold", [(0, "#fff0b0"), (.55, "#e0b04a"), (1, "#a87a1c")])
         + lin("oak", [(0, "#6e4b2a"), (1, "#4a3019")]) + rad("well", [(0, "#3a2716"), (1, "#22150a")], cy="45%")
         + lin("tok", [(0, "#6fa6ff"), (1, "#1d4c96")]))
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(41, 60, y1=330, op=(.25, .8))]
    def ridge(base, amp, ph, fill):
        pts = " ".join(f"{x},{base - amp * (.5 + .5 * math.sin(x / 90 + ph)) - amp * .35 * math.sin(x / 37 + ph * 2):.1f}" for x in range(0, 601, 20))
        return f'<polygon points="0,800 {pts} 600,800" fill="{fill}"/>'
    b.append(ridge(250, 60, 1.3, "#2a2c48"))
    cx, cy = 455, 232   # distant castle
    b.append(f'<g fill="#2a2c48"><rect x="{cx-40}" y="{cy-34}" width="80" height="40"/><rect x="{cx-54}" y="{cy-62}" width="22" height="68"/>'
             f'<rect x="{cx+32}" y="{cy-62}" width="22" height="68"/><rect x="{cx-10}" y="{cy-86}" width="20" height="92"/>'
             f'<polygon points="{cx-12},{cy-86} {cx},{cy-112} {cx+12},{cy-86}"/></g>'
             f'<polygon points="{cx+1},{cy-126} {cx+17},{cy-121} {cx+1},{cy-116}" fill="#e0b04a"/><rect x="{cx}" y="{cy-126}" width="2" height="16" fill="#2a2c48"/>')
    b.append(ridge(330, 50, 3.1, "#1d1f36"))
    b.append(text(300, 112, "Crown Lands", "Grenze", 92, "url(#gold)", 800, extra='filter="url(#k-drop)" stroke="#6b4a0c" stroke-width="1.5"'))
    b.append(text(300, 152, "Build the richest kingdom", "Alegreya Sans", 25, "#e6cf9f", 800))
    terr = {"F": ("#3f8443", "#2a5e2e"), "W": ("#f3cb52", "#d9a42a"), "L": ("#4094d6", "#2a6ba7"), "G": ("#a6d65e", "#7db43c"),
            "S": ("#918f4c", "#6c6833"), "M": ("#73737b", "#4d4d55"), "C": ("#e8589a", "#9e2f63")}
    for k, (a, z) in terr.items():
        d += lin("t" + k, [(0, a), (1, z)], 1, 1)
    grid = ["FFWWL", "FGWLL", "MGCWW", "MSGGF", "SSGFF"]
    crowns = {(0, 3): 1, (1, 3): 2, (2, 0): 2, (3, 0): 3, (0, 0): 1, (2, 4): 1, (4, 3): 1, (3, 1): 1}
    cs, x0, y0 = 82, 95, 268
    tw = 5 * cs
    # oak tray with grain
    b.append(f'<g filter="url(#k-drop)">{rect(x0 - 26, y0 - 26, tw + 52, tw + 52, "url(#oak)", 18)}</g>')
    b.append("".join(f'<line x1="{x0-20}" y1="{y0-20+k*9}" x2="{x0+tw+20}" y2="{y0-18+k*9}" stroke="#000" stroke-opacity=".07" stroke-width="2"/>' for k in range(0, 52)))
    b.append(rect(x0 - 8, y0 - 8, tw + 16, tw + 16, "url(#well)", 10, 'stroke="#1a0f05" stroke-width="2"'))
    for r, row in enumerate(grid):
        for c, t in enumerate(row):
            x, y = x0 + c * cs + 2, y0 + r * cs + 2
            s = cs - 4
            b.append(rect(x, y, s, s, f"url(#t{t})", 7, 'stroke="#1f1608" stroke-width="1.5"'))
            if t == "L":
                b.append("".join(f'<path d="M{x+10} {y+26+k*17} q 10 -7 20 0 t 20 0 t 20 0" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="3"/>' for k in range(3)))
            elif t == "W":
                b.append("".join(f'<line x1="{x+12+k*11}" y1="{y+68}" x2="{x+14+k*11}" y2="{y+34}" stroke="#9a6a0e" stroke-width="2.5"/><ellipse cx="{x+14+k*11}" cy="{y+34}" rx="3.5" ry="9" fill="#fbe39a" stroke="#9a6a0e" stroke-width="1.2"/>' for k in range(5)))
            elif t == "F":
                b.append("".join(f'<polygon points="{x+18+k*22},{y+24+(k%2)*12} {x+6+k*22},{y+58+(k%2)*12} {x+30+k*22},{y+58+(k%2)*12}" fill="#1d4a21" stroke="#123315" stroke-width="1.2"/>' for k in range(3)))
            elif t == "S":
                b.append(f'<ellipse cx="{x+28}" cy="{y+56}" rx="16" ry="7" fill="#32555a" opacity=".5"/>' + "".join(f'<line x1="{x+14+k*14}" y1="{y+68}" x2="{x+16+k*14}" y2="{y+34}" stroke="#3f3a17" stroke-width="2.5"/><ellipse cx="{x+16+k*14}" cy="{y+40}" rx="2.6" ry="6" fill="#5b3818"/>' for k in range(4)))
            elif t == "M":
                b.append(f'<polygon points="{x+12},{y+40} {x+26},{y+28} {x+40},{y+36} {x+42},{y+52} {x+22},{y+58}" fill="#9a9aa3" stroke="#2f2f35" stroke-width="2"/>'
                         f'<polygon points="{x+40},{y+58} {x+56},{y+44} {x+70},{y+52} {x+66},{y+70} {x+44},{y+72}" fill="#9a9aa3" stroke="#2f2f35" stroke-width="2"/>')
            elif t == "G":
                b.append("".join(f'<path d="M{x+14+k*18} {y+56} l3 -10 l3 10 M{x+20+k*18} {y+56} l3 -12" stroke="#4c8a28" stroke-width="2.5" fill="none"/>' for k in range(3)))
            elif t == "C":
                b.append(f'<g stroke="#2a1c0a" stroke-width="2" stroke-linejoin="round"><line x1="{x+39}" y1="{y+28}" x2="{x+39}" y2="{y+10}"/>'
                         f'<polygon points="{x+39},{y+10} {x+53},{y+15} {x+39},{y+20}" fill="#fff8e0"/>'
                         f'<path d="M{x+21} {y+70} V{y+32} h7 v-6 h7 v6 h9 v-6 h7 v6 h7 V{y+70} Z" fill="#efe4c8"/></g>'
                         f'<path d="M{x+33} {y+70} v-12 a6 6 0 0 1 12 0 v12 Z" fill="#3a2a14"/>')
            # bevel
            b.append(f'<path d="M{x+2} {y+s-2} V{y+2} H{x+s-2}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="3"/>'
                     f'<path d="M{x+s-2} {y+2} V{y+s-2} H{x+2}" fill="none" stroke="#000" stroke-opacity=".3" stroke-width="3"/>')
            if (r, c) in crowns:
                n = crowns[(r, c)]
                w = 16 * n + 8
                b.append(rect(x + s / 2 - w / 2, y + 4, w, 20, "#190e00", 6, 'opacity=".55"'))
                for k in range(n):
                    px, py = x + s / 2 + (k - (n - 1) / 2) * 16, y + 14
                    b.append(f'<path d="M{px-7} {py+6} L{px-7} {py-3} L{px-3.5} {py+1} L{px} {py-7} L{px+3.5} {py+1} L{px+7} {py-3} L{px+7} {py+6} Z" fill="#ffd23f" stroke="#3d2600" stroke-width="1.4"/>')
    # a king token hopping onto the kingdom
    kx, ky = 470, 236
    b.append(f'<path d="M{kx-60} {ky+120} Q {kx-50} {ky-10} {kx} {ky}" fill="none" stroke="#e0b04a" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round" opacity=".8"/>')
    b.append(f'<g filter="url(#k-drop)"><circle cx="{kx}" cy="{ky}" r="38" fill="url(#tok)" stroke="#123064" stroke-width="3"/>'
             f'<path d="M{kx-22} {ky-34} L{kx-22} {ky-52} L{kx-11} {ky-43} L{kx} {ky-60} L{kx+11} {ky-43} L{kx+22} {ky-52} L{kx+22} {ky-34} Z" fill="url(#gold)" stroke="#6b4a0c" stroke-width="2"/></g>'
             + emoji(kx, ky + 13, "🐺", 38))
    b.append(text(300, 742, "Squares × crowns = points", "Alegreya Sans", 24, "#f4e8cc", 800))
    b.append(footer("Domino drafting for 2–4 teams", "Alegreya Sans", "#e0b04a", 18, 1, 776, 700))
    return svg(d, "".join(b))


def deal_no_deal():
    d = (rad("bg", [(0, "#1d2a6b"), (1, "#05081f")], cy="30%") + lin("gold", [(0, "#fff1b8"), (.5, "#f5c542"), (1, "#a8780e")])
         + lin("case", [(0, "#eef1f6"), (.5, "#b8c0cc"), (1, "#7a8494")]))
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append('<polygon points="200,0 400,0 520,800 80,800" fill="#fff" opacity=".05"/>')
    b.append(text(300, 112, "DEAL", "Montserrat", 92, "url(#gold)", 900, ls=4, extra='filter="url(#k-drop)"'))
    b.append(text(300, 162, "— OR NO —", "Montserrat", 26, "#fff", 800, ls=6))
    b.append(text(300, 252, "DEAL", "Montserrat", 92, "url(#gold)", 900, ls=4, extra='filter="url(#k-drop)"'))
    nums = list(range(1, 13))
    opened = {3, 7, 10}
    for k, n in enumerate(nums):
        r, c = divmod(k, 4)
        x, y = 54 + c * 128, 300 + r * 120
        b.append(f'<g transform="translate({x} {y})" filter="url(#k-drop-s)">'
                 '<rect x="38" y="-14" width="34" height="20" rx="8" fill="none" stroke="#7a8494" stroke-width="6"/>'
                 + rect(0, 0, 110, 84, "url(#case)" if n not in opened else "#2a3155", 10, 'stroke="#5a6475" stroke-width="2"')
                 + (text(55, 56, n, "Montserrat", 38, "#1b2340", 900) if n not in opened else text(55, 54, "$", "Montserrat", 32, "#5a6475", 900))
                 + "</g>")
    # banker offer strip
    b.append(f'<g filter="url(#k-drop)">{rect(60, 676, 480, 76, "#05081f", 12, "stroke=\"url(#gold)\" stroke-width=\"3\"")}</g>')
    b.append(emoji(118, 728, "☎️", 38) + text(330, 724, "BANKER'S OFFER: $25,000", "Montserrat", 24, "#f5c542", 900))
    return svg(d, "".join(b))


def deep_cover():
    d = rad("bg", [(0, "#16213a"), (1, "#0b1220")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 66, "CLASSIFIED · WORD ASSOCIATION", "Chivo Mono", 14, "#93a2c0", 600, ls=4))
    b.append(text(300, 150, "Deep Cover", "Sora", 82, "#eef1f8", 800))
    # clue strip
    b.append(rect(130, 178, 340, 50, "#0e1a30", 25, 'stroke="#38bdf8" stroke-width="2"')
             + text(300, 211, 'CLUE: <tspan fill="#38bdf8">SKY</tspan> · 3', "Chivo Mono", 22, "#eef1f8", 700, ls=2))
    words = ["ROCKET", "NURSE", "STORM", "WALLET", "BIRD", "COAST", "LADDER", "KITE", "DANCE", "TRAIN", "DREAM", "CLOUD",
             "BRUSH", "GIFT", "NEEDLE", "SINGER", "MOON", "LIBRARY", "ANIMAL", "PLANE"]
    kind = {0: "b", 4: "b", 7: "b", 11: "b", 19: "b", 2: "r", 5: "r", 9: "r", 13: "r", 15: "r", 14: "m", 16: "b"}
    revealed = {0, 4, 7, 2, 14, 13}
    cw, ch, g = 102, 80, 9
    x0, y0 = (600 - 5 * cw - 4 * g) / 2, 262
    for k, w in enumerate(words):
        r, c = divmod(k, 5)
        x, y = x0 + c * (cw + g), y0 + r * (ch + g)
        kd = kind.get(k, "n")
        if k in revealed:
            fill, ink, st = {"b": ("#0284c7", "#fff", "#38bdf8"), "r": ("#dc2626", "#fff", "#f87171"),
                             "m": ("#05070c", "#f2b544", "#f2b544"), "n": ("#b39b71", "#241d10", "#d9c49a")}[kd]
        else:
            fill, ink, st = "#151f36", "#dbe3f3", "#26314a"
        b.append(rect(x, y, cw, ch, fill, 8, f'stroke="{st}" stroke-width="2"'))
        if k in revealed and kd == "m":
            b.append(emoji(x + cw/2, y + 48, "🐀", 34))
        else:
            b.append(text(x + cw/2, y + ch/2 + 6, w, "Chivo Mono", 15 if len(w) > 6 else 17, ink, 700))
    # stamp
    b.append('<g transform="translate(410 724) rotate(-8)" opacity=".85">' + rect(-130, -30, 260, 60, "none", 6, 'stroke="#f2b544" stroke-width="4"')
             + text(0, 10, "TOP SECRET", "Chivo Mono", 30, "#f2b544", 700, ls=6) + "</g>")
    b.append(text(40, 740, "BLUE vs RED", "Sora", 22, "#93a2c0", 800, "start"))
    return svg(d, "".join(b))



def azulejos():
    # matches the game: Lisbon night, a limestone wall board of glazed azulejos, a terracotta plate, Unbounded title
    T = {"B": ("#3a74e0", "#14348c", "#f6f1e3"), "Y": ("#ffd25a", "#d9921a", "#5a3604"), "R": ("#ec5a46", "#9a2316", "#fdebe2"),
         "K": ("#4a4e5e", "#15171f", "#ece5d2"), "T": ("#8fe0ee", "#2f9cb3", "#0b3b48")}
    order = "BYRKT"
    def motif(c, k):
        corners = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{k}" stroke-width="2"/>' for x, y in ((0, 0), (40, 0), (0, 40), (40, 40)))
        if c == "B":
            return corners + "".join(f'<ellipse cx="20" cy="10.5" rx="4.6" ry="7.5" fill="{k}" transform="rotate({a} 20 20)"/>' for a in (0, 90, 180, 270)) + f'<circle cx="20" cy="20" r="4.4" fill="#1b3c96" stroke="{k}" stroke-width="2"/>'
        if c == "Y":
            return corners + f'<circle cx="20" cy="20" r="7" fill="none" stroke="{k}" stroke-width="2.6"/><circle cx="20" cy="20" r="2.6" fill="{k}"/>' + "".join(f'<path d="M20 4.5v6" stroke="{k}" stroke-width="2.6" stroke-linecap="round" transform="rotate({i*45} 20 20)"/>' for i in range(8))
        if c == "R":
            return f'<path d="M20 3L37 20L20 37L3 20Z" fill="none" stroke="{k}" stroke-width="2.4"/><path d="M20 11L29 20L20 29L11 20Z" fill="{k}"/><circle cx="20" cy="20" r="2.4" fill="#9a2316"/>'
        if c == "K":
            return corners + f'<rect x="11" y="11" width="18" height="18" fill="{k}"/><rect x="11" y="11" width="18" height="18" fill="{k}" transform="rotate(45 20 20)"/><circle cx="20" cy="20" r="4" fill="#2a2d38"/>'
        return "".join(f'<path d="M4 {y}q4-5 8 0t8 0t8 0t8 0" fill="none" stroke="{k}" stroke-width="2.6" stroke-linecap="round"/>' for y in (11, 20, 29))
    def tile(x, y, s, c, op=1.0, rot=0):
        c1, c2, k = T[c]
        sc = s * 0.76 / 40
        g = (f'<g transform="rotate({rot} {x+s/2} {y+s/2})" opacity="{op}">'
             f'<rect x="{x}" y="{y+s*.06}" width="{s}" height="{s}" rx="{s*.13}" fill="#000" opacity="{.45 if op == 1 else 0}"/>'
             f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*.13}" fill="url(#g{c})"/>'
             f'<svg x="{x+s*.12}" y="{y+s*.12}" width="{s*.76}" height="{s*.76}" viewBox="0 0 40 40">{motif(c, k)}</svg>'
             f'<rect x="{x+1}" y="{y+1}" width="{s-2}" height="{s-2}" rx="{s*.12}" fill="url(#gloss)"/>'
             f'<rect x="{x}" y="{y+s*.9}" width="{s}" height="{s*.1}" rx="{s*.05}" fill="#000" opacity=".22"/></g>')
        return g
    d = (lin("sky", [(0, "#060b22"), (.6, "#18244f"), (1, "#5b3e66")])
         + lin("slab", [(0, "#f8f3e8"), (.55, "#ebe2cf"), (1, "#cfc0a3")])
         + rad("gloss", [(0, "rgba(255,255,255,.6)"), (.35, "rgba(255,255,255,0)")], cx="28%", cy="20%", r="60%")
         + rad("terra", [(0, "#e08a5c"), (.62, "#b9582f"), (1, "#6f2e14")], cy="50%", r="55%")
         + rad("glaze", [(0, "#fffdf6"), (.6, "#fbf9f3"), (1, "#e4ded0")], cx="40%", cy="35%")
         + lin("ttl", [(0, "#ffffff"), (1, "#dfe6ff")]))
    for c in order:
        d += lin("g" + c, [(0, T[c][0]), (1, T[c][1])], 1, 1)
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(77, 70, y1=420, op=(.2, .8)),
         '<circle cx="92" cy="214" r="70" fill="#f2ecd8" opacity=".12"/><circle cx="92" cy="214" r="24" fill="#f2ecd8"/>']
    # rooftops
    import random as _r
    rr = _r.Random(7); x = -20; roofs = []
    while x < 620:
        w = 50 + rr.random() * 60; h = 40 + rr.random() * 90; top = 800 - 110 - h
        roofs.append(f'<rect x="{x:.0f}" y="{top:.0f}" width="{w:.0f}" height="{h+120:.0f}" fill="#222a4d"/><path d="M{x-4:.0f} {top:.0f}L{x+w/2:.0f} {top-14-rr.random()*14:.0f}L{x+w+4:.0f} {top:.0f}Z" fill="#262848"/>')
        wy = top + 14
        while wy < 760:
            wx = x + 9
            while wx < x + w - 14:
                if rr.random() < .35: roofs.append(f'<rect x="{wx:.0f}" y="{wy:.0f}" width="8" height="13" rx="4" fill="#ffcf74" opacity="{.95 if rr.random() < .6 else .35}"/>')
                wx += 20
            wy += 28
        x += w + 4
    b.append("".join(roofs))
    # title
    b.append(text(300, 118, "Azulejos", "Unbounded", 70, "url(#ttl)", 900, ls=-1.5, extra='filter="url(#k-drop)" stroke="#0f2363" stroke-width="2" paint-order="stroke"'))
    b.append(text(300, 160, "Draft tiles, decorate the wall", "Figtree", 25, "#c8c2dc", 800))
    # limestone wall board, tilted
    bx, by, cs = 150, 222, 64
    board = [rect(bx - 22, by + 8, 5 * cs + 44, 5 * cs + 44, "#9d8c6c", 22), rect(bx - 22, by - 22, 5 * cs + 44, 5 * cs + 44, "url(#slab)", 22)]
    placed = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (2, 2), (2, 3), (3, 0), (3, 3), (4, 4), (2, 1), (1, 4)}
    for r in range(5):
        for c in range(5):
            col = order[(c - r + 5) % 5]
            x, y = bx + c * cs + 3, by + r * cs + 3
            board.append(rect(x, y, cs - 6, cs - 6, "#8a7656", 9, 'opacity=".45"'))
            if (r, c) in placed:
                board.append(tile(x + 1, y + 1, cs - 8, col))
            else:
                board.append(tile(x + 3, y + 3, cs - 12, col, op=.3))
    b.append(f'<g transform="rotate(-6 300 400)" filter="url(#k-drop)">{"".join(board)}</g>')
    # a tile flying onto the wall + shards
    b.append(tile(452, 222, 70, "K", rot=14))
    b.append('<path d="M452 300 q-30 40 -86 52" fill="none" stroke="#f6dc96" stroke-width="3" stroke-dasharray="4 9" opacity=".7"/>')
    # terracotta plate with four tiles
    px, py, pr = 168, 600, 108
    b.append(f'<circle cx="{px}" cy="{py+10}" r="{pr}" fill="#4f1f0c"/><circle cx="{px}" cy="{py}" r="{pr}" fill="url(#terra)"/><circle cx="{px}" cy="{py}" r="{pr*.78}" fill="url(#glaze)"/>'
             f'<circle cx="{px}" cy="{py}" r="{pr*.72}" fill="none" stroke="#1d3f9e" stroke-width="3" stroke-dasharray="6 7" opacity=".4"/>')
    for i, c in enumerate("BBTY"):
        b.append(tile(px - 58 + (i % 2) * 60, py - 58 + (i // 2) * 60, 54, c, rot=(-4, 3, 5, -3)[i]))
    # first-player coin
    b.append('<circle cx="330" cy="660" r="30" fill="#5a400f"/><circle cx="330" cy="654" r="30" fill="#cfa449"/><circle cx="324" cy="648" r="20" fill="#f6dc96" opacity=".6"/>')
    b.append(text(330, 669, "1", "Unbounded", 34, "#4a3207", 900))
    # broken tile shards
    for (sx, sy, rot, c) in ((430, 650, 20, "R"), (470, 676, -30, "R"), (452, 700, 60, "T")):
        b.append(f'<path d="M{sx} {sy} l18 -6 l-6 20 z" fill="{T[c][0]}" transform="rotate({rot} {sx} {sy})" stroke="#fff" stroke-opacity=".5"/>')
    b.append(footer("2–4 TEAMS  ·  TILE DRAFTING", "Figtree", "#c8c2dc", 15, 4, y=778, weight=800))
    return svg(d, "".join(b))

COVERS = {
    "alphabet": alphabet, "back-to-board": back_to_board, "bear-park": bear_park, "bingo": bingo, "bluff": bluff,
    "azulejos": azulejos, "cant-stop": cant_stop, "boardgame": cefr_quest, "chain": chain, "city": city, "classroom-auction": classroom_auction,
    "connect": connect, "control-deck": control_deck, "crown-lands": crown_lands, "deal-no-deal": deal_no_deal, "deep-cover": deep_cover,
}
