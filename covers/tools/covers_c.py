"""Batch C covers."""
import math, random
from kit import *


def emoji_game():
    d = lin("tt", [(0, "#ffffff"), (1, "#b9a8ff")])
    b = [rect(0, 0, 600, 800, "#0a0a14"),
         '<circle cx="80" cy="200" r="220" fill="#7c5cfc" opacity=".28" filter="url(#k-glow)"/>',
         '<circle cx="560" cy="640" r="240" fill="#fc5c7d" opacity=".22" filter="url(#k-glow)"/>']
    b.append(text(300, 74, "EMOJI GAME", "Outfit", 18, "#b9a8ff", 700, ls=8))
    b.append(text(300, 162, 'What <tspan fill="#fc5c7d">Changed?</tspan>', "Fraunces", 64, "#f0eeff", 700))
    b.append(text(300, 204, "Spot the difference. Beat the clock.", "Outfit", 20, "#a59cc8", 400))
    em = ["🐶", "🍕", "🚲", "🌵", "🎸", "🐙", "🍩", "⚽", "🦊", "🌈", "🍉", "🚀", "🐢", "🎈", "🧀", "🦋"]
    cs, g = 112, 14
    x0, y0 = (600 - 4 * cs - 3 * g) / 2, 240
    for k, e in enumerate(em):
        r, c = divmod(k, 4)
        x, y = x0 + c * (cs + g), y0 + r * (cs + g)
        hot = k == 9
        b.append(rect(x, y, cs, cs, "#1a1530" if not hot else "#2a1440", 22,
                      f'stroke="{"#fc5c7d" if hot else "#2e2752"}" stroke-width="{4 if hot else 2}"'))
        if hot:
            b.append(f'<g opacity=".9">{text(x + cs/2, y + cs/2 + 26, "?", "Fraunces", 74, "#fc5c7d", 700)}</g>')
        else:
            b.append(emoji(x + cs/2, y + cs/2 + 22, e, 60))
    b.append(footer("MEMORY · TEAMS · A1–A2", "Outfit", "#b9a8ff", 14, 5, 778))
    return svg(d, "".join(b))


def emoji_logic():
    d = rad("bg", [(0, "#193440"), (1, "#0d1b21")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(emoji(300, 92, "🐢 🍕 🚲 🎸", 54))
    b.append(text(300, 186, 'Emoji <tspan fill="#ffb03a">Logic</tspan>', "Space Grotesk", 86, "#f2f6f7", 700))
    b.append(text(300, 228, "Read the clues. Who lives where?", "Inter", 20, "#8fb2bd", 500))
    cols = ["#ff6b81", "#5fe0b0", "#a78bfa", "#ffb03a", "#4cc9f0"]
    rows = [["🐱", "🐶", "🐢", "🐟", "🦜"], ["🍕", "🍣", "🍔", "🌮", "🍩"], ["🚲", "🚗", "🛴", "🚂", "⛵"]]
    known = {(0, 2), (1, 0), (2, 3), (1, 4), (0, 0)}
    hx0, hw = 34, 106
    for i in range(5):
        x = hx0 + i * hw + 4
        c = cols[i]
        b.append(f'<polygon points="{x},330 {x+49},282 {x+98},330" fill="{c}"/>' + rect(x + 6, 330, 86, 330, "#13272f", 0, f'stroke="{c}" stroke-width="3"'))
        b.append(text(x + 49, 320, i + 1, "JetBrains Mono", 22, "#0d1b21", 800))
        for r, row in enumerate(rows):
            y = 350 + r * 100
            if (r, i) in known:
                b.append(emoji(x + 49, y + 66, row[i], 56))
            else:
                b.append(rect(x + 19, y + 16, 60, 60, "#193440", 10, 'stroke="#27505f" stroke-dasharray="5 5" stroke-width="2"')
                         + text(x + 49, y + 58, "?", "Space Grotesk", 30, "#527180", 700))
    # clue card
    b.append(f'<g filter="url(#k-drop)">{rect(46, 682, 508, 80, "#f2f6f7", 12)}</g>')
    b.append(text(300, 716, "Clue 3: The 🐢 lives next to the 🍕.", "Inter", 20, "#0d1b21", 600))
    b.append(text(300, 746, "Clue 4: The 🚂 is in a pink house.", "Inter", 20, "#0d1b21", 600))
    return svg(d, "".join(b))


def escalation():
    d = (lin("heat", [(0, "#4cc9f0"), (.5, "#ffc857"), (1, "#ef476f")], x2=1, y2=0)
         + lin("tt", [(0, "#4cc9f0"), (.5, "#ffc857"), (1, "#ef476f")], x2=1, y2=0))
    b = [rect(0, 0, 600, 800, "#12101f"), '<circle cx="300" cy="420" r="300" fill="#ef476f" opacity=".07" filter="url(#k-glow)"/>']
    b.append(text(300, 120, "Escalation", "Sora", 86, "url(#tt)", 800))
    b.append(text(300, 166, "FROM MILD TO WILD", "Inter", 17, "#a69fc9", 800, ls=6))
    # staircase of cards 1..10 rising
    for n in range(1, 11):
        x = 40 + (n - 1) * 52
        hgt = 40 + n * 32
        y = 700 - hgt
        t = (n - 1) / 9
        col = _mix(t)
        b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, 46, hgt, col, 10)}</g>' + text(x + 23, y + 34, n, "Sora", 24, "#12101f", 800))
    b.append(rect(40, 716, 520, 14, "url(#heat)", 7))
    b.append(text(40, 760, "1 · barely worth mentioning", "Inter", 16, "#4cc9f0", 600, "start"))
    b.append(text(560, 760, "10 · that escalated", "Inter", 16, "#ef476f", 600, "end"))
    # speech bubble prompt
    b.append(f'<g filter="url(#k-drop)">{rect(60, 210, 360, 96, "#f4f1ff", 18)}<polygon points="110,304 150,304 110,336" fill="#f4f1ff"/></g>')
    b.append(text(240, 250, "“A problem at school…”", "Sora", 22, "#16142a", 700))
    b.append(text(240, 284, "how bad is YOUR number?", "Inter", 18, "#5a5478", 500, italic=True))
    b.append(f'<g transform="translate(490 262) rotate(8)" filter="url(#k-drop)">{rect(-46, -62, 92, 124, "#16142a", 12, "stroke=\"#ffc857\" stroke-width=\"4\"")}'
             + text(0, 22, "7", "Sora", 66, "#ffc857", 800) + "</g>")
    return svg(d, "".join(b))


