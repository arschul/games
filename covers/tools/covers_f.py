"""Batch F covers."""
import math, random
from kit import *


def trivia_badges():
    d = lin("tt", [(0, "#c084fc"), (.5, "#a855f7"), (1, "#f59e0b")], x2=1, y2=0) + rad("bg", [(0, "#24123f"), (1, "#0f0f1a")], cy="35%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 104, "TRIVIA", "Bebas Neue", 96, "url(#tt)", ls=10))
    b.append(text(300, 194, "BADGE HUNTERS", "Bebas Neue", 84, "url(#tt)", ls=6))
    b.append(text(300, 232, "THE MORE YOU KNOW…", "Nunito", 18, "#a99bd6", 900, ls=5))
    badges = [("🌎", "#3b82f6", True), ("🧪", "#10b981", True), ("⚽", "#f59e0b", False), ("🎵", "#ec4899", True),
              ("🏛️", "#a855f7", False), ("🐾", "#22c55e", True), ("💻", "#06b6d4", False), ("🍕", "#f97316", True), ("🚀", "#6366f1", False)]
    for k, (e, col, got) in enumerate(badges):
        r, c = divmod(k, 3)
        cx, cy = 140 + c * 160, 330 + r * 148
        b.append(f'<g filter="url(#k-drop)"><polygon points="{hexpts(cx, cy, 64, 30)}" fill="{col if got else "#1e1b33"}" stroke="{"#fbbf24" if got else "#2a2a4a"}" stroke-width="5"/></g>')
        b.append(f'<g opacity="{1 if got else .3}">' + emoji(cx, cy + 18, e, 50) + "</g>")
        if got:
            b.append(f'<path d="M{cx-20} {cy+56} l -8 34 l 20 -10 l 8 18 l 8 -38 Z" fill="#fbbf24"/><path d="M{cx+20} {cy+56} l 8 34 l -20 -10 l -8 18 l -8 -38 Z" fill="#c2740b"/>')
    b.append(footer("TEAMS · 20 CATEGORIES · A1–B2", "Nunito", "#fbbf24", 15, 4, 776, 900))
    return svg(d, "".join(b))


def true_or_false():
    d = lin("tt", [(0, "#00e5a0"), (1, "#4cc9f0")], x2=1, y2=0) + lin("ff", [(0, "#ff8c00"), (1, "#ff4b6e")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#0d0d1a"), '<circle cx="80" cy="200" r="220" fill="#00e5a0" opacity=".12" filter="url(#k-glow)"/>',
         '<circle cx="520" cy="200" r="220" fill="#ff4b6e" opacity=".12" filter="url(#k-glow)"/>']
    b.append(text(300, 120, 'TRUE <tspan fill="#cfd2ea" font-size="70">OR</tspan>', "Bebas Neue", 120, "url(#tt)", ls=6))
    b.append(text(300, 232, "FALSE", "Bebas Neue", 120, "url(#ff)", ls=10))
    b.append(text(300, 270, "HOT SEAT &amp; BETTING", "Nunito", 18, "#8a8cb8", 900, ls=6))
    b.append(f'<g filter="url(#k-drop)">{rect(50, 308, 500, 190, "#1e1e35", 22, "stroke=\"#2e2e55\" stroke-width=\"3\"")}</g>')
    b.append(text(300, 360, "FACT OR FAKE?", "Nunito", 15, "#ffd700", 900, ls=4))
    b.append(text(300, 412, "An octopus has", "Nunito", 34, "#f4f5fb", 800) + text(300, 456, "three hearts.", "Nunito", 34, "#f4f5fb", 800))
    b.append(rect(50, 530, 240, 96, "#00a06f", 20, 'stroke="#00e5a0" stroke-width="4"') + text(170, 594, "TRUE", "Bebas Neue", 58, "#fff", ls=4))
    b.append(rect(310, 530, 240, 96, "#b0193a", 20, 'stroke="#ff4b6e" stroke-width="4"') + text(430, 594, "FALSE", "Bebas Neue", 58, "#fff", ls=4))
    for k in range(5):
        b.append(f'<ellipse cx="200" cy="{720 - k*10}" rx="46" ry="14" fill="#ffd700" stroke="#b8860b" stroke-width="3"/>')
    for k in range(3):
        b.append(f'<ellipse cx="300" cy="{720 - k*10}" rx="46" ry="14" fill="#ff8c00" stroke="#b35c00" stroke-width="3"/>')
    b.append(text(420, 720, "BET ×2", "Bebas Neue", 46, "#ffd700", ls=4))
    return svg(d, "".join(b))


def ultimate_ttt():
    b = [rect(0, 0, 600, 800, "#0a0a0f")]
    b.append(text(300, 70, "★ ULTIMATE ★", "Press Start 2P", 22, "#ffd600"))
    b.append(text(300, 132, "TIC TAC", "Press Start 2P", 50, "#00e5ff", extra='filter="url(#k-glow-s)"') + text(300, 132, "TIC TAC", "Press Start 2P", 50, "#e6fdff"))
    b.append(text(300, 196, "TOE", "Press Start 2P", 50, "#ff4081", extra='filter="url(#k-glow-s)"') + text(300, 196, "TOE", "Press Start 2P", 50, "#ffe3ee"))
    big = 156
    x0, y0 = (600 - 3 * big - 2 * 12) / 2, 238
    rr = random.Random(12)
    claimed = {(0, 0): "X", (1, 1): "O", (2, 0): "X"}
    for R in range(3):
        for C in range(3):
            bx, by = x0 + C * (big + 12), y0 + R * (big + 12)
            active = (R, C) == (1, 2)
            b.append(rect(bx, by, big, big, "#12121a", 12, f'stroke="{"#ffd600" if active else "#2a2a3d"}" stroke-width="{4 if active else 2}"'))
            cl = claimed.get((R, C))
            cs = big / 3
            for k in range(1, 3):
                b.append(f'<line x1="{bx+k*cs}" y1="{by+10}" x2="{bx+k*cs}" y2="{by+big-10}" stroke="#2a2a3d" stroke-width="3"/>'
                         f'<line x1="{bx+10}" y1="{by+k*cs}" x2="{bx+big-10}" y2="{by+k*cs}" stroke="#2a2a3d" stroke-width="3"/>')
            for r in range(3):
                for c in range(3):
                    v = rr.choice(["X", "O", "", "", ""])
                    cx, cy = bx + c * cs + cs/2, by + r * cs + cs/2
                    if v == "X":
                        b.append(f'<path d="M{cx-12} {cy-12} L{cx+12} {cy+12} M{cx+12} {cy-12} L{cx-12} {cy+12}" stroke="#00e5ff" stroke-width="5" stroke-linecap="round" opacity="{.35 if cl else 1}"/>')
                    elif v == "O":
                        b.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="none" stroke="#ff4081" stroke-width="5" opacity="{.35 if cl else 1}"/>')
            if cl == "X":
                b.append(f'<path d="M{bx+30} {by+30} L{bx+big-30} {by+big-30} M{bx+big-30} {by+30} L{bx+30} {by+big-30}" stroke="#00e5ff" stroke-width="16" stroke-linecap="round" filter="url(#k-glow-s)"/>'
                         f'<path d="M{bx+30} {by+30} L{bx+big-30} {by+big-30} M{bx+big-30} {by+30} L{bx+30} {by+big-30}" stroke="#d9fbff" stroke-width="8" stroke-linecap="round"/>')
            elif cl == "O":
                b.append(f'<circle cx="{bx+big/2}" cy="{by+big/2}" r="52" fill="none" stroke="#ff4081" stroke-width="16" filter="url(#k-glow-s)"/>'
                         f'<circle cx="{bx+big/2}" cy="{by+big/2}" r="52" fill="none" stroke="#ffe3ee" stroke-width="8"/>')
    b.append(text(300, 778, "CLASSIC · ULTIMATE · GAUNTLET", "Press Start 2P", 12, "#7c7caa"))
    return svg("", "".join(b))


def unscramble():
    d = lin("tt", [(0, "#ff6b6b"), (.33, "#ffd166"), (.66, "#4ecdc4"), (1, "#a78bfa")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#171C29"), '<circle cx="40" cy="140" r="200" fill="#2A1F38" opacity=".9"/><circle cx="580" cy="660" r="220" fill="#16283C" opacity=".9"/>',
         stars(14, 14, "#ffd166", 800, (2, 4), (.4, .8))]
    b.append(text(300, 130, "Unscramble!", "Fredoka One", 92, "url(#tt)"))
    b.append(text(300, 176, "the scrambliest word party game 🎉", "Nunito", 22, "#c9d2e6", 800))
    b.append(rect(220, 222, 160, 44, "#4A90E2", 22) + text(300, 252, "🍎 FRUITS", "Nunito", 20, "#fff", 900, ls=2))
    scr = [("P", -14, 92, 350), ("L", 10, 210, 334), ("A", -6, 330, 356), ("E", 14, 450, 330), ("P", -10, 270, 450)]
    cols = ["#ff6b6b", "#ffd166", "#4ecdc4", "#a78bfa", "#5AA9F5"]
    for k, (ch, rot, x, y) in enumerate(scr):
        b.append(f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop)">{rect(-46, -46, 92, 92, "#fff9f0", 18, f"stroke=\"{cols[k]}\" stroke-width=\"6\"")}'
                 + text(0, 22, ch, "Fredoka One", 62, "#1E344F") + "</g>")
    b.append('<path d="M300 512 v52" stroke="#c9d2e6" stroke-width="6" stroke-linecap="round"/><path d="M280 545 l20 22 l20 -22" fill="none" stroke="#c9d2e6" stroke-width="6" stroke-linecap="round"/>')
    for k, ch in enumerate("APPLE"):
        x = 90 + k * 86
        b.append(rect(x, 600, 76, 84, cols[k], 16, 'stroke="#fff" stroke-width="3"') + text(x + 38, 660, ch, "Fredoka One", 52, "#fff"))
    b.append(footer("TEAMS · EASY OR HARD · A1–B2", "Nunito", "#ffd166", 15, 3, 760, 900))
    return svg(d, "".join(b))


def chalkboard(b, x=0, y=0, w=600, h=800):
    b.append(rect(x, y, w, h, "#1e4535"))
    rr = random.Random(77)
    for _ in range(26):
        x1, y1 = rr.uniform(x, x + w), rr.uniform(y, y + h)
        b.append(f'<path d="M{x1:.0f} {y1:.0f} q {rr.uniform(20,60):.0f} {rr.uniform(-10,10):.0f} {rr.uniform(60,140):.0f} {rr.uniform(-6,6):.0f}" stroke="#f0ede0" stroke-opacity=".05" stroke-width="{rr.uniform(6,18):.0f}" fill="none"/>')


def vocab_toolkit():
    b = []
    chalkboard(b)
    b.append(rect(14, 14, 572, 772, "none", 10, 'stroke="#8a5a2b" stroke-width="14"'))
    b.append(emoji(110, 122, "✏️", 64) + text(160, 136, "Vocab Toolkit", "Caveat", 82, "#f0ede0", 700, "start"))
    b.append(text(300, 186, "Your word list → six activities", "Caveat", 36, "#f5d07a", 700))
    acts = [("🔍", "Word Search", "#5bb8d4"), ("🧀", "Save the Cheese", "#e8b84b"), ("🎱", "Bingo", "#e8604b"),
            ("🔀", "Anagram Scramble", "#4ecb71"), ("🧩", "Definition Match", "#f5d07a"), ("🃏", "Flashcards", "#c8a2f5")]
    for k, (e, name, col) in enumerate(acts):
        r, c = divmod(k, 2)
        x, y = 54 + c * 252, 230 + r * 168
        b.append(rect(x, y, 240, 148, "#245040", 16, f'stroke="{col}" stroke-width="3" stroke-dasharray="10 6"')
                 + emoji(x + 120, y + 72, e, 56) + text(x + 120, y + 124, name, "Caveat", 30, "#f0ede0", 700))
    b.append(rect(160, 742, 280, 14, "#f0ede0", 4, 'opacity=".85"') + rect(440, 742, 30, 14, "#e8b84b", 4))
    return svg("", "".join(b))


def wave():
    """Wave: teal radio-dial device, cream face, scoring wedge, red needle, smoked-glass screen swinging open."""
    d = (lin("sky", [(0, "#050b20"), (.6, "#0d2145"), (1, "#17406a")])
         + lin("shell", [(0, "#3aa0a9"), (.45, "#187180"), (1, "#0d4651")])
         + rad("face", [(0, "#fffaf0"), (.8, "#f7eed8"), (1, "#dccca5")], cy="100%", r="100%")
         + rad("glass", [(0, "#3a46a0"), (.7, "#1d2457"), (1, "#0c1033")], cy="100%", r="100%")
         + rad("cap", [(0, "#ffffff"), (.55, "#cbd6db"), (1, "#6f8188")], cx="38%", cy="30%", r="80%")
         + '<clipPath id="wv-win"><path d="M70 470 A230 230 0 0 1 530 470Z"/></clipPath>')
    cx, cy, R = 300, 470, 230
    def P(a, r):
        t = math.radians(a)
        return (cx + r * math.sin(t), cy - r * math.cos(t))
    def sec(r0, r1, a0, a1, fill):
        p0, p1, q1, q0 = P(a0, r1), P(a1, r1), P(a1, r0), P(a0, r0)
        return (f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r1} {r1} 0 0 1 {p1[0]:.1f} {p1[1]:.1f} L{q1[0]:.1f} {q1[1]:.1f} '
                f'A{r0} {r0} 0 0 0 {q0[0]:.1f} {q0[1]:.1f}Z" fill="{fill}" stroke="rgba(28,26,43,.25)" stroke-width="1.5"/>')
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(41, 60, y1=330)]
    for k in range(6):
        b.append(f'<circle cx="300" cy="470" r="{290 + k * 70}" fill="none" stroke="rgba(120,200,230,.12)" stroke-width="{4 - k * .5}" stroke-dasharray="{"40 18" if k % 2 == 0 else "2 14"}"/>')
    sea = lambda base, amp, ln, ph: "M-20 800 L-20 %d " % base + " ".join(
        f"L{x} {base + math.sin((x + ph) / ln * math.pi * 2) * amp:.1f}" for x in range(-20, 621, 10)) + " L620 800Z"
    b.append(f'<path d="{sea(640, 10, 200, 0)}" fill="#1a4c74"/><path d="{sea(700, 9, 160, 60)}" fill="#123a5e"/><path d="{sea(752, 8, 130, 20)}" fill="#0b2a47"/>')
    b.append(text(300, 150, "Wave", "Bowlby One", 128, "#f7eed8", 400, ls=2, extra='filter="url(#k-drop)"'))
    b.append(text(300, 196, "One clue. Find the hidden target.", "Figtree", 23, "#a9c3d6", 700))
    # device housing
    b.append('<g filter="url(#k-drop)"><path d="M40 650 Q40 676 66 676 L534 676 Q560 676 560 650 L560 470 A260 260 0 0 0 40 470Z" fill="url(#shell)"/></g>')
    b.append(f'<path d="M{cx-242} {cy} A242 242 0 0 1 {cx+242} {cy}" fill="none" stroke="#cbd6db" stroke-width="14"/>')
    b.append(f'<path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}Z" fill="url(#face)"/>')
    for u in range(0, 101, 5):
        a = (u - 50) * 1.8; ln = 16 if u % 10 == 0 else 8
        p0, p1 = P(a, R - 4 - ln), P(a, R - 4)
        b.append(f'<line x1="{p0[0]:.1f}" y1="{p0[1]:.1f}" x2="{p1[0]:.1f}" y2="{p1[1]:.1f}" stroke="#b9a77d" stroke-width="2.5" stroke-linecap="round"/>')
    tgt = 34  # degrees right of center
    w = []
    for lo, hi, col, n in [(-10, -6, "#f5d45e", 2), (-6, -2, "#ef8a3a", 3), (-2, 2, "#25b2c2", 4), (2, 6, "#ef8a3a", 3), (6, 10, "#f5d45e", 2)]:
        a0, a1 = tgt + lo * 1.8, tgt + hi * 1.8
        w.append(sec(30, R - 2, a0, a1, col))
        lp = P((a0 + a1) / 2, 202)
        w.append(text(f"{lp[0]:.1f}", f"{lp[1] + 8:.1f}", str(n), "Bowlby One", 22, "#1c1a2b", 400,
                      extra=f'transform="rotate({(a0 + a1) / 2:.1f} {lp[0]:.1f} {lp[1] + 0:.1f})"'))
    # smoked-glass screen swinging away (rotated 125deg around the hub)
    sh = (f'<g transform="rotate(152 {cx} {cy})"><path d="M{cx-234} {cy} A234 234 0 0 1 {cx+234} {cy}Z" fill="url(#glass)"/>'
          f'<path d="M{cx-234} {cy} A234 234 0 0 1 {cx+234} {cy}" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="4"/></g>')
    b.append(f'<g clip-path="url(#wv-win)">{"".join(w)}{sh}</g>')
    b.append(rect(52, 465, 496, 11, "#05232a", 5))
    # needle into the 4
    na = tgt + 0.6
    tip, gp = P(na, 236), P(na, 192)
    b.append(f'<g filter="url(#k-drop-s)"><line x1="{cx}" y1="{cy}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="#e3243c" stroke-width="7" stroke-linecap="round"/>'
             f'<circle cx="{gp[0]:.1f}" cy="{gp[1]:.1f}" r="11" fill="#e3243c" stroke="#fff" stroke-width="3.5"/></g>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="28" fill="url(#cap)"/><circle cx="{cx}" cy="{cy}" r="11" fill="#e3243c"/>')
    # spectrum card in the slot
    b.append(rect(120, 500, 360, 10, "#05232a", 5))
    b.append(f'<g filter="url(#k-drop-s)"><path d="M126 506 L306 506 L290 646 L126 646 Q118 646 118 638 L118 514 Q118 506 126 506Z" fill="#9fe2ea"/>'
             f'<path d="M306 506 L474 506 Q482 506 482 514 L482 638 Q482 646 474 646 L290 646Z" fill="#ffd59a"/></g>')
    b.append(text(208, 588, "Cold", "Bowlby One", 40, "#1c1a2b") + text(392, 588, "Hot", "Bowlby One", 40, "#1c1a2b"))
    b.append(text(300, 740, "Talk. Turn. Reveal.", "Figtree", 22, "#f7eed8", 800, extra='opacity=".85"'))
    return svg(d, "".join(b))


def wheel_quest():
    d = rad("bg", [(0, "#2a2150"), (1, "#141022")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 70, "PHIL YOUNG'S ENGLISH SCHOOL", "JetBrains Mono", 13, "#ff6f61", 700, ls=4))
    b.append(text(300, 148, "Wheel Quest", "Fraunces", 82, "#ff6f61", 800))
    b.append(text(300, 188, "Spin · guess · solve the sentence", "Space Grotesk", 21, "#c9c2e8", 500))
    # puzzle board
    puzzle = ["I _ _ V E", "A _ O G"]
    words = ["I LOVE", "MY DOG"]
    shown = set("IVEOG")
    for r, w in enumerate(words):
        x0 = (600 - len(w) * 50) / 2
        for k, ch in enumerate(w):
            x, y = x0 + k * 50, 218 + r * 62
            if ch == " ":
                continue
            b.append(rect(x, y, 44, 54, "#f4f1ff" if ch in shown else "#4fd8b0", 6, 'stroke="#141022" stroke-width="2"')
                     + (text(x + 22, y + 40, ch, "Fraunces", 32, "#141022", 800) if ch in shown else ""))
    # wheel
    cx, cy, R = 300, 590, 180
    cols = ["#4fd8b0", "#5fb8ff", "#b98cff", "#ff6f61", "#ffd479", "#ff5470"]
    vals = ["300", "500", "BANK", "200", "800", "×2", "400", "600", "LOSE", "250", "700", "150"]
    n = len(vals)
    for k, v in enumerate(vals):
        a0, a1 = math.radians(k * 360 / n - 90), math.radians((k + 1) * 360 / n - 90)
        p0 = (cx + R * math.cos(a0), cy + R * math.sin(a0))
        p1 = (cx + R * math.cos(a1), cy + R * math.sin(a1))
        col = "#1c1733" if v == "LOSE" else cols[k % 6]
        b.append(f'<path d="M{cx} {cy} L{p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 1 {p1[0]:.1f} {p1[1]:.1f} Z" fill="{col}" stroke="#141022" stroke-width="3"/>')
        am = (a0 + a1) / 2
        tx, ty = cx + R * .68 * math.cos(am), cy + R * .68 * math.sin(am)
        b.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="middle" dominant-baseline="middle" font-family="\'Space Grotesk\'" font-weight="700" font-size="22" '
                 f'fill="{"#fff" if v == "LOSE" else "#141022"}" transform="rotate({math.degrees(am)+90:.1f} {tx:.1f} {ty:.1f})">{v}</text>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#e8b04b" stroke-width="10"/>')
    for k in range(24):
        a = math.radians(k * 15)
        b.append(f'<circle cx="{cx + (R+1)*math.cos(a):.1f}" cy="{cy + (R+1)*math.sin(a):.1f}" r="4" fill="#ffd479"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="#e8b04b" stroke="#141022" stroke-width="4"/>' + emoji(cx, cy + 12, "⭐", 32))
    b.append(f'<polygon points="{cx-18},{cy-R-26} {cx+18},{cy-R-26} {cx},{cy-R+12}" fill="#ff5470" stroke="#fff" stroke-width="3"/>')
    return svg(d, "".join(b))


