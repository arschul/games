"""Batch E covers."""
import math, random
from kit import *


def ring_of_gems():
    d = rad("bg", [(0, "#22201a"), (1, "#0a0a09")], cy="45%") + lin("gold", [(0, "#f3dc94"), (1, "#c9a24b")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 104, "Ring of Gems", "Cinzel", 64, "url(#gold)", 700, extra='filter="url(#k-drop)"'))
    b.append(text(300, 146, "Match the pairs before the rings turn", "Patrick Hand", 26, "#eae4d6"))
    cx, cy = 300, 470
    gems = ["#ff6b6b", "#5ee6d3", "#f4d35e", "#a78bfa", "#60a5fa", "#4ade80"]
    rr = random.Random(5)
    for ring, (R, n, stone) in enumerate([(250, 18, "#4a453c"), (172, 12, "#5a544a"), (96, 6, "#6a6458")]):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{stone}" stroke-width="64"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{R+32}" fill="none" stroke="#000" stroke-opacity=".35" stroke-width="2"/>')
        for k in range(n):
            a = math.radians(k * 360 / n + ring * 9)
            x, y = cx + R * math.cos(a), cy + R * math.sin(a)
            up = rr.random() < .3
            if up:
                col = gems[rr.randrange(6)]
                b.append(f'<polygon points="{x},{y-20} {x+16},{y-4} {x},{y+20} {x-16},{y-4}" fill="{col}" stroke="#fff" stroke-width="2" filter="url(#k-drop-s)"/>'
                         f'<polygon points="{x},{y-20} {x+16},{y-4} {x-16},{y-4}" fill="#fff" opacity=".35"/>')
            else:
                b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="17" fill="#2a2620" stroke="#c9a24b" stroke-opacity=".6" stroke-width="2"/>')
    # rotation arrows
    for (R, a0, sweep) in [(250, -60, 40), (172, 140, -40)]:
        a1, a2 = math.radians(a0), math.radians(a0 + sweep)
        x1, y1, x2, y2 = cx + (R+44)*math.cos(a1), cy + (R+44)*math.sin(a1), cx + (R+44)*math.cos(a2), cy + (R+44)*math.sin(a2)
        b.append(f'<path d="M{x1:.1f} {y1:.1f} A {R+44} {R+44} 0 0 {1 if sweep>0 else 0} {x2:.1f} {y2:.1f}" fill="none" stroke="#f4d35e" stroke-width="4" stroke-linecap="round"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="56" fill="#1a1814" stroke="#c9a24b" stroke-width="3"/>' + emoji(cx, cy + 16, "💎", 46))
    return svg(d, "".join(b))