def _mix(t):
    a, bb, c = (0x4c, 0xc9, 0xf0), (0xff, 0xc8, 0x57), (0xef, 0x47, 0x6f)
    if t < .5:
        p, q, u = a, bb, t * 2
    else:
        p, q, u = bb, c, (t - .5) * 2
    return "#%02x%02x%02x" % tuple(int(p[i] + (q[i] - p[i]) * u) for i in range(3))


def escape2():
    d = rad("bg", [(0, "#13234a"), (1, "#071024")], cy="45%") + lin("wood", [(0, "#6b4a2b"), (1, "#3d2816")])
    b = [rect(0, 0, 600, 800, "url(#bg)"), stars(3, 40, "#9aa6b2", 800, (0.8, 1.6), (.1, .4))]
    b.append(text(300, 78, "ESCAPE 2", "Fraunces", 24, "#9aa6b2", 700, ls=10))
    b.append(text(300, 150, "The Riddle Door", "Fraunces", 64, "#f3ead6", 700, italic=True))
    # door
    b.append('<g filter="url(#k-drop)"><path d="M150 760 V320 Q 150 200 300 200 Q 450 200 450 320 V760 Z" fill="url(#wood)" stroke="#2a1a0c" stroke-width="8"/></g>')
    for k in range(5):
        b.append(f'<line x1="{180+k*60}" y1="{230 if k in (0,4) else 210}" x2="{180+k*60}" y2="760" stroke="#2a1a0c" stroke-opacity=".5" stroke-width="3"/>')
    cols = ["#22c3d6", "#f59e0b", "#8b5cf6", "#f472b6", "#22c55e"]
    for k, c in enumerate(cols):
        y = 320 + k * 82
        b.append(f'<g transform="translate(300 {y})" filter="url(#k-drop-s)">'
                 f'<path d="M-20 -6 V-22 A20 20 0 0 1 20 -22 V-6" fill="none" stroke="#cbd5e1" stroke-width="7"/>'
                 + rect(-32, -8, 64, 52, c, 10, 'stroke="#071024" stroke-width="3"')
                 + f'<circle cx="0" cy="12" r="7" fill="#071024"/><rect x="-3" y="14" width="6" height="16" fill="#071024"/>' + "</g>")
    # riddle scroll + whisper
    b.append(f'<g transform="translate(110 620) rotate(-8)" filter="url(#k-drop)">{rect(-90, -70, 180, 140, "#f6efdc", 8)}'
             + text(0, -32, "I have keys", "Fraunces", 18, "#3b2a1e", 600, italic=True)
             + text(0, -6, "but no locks.", "Fraunces", 18, "#3b2a1e", 600, italic=True)
             + text(0, 20, "What am I?", "Fraunces", 18, "#3b2a1e", 600, italic=True)
             + text(0, 52, "RIDDLE 3", "Inter", 12, "#8a6a3a", 800, ls=3) + "</g>")
    b.append(emoji(500, 600, "👂", 56) + '<path d="M450 560 q -20 30 0 60 M430 548 q -30 42 0 84" fill="none" stroke="#9aa6b2" stroke-width="4" stroke-linecap="round"/>')
    return svg(d, "".join(b))