def word_buzz():
    b = [rect(0, 0, 600, 800, "#0d0d0f"), '<circle cx="300" cy="560" r="230" fill="#f04060" opacity=".14" filter="url(#k-glow)"/>']
    b.append(text(300, 150, 'WORD<tspan fill="#f0e040">BUZZ</tspan>', "Syne", 52, "#f0f0f5", 800, ls=-1))
    b.append(text(300, 196, "BE FAST · SAY IT FIRST", "Space Mono", 18, "#666680", 700, ls=5))
    word = "ELEPHANT"
    shown = {0, 2, 4, 7}
    for k, ch in enumerate(word):
        x = 46 + k * 64
        b.append(rect(x, 250, 56, 72, "#16161a", 8, f'stroke="{"#f0e040" if k in shown else "#2a2a35"}" stroke-width="3"')
                 + (text(x + 28, 302, ch, "Space Mono", 38, "#f0e040", 700) if k in shown else text(x + 28, 304, "_", "Space Mono", 38, "#3a3a48", 700)))
    b.append(rect(46, 344, 508, 10, "#1e1e24", 5) + rect(46, 344, 320, 10, "#40e0f0", 5))
    # buzzer
    b.append('<ellipse cx="300" cy="660" rx="190" ry="54" fill="#1e1e24"/><ellipse cx="300" cy="640" rx="190" ry="54" fill="#2a2a35"/>'
             '<rect x="150" y="560" width="300" height="80" fill="#a01c34"/><ellipse cx="300" cy="640" rx="150" ry="40" fill="#a01c34"/>'
             '<ellipse cx="300" cy="560" rx="150" ry="44" fill="#f04060"/><ellipse cx="270" cy="548" rx="70" ry="16" fill="#fff" opacity=".3"/>')
    for k, (dx, dy) in enumerate([(-200, -110), (200, -110), (-230, -30), (230, -30)]):
        b.append(f'<path d="M{300+dx*.6:.0f} {560+dy*.6:.0f} L{300+dx:.0f} {560+dy:.0f}" stroke="#f0e040" stroke-width="6" stroke-linecap="round"/>')
    b.append(text(300, 470, "BZZZT!", "Syne", 52, "#f0e040", 800, ls=4))
    b.append(footer("A1–B2 · TEAMS · REVEAL SPEED", "Space Mono", "#40e0f0", 14, 3, 770, 700))
    return svg("", "".join(b))