def save_the_cheese():
    d = (lin("wall", [(0, "#182033"), (1, "#26324c")])
         + '<pattern id="wp" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M30 4 L39 30 L30 56 L21 30Z" fill="#ffffff" fill-opacity=".04"/></pattern>'
         + lin("sky", [(0, "#0a1430"), (1, "#2a3a66")])
         + lin("wood", [(0, "#c99158"), (.55, "#a96f3b"), (1, "#8a5a2e")])
         + lin("board", [(0, "#e2b57e"), (.6, "#c99258"), (1, "#b07a46")])
         + lin("cube", [(0, "#ffe384"), (.55, "#f4c542"), (1, "#e3a92e")])
         + lin("cTop", [(0, "#fff0a8"), (1, "#ffd75e")], x2=1) + lin("cFront", [(0, "#ffd457"), (1, "#e9b434")])
         + lin("cBack", [(0, "#d9a02a"), (1, "#b9821c")], x2=1, y2=0)
         + rad("fur", [(0, "#d3cdc6"), (.55, "#9f968e"), (1, "#5d554f")], cx="40%", cy="28%", r="80%")
         + rad("ear", [(0, "#ffd0d4"), (1, "#e58a96")], cx="45%", cy="40%", r="60%")
         + rad("hole", [(0, "#05070b"), (.8, "#14100c"), (1, "#2a1b10")], cx="50%", cy="70%", r="70%")
         + lin("tile", [(0, "#fdfbf6"), (1, "#e8e1d2")]) + lin("herb", [(0, "#72bd6b"), (1, "#3f8a3b")]))
    b = [rect(0, 0, 600, 800, "url(#wall)"), rect(0, 0, 600, 470, "url(#wp)")]
    outline = 'stroke="#5b3a0c" stroke-width="10" stroke-linejoin="round" paint-order="stroke"'
    b.append(text(300, 96, "Save the", "Lilita One", 64, "#f3ead2", extra='stroke="#0d1322" stroke-width="8" paint-order="stroke"'))
    b.append(text(300, 196, "Cheese!", "Lilita One", 112, "#f4c542", extra=outline))
    # window with moon
    win = ['<g transform="translate(396 236)">', rect(-12, -12, 184, 160, "url(#wood)", 6), rect(0, 0, 160, 136, "url(#sky)")]
    import random as _r
    rr = _r.Random(7)
    for _ in range(18):
        win.append(f'<circle cx="{rr.uniform(4,156):.1f}" cy="{rr.uniform(4,132):.1f}" r="{rr.uniform(.6,1.6):.2f}" fill="#fff" opacity="{rr.uniform(.3,1):.2f}"/>')
    win.append('<circle cx="112" cy="44" r="38" fill="#f3e9c6" opacity=".12"/><circle cx="112" cy="44" r="20" fill="#f3e9c6"/>')
    win.append(rect(76, 0, 8, 136, "url(#wood)") + rect(0, 64, 160, 8, "url(#wood)") + rect(-18, 132, 196, 14, "url(#wood)", 3) + "</g>")
    b.append("".join(win))
    # mouse hole
    b.append('<path d="M26 470 V420 A58 58 0 0 1 142 420 V470Z" fill="#7a4a22"/><path d="M36 470 V422 A48 48 0 0 1 132 422 V470Z" fill="url(#hole)"/>')
    # counter
    b.append(rect(0, 468, 600, 74, "url(#wood)"))
    for x in range(0, 600, 96):
        b.append(f'<rect x="{x+94}" y="468" width="2" height="74" fill="#3c1c08" opacity=".3"/>')
    b.append('<rect x="0" y="468" width="600" height="3" fill="#ffecd0" opacity=".55"/><rect x="0" y="482" width="600" height="2" fill="#3c1c08" opacity=".3"/>')
    for x in (232, 290):
        b.append(f'<g fill="#f1ead8" opacity=".8"><ellipse cx="{x}" cy="476" rx="7" ry="5"/><circle cx="{x-7}" cy="469" r="2.6"/><circle cx="{x}" cy="466" r="2.6"/><circle cx="{x+7}" cy="469" r="2.6"/></g>')
    # cheese on plate
    b.append('<ellipse cx="470" cy="470" rx="124" ry="14" fill="#2f5d9c"/><ellipse cx="470" cy="468" rx="116" ry="11" fill="#f6f3ec"/>')
    b.append('<g transform="translate(360 300) scale(.82)" filter="url(#k-drop-s)">'
             '<polygon points="16,176 16,152 246,76 246,180" fill="url(#cFront)"/><polygon points="16,152 246,76 268,64 40,142" fill="url(#cTop)"/>'
             '<polygon points="246,76 268,64 268,168 246,180" fill="url(#cBack)"/>'
             '<g fill="#d39a22" opacity=".85"><ellipse cx="86" cy="156" rx="13" ry="10"/><ellipse cx="148" cy="132" rx="17" ry="13"/><ellipse cx="206" cy="152" rx="14" ry="11"/><ellipse cx="200" cy="108" rx="9" ry="7"/><ellipse cx="232" cy="124" rx="7" ry="9"/></g>'
             '<path d="M16 152 L246 76" stroke="#fff" stroke-opacity=".7" stroke-width="3"/></g>')
    # mouse
    b.append('<g transform="translate(150 360) scale(.95)" filter="url(#k-drop-s)">'
             '<path d="M36 92 C 10 100, 2 78, 16 66 C 26 58, 22 46, 12 40" fill="none" stroke="#e5a3a8" stroke-width="5" stroke-linecap="round"/>'
             '<ellipse cx="62" cy="114" rx="14" ry="5" fill="#e9a7ad"/><ellipse cx="112" cy="114" rx="14" ry="5" fill="#e9a7ad"/>'
             '<ellipse cx="82" cy="82" rx="54" ry="33" fill="url(#fur)"/><circle cx="112" cy="40" r="20" fill="#8d847c"/><circle cx="112" cy="40" r="13" fill="url(#ear)"/>'
             '<ellipse cx="130" cy="70" rx="31" ry="25" fill="url(#fur)"/><path d="M150 58 Q174 70 170 80 Q158 88 140 84 Z" fill="url(#fur)"/>'
             '<circle cx="170" cy="78" r="6" fill="#f08a9a"/><circle cx="142" cy="63" r="6" fill="#1d1820"/><circle cx="144" cy="61" r="2" fill="#fff"/>'
             '<g stroke="#3b3430" stroke-width="1.6" stroke-linecap="round" opacity=".8"><path d="M160 82 L186 76"/><path d="M160 85 L186 88"/><path d="M158 87 L180 98"/></g></g>')
    # cheese board with cubes
    b.append('<g filter="url(#k-drop)">' + rect(28, 572, 544, 120, "url(#board)", 24) + "</g>")
    b.append('<circle cx="540" cy="632" r="13" fill="#1a2a37"/>')
    word, shown = "CHEESE", set("CE")
    for k, ch in enumerate(word):
        x, y = 50 + k * 76, 590
        b.append(rect(x, y, 66, 74, "#2c1a0c", 10))
        if ch in shown:
            b.append(rect(x - 3, y - 5, 72, 78, "#b9821c", 11) + rect(x - 3, y - 7, 72, 74, "url(#cube)", 11)
                     + f'<circle cx="{x+9}" cy="{y+4}" r="3.5" fill="#c4821a" opacity=".6"/><circle cx="{x+60}" cy="{y+58}" r="5" fill="#c4821a" opacity=".55"/>'
                     + text(x + 33, y + 54, ch, "Lilita One", 52, "#5b3a0c"))
        else:
            b.append(f'<rect x="{x+14}" y="{y+58}" width="38" height="4" rx="2" fill="#f4c542" opacity=".35"/>')
    # delft tiles
    for k, ch in enumerate("QWERTY"):
        x, y = 44 + k * 88, 714
        fill, ink = ("url(#herb)", "#fff") if ch == "E" else (("#8e897f", "#cfcac0") if ch in "QT" else ("url(#tile)", "#24508e"))
        frame = "#24561f" if ch == "E" else ("#5f5b54" if ch in "QT" else "#2f5d9c")
        b.append(f'<g filter="url(#k-drop-s)">' + rect(x, y, 76, 70, fill, 10) + "</g>"
                 + f'<rect x="{x+5}" y="{y+5}" width="66" height="60" rx="7" fill="none" stroke="{frame}" stroke-width="2.5"/>'
                 + text(x + 38, y + 52, ch, "Lilita One", 44, ink))
        if ch in "QT":
            b.append(f'<line x1="{x+14}" y1="{y+52}" x2="{x+62}" y2="{y+18}" stroke="#e2412f" stroke-width="6" stroke-linecap="round"/>')
    return svg(d, "".join(b))