def escape_vault():
    d = rad("steel", [(0, "#9aa4b2"), (.7, "#5b6573"), (1, "#2f3640")], cy="40%") + rad("bg", [(0, "#1c2430"), (1, "#0a0e14")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 78, "ESCAPE", "JetBrains Mono", 26, "#38e1a6", 800, ls=14))
    b.append(text(300, 146, "The Cipher Vault", "JetBrains Mono", 46, "#e6edf3", 800))
    # vault door
    cx, cy = 300, 420
    b.append(f'<g filter="url(#k-drop)"><circle cx="{cx}" cy="{cy}" r="210" fill="#2f3640"/><circle cx="{cx}" cy="{cy}" r="196" fill="url(#steel)"/></g>')
    for k in range(12):
        a = math.radians(k * 30)
        b.append(f'<circle cx="{cx+178*math.cos(a):.1f}" cy="{cy+178*math.sin(a):.1f}" r="8" fill="#3c4450"/>')
    # caesar ring
    b.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="#1f2630" stroke="#0a0e14" stroke-width="4"/>')
    for k, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        a = math.radians(k * 360 / 26 - 90)
        b.append(text(f"{cx+132*math.cos(a):.1f}", f"{cy+132*math.sin(a)+6:.1f}", ch, "JetBrains Mono", 15, "#38e1a6", 700))
    for k, ch in enumerate("DEFGHIJKLMNOPQRSTUVWXYZABC"):
        a = math.radians(k * 360 / 26 - 90)
        b.append(text(f"{cx+106*math.cos(a):.1f}", f"{cy+106*math.sin(a)+5:.1f}", ch, "JetBrains Mono", 12, "#9aa4b2", 600))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="88" fill="url(#steel)" stroke="#0a0e14" stroke-width="4"/>')
    for k in range(3):
        a = math.radians(k * 120 + 20)
        b.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+82*math.cos(a):.1f}" y2="{cy+82*math.sin(a):.1f}" stroke="#2f3640" stroke-width="14" stroke-linecap="round"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#2f3640"/>')
    # pigpen glyphs + color code + keypad strip
    pig = ['M0 0 H30 V30', 'M0 0 V30 H30 V0', 'M30 0 H0 V30 H30', 'M0 0 H30 V30 H0 Z']
    for k, p in enumerate(pig):
        b.append(f'<g transform="translate({60+k*48} 676)"><path d="{p}" fill="none" stroke="#e6edf3" stroke-width="4"/>'
                 + ('<circle cx="15" cy="15" r="4" fill="#e6edf3"/>' if k % 2 else "") + "</g>")
    for k, c in enumerate(["#ef4444", "#3b82f6", "#facc15", "#22c55e"]):
        b.append(f'<circle cx="{380+k*42}" cy="690" r="15" fill="{c}"/>')
    b.append(rect(60, 726, 480, 44, "#0a0e14", 8, 'stroke="#38e1a6" stroke-width="2"') + text(300, 756, "► 4 · 1 · 7 · 9 · _", "JetBrains Mono", 22, "#38e1a6", 700, ls=4))
    return svg(d, "".join(b))


