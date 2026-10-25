"""Batch D covers."""
import math, random
from kit import *


def wood_tile(x, y, s, ch, fill="#e9c88f", ink="#2b1d0f", size=None):
    size = size or s * .62
    return (f'<g filter="url(#k-drop-s)">{rect(x, y, s, s, fill, s*.14, "stroke=\"#8a5a2b\" stroke-width=\"3\"")}'
            f'{rect(x+4, y+4, s-8, s*.25, "#fff", s*.1, "opacity=\".25\"")}</g>'
            + text(x + s/2, y + s/2 + size*.36, ch, "Alfa Slab One", size, ink))


def letter_swap():
    b = [rect(0, 0, 600, 800, "#1b2026")]
    b.append(text(300, 104, "LETTER", "DM Sans", 72, "#e8ecef", 800, ls=10))
    for k, ch in enumerate("SWAP"):
        b.append(wood_tile(96 + k * 106, 136, 92, ch))
    b.append(text(300, 288, "Change one letter. Make a new word.", "DM Sans", 20, "#8e9aa6", 500))
    ladder = ["LATE", "LAME", "CAME", "CAKE", "BAKE"]
    changed = [None, 2, 0, 2, 0]
    for r, w in enumerate(ladder):
        y = 320 + r * 92
        for c, ch in enumerate(w):
            hot = changed[r] == c
            b.append(wood_tile(150 + c * 78, y, 70, ch, "#f6d38a" if hot else "#d9c4a0", "#b4281c" if hot else "#2b1d0f"))
    b.append(footer("TEAMS · 4-LETTER WORDS · AGAINST THE CLOCK", "DM Sans", "#c3cad0", 13, 3, 782))
    return svg("", "".join(b))


def lexicon_duel():
    d = lin("tt", [(0, "#f5d68a"), (.5, "#e8b84b"), (1, "#5ba3e8")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#0d0d12"),
         '<circle cx="0" cy="560" r="260" fill="#e8b84b" opacity=".12" filter="url(#k-glow)"/>',
         '<circle cx="600" cy="560" r="260" fill="#5ba3e8" opacity=".12" filter="url(#k-glow)"/>']
    b.append(text(300, 72, "A GAME OF WORDS &amp; WAR", "DM Mono", 15, "#6b6880", 500, ls=5))
    b.append(text(300, 160, "Lexicon Duel", "DM Sans", 84, "url(#tt)", 800))
    b.append(text(300, 200, "FORGE WORDS. DEAL DAMAGE.", "DM Mono", 16, "#9a97b0", 500, ls=4))
    def board(x0, col, letters, used):
        out = [rect(x0 - 10, 280, 244, 244, "#14141d", 14, f'stroke="{col}" stroke-width="3"')]
        for k, ch in enumerate(letters):
            r, c = divmod(k, 4)
            x, y = x0 + c * 57, 290 + r * 57
            on = k in used
            out.append(rect(x, y, 50, 50, col if on else "#1e1e2c", 8, f'stroke="{col}" stroke-opacity=".5" stroke-width="1.5"')
                       + text(x + 25, y + 34, ch, "DM Sans", 26, "#0d0d12" if on else "#e8e8f0", 800))
        return "".join(out)
    b.append(board(42, "#e8b84b", "STARBLOEMIKNDWPU", {0, 1, 2, 5, 6}))
    b.append(board(334, "#5ba3e8", "QUESTFLAMIRODNEY", {0, 1, 2, 3, 4}))
    # clash
    b.append('<g transform="translate(300 400)"><polygon points="0,-60 14,-14 60,0 14,14 0,60 -14,14 -60,0 -14,-14" fill="#fff" opacity=".9" filter="url(#k-glow-s)"/></g>')
    b.append(text(155, 560, "STAB", "DM Mono", 26, "#e8b84b", 500, ls=6) + text(447, 560, "QUEST", "DM Mono", 26, "#5ba3e8", 500, ls=6))
    def hp(x, col, frac, lab):
        return (text(x, 616, lab, "DM Mono", 14, col, 500, "start", 3) + rect(x, 626, 220, 16, "#1e1e2c", 8)
                + rect(x, 626, 220 * frac, 16, col, 8))
    b.append(hp(42, "#e8b84b", .62, "CHAMPION  62") + hp(334, "#5ba3e8", .38, "CHALLENGER  38"))
    b.append(text(300, 712, "−24", "DM Sans", 72, "#f06060", 800, extra='filter="url(#k-drop)"'))
    b.append(footer("PVP · SOLO WAVES · DICTIONARY CHECKED", "DM Mono", "#6b6880", 13, 3, 776, 500))
    return svg(d, "".join(b))


def linking_park():
    d = lin("sky", [(0, "#0b1a2e"), (1, "#1a2e1a")]) + lin("gt", [(0, "#8fe06a"), (1, "#3a7a1e")])
    b = [rect(0, 0, 600, 800, "url(#sky)"), stars(11, 50, "#fff", 320, (.6, 1.6), (.2, .7)),
         '<circle cx="70" cy="352" r="26" fill="#f6efc8"/><circle cx="81" cy="344" r="23" fill="#0b1a2e"/>']
    b.append(text(300, 160, "LINKING", "Bebas Neue", 122, "url(#gt)", ls=6, extra='filter="url(#k-drop)"'))
    b.append(text(300, 268, "PARK", "Bebas Neue", 122, "url(#gt)", ls=6, extra='filter="url(#k-drop)"'))
    b.append(text(300, 306, "TRANSITION WORD GAME", "Nunito", 18, "#d4a017", 900, ls=6))
    b.append('<path d="M0 520 Q 300 450 600 520 V800 H0 Z" fill="#2d6020"/><ellipse cx="300" cy="610" rx="170" ry="40" fill="#1e4a6b"/>'
             '<path d="M0 640 Q 300 600 600 650 V800 H0 Z" fill="#3a7a20"/>')
    def tree(x, y, s):
        return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-8" y="0" width="16" height="70" fill="#5c3d1e"/>'
                '<circle cx="0" cy="-20" r="46" fill="#2d6020"/><circle cx="-26" cy="4" r="32" fill="#3a7a20"/><circle cx="24" cy="0" r="34" fill="#4a8a2a"/></g>')
    b.append(tree(70, 450, 1.1) + tree(540, 470, 1.2) + tree(150, 520, .7))
    # signpost
    b.append('<rect x="292" y="380" width="16" height="320" fill="#7a5030" stroke="#3a2410" stroke-width="3"/>')
    signs = [("HOWEVER", -6, "#d4a017"), ("THEREFORE", 5, "#c8a84b"), ("IN ADDITION", -4, "#d4a017")]
    for k, (w, rot, col) in enumerate(signs):
        y = 410 + k * 76
        dx = 70 if k % 2 == 0 else -70
        b.append(f'<g transform="translate({300+dx} {y}) rotate({rot})" filter="url(#k-drop-s)">'
                 f'<polygon points="-120,-26 100,-26 130,0 100,26 -120,26" fill="{col}" stroke="#3a2410" stroke-width="3" transform="scale({1 if dx>0 else -1} 1)"/>'
                 + text(0, 11, w, "Bebas Neue", 34, "#2a1a08", ls=3) + "</g>")
    b.append(footer("A1–B2 · TEAMS · DRAG THE CONNECTOR", "Nunito", "#c8e6a0", 13, 3, 784, 900))
    return svg(d, "".join(b))


