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
    d = rad("bg", [(0, "#1e2733"), (1, "#0d1117")], cy="35%") + lin("amb", [(0, "#fbbf24"), (1, "#d97706")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 108, "Back to", "Sora", 62, "#f5f7fa", 800))
    b.append(text(300, 176, 'the <tspan fill="url(#amb)">Board</tspan>', "Sora", 62, "#f5f7fa", 800))
    # board
    b.append(f'<g filter="url(#k-drop)">{rect(70, 220, 460, 230, "#1d3b33", 10, "stroke=\"#8a6a3a\" stroke-width=\"10\"")}</g>')
    b.append(text(300, 318, "Things that fly", "Caveat", 56, "#f4f1e8", 700))
    b.append('<path d="M150 345 q 150 -12 300 0" stroke="#f4f1e8" stroke-width="3" fill="none" opacity=".7"/>')
    b.append(text(300, 395, "?  ?  ?", "Caveat", 40, "#f59e0b", 700))
    b.append(rect(120, 452, 360, 10, "#8a6a3a", 3))
    # chair + student from behind
    b.append('<g transform="translate(300 600)">'
             '<rect x="-62" y="-40" width="124" height="100" rx="16" fill="#0d9488" stroke="#064e48" stroke-width="4"/>'
             '<rect x="-50" y="60" width="10" height="60" fill="#3a4555"/><rect x="40" y="60" width="10" height="60" fill="#3a4555"/>'
             '<path d="M-56 -40 Q -60 -92 0 -96 Q 60 -92 56 -40 Z" fill="#334155"/>'
             '<circle cx="0" cy="-122" r="36" fill="#1f2937"/>'
             '<path d="M-36 -126 Q 0 -168 36 -126 Q 20 -140 0 -142 Q -20 -140 -36 -126 Z" fill="#111827"/>'
             '</g>')
    # team bubbles
    def bubble(x, y, w, word, col, tail):
        tx = x + (20 if tail == "l" else w - 20)
        return (f'<g filter="url(#k-drop-s)">{rect(x, y, w, 52, col, 26)}'
                f'<polygon points="{tx-10},{y+48} {tx+10},{y+48} {tx + (-14 if tail=="l" else 14)},{y+72}" fill="{col}"/></g>'
                + text(x + w/2, y + 35, word, "Sora", 24, "#0d1117", 800))
    b.append(bubble(28, 500, 140, "BIRD!", "#2dd4bf", "l"))
    b.append(bubble(432, 492, 140, "PLANE!", "#fbbf24", "r"))
    b.append(bubble(24, 640, 120, "KITE!", "#f59e0b", "l"))
    b.append(bubble(452, 636, 130, "BEE!", "#2dd4bf", "r"))
    b.append(footer("100 CATEGORIES · A1–B2", "Sora", "#95a5b8", 14, 4, 784))
    return svg(d, "".join(b))