def scattergories():
    d = (rad("lamp", [(0, "#4a4a52"), (.55, "#1d2740"), (1, "#0d1322")], cx="60%", cy="38%", r="80%")
         + lin("paper", [(0, "#f4df7a"), (1, "#ebcf5f")])
         + lin("brass", [(0, "#f3d68a"), (.55, "#c99a3b"), (1, "#76561a")])
         + lin("flapT", [(0, "#3d424d"), (1, "#2e323b")]) + lin("flapB", [(0, "#2a2e36"), (1, "#1e2229")])
         + lin("sand", [(0, "#f2cf86"), (1, "#c9924a")]))
    b = [rect(0, 0, 600, 800, "url(#lamp)"), '<rect x="12" y="12" width="576" height="776" rx="22" fill="none" stroke="#c99a3b" stroke-opacity=".38" stroke-width="2" stroke-dasharray="8 6"/>']
    b.append(text(300, 112, "Scattergories", "Anton", 84, "#f4df7a", ls=1))
    # legal pad
    b.append('<g transform="rotate(3 400 520)">' + rect(232, 300, 330, 430, "#d9be55", 6, 'filter="url(#k-drop)"') + "</g>")
    b.append('<g transform="rotate(1.5 400 520)" filter="url(#k-drop-s)">' + rect(222, 290, 330, 430, "url(#paper)", 6))
    for k in range(8):
        y = 372 + k * 44
        b.append(f'<line x1="222" y1="{y}" x2="552" y2="{y}" stroke="#7aa6d6" stroke-width="2"/>')
    b.append('<line x1="268" y1="290" x2="268" y2="720" stroke="#d2352b" stroke-width="2"/><line x1="273" y1="290" x2="273" y2="720" stroke="#d2352b" stroke-width="2"/>')
    b.append(rect(214, 278, 346, 40, "#6a2421", 8))
    rows = [("Animals", "the bear", 3), ("Sports", "baseball", 3), ("Fruit", "kiwi", 1), ("Jobs", "plumber", 2), ("Colors", "blue", 3)]
    for k, (c, a, pts) in enumerate(rows):
        y = 362 + k * 44 + 44
        b.append(text(250, y - 10, k + 1, "Caveat", 26, "#d2352b", 700))
        b.append(text(288, y - 12, c, "Figtree", 20, "#1d2742", 800, "start"))
        b.append(text(392, y - 10, a, "Caveat", 26, "#1d2742", 700, "start"))
        cx = 522
        b.append(f'<circle cx="{cx}" cy="{y-18}" r="15" fill="#e2b047" stroke="#76561a" stroke-width="2"/>' + text(cx, y - 10, pts, "Anton", 19, "#2a1d05"))
    b.append("</g>")
    # split-flap letter
    b.append(f'<g filter="url(#k-drop)">{rect(40, 170, 200, 250, "#1b1e25", 18, "stroke=\"#c99a3b\" stroke-width=\"6\"")}</g>')
    b.append(rect(62, 190, 156, 100, "url(#flapT)", 10) + rect(62, 290, 156, 100, "url(#flapB)", 10))
    b.append('<clipPath id="ft"><rect x="62" y="190" width="156" height="100"/></clipPath><clipPath id="fb"><rect x="62" y="291" width="156" height="99"/></clipPath>')
    b.append(text(140, 372, "B", "Anton", 196, "#f3e9cf", extra='clip-path="url(#ft)"') + text(140, 372, "B", "Anton", 196, "#f3e9cf", extra='clip-path="url(#fb)"'))
    b.append('<rect x="56" y="289" width="168" height="3" fill="#0c0e12"/><rect x="52" y="284" width="9" height="12" rx="3" fill="url(#brass)"/><rect x="219" y="284" width="9" height="12" rx="3" fill="url(#brass)"/>')
    b.append(rect(90, 398, 100, 14, "url(#brass)", 4))
    # hourglass
    hx, hy = 70, 470
    g = (f'<g transform="translate({hx} {hy}) scale(.7)">'
         '<path d="M52 36 C52 112 102 138 107 160 C102 182 52 208 52 284 L168 284 C168 208 118 182 113 160 C118 138 168 112 168 36 Z" fill="rgba(200,225,255,.14)" stroke="rgba(255,255,255,.55)" stroke-width="3"/>'
         '<clipPath id="ht"><path d="M52 36 C52 112 102 138 107 160 L113 160 C118 138 168 112 168 36 Z"/></clipPath>'
         '<clipPath id="hb"><path d="M107 160 C102 182 52 208 52 284 L168 284 C168 208 118 182 113 160 Z"/></clipPath>'
         '<rect x="40" y="105" width="140" height="60" fill="url(#sand)" clip-path="url(#ht)"/>'
         '<path d="M40 284 L40 250 Q110 222 180 250 L180 284Z" fill="url(#sand)" clip-path="url(#hb)"/>'
         '<line x1="110" y1="160" x2="110" y2="236" stroke="#e7b96a" stroke-width="4" stroke-dasharray="6 4"/>'
         '<rect x="26" y="24" width="10" height="272" rx="4" fill="url(#brass)"/><rect x="184" y="24" width="10" height="272" rx="4" fill="url(#brass)"/>'
         '<rect x="14" y="12" width="192" height="26" rx="9" fill="url(#brass)"/><rect x="14" y="282" width="192" height="26" rx="9" fill="url(#brass)"/></g>')
    b.append(g)
    # TIME! stamp
    b.append('<g transform="rotate(-9 330 230)" opacity=".92"><rect x="252" y="182" width="170" height="86" rx="10" fill="none" stroke="#d2352b" stroke-width="5"/>'
             '<rect x="260" y="190" width="154" height="70" rx="6" fill="none" stroke="#d2352b" stroke-width="2"/>' + text(337, 248, "TIME!", "Anton", 58, "#d2352b", ls=2) + "</g>")
    # team tents
    for k, (em, col) in enumerate([("🦁", "#e5483d"), ("🦅", "#2f7fe0"), ("🐝", "#f2b51d"), ("🐸", "#2fb36a")]):
        x = 40 + k * 134
        b.append(f'<g filter="url(#k-drop-s)">{rect(x, 742, 120, 40, col, 10)}</g>' + emoji(x + 24, 772, em, 24) + text(x + 92, 774, [12, 9, 15, 7][k], "Anton", 28, "#1d2742" if col == "#f2b51d" else "#fff"))
    return svg(d, "".join(b))


def scrambler():
    d = ""
    b = [rect(0, 0, 600, 800, "#f6f5fa"), '<circle cx="40" cy="760" r="220" fill="#ffd166" opacity=".25"/><circle cx="580" cy="80" r="200" fill="#7c5cfc" opacity=".12"/>']
    b.append(rect(190, 64, 220, 34, "#fff", 17, 'stroke="#ff6b35" stroke-width="2"') + text(300, 87, "ENGLISH STORIES", "DM Sans", 14, "#e8500f", 800, ls=3))
    b.append(text(300, 186, "Scrambler", "Syne", 60, "#14121c", 800))
    b.append(text(300, 238, "Put the story back in order.", "DM Sans", 21, "#6b6880", 500))
    tiles = [("the park", "#ffd166", -6), ("ran", "#06d6a0", 4), ("The dog", "#8f75ff", -3), ("to", "#ff6b35", 7), ("happily", "#ffd166", -5)]
    pos = [(80, 300), (330, 290), (150, 390), (420, 380), (250, 470)]
    for (w, col, rot), (x, y) in zip(tiles, pos):
        wd = 50 + len(w) * 22
        b.append(f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop-s)">{rect(0, 0, wd, 70, "#fff", 14, f"stroke=\"{col}\" stroke-width=\"5\"")}'
                 + text(wd/2, 46, w, "DM Sans", 32, "#14121c", 800) + "</g>")
    b.append(f'<g filter="url(#k-drop-s)">{rect(40, 600, 520, 72, "#14121c", 16)}</g>' + text(300, 646, "The dog ran happily to the park.", "DM Sans", 25, "#fff", 700))
    for k, (lv, col) in enumerate([("A1", "#c08c00"), ("A2", "#039873"), ("B1", "#6a48f0"), ("B2", "#e8500f")]):
        x = 90 + k * 110
        b.append(rect(x, 712, 90, 48, "#fff", 12, f'stroke="{col}" stroke-width="2.5"') + text(x + 45, 745, lv, "Syne", 24, col, 800))
    return svg(d, "".join(b))