def mastermind():
    d = rad("bg", [(0, "#2a1a5a"), (1, "#0e0a1f")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)"), '<circle cx="120" cy="680" r="160" fill="#7c3aed" opacity=".2" filter="url(#k-glow)"/>']
    b.append(emoji(118, 120, "🎯", 60) + text(160, 140, "Mastermind", "Montserrat", 66, "#f4f0ff", 900, "start"))
    b.append(text(300, 186, "CRACK THE SECRET COLOR CODE", "Open Sans", 16, "#a99bd6", 700, ls=4))
    pal = ["#ef4444", "#3b82f6", "#22c55e", "#facc15", "#a855f7", "#f97316"]
    rows = [[0, 1, 2, 3], [1, 0, 4, 3], [5, 0, 3, 1], [2, 0, 3, 1], [3, 0, 2, 1]]
    fb = [(1, 2), (0, 3), (1, 2), (2, 2), (4, 0)]
    b.append(f'<g filter="url(#k-drop)">{rect(90, 214, 420, 540, "#5b3a1e", 26, "stroke=\"#2a1608\" stroke-width=\"5\"")}</g>')
    b.append(rect(110, 230, 380, 72, "#2a1608", 14))
    for k in range(4):
        b.append(f'<circle cx="{170+k*72}" cy="266" r="24" fill="#4a2e18"/>' + text(170 + k * 72, 276, "?", "Montserrat", 26, "#e8c99a", 900))
    for r, row in enumerate(rows):
        y = 350 + r * 84
        for c, p in enumerate(row):
            b.append(f'<circle cx="{170+c*72}" cy="{y}" r="25" fill="{pal[p]}" stroke="#2a1608" stroke-width="3"/>'
                     f'<circle cx="{164+c*72}" cy="{y-8}" r="7" fill="#fff" opacity=".45"/>')
        blk, wht = fb[r]
        pegs = ["#111"] * blk + ["#fff"] * wht + ["#3a2210"] * (4 - blk - wht)
        for i, col in enumerate(pegs):
            px, py = 440 + (i % 2) * 22, y - 11 + (i // 2) * 22
            b.append(f'<circle cx="{px}" cy="{py}" r="8" fill="{col}" stroke="#2a1608" stroke-width="2"/>')
    return svg(d, "".join(b))


def robot(x, y, col, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#k-drop-s)">'
            f'<line x1="0" y1="-38" x2="0" y2="-50" stroke="{col}" stroke-width="4"/><circle cx="0" cy="-52" r="6" fill="{col}"/>'
            f'<rect x="-26" y="-38" width="52" height="40" rx="10" fill="{col}" stroke="#050a17" stroke-width="3"/>'
            '<circle cx="-10" cy="-18" r="7" fill="#e6fbff"/><circle cx="10" cy="-18" r="7" fill="#e6fbff"/>'
            '<circle cx="-10" cy="-18" r="3" fill="#050a17"/><circle cx="10" cy="-18" r="3" fill="#050a17"/>'
            f'<rect x="-20" y="4" width="40" height="30" rx="6" fill="{col}" stroke="#050a17" stroke-width="3"/>'
            '<rect x="-24" y="34" width="14" height="10" rx="3" fill="#313c52"/><rect x="10" y="34" width="14" height="10" rx="3" fill="#313c52"/></g>')


def maze_race():
    d = rad("bg", [(0, "#0c1834"), (1, "#050a17")], cy="40%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 120, 'MAZE <tspan fill="#22d3ee">RACE</tspan>', "Exo 2", 96, "#eef3f9", 900, extra='font-style="italic"'))
    b.append(text(300, 162, "RACE YOUR ROBOT · WALL IN YOUR RIVALS", "Open Sans", 15, "#8fa6c9", 700, ls=3))
    cs, n = 56, 9
    x0, y0 = (600 - n * cs) / 2, 200
    b.append(rect(x0 - 10, y0 - 10, n * cs + 20, n * cs + 20, "#313c52", 14))
    for r in range(n):
        for c in range(n):
            b.append(rect(x0 + c*cs + 3, y0 + r*cs + 3, cs - 6, cs - 6, "#0c1834", 6))
    walls = [(1, 1, "h", 2, "#ef4444"), (3, 2, "v", 2, "#3b82f6"), (5, 4, "h", 2, "#ef4444"), (2, 6, "v", 2, "#3b82f6"),
             (6, 1, "h", 2, "#3b82f6"), (7, 5, "v", 2, "#ef4444"), (4, 7, "h", 2, "#3b82f6"), (0, 4, "v", 2, "#ef4444")]
    for (r, c, o, ln, col) in walls:
        if o == "h":
            b.append(rect(x0 + c*cs + 2, y0 + r*cs - 5, ln*cs - 4, 10, col, 4, 'filter="url(#k-drop-s)"'))
        else:
            b.append(rect(x0 + c*cs - 5, y0 + r*cs + 2, 10, ln*cs - 4, col, 4, 'filter="url(#k-drop-s)"'))
    # goal rows
    b.append(rect(x0, y0 - 4, n * cs, 4, "#ef4444") + rect(x0, y0 + n * cs, n * cs, 4, "#3b82f6"))
    # conduit path hint
    b.append(f'<polyline points="{x0+4.5*cs},{y0+7.5*cs} {x0+4.5*cs},{y0+5.5*cs} {x0+6.5*cs},{y0+5.5*cs} {x0+6.5*cs},{y0+3.5*cs}" fill="none" stroke="#22d3ee" stroke-width="4" stroke-dasharray="6 8" opacity=".8"/>')
    b.append(robot(x0 + 4.5*cs, y0 + 7.5*cs + 6, "#3b82f6", .9) + robot(x0 + 3.5*cs, y0 + 1.5*cs + 6, "#ef4444", .9))
    b.append(footer("2 OR 4 PLAYERS · STRATEGY", "Exo 2", "#22d3ee", 16, 5, 744, 800))
    return svg(d, "".join(b))


def minefield():
    d = rad("bg", [(0, "#1a2440"), (1, "#0b1220")], cy="30%") + lin("amb", [(0, "#fbbf24"), (1, "#f59e0b")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(emoji(108, 132, "💣", 66) + text(150, 150, "Minefield", "Sora", 78, "url(#amb)", 800, "start"))
    b.append(text(300, 196, "ANSWER TO DIG · GRAB TREASURE · DODGE MINES", "Inter", 14, "#93a3c2", 800, ls=2))
    cs, g = 90, 10
    x0, y0 = (600 - 5 * cs - 4 * g) / 2, 236
    dug = {2: "💎", 6: "💥", 9: "🪙", 13: "🔄", 17: "💰", 19: "💣"}
    for k in range(25):
        r, c = divmod(k, 5)
        x, y = x0 + c * (cs + g), y0 + r * (cs + g)
        if y > 700:
            break
        if k in dug:
            hot = dug[k] in ("💥", "💣")
            b.append(rect(x, y, cs, cs, "#3a1420" if hot else "#0f2a2a", 14, f'stroke="{"#ef4444" if hot else "#10b981"}" stroke-width="3"')
                     + emoji(x + cs/2, y + cs/2 + 18, dug[k], 50))
        else:
            b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, cs, cs, "#1a2440", 14, "stroke=\"#25314c\" stroke-width=\"2\"")}</g>'
                     + text(x + cs/2, y + cs/2 + 12, k + 1, "Sora", 32, "#dde4f0", 700))
    b.append(text(300, 780, "TEAMS · STEAL · SWAP SCORES", "Sora", 16, "#f59e0b", 800, ls=4))
    return svg(d, "".join(b))


def mistake_hunters():
    d = ""
    b = [rect(0, 0, 600, 800, "#0d0f14")]
    b.append(text(300, 112, "MISTAKE", "Bebas Neue", 110, "#f0c040", ls=8))
    b.append(text(300, 214, "HUNTERS", "Bebas Neue", 110, "#f0c040", ls=8))
    b.append(text(300, 250, "FIND THE GRAMMAR MISTAKES", "DM Sans", 16, "#6b7592", 700, ls=5))
    lines = [("Yesterday she ", ("go", "#a05af0"), " to the"), ("libary and ", None, ""), ("buyed two ", ("books", None), "."), ]
    b.append(f'<g filter="url(#k-drop)">{rect(40, 290, 520, 300, "#161a23", 18, "stroke=\"#2a3045\" stroke-width=\"2\"")}</g>')
    b.append(text(70, 352, 'Yesterday she <tspan fill="#a05af0" text-decoration="underline">go</tspan> to the', "DM Mono", 30, "#e8ecf4", 500, "start"))
    b.append(text(70, 404, '<tspan fill="#f05a5a" text-decoration="underline">libary</tspan> and bought', "DM Mono", 30, "#e8ecf4", 500, "start"))
    b.append(text(70, 456, 'two <tspan fill="#5aabf0" text-decoration="underline">interest</tspan> books', "DM Mono", 30, "#e8ecf4", 500, "start"))
    b.append(text(70, 508, '<tspan fill="#40d490" text-decoration="underline">about always</tspan> dogs.', "DM Mono", 30, "#e8ecf4", 500, "start"))
    for (cx, cy, rx) in [(340, 342, 30), (124, 394, 66)]:
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="28" fill="none" stroke="#f0c040" stroke-width="3" transform="rotate(-4 {cx} {cy})"/>')
    chips = [("SPELLING", "#f05a5a"), ("VERB TENSE", "#a05af0"), ("WORD FORM", "#5aabf0"), ("WORD ORDER", "#40d490")]
    for k, (lab, col) in enumerate(chips):
        r, c = divmod(k, 2)
        x, y = 60 + c * 250, 640 + r * 58
        b.append(rect(x, y, 230, 44, col + "22", 22, f'stroke="{col}" stroke-width="2.5"') + text(x + 115, y + 29, lab, "DM Sans", 18, col, 800, ls=2))
    return svg(d, "".join(b))


def orbit():
    d = lin("tt", [(0, "#00e5ff"), (.5, "#7c4dff"), (1, "#ff4081")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "#0a0a0f"), stars(21, 70, "#e0e0ff", 800, (.6, 1.6), (.15, .6))]
    for r in (330, 260, 190):
        b.append(f'<ellipse cx="300" cy="470" rx="{r}" ry="{r*.32}" fill="none" stroke="#7c4dff" stroke-opacity=".25" stroke-width="2" transform="rotate(-18 300 470)"/>')
    b.append(glow_text(300, 136, "ORBIT", "Orbitron", 112, "url(#tt)", "#7c4dff", 900, ls=18))
    b.append(text(300, 180, "ROTATION STRATEGY GAME", "Space Mono", 16, "#6060a0", 700, ls=5))
    cs = 98
    x0, y0 = (600 - 4 * cs) / 2, 250
    b.append(f'<g filter="url(#k-drop)">{rect(x0 - 18, y0 - 18, 4 * cs + 36, 4 * cs + 36, "#12121a", 30, "stroke=\"#2a2a40\" stroke-width=\"3\"")}</g>')
    arrows = ["→", "→", "→", "↓", "↑", "→", "↓", "↓", "↑", "↑", "←", "↓", "↑", "←", "←", "←"]
    marbles = {0: "p1", 5: "p1", 10: "p1", 3: "p2", 6: "p2", 12: "p2", 9: "p2", 1: "p1"}
    for k, a in enumerate(arrows):
        r, c = divmod(k, 4)
        cx, cy = x0 + c * cs + cs/2, y0 + r * cs + cs/2
        b.append(f'<circle cx="{cx}" cy="{cy}" r="40" fill="#0f0f1e" stroke="#2a2a40" stroke-width="2.5"/>')
        m = marbles.get(k)
        if m:
            col, dk = ("#00e5ff", "#007a9e") if m == "p1" else ("#ff4081", "#9e1a40")
            b.append(f'<circle cx="{cx}" cy="{cy}" r="31" fill="{dk}"/><circle cx="{cx}" cy="{cy}" r="27" fill="{col}"/>'
                     f'<circle cx="{cx-9}" cy="{cy-9}" r="8" fill="#fff" opacity=".55"/>')
        else:
            b.append(text(cx, cy + 10, a, "Space Mono", 28, "#45457a", 700))
    b.append(text(300, 712, "FOUR IN A ROW · THEN EVERYTHING SPINS", "Space Mono", 15, "#e0e0ff", 700, ls=2))
    b.append(f'<circle cx="230" cy="752" r="12" fill="#00e5ff"/>' + text(300, 760, "vs", "Orbitron", 20, "#6060a0", 700) + '<circle cx="370" cy="752" r="12" fill="#ff4081"/>')
    return svg(d, "".join(b))


def order_up():
    d = rad("bg", [(0, "#0f3460"), (1, "#1a1a2e")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 136, 'Order <tspan fill="#e94560">Up!</tspan>', "Montserrat", 104, "#ffffff", 900, extra='filter="url(#k-drop)"'))
    b.append(text(300, 180, "SMALLEST → BIGGEST · FASTEST TEAM WINS", "Montserrat", 15, "#c9c9d9", 700, ls=2))
    items = [("🐜", "ant"), ("🐭", "mouse"), ("🐈", "cat"), ("🐴", "horse"), ("🐘", "elephant")]
    for k, (e, w) in enumerate(items):
        y = 224 + k * 104
        x = 70 + (14 if k == 2 else 0)
        rot = -3 if k == 2 else 0
        b.append(f'<g transform="rotate({rot} 300 {y+44})" filter="url(#k-drop-s)">{rect(x, y, 460, 88, "#1e2a45", 16, "stroke=\"#f5a623\" stroke-width=\"2.5\"" if k != 2 else "stroke=\"#e94560\" stroke-width=\"4\"")}'
                 + f'<circle cx="{x+46}" cy="{y+44}" r="28" fill="#e94560"/>' + text(x + 46, y + 55, k + 1, "Montserrat", 30, "#fff", 900)
                 + emoji(x + 128, y + 62, e, 46) + text(x + 180, y + 58, w, "Montserrat", 32, "#eaeaea", 800, "start")
                 + "".join(f'<rect x="{x+410}" y="{y+30+i*12}" width="26" height="4" rx="2" fill="#888"/>' for i in range(3)) + "</g>")
    b.append(footer("DRAG · DROP · RACE", "Montserrat", "#f5a623", 15, 6, 778, 800))
    return svg(d, "".join(b))


def perfect_fit():
    """Molded-plastic pop-up toy: teal tray on a pegboard, chrome wind-up timer, Shrikhand title."""
    d = (rad("pfLamp", [(0, "#ffbf6e"), (1, "#22313f")], cx="20%", cy="0%", r="90%")
         + lin("pfTray", [(0, "#2cc6bb"), (.5, "#14a39b"), (1, "#0f8c84")], x2=.2, y2=1)
         + rad("pfGloss", [(0, "#ffffff"), (1, "#ffffff00")], cx="34%", cy="24%", r="60%")
         + rad("pfFace", [(0, "#fffdf6"), (1, "#ece2cc")])
         + rad("pfBezel", [(0, "#ffffff"), (.45, "#d9dee4"), (.85, "#7d8794"), (1, "#5a636e")], cx="38%", cy="30%", r="80%")
         + '<pattern id="pfPeg" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="16" r="4" fill="#ffffff" opacity=".07"/><circle cx="15" cy="15" r="3.8" fill="#121a23"/></pattern>'
         + '<filter id="pfIn" x="-20%" y="-20%" width="140%" height="140%"><feOffset in="SourceAlpha" dy="5"/><feGaussianBlur stdDeviation="2.5" result="b"/>'
           '<feComposite in="SourceAlpha" in2="b" operator="arithmetic" k2="-1" k3="1" result="i"/><feFlood flood-color="#000" flood-opacity=".8"/>'
           '<feComposite in2="i" operator="in" result="s"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="s"/></feMerge></filter>')
    b = [rect(0, 0, 600, 800, "#22313f"), rect(0, 0, 600, 800, "url(#pfLamp)", 0, 'opacity=".45"'), rect(0, 0, 600, 800, "url(#pfPeg)")]
    # title
    b.append(text(300, 128, "Perfect Fit", "Shrikhand", 92, "#063f3b", extra='transform="translate(0,7)"'))
    b.append(text(300, 128, "Perfect Fit", "Shrikhand", 92, "#fbf3e2"))
    b.append(text(300, 172, "Fit every shape before the board pops!", "Atkinson Hyperlegible", 22, "#e9dcc2", 700))
    # tray
    b.append(rect(64, 214, 472, 26, "#9aa4af", 13, 'stroke="#5c656f" stroke-width="2"'))
    b.append(rect(40, 238, 520, 470, "#0b6762", 36))
    b.append(f'<g filter="url(#k-drop)">{rect(40, 228, 520, 470, "url(#pfTray)", 36)}</g>')
    b.append(rect(40, 228, 520, 200, "url(#pfGloss)", 36, 'opacity=".18"'))
    shapes = ["circle", "star", "tri", "square", "hex", "heart", "cross", "diamond", "square"]
    cols = {0: "#e8453c", 1: "#f5b300", 3: "#2f7ff0", 5: "#e84393", 6: "#8b5cf6", 8: "#ff7a1a"}
    rims = ["#e8453c", "#f5b300", "#38cf6d", "#2f7ff0", "#ff7a1a", "#e84393", "#8b5cf6", "#2cc6bb", "#ff7a1a"]
    for k, sh in enumerate(shapes):
        r_, c = divmod(k, 3)
        cx, cy = 150 + c * 150, 320 + r_ * 140
        b.append(f'<g filter="url(#pfIn)">{_shape(sh, cx, cy, 48, "#063f3b", rims[k])}</g>')
        col = cols.get(k)
        if col:
            b.append(f'<g filter="url(#k-drop-s)">{_shape(sh, cx, cy, 44, col, "#ffffff55")}</g>')
            b.append(_shape(sh, cx, cy, 44, "url(#pfGloss)", "none").replace('fill="url', 'opacity=".55" fill="url'))
            b.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{col}" stroke="#00000044" stroke-width="2"/>')
    # loose piece in flight toward its hole
    b.append('<path d="M500 640 Q 560 470 462 352" fill="none" stroke="#fbf3e2" stroke-width="3" stroke-dasharray="4 9" opacity=".7"/>')
    b.append(f'<g filter="url(#k-drop)" transform="rotate(-18 505 690)">{_shape("tri", 505, 690, 56, "#38cf6d", "#ffffff66")}</g>')
    # chrome kitchen timer
    b.append('<circle cx="122" cy="690" r="88" fill="#4b535d"/><circle cx="122" cy="684" r="88" fill="url(#pfBezel)"/>'
             '<circle cx="122" cy="684" r="72" fill="url(#pfFace)"/>'
             '<path d="M122 684 L122 626 A58 58 0 0 1 172 713 Z" fill="#ff4b3e" opacity=".92"/>'
             '<circle cx="122" cy="684" r="18" fill="#c8ced6" stroke="#6c7682" stroke-width="2"/>'
             '<path d="M114 592 L130 592 L122 608 Z" fill="#ff4b3e"/>')
    b.append(rect(0, 752, 600, 48, "#4a311c"))
    b.append(footer("TEAMS OR SOLO \u00b7 SHAPES \u00b7 AGAINST THE CLOCK", "Atkinson Hyperlegible", "#e9dcc2", 15, 3, 782))
    return svg(d, "".join(b))


def _shape(kind, cx, cy, r, fill, stroke):
    a = f'fill="{fill}" stroke="{stroke}" stroke-width="3"'
    if kind == "circle":
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" {a}/>'
    if kind == "square":
        return f'<rect x="{cx-r*.85}" y="{cy-r*.85}" width="{r*1.7}" height="{r*1.7}" rx="6" {a}/>'
    if kind == "tri":
        return f'<polygon points="{cx},{cy-r} {cx+r},{cy+r*.8} {cx-r},{cy+r*.8}" {a}/>'
    if kind == "hex":
        return f'<polygon points="{hexpts(cx, cy, r)}" {a}/>'
    if kind == "diamond":
        return f'<polygon points="{cx},{cy-r} {cx+r*.75},{cy} {cx},{cy+r} {cx-r*.75},{cy}" {a}/>'
    if kind == "star":
        p = " ".join(f"{cx + (r if i%2==0 else r*.45)*math.cos(math.radians(i*36-90)):.1f},{cy + (r if i%2==0 else r*.45)*math.sin(math.radians(i*36-90)):.1f}" for i in range(10))
        return f'<polygon points="{p}" {a}/>'
    if kind == "cross":
        w = r * .38
        return f'<path d="M{cx-w} {cy-r} h{2*w} v{r-w} h{r-w} v{2*w} h-{r-w} v{r-w} h-{2*w} v-{r-w} h-{r-w} v-{2*w} h{r-w} Z" {a}/>'
    if kind == "heart":
        return f'<path d="M{cx} {cy+r*.85} C {cx-r*1.4} {cy-r*.1} {cx-r*.6} {cy-r*1.1} {cx} {cy-r*.35} C {cx+r*.6} {cy-r*1.1} {cx+r*1.4} {cy-r*.1} {cx} {cy+r*.85} Z" {a}/>'
    if kind == "moon":
        return f'<path d="M{cx+r*.3} {cy-r} A {r} {r} 0 1 0 {cx+r*.3} {cy+r} A {r*.75} {r*.75} 0 1 1 {cx+r*.3} {cy-r} Z" {a}/>'


def problem_solvers():
    d = lin("yl", [(0, "#fde68a"), (1, "#f7c948")])
    b = [rect(0, 0, 600, 800, "#0f0e17"), '<circle cx="300" cy="300" r="240" fill="#f7c948" opacity=".1" filter="url(#k-glow)"/>']
    b.append(emoji(300, 118, "💡", 82))
    b.append(text(300, 210, "Problem", "Fredoka One", 86, "url(#yl)"))
    b.append(text(300, 296, "Solvers", "Fredoka One", 86, "url(#yl)"))
    b.append(text(300, 336, "Ridiculous problems. Ridiculous solutions.", "Nunito", 20, "#9b99b8", 700))
    b.append(f'<g transform="translate(300 420) rotate(-2)" filter="url(#k-drop)">{rect(-220, -44, 440, 88, "#ff6b6b", 16)}'
             + text(0, -8, "PROBLEM:", "Nunito", 16, "#2a0a0a", 900, ls=4) + text(0, 24, "Your cat is stuck on the Moon.", "Nunito", 24, "#fff", 900) + "</g>")
    # sketch paper with doodle solution
    b.append(f'<g transform="translate(300 600) rotate(2)" filter="url(#k-drop)">{rect(-200, -110, 400, 220, "#fdfcf6", 10)}'
             + "".join(f'<line x1="-190" y1="{-80+i*26}" x2="190" y2="{-80+i*26}" stroke="#bfe0f5" stroke-width="1.5"/>' for i in range(8))
             + '<path d="M-150 80 Q -120 -60 -60 -70" fill="none" stroke="#6bcbf7" stroke-width="5" stroke-linecap="round"/>'
             + '<path d="M-150 80 l 300 0" stroke="#7de8a0" stroke-width="5"/>'
             + '<path d="M-40 60 l 30 -120 l 30 120 Z" fill="none" stroke="#ff6b6b" stroke-width="5" stroke-linejoin="round"/>'
             + '<path d="M-24 64 q 14 30 28 0" fill="none" stroke="#f7c948" stroke-width="5"/>'
             + '<circle cx="120" cy="-62" r="32" fill="none" stroke="#9b99b8" stroke-width="4"/>'
             + text(80, 40, "giant", "Caveat", 30, "#333", 700) + text(84, 70, "trampoline!", "Caveat", 30, "#333", 700)
             + "</g>")
    b.append(footer("DRAW IT · PITCH IT · TEACHER PICKS", "Nunito", "#f7c948", 14, 3, 776, 900))
    return svg(d, "".join(b))


def question_mark():
    d = lin("bg", [(0, "#1a1342"), (1, "#3b1f8a")]) + lin("beam", [(0, "#ffffff"), (1, "#ffffff")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append('<polygon points="60,0 120,0 320,800 -60,800" fill="#fff" opacity=".06"/><polygon points="480,0 540,0 660,800 280,800" fill="#fff" opacity=".06"/>')
    for k in range(20):
        b.append(f'<circle cx="{15+k*30}" cy="14" r="5" fill="#ffcc33" opacity="{.9 if k%2 else .45}"/>')
    b.append(rect(70, 66, 100, 100, "#ffcc33", 18, 'stroke="#2a1d00" stroke-width="4"') + text(120, 146, "?", "Bungee", 84, "#1b1440"))
    b.append(text(196, 112, "QUESTION", "Bungee", 50, "#fbf8ff", anchor="start"))
    b.append(text(196, 166, "MARK", "Bungee", 50, "#ffcc33", anchor="start"))
    b.append(text(300, 214, "FLIP A WORD. GUESS THE QUESTION.", "Outfit", 18, "#d9d3f2", 700, ls=3))
    words = [("What", True), ("is", False), ("the", True), ("capital", False), ("of", True), ("Brazil", False), ("?", True)]
    y = 270
    x = 54
    layout = [(54, 270, 150), (216, 270, 100), (328, 270, 120), (54, 380, 220), (286, 380, 100), (398, 380, 150), (240, 490, 120)]
    for k, ((w, shown), (x, y, wd)) in enumerate(zip(words, layout)):
        if shown:
            b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, wd, 88, "#fbf8ff", 14, "stroke=\"#ffcc33\" stroke-width=\"4\"")}</g>'
                     + text(x + wd/2, y + 58, w, "Outfit", 38, "#1b1440", 800))
        else:
            b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, wd, 88, "#4a3bc4", 14, "stroke=\"#8a7cf0\" stroke-width=\"3\"")}</g>'
                     + text(x + wd/2, y + 60, k + 1, "Bungee", 42, "#fbf8ff"))
    b.append(text(300, 660, "“Brasília!”", "Outfit", 44, "#2fd27a", 800, italic=True))
    b.append(footer("TEAMS · CALL A NUMBER · ONE POINT", "Outfit", "#ffcc33", 14, 4, 770, 800))
    return svg(d, "".join(b))