def feud():
    d = rad("bg", [(0, "#1a2a8a"), (1, "#0a0a1a")], cy="30%") + lin("gold", [(0, "#fff3a0"), (.5, "#FFD700"), (1, "#B8860B")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    for k in range(18):  # marquee lights
        b.append(f'<circle cx="{40+k*31}" cy="30" r="6" fill="#FFD700" opacity="{.9 if k%2 else .4}"/>')
    b.append(glow_text(300, 168, "FEUD", "Bebas Neue", 170, "url(#gold)", "#FFD700", ls=10))
    b.append(text(300, 212, "100 PEOPLE SURVEYED…", "Nunito", 22, "#ffffff", 900, ls=4))
    b.append(f'<g filter="url(#k-drop)">{rect(40, 244, 520, 420, "#111133", 18, "stroke=\"url(#gold)\" stroke-width=\"6\"")}</g>')
    ans = [("SANDWICH", 38), ("PIZZA", 24), None, ("SALAD", 12), None, None]
    for k, a in enumerate(ans):
        col, row = divmod(k, 3)
        x, y = 62 + col * 252, 268 + row * 128
        if a:
            b.append(rect(x, y, 236, 108, "#003399", 8, 'stroke="#4488FF" stroke-width="3"')
                     + text(x + 14, y + 66, a[0], "Bebas Neue", 34, "#fff", anchor="start")
                     + rect(x + 172, y + 24, 52, 60, "#0a0a1a", 6) + text(x + 198, y + 68, a[1], "Bebas Neue", 36, "#FFD700"))
        else:
            b.append(rect(x, y, 236, 108, "#1a1a3a", 8, 'stroke="#2a2a6a" stroke-width="3"')
                     + f'<circle cx="{x+118}" cy="{y+54}" r="30" fill="#003399" stroke="#4488FF" stroke-width="3"/>'
                     + text(x + 118, y + 68, k + 1, "Bebas Neue", 40, "#fff"))
    b.append(text(300, 704, "“Name something you eat for lunch”", "Nunito", 22, "#cfd6ff", 800, italic=True))
    for k in range(3):
        b.append(text(220 + k * 80, 770, "✕", "Nunito", 48, "#ff2222" if k < 1 else "#3a1a2a", 900))
    return svg(d, "".join(b))


def forbidden_island():
    d = (rad("sea", [(0, "#1e4fa6"), (1, "#061524")], cy="50%", r="70%") + lin("gold", [(0, "#ffe39a"), (1, "#d97706")]))
    b = [rect(0, 0, 600, 800, "url(#sea)")]
    for k in range(14):
        y = 230 + k * 40
        b.append(f'<path d="M0 {y} q 25 -10 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0 t 50 0" fill="none" stroke="#5eead4" stroke-opacity=".12" stroke-width="2"/>')
    b.append(text(300, 98, "Forbidden", "Cinzel", 66, "url(#gold)", 700, extra='filter="url(#k-drop)"'))
    b.append(text(300, 166, "Island", "Cinzel", 66, "url(#gold)", 700, extra='filter="url(#k-drop)"'))
    b.append(text(300, 202, "CAPTURE THE TREASURES · ESCAPE TOGETHER", "Inter", 13, "#eaf3fa", 700, ls=3))
    layout = ["..XX..", ".XXXX.", "XXXXXX", "XXXXXX", ".XXXX.", "..XX.."]
    cs = 74
    x0, y0 = (600 - 6 * cs) / 2, 236
    flooded = {(1, 1), (3, 5), (4, 2)}
    sunk = {(2, 0)}
    treasures = {(0, 2): "#a855f7", (2, 4): "#ef4444", (4, 4): "#38bdf8", (5, 3): "#f59e0b"}
    for r, row in enumerate(layout):
        for c, ch in enumerate(row):
            if ch != "X" or (r, c) in sunk:
                continue
            x, y = x0 + c * cs, y0 + r * cs
            fl = (r, c) in flooded
            b.append(f'<g filter="url(#k-drop-s)">{rect(x + 4, y + 4, cs - 8, cs - 8, "#3b7ddd" if fl else "#d9c08a", 8, "stroke=\"#0d2233\" stroke-width=\"2\"")}</g>')
            if not fl:
                rr = random.Random(r * 9 + c)
                b.append(f'<path d="M{x+12} {y+cs-18} q 16 -{rr.randint(10,24)} 32 -4 t 18 -6" fill="none" stroke="#8f7a4a" stroke-width="3"/>')
            else:
                b.append(f'<path d="M{x+10} {y+40} q 9 -6 18 0 t 18 0 t 18 0" fill="none" stroke="#bfe3ff" stroke-width="3"/>')
            if (r, c) in treasures:
                col = treasures[(r, c)]
                b.append(f'<polygon points="{x+cs/2},{y+16} {x+cs/2+16},{y+34} {x+cs/2},{y+58} {x+cs/2-16},{y+34}" fill="{col}" stroke="#fff" stroke-width="2.5"/>')
    # pawns
    for (r, c, col) in [(2, 2, "#fbbf24"), (3, 3, "#22c55e"), (1, 3, "#ef4444")]:
        x, y = x0 + c * cs + cs/2, y0 + r * cs + cs/2
        b.append(f'<g transform="translate({x} {y})" filter="url(#k-drop-s)"><circle cx="0" cy="-12" r="9" fill="{col}" stroke="#061524" stroke-width="2"/>'
                 f'<path d="M-12 14 Q 0 -10 12 14 Z" fill="{col}" stroke="#061524" stroke-width="2"/></g>')
    # helicopter
    b.append(emoji(510, 290, "🚁", 52))
    # water meter
    b.append(rect(30, 700, 540, 26, "#020a12", 13) + rect(30, 700, 230, 26, "#3b7ddd", 13) + text(300, 760, "WATER LEVEL RISING", "Inter", 14, "#5eead4", 800, ls=5))
    return svg(d, "".join(b))


def grammar_boom():
    d = rad("bg", [(0, "#232a45"), (1, "#101322")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 132, 'Grammar <tspan fill="#e8b34b">Boom</tspan>', "Playfair Display", 68, "#f2ecdd", 700))
    b.append(text(300, 176, "PICK A TILE · ANSWER · FACE YOUR FATE", "DM Sans", 15, "#9aa3c0", 700, ls=3))
    cs, g = 104, 14
    x0, y0 = (600 - 4 * cs - 3 * g) / 2, 220
    flipped = {1: ("+20", "#51cf66"), 6: ("SWAP", "#4dabf7"), 11: ("×2", "#b197fc")}
    for k in range(16):
        r, c = divmod(k, 4)
        x, y = x0 + c * (cs + g), y0 + r * (cs + g)
        if k == 9:
            continue
        if k in flipped:
            lab, col = flipped[k]
            b.append(rect(x, y, cs, cs, col, 14) + text(x + cs/2, y + cs/2 + 12, lab, "DM Sans", 34, "#101322", 800))
        else:
            b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, cs, cs, "#f2ecdd", 14, "stroke=\"#e8b34b\" stroke-width=\"3\"")}</g>'
                     + text(x + cs/2, y + cs/2 + 18, k + 1, "Playfair Display", 48, "#101322", 700))
    # boom tile
    r, c = divmod(9, 4)
    x, y = x0 + c * (cs + g) + cs/2, y0 + r * (cs + g) + cs/2
    spikes = []
    for k in range(16):
        a = math.radians(k * 22.5)
        rr = 120 if k % 2 == 0 else 66
        spikes.append(f"{x + rr*math.cos(a):.1f},{y + rr*math.sin(a):.1f}")
    b.append(f'<polygon points="{" ".join(spikes)}" fill="#ff6b6b" stroke="#ffd43b" stroke-width="6" filter="url(#k-drop)"/>')
    b.append(text(x, y + 18, "BOOM!", "Playfair Display", 48, "#fff", 900, extra='stroke="#101322" stroke-width="5" paint-order="stroke"'))
    b.append(emoji(x - 4, y - 50, "💣", 0))
    b.append(footer("TEAMS · A1–B2 GRAMMAR", "DM Sans", "#e8b34b", 15, 4, 772, 800))
    return svg(d, "".join(b))