def word_gap():
    d = rad("bg", [(0, "#1e2f45"), (1, "#0f1923")], cy="40%")
    b = [rect(0, 0, 600, 800, "url(#bg)"), stars(41, 80, "#fff", 800, (.6, 1.8), (.2, .8))]
    b.append(text(280, 140, "WordGap", "Fraunces", 96, "#ffcc00", 700) + emoji(520, 112, "✨", 50))
    b.append(text(300, 186, "EFL CLASSROOM CHALLENGE", "Nunito", 17, "#4ecdc4", 900, ls=6))
    b.append(f'<g filter="url(#k-drop)">{rect(40, 240, 520, 150, "#1e2f45", 20, "stroke=\"#2e4a6a\" stroke-width=\"3\"")}</g>')
    b.append(text(300, 302, "She has lived here", "Nunito", 34, "#eef3f9", 800))
    b.append(text(300, 352, '<tspan fill="#ffcc00">______</tspan> 2015.', "Nunito", 34, "#eef3f9", 800))
    floats = [("since", 160, 520, "#4ecdc4", -8, True), ("for", 420, 480, "#ff6b6b", 6, False), ("ago", 450, 640, "#a78bfa", -4, False),
              ("during", 170, 660, "#ff6b6b", 5, False)]
    for (w, x, y, col, rot, good) in floats:
        b.append(f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#k-drop)">{rect(-80, -36, 160, 72, "#0f1923", 36, f"stroke=\"{col}\" stroke-width=\"4\"")}'
                 + text(0, 12, w, "Nunito", 32, col, 900) + "</g>")
    b.append('<path d="M190 480 Q 220 420 260 380" fill="none" stroke="#4ecdc4" stroke-width="3" stroke-dasharray="6 8"/>')
    b.append(emoji(250, 470, "👆", 46))
    b.append(footer("WORDS DRIFT · CLICK THE RIGHT ONE", "Nunito", "#ffcc00", 14, 3, 776, 900))
    return svg(d, "".join(b))