def record_breaker():
    d = lin("gold", [(0, "#ffe680"), (1, "#f5c518")])
    b = [rect(0, 0, 600, 800, "#0a0a0f"), '<circle cx="300" cy="460" r="260" fill="#f5c518" opacity=".08" filter="url(#k-glow)"/>']
    b.append(text(300, 66, "WORLD RECORDS PARTY GAME", "Barlow", 15, "#6b6b88", 700, ls=6))
    b.append(text(300, 168, "RECORD", "Teko", 136, "url(#gold)", 600, ls=4))
    b.append(text(300, 270, "BREAKER", "Teko", 136, "#f0f0f8", 600, ls=4))
    b.append(text(300, 306, "HOW HIGH DARE YOU GO?", "Barlow", 17, "#a0a0c0", 700, ls=6))
    b.append(emoji(300, 450, "🏆", 120))
    # gauge
    b.append(f'<g filter="url(#k-drop)">{rect(60, 520, 480, 120, "#13131c", 16, "stroke=\"#1c1c2a\" stroke-width=\"2\"")}</g>')
    b.append(text(300, 566, "Longest fingernails (cm)?", "Barlow", 22, "#f0f0f8", 600))
    b.append(rect(90, 590, 420, 16, "#1c1c2a", 8) + rect(90, 590, 300, 16, "#30d158", 8) + rect(390, 590, 70, 16, "#ff2d55", 0, 'opacity=".75"'))
    b.append(f'<polygon points="380,580 400,580 390,596" fill="#f5c518"/>' + text(390, 634, "YOU: 870", "Teko", 22, "#f5c518", 600))
    b.append(text(300, 700, "909.6", "Teko", 64, "#f5c518", 600))
    b.append(text(300, 740, "ACTUAL RECORD · DON'T GO OVER!", "Barlow", 14, "#ff2d55", 800, ls=4))
    return svg(d, "".join(b))