def herd_up():
    d = lin("org", [(0, "#ffd166"), (1, "#ff6b35")]) + rad("bg", [(0, "#221f35"), (1, "#0f0e17")], cy="40%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 150, "HERD UP!", "Bebas Neue", 156, "url(#org)", ls=4, extra='filter="url(#k-drop)"'))
    b.append(text(300, 196, "THINK LIKE THE GROUP", "Nunito", 20, "#a7a9be", 900, ls=8))
    # meadow
    b.append('<path d="M0 520 Q 300 440 600 520 V800 H0 Z" fill="#164a2c"/><path d="M0 580 Q 300 520 600 590 V800 H0 Z" fill="#1d5c36"/>')
    def cow(x, y, s, flip=False):
        f = -1 if flip else 1
        return (f'<g transform="translate({x} {y}) scale({s*f} {s})" filter="url(#k-drop-s)">'
                '<rect x="-60" y="-20" width="120" height="70" rx="30" fill="#fffffe" stroke="#1a1828" stroke-width="5"/>'
                '<path d="M-30 -18 q 20 10 10 30 q -20 6 -30 -10 Z" fill="#1a1828"/><path d="M30 10 q 20 -10 20 20 q -14 14 -26 -4 Z" fill="#1a1828"/>'
                '<rect x="-48" y="40" width="14" height="36" rx="5" fill="#fffffe" stroke="#1a1828" stroke-width="4"/>'
                '<rect x="30" y="40" width="14" height="36" rx="5" fill="#fffffe" stroke="#1a1828" stroke-width="4"/>'
                '<ellipse cx="-74" cy="-26" rx="34" ry="30" fill="#fffffe" stroke="#1a1828" stroke-width="5"/>'
                '<ellipse cx="-84" cy="-10" rx="22" ry="14" fill="#ef9fb6" stroke="#1a1828" stroke-width="4"/>'
                '<circle cx="-90" cy="-12" r="3" fill="#1a1828"/><circle cx="-78" cy="-12" r="3" fill="#1a1828"/>'
                '<circle cx="-70" cy="-36" r="5" fill="#1a1828"/>'
                '<path d="M-60 -52 q 10 -16 22 -10 M-92 -50 q -6 -18 -20 -12" stroke="#1a1828" stroke-width="5" fill="none" stroke-linecap="round"/>'
                '</g>')
    b.append(cow(170, 520, 1.15) + cow(460, 560, .95, True) + cow(320, 680, .8))
    # answer cards
    def card(x, y, rot, word, col):
        return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop)">' + rect(-80, -36, 160, 72, col, 12)
                + text(0, 12, word, "Bebas Neue", 40, "#0f0e17", ls=2) + "</g>")
    b.append(card(120, 290, -8, "PIZZA", "#ffd166") + card(300, 268, 3, "PIZZA", "#06d6a0") + card(480, 296, 10, "PIZZA", "#ffd166")
             + card(300, 370, -4, "SUSHI", "#ef476f"))
    b.append(text(300, 425, "Name a food everyone loves", "Nunito", 20, "#fffffe", 800, italic=True))
    return svg(d, "".join(b))