def bear_park():
    d = lin("park", [(0, "#5f8f45"), (1, "#3f6b2f")]) + lin("amb", [(0, "#ffd27a"), (1, "#f3b33d")])
    b = [rect(0, 0, 600, 800, "#10161d")]
    # park board
    cs = 60
    x0, y0, cols, rows = 30, 230, 9, 9
    b.append(rect(x0 - 8, y0 - 8, cols * cs + 16, rows * cs + 16, "#33414f", 14))
    for r in range(rows):
        for c in range(cols):
            b.append(rect(x0 + c*cs + 1.5, y0 + r*cs + 1.5, cs - 3, cs - 3, "#6a9a4c" if (r + c) % 2 else "#5f8f45", 6))
    pieces = [  # (cells, color)
        ([(0, 0), (0, 1), (1, 0), (1, 1)], "#4fa3e0"),            # polar enclosure
        ([(0, 2), (0, 3), (0, 4), (1, 3)], "#e9a23b"),            # T
        ([(2, 0), (3, 0), (4, 0), (4, 1)], "#d8604a"),            # L
        ([(1, 4), (1, 5), (2, 5), (2, 6)], "#a77bd6"),            # S
        ([(0, 5), (0, 6), (0, 7), (0, 8)], "#5bbfa8"),            # I
        ([(2, 1), (2, 2), (3, 1)], "#e8d36a"),
        ([(5, 0), (5, 1), (6, 0), (6, 1), (7, 0)], "#c97b4a"),
        ([(1, 7), (1, 8), (2, 8)], "#e86f9b"),
    ]
    for cells, col in pieces:
        for (r, c) in cells:
            b.append(rect(x0 + c*cs + 2, y0 + r*cs + 2, cs - 4, cs - 4, col, 7, 'stroke="#1d232b" stroke-opacity=".5" stroke-width="2"'))
        b.append("".join(rect(x0 + c*cs + 6, y0 + r*cs + 6, cs - 12, 8, "#fff", 4, 'opacity=".25"') for (r, c) in cells))
    # little park icons
    b.append(emoji(x0 + 3*cs + cs/2, y0 + 3*cs + 42, "🌳", 36) + emoji(x0 + 6*cs + cs/2, y0 + 4*cs + 42, "🪵", 32)
             + emoji(x0 + 5*cs + cs/2, y0 + 6*cs + 42, "🌼", 30))
    # big bear head
    b.append('<g transform="translate(420 600)" filter="url(#k-drop)">'
             '<circle cx="-62" cy="-62" r="34" fill="#8b5a2b"/><circle cx="62" cy="-62" r="34" fill="#8b5a2b"/>'
             '<circle cx="-62" cy="-62" r="17" fill="#d9a46a"/><circle cx="62" cy="-62" r="17" fill="#d9a46a"/>'
             '<circle cx="0" cy="0" r="96" fill="#9c6633"/>'
             '<ellipse cx="0" cy="34" rx="50" ry="38" fill="#e2b77f"/>'
             '<ellipse cx="0" cy="16" rx="18" ry="13" fill="#2b1a10"/>'
             '<path d="M0 30 v14 M-14 50 q 14 12 28 0" stroke="#2b1a10" stroke-width="5" fill="none" stroke-linecap="round"/>'
             '<circle cx="-36" cy="-18" r="10" fill="#2b1a10"/><circle cx="36" cy="-18" r="10" fill="#2b1a10"/>'
             '<circle cx="-33" cy="-21" r="3.5" fill="#fff"/><circle cx="39" cy="-21" r="3.5" fill="#fff"/>'
             '</g>')
    # title panel
    b.append(f'<g filter="url(#k-drop)">{rect(40, 44, 520, 150, "#1d232b", 18, "stroke=\"#f3b33d\" stroke-width=\"3\"")}</g>')
    b.append(text(300, 134, "Bear Park", "Fredoka", 86, "url(#amb)", 700))
    b.append(text(300, 172, "BUILD THE BEST BEAR PARK", "Inter", 15, "#aab5c3", 800, ls=4))
    b.append(rect(0, 750, 600, 50, "#10161d", 0, 'opacity=".85"') + footer("TILE PUZZLE · 2–4 TEAMS", "Inter", "#f3b33d", 14, 4, 782, 800))
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
    d = rad("bg", [(0, "#2a2140"), (1, "#0f0e17")], cy="45%") + lin("org", [(0, "#ffd166"), (1, "#ff6b35")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append('<circle cx="300" cy="470" r="230" fill="#ff6b35" opacity=".10" filter="url(#k-glow)"/>')
    b.append(text(300, 96, "CLASSROOM", "Bebas Neue", 38, "#a7a9be", ls=12))
    b.append(text(300, 220, "AUCTION", "Bebas Neue", 156, "url(#org)", ls=4, extra='filter="url(#k-drop)"'))
    # gavel
    b.append('<g transform="translate(300 470) rotate(-35)" filter="url(#k-drop)">'
             '<rect x="-14" y="-10" width="28" height="210" rx="10" fill="#8b4a22" stroke="#3a1c0c" stroke-width="4"/>'
             '<rect x="-90" y="-80" width="180" height="76" rx="18" fill="#a85a2a" stroke="#3a1c0c" stroke-width="5"/>'
             '<rect x="-96" y="-84" width="26" height="84" rx="8" fill="#ffd166" stroke="#3a1c0c" stroke-width="4"/>'
             '<rect x="70" y="-84" width="26" height="84" rx="8" fill="#ffd166" stroke="#3a1c0c" stroke-width="4"/>'
             '</g>')
    b.append('<ellipse cx="300" cy="640" rx="130" ry="22" fill="#000" opacity=".4"/>'
             + rect(200, 600, 200, 40, "#6b3a1c", 10, 'stroke="#3a1c0c" stroke-width="4"'))
    # paddles
    def paddle(x, y, rot, n, col):
        return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop-s)">'
                '<rect x="-7" y="30" width="14" height="80" rx="6" fill="#d9c4a0"/>'
                f'<circle cx="0" cy="0" r="46" fill="{col}" stroke="#fffffe" stroke-width="5"/>'
                + text(0, 15, n, "Bebas Neue", 46, "#fffffe") + "</g>")
    b.append(paddle(90, 390, -18, "12", "#ef476f") + paddle(510, 380, 16, "7", "#06d6a0") + paddle(110, 640, -8, "23", "#ffd166")
             + paddle(490, 650, 10, "4", "#ff6b35"))
    b.append(text(300, 300, "GOING… GOING… GONE!", "Nunito", 22, "#fffffe", 900, ls=3))
    b.append(footer("BID · PROVE IT · WIN", "Bebas Neue", "#ffd166", 26, 8, 772, 400))
    return svg(d, "".join(b))