def sentence_auction():
    d = lin("gold", [(0, "#fff0a8"), (1, "#e8a820")])
    b = [rect(0, 0, 600, 800, "#0a0a0f"), '<circle cx="300" cy="120" r="260" fill="#f5c842" opacity=".08" filter="url(#k-glow)"/>']
    b.append(glow_text(300, 112, "SENTENCE", "Bebas Neue", 108, "url(#gold)", "#f5c842", ls=6))
    b.append(glow_text(300, 210, "AUCTION", "Bebas Neue", 108, "url(#gold)", "#f5c842", ls=6))
    b.append(text(300, 248, "BID ON CORRECT SENTENCES", "DM Mono", 15, "#7777aa", 500, ls=4))
    lots = [("She don't like coffee.", False, "$300"), ("I have lived here for years.", True, "$650"), ("He go to school by bus.", False, "$200")]
    for k, (s, ok, bid) in enumerate(lots):
        y = 290 + k * 120
        b.append(f'<g filter="url(#k-drop-s)">{rect(40, y, 520, 100, "#12121a", 14, "stroke=\"#2a2a3d\" stroke-width=\"2\"")}</g>')
        b.append(text(64, y + 30, f"LOT 0{k+1}", "DM Mono", 13, "#7777aa", 500, "start", 3))
        b.append(text(64, y + 68, s, "DM Sans", 25, "#eeeef5", 600, "start"))
        b.append(rect(452, y + 46, 88, 38, "#f5c842", 8) + text(496, y + 72, bid, "Bebas Neue", 28, "#0a0a0f"))
        b.append(f'<circle cx="520" cy="{y+24}" r="14" fill="{"#2ecc71" if ok else "#e74c3c"}"/>' + text(520, y + 30, "✓" if ok else "✕", "DM Sans", 16, "#fff", 800))
    # money stack
    for k in range(5):
        b.append(rect(90 + k * 4, 700 - k * 14, 150, 30, "#2ecc71", 6, 'stroke="#145a32" stroke-width="2"'))
    b.append(text(170, 690, "$", "Bebas Neue", 30, "#145a32"))
    b.append(text(420, 724, "$1,000", "Bebas Neue", 76, "url(#gold)"))
    return svg(d, "".join(b))