def resistance():
    d = rad("bg", [(0, "#1a2130"), (1, "#0a0d13")], cy="30%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(60, 90, "OPERATION TRACKER · SOCIAL DEDUCTION", "IBM Plex Mono", 13, "#8a94ac", 500, "start", 3))
    b.append(text(60, 172, "The", "Playfair Display", 52, "#edf0f6", 700, "start", italic=True))
    b.append(text(60, 252, "Resistance", "Playfair Display", 92, "#f0b441", 900, "start"))
    b.append('<line x1="60" y1="276" x2="540" y2="276" stroke="#27314a" stroke-width="2"/>')
    # masks / agents
    for k in range(5):
        x = 92 + k * 104
        spy = k in (1, 3)
        b.append(f'<g transform="translate({x} 400)" filter="url(#k-drop-s)">'
                 f'<circle cx="0" cy="-34" r="30" fill="#1a2130" stroke="{"#e5484d" if spy else "#3ecf8e"}" stroke-width="3"/>'
                 f'<path d="M-44 54 Q -40 0 0 -2 Q 40 0 44 54 Z" fill="#1a2130" stroke="{"#e5484d" if spy else "#3ecf8e"}" stroke-width="3"/>'
                 + (f'<rect x="-22" y="-44" width="44" height="14" rx="7" fill="#e5484d"/>' if spy else '<circle cx="-10" cy="-36" r="4" fill="#edf0f6"/><circle cx="10" cy="-36" r="4" fill="#edf0f6"/>')
                 + "</g>")
    b.append(text(300, 520, "Who is the spy?", "Playfair Display", 34, "#edf0f6", 700, italic=True))
    # mission track
    res = ["ok", "fail", "ok", None, None]
    for k, rr in enumerate(res):
        x = 110 + k * 95
        col = {"ok": "#3ecf8e", "fail": "#e5484d"}.get(rr, "#27314a")
        b.append(f'<circle cx="{x}" cy="630" r="38" fill="{col if rr else "#121825"}" stroke="{col}" stroke-width="4"/>'
                 + text(x, 640, {"ok": "✓", "fail": "✕"}.get(rr, f"0{k+1}"), "IBM Plex Mono", 28 if rr else 20, "#0a0d13" if rr else "#5a6478", 700))
    b.append(text(300, 712, "OP-01 → OP-05", "IBM Plex Mono", 15, "#8a94ac", 500, ls=4))
    b.append(footer("5–10 PLAYERS · FIND THE LIARS", "IBM Plex Mono", "#f0b441", 14, 3, 770, 600))
    return svg(d, "".join(b))


def reveal_it():
    d = rad("bg", [(0, "#172033"), (1, "#0b1220")], cy="30%") + lin("tt", [(0, "#c7d2fe"), (1, "#818cf8")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 124, "Reveal It!", "Fredoka One", 96, "url(#tt)"))
    b.append(text(300, 170, "Fewer squares open, more points.", "Nunito", 21, "#94a3b8", 700))
    cs = 92
    x0, y0 = (600 - 5 * cs) / 2, 210
    b.append(f'<g filter="url(#k-drop)">{rect(x0 - 10, y0 - 10, 5 * cs + 20, 5 * cs + 20, "#1e293b", 18)}</g>')
    b.append(f'<clipPath id="cl"><rect x="{x0}" y="{y0}" width="{5*cs}" height="{5*cs}" rx="10"/></clipPath>')
    b.append(f'<g clip-path="url(#cl)">{rect(x0, y0, 5*cs, 5*cs, "#fef3c7")}{emoji(300, y0 + 5*cs/2 + 140, "🦒", 400)}</g>')
    openc = {6, 7, 12, 17, 13}
    for k in range(25):
        if k in openc:
            continue
        r, c = divmod(k, 5)
        x, y = x0 + c * cs, y0 + r * cs
        b.append(rect(x + 2, y + 2, cs - 4, cs - 4, "#4f46e5", 8, 'stroke="#a5b4fc" stroke-width="2"') + text(x + cs/2, y + cs/2 + 12, k + 1, "Fredoka One", 32, "#e0e7ff"))
    b.append(text(300, 736, "What is it?", "Fredoka One", 40, "#a5b4fc"))
    b.append(footer("16 CATEGORIES · TEAMS", "Nunito", "#64748b", 14, 4, 778, 900))
    return svg(d, "".join(b))


COVERS = {
    "letter-swap": letter_swap, "letter-battle": lexicon_duel, "linking-park": linking_park, "mastermind": mastermind,
    "maze-race": maze_race, "minefield": minefield, "mistake-hunters": mistake_hunters, "orbit": orbit, "order-up": order_up,
    "perfect-fit": perfect_fit, "problem-solvers": problem_solvers, "question-mark": question_mark,
    "record-breaker": record_breaker, "resistance": resistance, "reveal-it": reveal_it,
}