def connect():
    d = lin("tt", [(0, "#ff3355"), (.5, "#ffd700"), (1, "#0099ff")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#0a0a0f")]
    b.append('<circle cx="0" cy="500" r="260" fill="#ff3355" opacity=".14" filter="url(#k-glow)"/><circle cx="600" cy="500" r="260" fill="#0099ff" opacity=".14" filter="url(#k-glow)"/>')
    b.append(glow_text(300, 142, "CONNECT", "Bebas Neue", 132, "url(#tt)", "#ffd700", ls=8))
    b.append(text(300, 186, "WORD BATTLE ARENA", "Barlow Condensed", 22, "#e8e8f0", 700, ls=8))
    grid = ["SCRANEW", "TOMBLID", "ARIVETH", "RAPENOS", "ECLOUDA", "MOSTRAP", "PLINKER"]
    red = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (2, 2), (3, 3), (3, 2), (4, 1)}
    blue = {(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (2, 5), (3, 5), (1, 6)}
    cs, g = 66, 6
    x0, y0 = (600 - 7 * cs - 6 * g) / 2, 230
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            x, y = x0 + c * (cs + g), y0 + r * (cs + g)
            if (r, c) in red:
                fill, ink, st = "#cc0022", "#fff", "#ff3355"
            elif (r, c) in blue:
                fill, ink, st = "#0055cc", "#fff", "#0099ff"
            else:
                fill, ink, st = "#13131a", "#c8c8d6", "#2a2a3a"
            b.append(rect(x, y, cs, cs, fill, 8, f'stroke="{st}" stroke-width="2"') + text(x + cs/2, y + cs/2 + 14, ch, "Bebas Neue", 40, ink))
    b.append(footer("7×7 · TEAMS · POWERS", "Barlow Condensed", "#ffd700", 20, 8, 778))
    return svg(d, "".join(b))


def control_deck():
    d = lin("hous", [(0, "#26313a"), (1, "#161d22")])
    b = [rect(0, 0, 600, 800, "#0c1114")]
    stripes = "".join(f'<polygon points="{x},0 {x+20},0 {x-4},24 {x-24},24" fill="#f6d94a"/>' for x in range(0, 640, 40))
    b.append(f'<g>{rect(0, 0, 600, 24, "#111")}{stripes}</g>')
    b.append(text(40, 78, "● VOICE-COMMAND CONSOLE", "Space Mono", 14, "#2fd8c9", 700, "start", 2))
    b.append(text(40, 156, "CONTROL", "Bricolage Grotesque", 88, "#eef4f5", 800, "start"))
    b.append(text(40, 240, "DECK", "Bricolage Grotesque", 88, "#eef4f5", 800, "start"))
    # LED readout
    b.append(rect(40, 268, 520, 64, "#090d10", 8, 'stroke="#2c3941" stroke-width="2"'))
    b.append(glow_text(60, 310, "SET COOLANT TO 7", "Space Mono", 26, "#ffb648", "#ffb648", 700, 3, anchor="start"))
    # panel
    b.append(f'<g filter="url(#k-drop)">{rect(30, 356, 540, 400, "url(#hous)", 18, "stroke=\"#2c3941\" stroke-width=\"3\"")}</g>')
    # dials
    def dial(x, y, ang, label, col):
        a = math.radians(ang)
        ticks = "".join(f'<line x1="{x+52*math.cos(math.radians(t)):.1f}" y1="{y+52*math.sin(math.radians(t)):.1f}" '
                        f'x2="{x+60*math.cos(math.radians(t)):.1f}" y2="{y+60*math.sin(math.radians(t)):.1f}" stroke="#8fa1a9" stroke-width="2"/>'
                        for t in range(135, 406, 27))
        return (ticks + f'<circle cx="{x}" cy="{y}" r="44" fill="#2a353d" stroke="#0c1114" stroke-width="4"/>'
                f'<circle cx="{x}" cy="{y}" r="34" fill="#1f272e"/>'
                f'<line x1="{x}" y1="{y}" x2="{x+30*math.cos(a):.1f}" y2="{y+30*math.sin(a):.1f}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>'
                + text(x, y + 84, label, "Space Mono", 13, "#8fa1a9", 700, ls=2))
    b.append(dial(130, 450, 300, "COOLANT", "#ffb648") + dial(300, 450, 200, "THRUST", "#2fd8c9") + dial(470, 450, 30, "PRESSURE", "#ff6f6f"))
    # sliders
    for i, (v, col, lab) in enumerate([(.3, "#43d17a", "O2"), (.75, "#f6d94a", "FUEL"), (.55, "#2fd8c9", "SHIELD")]):
        y = 600 + i * 46
        b.append(text(64, y + 6, lab, "Space Mono", 13, "#8fa1a9", 700, "start"))
        b.append(rect(150, y - 4, 250, 10, "#090d10", 5) + rect(150, y - 4, 250 * v, 10, col, 5)
                 + rect(150 + 250 * v - 12, y - 16, 24, 34, "#d4dde0", 5, 'stroke="#0c1114" stroke-width="3"'))
    # switches
    for i, on in enumerate([1, 0, 1]):
        x = 440 + i * 38
        col = "#43d17a" if on else "#ef4444"
        b.append(rect(x, 590, 26, 96, "#090d10", 13) + f'<circle cx="{x+13}" cy="{(608 if on else 668)}" r="13" fill="#d4dde0"/>'
                 + f'<circle cx="{x+13}" cy="706" r="5" fill="{col}"/>')
    b.append(f'<g>{rect(0, 776, 600, 24, "#111")}<g transform="translate(0 776)">{stripes}</g></g>')
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


COVERS = {
    "alphabet": alphabet, "back-to-board": back_to_board, "bear-park": bear_park, "bingo": bingo, "bluff": bluff,
    "cant-stop": cant_stop, "boardgame": cefr_quest, "chain": chain, "city": city, "classroom-auction": classroom_auction,
    "connect": connect, "control-deck": control_deck, "crown-lands": crown_lands, "deal-no-deal": deal_no_deal, "deep-cover": deep_cover,
}