def song_word_race():
    d = lin("org", [(0, "#ffd166"), (1, "#f5b400")]) + rad("bg", [(0, "#1c2538"), (1, "#0f1420")], cy="45%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 112, "Song Word", "Sora", 76, "#f4f6fb", 800))
    b.append(text(300, 196, "Race", "Sora", 96, "url(#org)", 800))
    b.append(text(300, 236, "RACE TO THE MIC · SING THE SONG", "Inter", 15, "#94a3b8", 800, ls=3))
    # mic
    b.append('<g transform="translate(300 450)" filter="url(#k-drop)">'
             '<rect x="-48" y="-120" width="96" height="150" rx="48" fill="#2a3550" stroke="#f5b400" stroke-width="5"/>'
             + "".join(f'<line x1="-40" y1="{-96+i*16}" x2="40" y2="{-96+i*16}" stroke="#4a5a80" stroke-width="3"/>' for i in range(8))
             + '<path d="M-74 -10 Q -74 74 0 74 Q 74 74 74 -10" fill="none" stroke="#c8d0e0" stroke-width="8"/>'
             '<rect x="-6" y="74" width="12" height="70" fill="#c8d0e0"/><rect x="-56" y="140" width="112" height="14" rx="7" fill="#c8d0e0"/></g>')
    for (x, y, s, rot) in [(120, 360, 50, -12), (480, 330, 56, 10), (150, 520, 40, 8), (470, 520, 46, -8)]:
        b.append(f'<g transform="rotate({rot} {x} {y})">' + text(x, y, "♪" if s % 2 else "♫", "Sora", s, "#ff6b6b", 800) + "</g>")
    b.append(f'<g filter="url(#k-drop)">{rect(110, 640, 380, 100, "#f4f6fb", 20)}</g>' + text(300, 708, "LOVE", "Sora", 62, "#0f1420", 800, ls=10))
    return svg(d, "".join(b))


def sound_off():
    d = rad("bg", [(0, "#16233b"), (1, "#0b1220")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 132, 'SOUND <tspan fill="#22d3ee">OFF</tspan>', "Sora", 80, "#f2f6fb", 800))
    b.append(text(300, 176, "MINIMAL-PAIR LISTENING BATTLE", "Inter", 16, "#94a3b8", 800, ls=4))
    # waveform
    rr = random.Random(2)
    bars = []
    for k in range(60):
        h = 10 + abs(math.sin(k * .35)) * 70 * rr.uniform(.5, 1)
        bars.append(rect(30 + k * 9, 300 - h/2, 5, h, "#22d3ee" if k < 34 else "#1d2d49", 2.5))
    b.append("".join(bars))
    pairs = [("ship", "sheep", "/ɪ/ vs /iː/"), ("think", "sink", "/θ/ vs /s/")]
    for k, (a, bb, ipa) in enumerate(pairs):
        y = 400 + k * 170
        b.append(f'<g filter="url(#k-drop)">{rect(40, y, 245, 140, "#16233b", 18, "stroke=\"#22d3ee\" stroke-width=\"3\"")}'
                 f'{rect(315, y, 245, 140, "#16233b", 18, "stroke=\"#a3e635\" stroke-width=\"3\"")}</g>')
        b.append(text(162, y + 84, a, "Sora", 46, "#f2f6fb", 800) + text(437, y + 84, bb, "Sora", 46, "#f2f6fb", 800))
        b.append(rect(240, y + 52, 120, 36, "#0b1220", 18, 'stroke="#2a3a5a" stroke-width="2"') + text(300, y + 76, "vs", "Sora", 18, "#94a3b8", 800))
        b.append(text(300, y + 166, ipa, "Inter", 17, "#a3e635", 600))
    b.append(emoji(530, 310, "🔊", 50))
    b.append(footer("TUNED FOR BRAZILIAN LEARNERS · A1–B2", "Inter", "#22d3ee", 13, 3, 784, 800))
    return svg(d, "".join(b))


def stairs():
    d = lin("bg", [(0, "#161d33"), (1, "#0e1220")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(emoji(80, 106, "⛰️", 54) + text(124, 120, "Stairs", "Playfair Display", 82, "#eef1f8", 900, "start"))
    b.append(text(300, 168, "Push your luck — bank before you fall.", "DM Sans", 20, "#9db8f2", 500))
    b.append(text(300, 200, "STAIRCASE CLIMBING CHALLENGE", "DM Sans", 13, "#ffcf5c", 800, ls=4))
    for side, (x0, dirn, col) in enumerate([(60, 1, "#5b8cff"), (540, -1, "#ff7a7a")]):
        for s in range(13):
            x = x0 + dirn * s * 18
            y = 730 - s * 34
            b.append(rect(min(x, x + dirn * 44) if dirn > 0 else x - 44, y, 44, 30, "#ffcf5c" if s % 4 else "#e8b23c", 6, 'stroke="#8a5a10" stroke-width="2"')
                     + text(x + dirn * 22, y + 22, s, "DM Sans", 16, "#2a1a04", 800))
        tok = 7 if side == 0 else 4
        tx = x0 + dirn * tok * 18 + dirn * 22
        ty = 730 - tok * 34 - 26
        b.append(f'<circle cx="{tx}" cy="{ty}" r="18" fill="{col}" stroke="#fff" stroke-width="4" filter="url(#k-drop-s)"/>')
        fx, fy = x0 + dirn * 12 * 18 + dirn * 22, 730 - 12 * 34 - 8
        b.append(f'<line x1="{fx}" y1="{fy}" x2="{fx}" y2="{fy-56}" stroke="#eef1f8" stroke-width="4"/><polygon points="{fx},{fy-56} {fx+dirn*34},{fy-44} {fx},{fy-32}" fill="#ff7a7a"/>')
    b.append(f'<g filter="url(#k-drop)">{rect(200, 560, 200, 110, "#1f2a47", 18, "stroke=\"#5b8cff\" stroke-width=\"3\"")}</g>'
             + text(300, 604, "ROLL OR BANK?", "DM Sans", 18, "#9db8f2", 800, ls=2) + emoji(300, 650, "🎲  🏦", 34))
    return svg(d, "".join(b))


def stop_twist():
    d = (lin("sky", [(0, "#0a1024"), (.6, "#1b1f3d"), (1, "#4a2d43")]) + lin("ylw", [(0, "#ffd23c"), (1, "#f2b414")])
         + lin("post", [(0, "#5d6168"), (.4, "#eef0f2"), (1, "#4d5157")], x2=1, y2=0) + lin("tile", [(0, "#2a2c31"), (1, "#0f1013")])
         + lin("plate", [(0, "#fdfcf7"), (1, "#dcd7c9")]) + lin("road", [(0, "#17181b"), (1, "#24262b")]))
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(31, 70, y1=330)]
    r = random.Random(5); x = -10; city = ""; wins = ""
    while x < 610:
        w = 40 + r.random() * 70; h = 50 + r.random() * 150
        city += rect(round(x), round(560 - h), round(w), round(h + 2), "#0c0f1c")
        for yy in range(int(560 - h + 12), 548, 18):
            for xx in range(int(x + 8), int(x + w - 10), 15):
                if r.random() < .22:
                    wins += rect(xx, yy, 6, 8, "#ffcf6b", extra='opacity=".7"')
        x += w + 3
    b.append(city + wins)
    b.append(rect(0, 556, 600, 244, "url(#road)") + rect(0, 552, 600, 7, "#8d8a80") + rect(0, 578, 600, 6, "#f2b81c", extra='opacity=".85"'))
    b.append("".join(rect(xx, 782, 64, 7, "#e9e4d4", 2, 'opacity=".6"') for xx in range(-20, 620, 120)))
    # title: STOP octagon + TWIST
    b.append(f'<g transform="translate(132 132) rotate(-8)" filter="url(#k-drop)"><polygon points="{_oct(0,0,100)}" fill="#f6f3ea"/>'
             f'<polygon points="{_oct(0,0,92)}" fill="#c81e2b"/>' + text(0, 22, "STOP", "Bungee", 54, "#fff") + "</g>")
    b.append(text(242, 170, "TWIST", "Bungee", 90, "#f7c21b", anchor="start", extra='filter="url(#k-drop)"'))
    b.append(text(246, 212, "the category race", "Overpass", 26, "#c9c4b6", 800, "start"))
    # rule sign on posts
    b.append(rect(170, 450, 18, 130, "url(#post)") + rect(412, 450, 18, 130, "url(#post)"))
    b.append(f'<g filter="url(#k-drop)">{rect(40, 258, 520, 210, "url(#ylw)", 22, "stroke=\"#c7920a\" stroke-width=\"2\"")}</g>')
    b.append(rect(54, 272, 492, 182, "none", 14, 'stroke="#151515" stroke-width="6"'))
    b.append('<g transform="translate(78 315) scale(1.0)"><path d="M50 3 97 50 50 97 3 50Z" fill="#141414"/><path d="M50 10 90 50 50 90 10 50Z" fill="#ffd23c"/>'
             '<path d="M44 76V60c0-7 13-7 13-14s-13-7-13-14v-6" fill="none" stroke="#141414" stroke-width="7" stroke-linecap="round"/><path d="M35 29 44 15 53 29Z" fill="#141414"/></g>')
    b.append(text(200, 314, "Round 3: Last letter", "Overpass", 22, "#2a2a2a", 800, "start"))
    b.append(text(200, 380, "Ends with", "Overpass", 50, "#151515", 900, "start"))
    b.append(rect(440, 330, 74, 78, "url(#tile)", 10) + rect(440, 368, 74, 2, "#000") + text(477, 395, "E", "Bungee", 58, "#ffb23e"))
    b.append(text(200, 428, "Every answer ends with E.", "Overpass", 20, "#2a2a2a", 700, "start"))
    # license plates
    plates = [("👤", "Name", "#c81e2b"), ("🐾", "Animal", "#1d4fa0"), ("🍕", "Food", "#0f6a43"),
              ("🌍", "Place", "#6b3fa0"), ("🏃", "Verb", "#e2650f"), ("🎵", "Music", "#0e7a8a")]
    for k, (ic, lb, band) in enumerate(plates):
        rr, cc = divmod(k, 3)
        px, py = 28 + cc * 186, 604 + rr * 86
        b.append(f'<g filter="url(#k-drop-s)">{rect(px, py, 172, 72, "url(#plate)", 10, "stroke=\"#b8b3a4\" stroke-width=\"2\"")}</g>'
                 + rect(px + 6, py + 6, 160, 11, band, 4) + emoji(px + 32, py + 55, ic, 26)
                 + text(px + 56, py + 56, lb, "Overpass", 27, "#1d2a4a", 900, "start")
                 + f'<circle cx="{px+14}" cy="{py+28}" r="3.5" fill="#222"/><circle cx="{px+158}" cy="{py+28}" r="3.5" fill="#222"/>')
    return svg(d, "".join(b))


def _oct(cx, cy, r):
    return " ".join(f"{cx + r*math.cos(math.radians(22.5+45*k)):.1f},{cy + r*math.sin(math.radians(22.5+45*k)):.1f}" for k in range(8))


def take_a_seat():
    d = rad("bg", [(0, "#2e2360"), (1, "#0d0b1d")], cy="55%", r="70%") + lin("amb", [(0, "#fde68a"), (1, "#fbbf24")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 116, 'Take a <tspan fill="url(#amb)">Seat</tspan>', "Bricolage Grotesque", 92, "#f4f2ff", 800))
    b.append(text(300, 160, "Answer before the clock runs out — or sit down.", "Inter", 19, "#b9b3e0", 500))
    b.append(f'<g filter="url(#k-drop)">{rect(90, 196, 420, 120, "#f4f2ff", 20)}</g>'
             + text(300, 238, "PROMPT", "Inter", 14, "#b45309", 800, ls=4) + text(300, 286, "a verb starting with G", "Bricolage Grotesque", 36, "#1c1917", 800))
    # spotlight
    b.append('<polygon points="270,320 330,320 420,700 180,700" fill="#fbbf24" opacity=".14"/>')
    b.append('<ellipse cx="300" cy="700" rx="130" ry="22" fill="#fbbf24" opacity=".25"/>')
    # student standing
    b.append('<g transform="translate(300 600)"><circle cx="0" cy="-130" r="34" fill="#f4f2ff"/><path d="M-50 90 L-44 -70 Q 0 -96 44 -70 L50 90 Z" fill="#fbbf24"/>'
             '<rect x="-40" y="90" width="26" height="80" rx="10" fill="#2b2652"/><rect x="14" y="90" width="26" height="80" rx="10" fill="#2b2652"/></g>')
    def chair(x, y, s, sitting=False):
        out = (f'<g transform="translate({x} {y}) scale({s})">'
               '<rect x="-30" y="-70" width="60" height="70" rx="10" fill="#4c4590"/><rect x="-36" y="0" width="72" height="16" rx="6" fill="#6a63b8"/>'
               '<rect x="-30" y="16" width="8" height="50" fill="#3a3470"/><rect x="22" y="16" width="8" height="50" fill="#3a3470"/>')
        if sitting:
            out += '<circle cx="0" cy="-92" r="22" fill="#b9b3e0"/><rect x="-24" y="-66" width="48" height="66" rx="16" fill="#8a84c8"/>'
        return out + "</g>"
    b.append(chair(80, 670, .9, True) + chair(170, 690, .9, True) + chair(430, 690, .9, True) + chair(520, 670, .9))
    b.append('<circle cx="500" cy="420" r="52" fill="#0d0b1d" stroke="#fb7185" stroke-width="7"/>'
             '<circle cx="500" cy="420" r="52" fill="none" stroke="#fbbf24" stroke-width="7" stroke-dasharray="120 330" transform="rotate(-90 500 420)"/>'
             + text(500, 434, "5", "Bricolage Grotesque", 44, "#f4f2ff", 800))
    b.append(footer("WHOLE CLASS · 214 PROMPTS", "Inter", "#fbbf24", 14, 4, 780, 800))
    return svg(d, "".join(b))


def tangled_paths():
    d = lin("card", [(0, "#f1dcb2"), (1, "#d9bd8a")])
    b = [rect(0, 0, 600, 800, "#12161c")]
    b.append(text(300, 104, "Tangled Paths", "Sora", 66, "#eef2f6", 800))
    b.append(text(300, 146, "LAY A TILE · FOLLOW YOUR PATH · SURVIVE", "Inter", 14, "#aab5c3", 800, ls=3))
    T = 150
    x0, y0 = 0, 190
    cols = ["#e8742b", "#2f9e57", "#3a7bd5", "#c94a8a", "#d4a520", "#6b5bd1"]
    rr = random.Random(8)
    for r in range(4):
        for c in range(4):
            x, y = x0 + c * T, y0 + r * T
            if (r, c) in {(0, 3), (3, 0)}:
                b.append(rect(x + 4, y + 4, T - 8, T - 8, "#2c3139", 8))
                continue
            b.append(f'<g filter="url(#k-drop-s)">{rect(x + 4, y + 4, T - 8, T - 8, "url(#card)", 10, "stroke=\"#8a6a3a\" stroke-width=\"2\"")}</g>')
            pts = [(x + 4 + T*.33, y + 4), (x + 4 + T*.66, y + 4), (x + T - 4, y + T*.33), (x + T - 4, y + T*.66),
                   (x + T*.66, y + T - 4), (x + T*.33, y + T - 4), (x + 4, y + T*.66), (x + 4, y + T*.33)]
            order = list(range(8))
            rr.shuffle(order)
            for k in range(4):
                a, bb = pts[order[2*k]], pts[order[2*k+1]]
                col = cols[(r * 4 + c + k) % 6] if k == 0 else "#8a7a5a"
                w = 9 if k == 0 else 6
                b.append(f'<path d="M{a[0]:.0f} {a[1]:.0f} Q {x+T/2} {y+T/2} {bb[0]:.0f} {bb[1]:.0f}" fill="none" stroke="#fff6e2" stroke-width="{w+5}" stroke-linecap="round"/>'
                         f'<path d="M{a[0]:.0f} {a[1]:.0f} Q {x+T/2} {y+T/2} {bb[0]:.0f} {bb[1]:.0f}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
    for (cx, cy, col) in [(x0 + 1.33*T, y0 + 4, "#e8742b"), (x0 + 4, y0 + 2.66*T, "#2f9e57"), (x0 + 3*T - 4, y0 + 1.66*T, "#3a7bd5")]:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{col}" stroke="#fff" stroke-width="4" filter="url(#k-drop-s)"/>')
    b.append(rect(0, 752, 600, 48, "#12161c", 0, 'opacity=".85"') + footer("2–8 PLAYERS · LAST STONE STANDING", "Inter", "#f0bf55", 14, 3, 782, 800))
    return svg(d, "".join(b))


def lost_signal():
    d = lin("sky", [(0, "#0a0b10"), (1, "#141a2a")]) + lin("gold", [(0, "#f6dc94"), (1, "#e8b84b")])
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(31, 90, "#fff", 500, (.6, 1.8), (.2, .8))]
    b.append(text(300, 88, "A CHOOSE-YOUR-OWN ADVENTURE", "Lato", 14, "#c97b3a", 700, ls=5))
    b.append(text(300, 168, "The Lost", "Playfair Display", 78, "url(#gold)", 700))
    b.append(text(300, 252, "Signal", "Playfair Display", 78, "url(#gold)", 700))
    # antenna + waves
    b.append('<g transform="translate(300 500)"><polygon points="0,-150 -40,90 40,90" fill="none" stroke="#6a6154" stroke-width="5"/>'
             '<line x1="-30" y1="30" x2="30" y2="30" stroke="#6a6154" stroke-width="4"/><line x1="-18" y1="-30" x2="18" y2="-30" stroke="#6a6154" stroke-width="4"/>'
             '<circle cx="0" cy="-156" r="9" fill="#ff5d5d"/><circle cx="0" cy="-156" r="16" fill="#ff5d5d" opacity=".4" filter="url(#k-glow-s)"/></g>')
    for k in range(1, 4):
        r = 36 * k
        b.append(f'<path d="M{300-r} {344-r*.2} A {r} {r} 0 0 1 {300+r} {344-r*.2}" fill="none" stroke="#e8b84b" stroke-opacity="{1-.25*k}" stroke-width="4" transform="translate(0 0)"/>')
    # forest silhouette
    trees = "".join(f'<polygon points="{x},{560 - h} {x-28},{640} {x+28},{640}" fill="#06070a"/>' for x, h in
                    [(30, 120), (80, 160), (130, 110), (470, 140), (520, 180), (570, 120), (200, 80), (400, 90)])
    b.append(trees + rect(0, 636, 600, 164, "#06070a"))
    rr = random.Random(9)
    for _ in range(18):
        x, y = rr.uniform(20, 580), rr.uniform(560, 760)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3" fill="#d9f99d"/><circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#d9f99d" opacity=".3" filter="url(#k-glow-s)"/>')
    b.append(text(300, 712, "106 ENDINGS · A2–B1", "Lato", 18, "#e8b84b", 700, ls=6))
    b.append(text(300, 752, "Which way will you go?", "Playfair Display", 22, "#efe8d9", 400, italic=True))
    return svg(d, "".join(b))


def think_on_feet():
    # night railway station: split-flap departure board under an arched glass roof
    d = (lin("tsky", [(0, "#070c16"), (.6, "#122036"), (1, "#24405a")]) + lin("tbrass", [(0, "#f2d38a"), (.5, "#c99a3b"), (1, "#7a5a1c")])
         + lin("tenam", [(0, "#257460"), (.6, "#1f5a4a"), (1, "#16473a")]) + lin("tflap", [(0, "#2a2d31"), (.49, "#1d1f22"), (.5, "#050506"), (.51, "#1a1c1f"), (1, "#141618")])
         + rad("tface", [(0, "#fffaf0"), (1, "#e6dcc2")], cx="40%", cy="35%") + rad("tlamp", [(0, "#ffcf7a"), (1, "#ffcf7a00")], r="50%"))
    b = [rect(0, 0, 600, 800, "url(#tsky)"), stars(41, 60, y1=420)]
    cx, cy, R = 300, 560, 420
    b.append('<g stroke="#2b3640" stroke-width="5" fill="none">' + "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{cx - R*math.cos(math.pi*k/10):.0f}" y2="{cy - R*math.sin(math.pi*k/10):.0f}"/>' for k in range(1, 10))
        + "".join(f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}"/>' for r in (160, 290)) + f'<path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" stroke-width="14"/></g>')
    b.append('<circle cx="40" cy="300" r="70" fill="url(#tlamp)"/><circle cx="560" cy="300" r="70" fill="url(#tlamp)"/>')
    # title plate
    b.append(rect(46, 40, 508, 150, "url(#tbrass)", 14) + rect(56, 50, 488, 130, "url(#tenam)", 9))
    b.append(text(300, 116, "Think on", "Antonio", 64, "#f1e9d2", 700) + text(300, 172, "Your Feet", "Antonio", 64, "#ffd77e", 700))
    # station clock hanging between title and board
    b.append(rect(298, 190, 4, 26, "#7a5a1c") + '<circle cx="300" cy="258" r="46" fill="url(#tbrass)"/><circle cx="300" cy="258" r="38" fill="url(#tface)"/>'
             + "".join(f'<line x1="{300 + 31*math.sin(k*math.pi/6):.1f}" y1="{258 - 31*math.cos(k*math.pi/6):.1f}" x2="{300 + 36*math.sin(k*math.pi/6):.1f}" y2="{258 - 36*math.cos(k*math.pi/6):.1f}" stroke="#2a2418" stroke-width="2.5"/>' for k in range(12))
             + '<path d="M300 258 L300 222 A36 36 0 0 1 335 252 Z" fill="#ff6a1f" opacity=".55"/><line x1="300" y1="258" x2="327" y2="236" stroke="#c4261a" stroke-width="3" stroke-linecap="round"/><circle cx="300" cy="258" r="4" fill="#2a2418"/>')
    # departure board
    b.append(rect(30, 318, 540, 270, "url(#tbrass)", 14) + rect(40, 328, 520, 250, "#111214", 9))
    rows = [("1", "FRUITS", "A1", "#2f9a4d"), ("2", "SPORTS", "A1", "#2f9a4d"), ("+", "JOBS", "A2", "#13867f")]
    for k, (n, word, lv, col) in enumerate(rows):
        y = 344 + k * 76
        b.append(rect(52, y, 40, 64, "#ff7a2e" if n == "+" else "url(#tbrass)", 6) + text(72, y + 47, n, "Antonio", 40, "#2b1d06", 700))
        for i in range(8):
            x = 100 + i * 44
            ch = word[i] if i < len(word) else ""
            b.append(rect(x, y, 40, 64, "url(#tflap)", 4) + (text(x + 20, y + 50, ch, "Antonio", 48, "#f1e9d2", 700) if ch else ""))
        b.append(rect(460, y, 88, 64, col, 8, 'stroke="#fff" stroke-opacity=".75" stroke-width="3"') + text(504, y + 48, lv, "Antonio", 40, "#fff", 700))
    # answer lamps + tickets
    b.append(rect(40, 612, 250, 66, "#c22a1a", 14) + '<circle cx="78" cy="645" r="19" fill="#ff7a63"/>' + text(180, 662, "Wrong", "Antonio", 42, "#fff", 700))
    b.append(rect(310, 612, 250, 66, "#24934a", 14) + '<circle cx="522" cy="645" r="19" fill="#7dffa6"/>' + text(410, 662, "Correct", "Antonio", 42, "#06240f", 700))
    for k, (em, col) in enumerate([("🦊", "#ff6a1f"), ("🦈", "#2f7bff"), ("🐸", "#21b35a"), ("🦉", "#a35cff")]):
        x = 40 + k * 132
        b.append(rect(x, 698, 122, 40, col, 8) + emoji(x + 24, 727, em, 24) + rect(x + 46, 712, 10, 10, "#ff7a63", 5) + rect(x + 62, 712, 10, 10, "#3a1412", 5) + rect(x + 78, 712, 10, 10, "#3a1412", 5))
    b.append(footer("2–6 teams · CEFR level filter", "Atkinson Hyperlegible", "#c99a3b", 18, 1, 772, 700))
    return svg(d, "".join(b))


def top_ten():
    d = lin("tt", [(0, "#ff9f1c"), (.5, "#ff4d6d"), (1, "#4cc9f0")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#0e0e12")]
    b.append(text(300, 140, "TOP TEN", "Bebas Neue", 150, "url(#tt)", ls=8))
    b.append(text(300, 180, "RANK · DEBATE · GUESS", "DM Sans", 17, "#6b6b80", 700, ls=6))
    items = [("Pizza", True), ("Hamburger", True), ("", False), ("Sushi", True), ("", False), ("", False), ("Tacos", True), ("", False), ("", False), ("Salad", True)]
    for k, (w, shown) in enumerate(items):
        y = 210 + k * 54
        col = "#ffd60a" if k == 0 else ("#ff9f1c" if k < 3 else "#2a2a38")
        b.append(rect(60, y, 480, 46, "#16161d" if not shown else "#1e1e28", 10, f'stroke="{col}" stroke-width="2"')
                 + rect(60, y, 60, 46, col if k < 3 else "#2a2a38", 10) + text(90, y + 33, f"#{k+1}", "Bebas Neue", 28, "#0e0e12" if k < 3 else "#f0f0f5"))
        b.append(text(140, y + 33, w if shown else "? ? ?", "DM Sans", 23, "#f0f0f5" if shown else "#4a4a5e", 700, "start"))
    b.append(text(300, 768, "World's favorite foods", "DM Sans", 22, "#4cc9f0", 600, italic=True))
    return svg(d, "".join(b))


def top_twenty():
    d = lin("gold", [(0, "#fff0a8"), (1, "#f0c040")])
    b = [rect(0, 0, 600, 800, "#0a0a0f"), '<circle cx="300" cy="140" r="240" fill="#f0c040" opacity=".09" filter="url(#k-glow)"/>']
    b.append(glow_text(300, 160, "RANK IT", "Bebas Neue", 156, "url(#gold)", "#f0c040", ls=10))
    b.append(text(300, 204, "TOP TWENTY · THE TRIVIA GAME", "DM Sans", 16, "#666688", 700, ls=6))
    found = {1: "Russia", 2: "Canada", 5: "Brazil", 7: "India", 8: "Argentina", 13: "Mexico", 19: "Peru"}
    for k in range(20):
        r, c = divmod(k, 2)
        x, y = 40 + c * 268, 236 + r * 48
        f = found.get(k + 1)
        b.append(rect(x, y, 252, 40, "#1c1c28" if f else "#13131a", 8, f'stroke="{"#4cdb8a" if f else "#2a2a3a"}" stroke-width="2"')
                 + text(x + 26, y + 28, k + 1, "Bebas Neue", 24, "#f0c040") + text(x + 54, y + 28, f or "· · ·", "DM Sans", 19, "#e8e8f0" if f else "#3a3a50", 700, "start"))
    b.append(text(300, 762, "“Largest countries in the world”", "DM Sans", 21, "#e8e8f0", 600, italic=True))
    return svg(d, "".join(b))


COVERS = {
    "ring-memory": ring_of_gems, "hangman": save_the_cheese, "scattergories": scattergories, "scrambler": scrambler,
    "sentence-auction": sentence_auction, "song-word-race": song_word_race, "sound-off": sound_off, "stairs": stairs,
    "stop-twist": stop_twist, "take-a-seat": take_a_seat, "tangled-paths": tangled_paths, "adventure": lost_signal,
    "categories": think_on_feet, "topten": top_ten, "toptwenty": top_twenty,
}