def word_quest():
    d = lin("tt", [(0, "#7f5af0"), (1, "#2cb67d")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#0f0e17"), '<circle cx="300" cy="460" r="250" fill="#7f5af0" opacity=".12" filter="url(#k-glow)"/>']
    b.append(text(300, 122, "WordQuest", "Syne", 50, "url(#tt)", 800))
    b.append(text(300, 166, "TEACHER EDITION", "Space Mono", 17, "#72757e", 700, ls=8))
    def pat(g, t="BLUNT"):
        return "".join("c" if g[i] == t[i] else ("p" if g[i] in t else "a") for i in range(5))
    rows = [(w, pat(w)) for w in ["CRANE", "SPOIL", "BLUSH", "BLUNT"]] + [("", ""), ("", "")]
    col = {"c": "#2cb67d", "p": "#e9b949", "a": "#100f1e"}
    st = {"c": "#2cb67d", "p": "#e9b949", "a": "#3d3a68"}
    cs, g = 82, 10
    x0 = (600 - 5 * cs - 4 * g) / 2
    for r, (w, pat) in enumerate(rows):
        for c in range(5):
            x, y = x0 + c * (cs + g), 200 + r * (cs + g)
            if w:
                k = pat[c] if pat[c] in col else "a"
                b.append(rect(x, y, cs, cs, col[k], 8, f'stroke="{st[k]}" stroke-width="3"') + text(x + cs/2, y + cs/2 + 14, w[c], "Space Mono", 40, "#fffffe" if k != "a" else "#4a4960", 700))
            else:
                b.append(rect(x, y, cs, cs, "none", 8, 'stroke="#2e2c50" stroke-width="3"'))
    b.append(text(300, 768, "CUSTOM WORD · DICTIONARY CHECK", "Space Mono", 14, "#7f5af0", 700, ls=3))
    return svg(d, "".join(b))


def word_search():
    b = []
    chalkboard(b)
    b.append(rect(14, 14, 572, 772, "none", 10, 'stroke="#8a5a2b" stroke-width="14"'))
    b.append(text(300, 104, "Word Search", "Caveat", 86, "#f0ede0", 700))
    b.append(text(300, 152, "MAKER", "Caveat", 44, "#f5d07a", 700, ls=12))
    grid = ["CATSPLMQ", "RXDOGBEA", "OWLNKTSR", "BFISHUAE", "EHORSEMB", "ARABBITZ", "RQFROGVW", "YDUCKLON"]
    found = [((0, 0), (0, 2), "#4ecb71"), ((1, 2), (1, 4), "#5bb8d4"), ((2, 0), (2, 2), "#e8b84b"), ((3, 1), (3, 4), "#e8604b"),
             ((4, 1), (4, 5), "#c8a2f5"), ((5, 1), (5, 6), "#4ecb71"), ((7, 1), (7, 4), "#5bb8d4")]
    cs = 58
    x0, y0 = (600 - 8 * cs) / 2, 190
    for (r1, c1), (r2, c2), col in found:
        xa, ya = x0 + c1 * cs + cs/2, y0 + r1 * cs + cs/2
        xb, yb = x0 + c2 * cs + cs/2, y0 + r2 * cs + cs/2
        b.append(f'<line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}" stroke="{col}" stroke-opacity=".45" stroke-width="44" stroke-linecap="round"/>')
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            b.append(text(x0 + c * cs + cs/2, y0 + r * cs + cs/2 + 13, ch, "DM Mono", 34, "#f0ede0", 500))
    b.append(text(300, 712, "cat · dog · owl · fish · horse · rabbit · duck", "Caveat", 30, "#c8c4b0", 700))
    b.append(text(300, 752, "⏱ Beat the clock", "Caveat", 30, "#f5d07a", 700))
    return svg("", "".join(b))


COVERS = {
    "trivia-teams": trivia_badges, "truorfalse": true_or_false, "tictactoe": ultimate_ttt, "unscramble": unscramble,
    "vocab-toolkit": vocab_toolkit, "wave": wave, "wheel": wheel_quest, "word-buzz": word_buzz, "word-gap-game": word_gap,
    "teacher-wordle": word_quest, "wordsearch": word_search,
}
