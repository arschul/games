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
    d = (lin("wqsky", [(0, "#060b18"), (.6, "#101d38"), (1, "#2a3a5e")]) + lin("wqsea", [(0, "#16294a"), (1, "#050b17")])
         + lin("wqdeck", [(0, "#7a4c24"), (1, "#3f2410")]) + lin("wqboard", [(0, "#7a4c24"), (.5, "#5c3818"), (1, "#3f2410")])
         + rad("wqbrass", [(0, "#fff0b0"), (.35, "#e3b85a"), (.8, "#9a6c1e"), (1, "#5a3c0a")], cx="40%", cy="35%")
         + lin("wqtile", [(0, "#1f3a5a"), (1, "#0c1a2e")]) + rad("wqcloth", [(0, "#fffaf0"), (.6, "#efe4cc"), (1, "#d6c7a3")], cx="35%", cy="25%")
         + rad("wqmoon", [(.55, "#f4ecd0"), (1, "rgba(244,236,208,0)")], cy="50%"))
    b = [rect(0, 0, 600, 800, "url(#wqsky)"), stars(53, 70, y1=300)]
    b.append('<circle cx="470" cy="352" r="46" fill="url(#wqmoon)" opacity=".35"/><circle cx="470" cy="352" r="22" fill="#f4ecd0"/>')
    b.append(rect(0, 362, 600, 70, "url(#wqsea)"))
    for k in range(8):
        w = 16 + k * 8
        b.append(rect(470 - w / 2, 368 + k * 7.5, w, 2.5, "#f4ecd0", 1, f'opacity="{.5 - k * .05:.2f}"'))
    b.append(rect(0, 430, 600, 370, "url(#wqdeck)"))
    for k in range(9):
        b.append(rect(0, 470 + k * 42, 600, 2, "#2a170a", 0, 'opacity=".7"'))
    b.append(rect(0, 424, 600, 14, "#6b2e1f", 3))
    b.append(text(300, 92, "Wheel Quest", "Alfa Slab One", 76, "#3a1c08"))
    b.append(text(300, 86, "Wheel Quest", "Alfa Slab One", 76, "#f3d27a"))
    b.append(text(300, 124, "Spin, guess and solve the sentence", "Hanken Grotesk", 22, "#e6d6b0", 700))
    # nameboard
    b.append(f'<g filter="url(#k-drop)">{rect(48, 150, 504, 176, "#6b2e1f", 16)}{rect(60, 162, 480, 152, "url(#wqboard)", 10)}</g>')
    words, shown = ["SPIN THE", "WHEEL"], set("SNTHE")
    for r, w in enumerate(words):
        x0 = (600 - len(w) * 54) / 2
        for k, ch in enumerate(w):
            x, y = x0 + k * 54 + 3, 176 + r * 68
            if ch == " ":
                continue
            if ch in shown:
                b.append(rect(x, y, 48, 60, "url(#wqcloth)", 6, 'stroke="#c99a3b" stroke-width="3"') + text(x + 24, y + 46, ch, "Alfa Slab One", 38, "#1b2c4a"))
            else:
                b.append(rect(x, y, 48, 60, "url(#wqtile)", 6, 'stroke="#c99a3b" stroke-width="3"') + f'<circle cx="{x+24}" cy="{y+30}" r="8" fill="#c99a3b" opacity=".4"/>')
    # helm
    cx, cy, R = 300, 600, 160
    for k in range(8):
        a = math.radians(k * 45)
        x1, y1 = cx + 150 * math.sin(a), cy - 150 * math.cos(a)
        x2, y2 = cx + 205 * math.sin(a), cy - 205 * math.cos(a)
        b.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#4a1d10" stroke-width="18" stroke-linecap="round"/><line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#a0553a" stroke-width="7" stroke-linecap="round"/>')
        b.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="11" fill="#7a3522" stroke="#2a0f07" stroke-width="2"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R+18}" fill="#6b2e1f" stroke="#2a0f07" stroke-width="4" filter="url(#k-drop)"/><circle cx="{cx}" cy="{cy}" r="{R+9}" fill="none" stroke="#c99a3b" stroke-width="3"/>')
    paint = [("#1f3a5a", "#f3e6c6"), ("#efe4cc", "#6b2e1f"), ("#1d6f66", "#f3e6c6"), ("#c98a2b", "#24180f")]
    vals = ["800", "300", "BANK", "700", "1000", "500", "LOSE", "900", "400", "600", "200", "800", "300", "BANK", "700", "500"]
    n = len(vals)
    for k, v in enumerate(vals):
        a0, a1 = math.radians(k * 360 / n - 90 - 11.25), math.radians((k + 1) * 360 / n - 90 - 11.25)
        p0, p1 = (cx + R * math.cos(a0), cy + R * math.sin(a0)), (cx + R * math.cos(a1), cy + R * math.sin(a1))
        col, ink = ("#c22a22", "#fff4e0") if v == "BANK" else ("#2b3447", "#a9c4ff") if v == "LOSE" else paint[k % 4]
        b.append(f'<path d="M{cx} {cy} L{p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 1 {p1[0]:.1f} {p1[1]:.1f} Z" fill="{col}" stroke="#c99a3b" stroke-width="2"/>')
        am = math.degrees((a0 + a1) / 2) + 90
        if v in ("BANK", "LOSE"):
            b.append(f'<g transform="rotate({am:.1f} {cx} {cy})">' + (f'<path transform="translate({cx} {cy-R+30})" d="M3 -15 L-7 3 H0 L-3 17 L9 -3 H2 Z" fill="#ffe27a"/>' if v == "BANK" else f'<g transform="translate({cx} {cy-R+30})" fill="none" stroke="#a9c4ff" stroke-width="3.5" stroke-linecap="round"><circle cy="-11" r="4"/><path d="M0 -7 V15 M-8 -1 H8 M-11 7 Q-10 17 0 17 Q10 17 11 7"/></g>') + '</g>')
        else:
            st = 22 if len(v) > 3 else 25
            b.append(f'<g transform="rotate({am:.1f} {cx} {cy})">' + "".join(text(cx, cy - R + 26 + j * st, ch, "Alfa Slab One", 24 if len(v) > 3 else 27, ink) for j, ch in enumerate(v)) + '</g>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="url(#wqbrass)" stroke="#5a3c0a" stroke-width="3"/>')
    b.append(f'<path transform="translate({cx} {cy})" d="M0 -34 L6 -6 L34 0 L6 6 L0 34 L-6 6 L-34 0 L-6 -6Z" fill="#6b2e1f"/><circle cx="{cx}" cy="{cy}" r="6" fill="#f3d27a"/>')
    b.append(f'<path d="M{cx} {cy-R+8} L{cx-13} {cy-R-48} Q{cx} {cy-R-66} {cx+13} {cy-R-48} Z" fill="url(#wqbrass)" stroke="#4a3208" stroke-width="3" filter="url(#k-drop-s)"/><circle cx="{cx}" cy="{cy-R-48}" r="6" fill="#2a1a0c"/>')
    # coins
    for x, y in [(96, 700), (122, 722), (500, 690), (476, 724)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="17" fill="url(#wqbrass)" stroke="#4a3208" stroke-width="2"/>')
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
    """Letterpress print shop: wooden type locked in an iron chase, inked words."""
    d = (lin("wsWall", [("0", "#2a2530"), ("1", "#141317")])
         + rad("wsLamp", [("0", "rgba(255,206,140,.32)"), ("1", "rgba(255,206,140,0)")], cy="0%", r="80%")
         + lin("wsIron", [("0", "#4a4a52"), (".55", "#26262b"), ("1", "#34343a")], x2=1, y2=1)
         + lin("wsMaple", [("0", "#d6a166"), ("1", "#ad7943")])
         + rad("wsFace", [("0", "#fbf3e0"), ("1", "#d8c6a4")], cx="30%", cy="25%", r="90%")
         + lin("wsBrass", [("0", "#f2d98d"), (".5", "#c8a24a"), ("1", "#8c6c25")]))
    b = [rect(0, 0, 600, 800, "url(#wsWall)")]
    rnd = random.Random(19)
    for _ in range(9):
        x, y, sz = rnd.uniform(0, 600), rnd.uniform(120, 820), rnd.uniform(140, 260)
        b.append(text(round(x), round(y), rnd.choice("AEQRWS&"), "Abril Fatface", round(sz), "rgba(233,220,196,.05)",
                      extra=f'transform="rotate({rnd.uniform(-12, 12):.1f} {x:.0f} {y:.0f})"'))
    b.append(rect(0, 0, 600, 800, "url(#wsLamp)"))
    b.append(text(300, 106, "Word", "Abril Fatface", 100, "#f1e9da"))
    b.append(text(300, 196, "Search", "Abril Fatface", 100, "#f1e9da"))
    grid = ["CATSPLM", "RXDOGBE", "OWLNKTS", "BFISHUA", "EHORSEM", "ARABBIT", "YDUCKLO"]
    n, cs, gap = 7, 56, 5
    side = n * cs + (n - 1) * gap
    x0, y0 = (600 - side) / 2, 262
    b.append(rect(x0 - 40, y0 - 40, side + 80, side + 80, "url(#wsIron)", 12, 'filter="url(#k-drop)"'))
    b.append(rect(x0 - 24, y0 - 24, side + 48, side + 48, "url(#wsMaple)", 5))
    b.append(rect(x0 - 10, y0 - 10, side + 20, side + 20, "#1a1310", 3))
    for qx, qy, rot in ((x0 + side * .62, y0 - 47, 0), (x0 - 47, y0 + side * .3, 90), (x0 + side + 35, y0 + side * .7, 90)):
        b.append(f'<g transform="rotate({rot} {qx + 22} {qy + 9})">' + rect(qx, qy, 44, 18, "url(#wsBrass)", 4) + '</g>')
    pitch = cs + gap
    found = [((0, 0), (0, 2), "#2F5FD0"), ((1, 2), (1, 4), "#E0442E"), ((3, 1), (3, 4), "#2E9E5B"),
             ((4, 1), (4, 5), "#C8338E"), ((6, 1), (6, 4), "#C9930F"), ((2, 0), (2, 2), "#12A0A8")]
    tint = {}
    for (r1, c1), (r2, c2), col in found:
        steps = max(abs(r2 - r1), abs(c2 - c1))
        for i in range(steps + 1):
            tint[(r1 + (r2 - r1) * i // steps, c1 + (c2 - c1) * i // steps)] = col
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            x, y = x0 + c * pitch, y0 + r * pitch
            b.append(rect(x, y + 3, cs, cs, "#8f6c45", 5))
            b.append(rect(x, y, cs, cs, "url(#wsFace)", 5))
            if (r, c) in tint:
                b.append(rect(x, y, cs, cs, tint[(r, c)], 5, 'fill-opacity=".3"'))
            b.append(text(x + cs / 2, y + cs / 2 + 14, ch, "Archivo", 40, "#2a2420", 800))
    for (r1, c1), (r2, c2), col in found:
        xa, ya = x0 + c1 * pitch + cs / 2, y0 + r1 * pitch + cs / 2
        xb, yb = x0 + c2 * pitch + cs / 2, y0 + r2 * pitch + cs / 2
        ang = math.degrees(math.atan2(yb - ya, xb - xa)); L = math.hypot(xb - xa, yb - ya); h = cs * .86
        b.append(f'<rect x="{xa - h/2:.1f}" y="{ya - h/2:.1f}" width="{L + h:.1f}" height="{h:.1f}" rx="{h/2:.1f}" fill="none" '
                 f'stroke="{col}" stroke-width="5" transform="rotate({ang:.1f} {xa:.1f} {ya:.1f})"/>')
    sy = y0 + side + 58
    for i, (w, col) in enumerate((("CAT", "#2F5FD0"), ("DOG", "#E0442E"), ("FISH", "#2E9E5B"), ("HORSE", "#C8338E"))):
        sw = 22 + len(w) * 19
        sx = [83, 182, 281, 399][i]
        b.append(rect(sx, sy + 3, sw, 38, "rgba(0,0,0,.45)", 6))
        b.append(rect(sx, sy, sw, 38, col, 6))
        b.append(text(sx + sw / 2, sy + 27, w, "Archivo", 22, "#fff", 800, ls=1.5))
    return svg(d, "".join(b))


COVERS = {
    "trivia-teams": trivia_badges, "truorfalse": true_or_false, "tictactoe": ultimate_ttt, "unscramble": unscramble,
    "vocab-toolkit": vocab_toolkit, "wave": wave, "wheel": wheel_quest, "word-buzz": word_buzz, "word-gap-game": word_gap,
    "teacher-wordle": word_quest, "wordsearch": word_search,
}