def hex_duel():
    d = rad("bg", [(0, "#4a2c18"), (1, "#1a0f08")], cy="30%") + lin("org", [(0, "#ffb26b"), (1, "#e2672a")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    for k in range(30):
        b.append(f'<line x1="0" y1="{k*28}" x2="600" y2="{k*28+6}" stroke="#000" stroke-opacity=".12" stroke-width="2"/>')
    b.append(text(300, 136, "Hex Duel", "Barlow Condensed", 128, "url(#org)", 800, extra='filter="url(#k-drop)"'))
    b.append(text(300, 182, "WIN DUELS · TAKE TILES · OWN THE BOARD", "Figtree", 16, "#e8d2b8", 700, ls=3))
    teams = {"F": ("#e8743b", "🦊"), "W": ("#3a8fd6", "🐳"), "G": ("#4caf50", "🐸"), "L": ("#e2b33b", "🦁")}
    r = 46
    owner = [["F", "F", ".", "W", "W"], ["F", "F", "G", "W", "W"], [".", "G", "G", "L", "W"], ["G", "G", "L", "L", "."],
             ["G", ".", "L", "L", "L"], ["F", "G", ".", "L", "W"]]
    for row, cells in enumerate(owner):
        for col, o in enumerate(cells):
            cx = 120 + col * r * 1.75 + (r * .875 if row % 2 else 0)
            cy = 270 + row * r * 1.52
            if o == ".":
                b.append(f'<polygon points="{hexpts(cx, cy, r-3, 30)}" fill="#3a2414" stroke="#6b4a2b" stroke-width="3"/>')
            else:
                c, e = teams[o]
                b.append(f'<g filter="url(#k-drop-s)"><polygon points="{hexpts(cx, cy, r-3, 30)}" fill="{c}" stroke="#1a0f08" stroke-width="3"/></g>'
                         + emoji(cx, cy + 12, e, 32))
    # duel banner
    b.append(f'<g filter="url(#k-drop)">{rect(90, 700, 420, 66, "#2a1a10", 33, "stroke=\"url(#org)\" stroke-width=\"4\"")}</g>'
             + text(300, 744, "🦊  DUEL!  🐸", "Barlow Condensed", 34, "#ffb26b", 800, ls=3))
    return svg(d, "".join(b))


def hot_seat():
    d = rad("bg", [(0, "#1a2540"), (1, "#0b1220")], cy="40%") + lin("fire", [(0, "#fbbf24"), (1, "#ea580c")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append('<circle cx="300" cy="450" r="260" fill="#f97316" opacity=".12" filter="url(#k-glow)"/>')
    b.append(emoji(300, 104, "🔥", 76))
    b.append(text(300, 196, 'Hot <tspan fill="url(#fire)">Seat</tspan>', "Sora", 96, "#f6f7fb", 800))
    b.append(text(300, 236, "DESCRIBE IT · DON'T SAY IT", "Inter", 17, "#94a3b8", 800, ls=5))
    b.append(f'<g filter="url(#k-drop)">{rect(70, 272, 460, 420, "#111c30", 22, "stroke=\"#f97316\" stroke-width=\"4\"")}</g>')
    b.append(rect(262, 296, 76, 32, "#ea580c", 16) + text(300, 319, "A2", "Sora", 18, "#fff", 800))
    b.append(text(300, 410, "weather", "Sora", 82, "#f6f7fb", 800))
    b.append(text(300, 452, "DO NOT SAY", "Inter", 14, "#ef4444", 800, ls=4))
    for k, w in enumerate(["rain", "sun", "forecast", "temperature"]):
        r, c = divmod(k, 2)
        x, y = 100 + c * 206, 470 + r * 62
        b.append(rect(x, y, 194, 50, "#1f2a44", 10, 'stroke="#3a1f2a" stroke-width="2"') + text(x + 97, y + 33, w, "Sora", 22, "#f6f7fb", 600)
                 + f'<line x1="{x+20}" y1="{y+25}" x2="{x+174}" y2="{y+25}" stroke="#ef4444" stroke-width="3" opacity=".75"/>')
    b.append(text(300, 664, "1:00", "Sora", 40, "#fbbf24", 800))
    b.append(footer("TEAMS · TIMER · A1–B2", "Inter", "#f97316", 14, 5, 760, 800))
    return svg(d, "".join(b))


def interrupt():
    d = rad("felt", [(0, "#1f4436"), (1, "#0e2019")], cy="40%")
    b = [rect(0, 0, 600, 800, "url(#felt)")]
    b.append(text(300, 150, 'Inter<tspan font-style="italic" fill="#E0B252">rupt!</tspan>', "Instrument Serif", 116, "#FBFAF6"))
    b.append(text(300, 196, "Tell the story. Play your cards. Steal the turn.", "Inter Tight", 19, "#8FAFA0", 500))
    cards = [("CHARACTER", "a nervous pilot", "#D8556B", -24), ("PLACE", "an old lighthouse", "#4C8FD1", -8),
             ("EVENT", "the lights go out", "#2FA98A", 8), ("ASPECT", "suddenly", "#9B7BD4", 24)]
    for k, (kind, txt, col, rot) in enumerate(cards):
        cx = 165 + (k % 2) * 270
        cy = 370 + (k // 2) * 230
        b.append(f'<g transform="translate({cx} {cy}) rotate({rot*0.25})" filter="url(#k-drop)">'
                 + rect(-118, -95, 236, 190, "#FBFAF6", 14, f'stroke="{col}" stroke-width="5"')
                 + rect(-118, -95, 236, 42, col, 14) + rect(-118, -67, 236, 14, col)
                 + text(0, -67, kind, "Inter Tight", 15, "#fff", 800, ls=3)
                 + text(0, 26, txt, "Instrument Serif", 30, "#14261F", italic=True)
                 + "</g>")
    b.append(f'<g transform="translate(300 736) rotate(-4)" filter="url(#k-drop)">{rect(-80, -30, 160, 60, "#E0B252", 30)}'
             + text(0, 10, "STEAL!", "Inter Tight", 28, "#14261F", 800, ls=2) + "</g>")
    return svg(d, "".join(b))


def _wrap2(s):
    w = s.split()
    if len(w) <= 2:
        return [s]
    h = len(w) // 2
    return [" ".join(w[:h]), " ".join(w[h:])]


def inventions():
    d = lin("par", [(0, "#fdf6e3"), (1, "#f4e8c1")])
    b = [rect(0, 0, 600, 800, "#3a1f12"), f'<g filter="url(#k-drop)">{rect(30, 30, 540, 740, "url(#par)", 18, "stroke=\"#c8972a\" stroke-width=\"4\"")}</g>']
    b.append("".join(f'<line x1="30" y1="{y}" x2="570" y2="{y-30}" stroke="#c8972a" stroke-opacity=".08" stroke-width="10"/>' for y in range(60, 820, 40)))
    b.append(emoji(300, 120, "🕰️", 64))
    b.append(text(300, 204, "Inventions", "Playfair Display", 80, "#2c1810", 900))
    b.append(text(300, 242, "PLACE THEM IN ORDER", "DM Sans", 16, "#8a5a2e", 700, ls=6))
    items = [("🛞", "3500 BC"), ("🧭", "1100"), ("💡", "1879"), ("✈️", "1903"), ("📺", "1927"), ("📱", "2007")]
    b.append('<line x1="300" y1="280" x2="300" y2="740" stroke="#c8972a" stroke-width="6"/>')
    for k, (e, yr) in enumerate(items):
        y = 300 + k * 76
        left = k % 2 == 0
        b.append(f'<circle cx="300" cy="{y+20}" r="10" fill="#c0392b" stroke="#fdf6e3" stroke-width="3"/>')
        cx = 180 if left else 420
        b.append(f'<g filter="url(#k-drop-s)">{rect(cx - 90, y - 10, 180, 62, "#fffaf0", 12, "stroke=\"#c8972a\" stroke-width=\"2\"")}</g>'
                 + emoji(cx - 52, y + 36, e, 36) + text(cx + 26, y + 32, yr if k not in (3,) else "?", "Playfair Display", 24, "#2c1810", 700))
    return svg(d, "".join(b))


def last_one_standing():
    d = lin("gold", [(0, "#ffe9a0"), (1, "#f5c842")])
    b = [rect(0, 0, 600, 800, "#0a0b10")]
    b.append('<polygon points="250,0 350,0 470,800 130,800" fill="#f5c842" opacity=".07"/>')
    b.append(glow_text(300, 112, "LAST ONE", "Bebas Neue", 104, "url(#gold)", "#f5c842", ls=6))
    b.append(glow_text(300, 208, "STANDING", "Bebas Neue", 104, "url(#gold)", "#f5c842", ls=6))
    b.append(text(300, 246, "THE ELIMINATION GAME", "DM Sans", 16, "#5a607a", 700, ls=8))
    cats = [("Countries", "🌍"), ("Animals", "🦁"), ("Colors", "🎨"), ("Sports", "⚽"), ("Months", "📅"), ("Fruits", "🍓"),
            ("Jobs", "💼"), ("Music", "🎸"), ("Food", "🍕")]
    out = {0, 2, 3, 5, 6, 8, 1, 7}
    for k, (c, e) in enumerate(cats):
        r, col = divmod(k, 3)
        x, y = 50 + col * 172, 290 + r * 128
        alive = k not in out
        b.append(rect(x, y, 156, 110, "#11131d" if not alive else "#1a1d2e", 12,
                      f'stroke="{"#f5c842" if alive else "#1e2235"}" stroke-width="{4 if alive else 2}"'))
        b.append(f'<g opacity="{1 if alive else .3}">' + emoji(x + 78, y + 58, e, 40) + text(x + 78, y + 94, c, "DM Sans", 18, "#e8eaf0", 700) + "</g>")
        if not alive:
            b.append(f'<path d="M{x+30} {y+20} L{x+126} {y+90} M{x+126} {y+20} L{x+30} {y+90}" stroke="#e5484d" stroke-width="6" stroke-linecap="round" opacity=".8"/>')
    b.append(text(300, 720, "Choose differently from me", "DM Sans", 24, "#e8eaf0", 700))
    b.append(text(300, 754, "and you win.", "DM Sans", 24, "#f5c842", 700))
    return svg(d, "".join(b))


def left_to_right():
    d = lin("die", [(0, "#ffffff"), (1, "#cfd4ff")])
    b = [rect(0, 0, 600, 800, "#0d0f1a")]
    b.append('<circle cx="300" cy="330" r="220" fill="#00c8ff" opacity=".12" filter="url(#k-glow)"/>')
    b.append(glow_text(300, 112, "LEFT TO", "Black Ops One", 84, "#e9fbff", "#00c8ff", ls=4))
    b.append(glow_text(300, 200, "RIGHT", "Black Ops One", 100, "#e9fbff", "#00c8ff", ls=6))
    b.append(text(300, 238, "ELIMINATE YOUR SQUARES — LAST ONE STANDING WINS", "Barlow Condensed", 16, "#8b93c4", 700, ls=2))
    # 3D die
    cx, cy, s = 300, 360, 70
    b.append(f'<g filter="url(#k-drop)"><polygon points="{cx},{cy-s} {cx+s*1.1},{cy-s*.45} {cx},{cy+s*.1} {cx-s*1.1},{cy-s*.45}" fill="#ffffff"/>'
             f'<polygon points="{cx-s*1.1},{cy-s*.45} {cx},{cy+s*.1} {cx},{cy+s*1.2} {cx-s*1.1},{cy+s*.65}" fill="#c9cff5"/>'
             f'<polygon points="{cx+s*1.1},{cy-s*.45} {cx},{cy+s*.1} {cx},{cy+s*1.2} {cx+s*1.1},{cy+s*.65}" fill="#a3abe6"/></g>')
    b.append(f'<ellipse cx="{cx}" cy="{cy-s*.45}" rx="12" ry="7" fill="#ff2d87"/>')
    for (dx, dy) in [(-.55, .1), (-.55, .75), (-.3, .45)]:
        b.append(f'<ellipse cx="{cx+dx*s}" cy="{cy+dy*s}" rx="7" ry="9" fill="#14172a"/>')
    for (dx, dy) in [(.3, .05), (.8, .55), (.55, .3)]:
        b.append(f'<ellipse cx="{cx+dx*s}" cy="{cy+dy*s}" rx="7" ry="9" fill="#14172a"/>')
    cols = ["#ff2d87", "#00ff99", "#ffe600", "#ff7b00"]
    for p, col in enumerate(cols):
        y = 500 + p * 66
        b.append(text(40, y + 30, f"P{p+1}", "Black Ops One", 24, col, anchor="start"))
        for k in range(6):
            x = 110 + k * 76
            filled = (k + p) % 3 != 0
            b.append(rect(x, y, 64, 46, col if filled else "#14172a", 8, f'stroke="{col}" stroke-width="2.5" fill-opacity="{.85 if filled else 1}"')
                     + text(x + 32, y + 32, k + 1, "Black Ops One", 22, "#0d0f1a" if filled else col))
    return svg(d, "".join(b))


COVERS = {
    "emoji": emoji_game, "emoji-logic": emoji_logic, "escalation": escalation, "escape2": escape2, "escape": escape_vault,
    "family-feud-efl": feud, "forbidden-island": forbidden_island, "grammar-boom": grammar_boom, "herd-up": herd_up,
    "hex-duel": hex_duel, "hot-seat": hot_seat, "interrupt": interrupt, "inventions": inventions,
    "last-one-standing": last_one_standing, "leftright": left_to_right,
}
