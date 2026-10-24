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
    d = lin("bg", [(0, "#f2fbff"), (1, "#d6ecf5")])
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 104, '<tspan fill="#f88c30">Save</tspan> the <tspan fill="#f5c842">Cheese!</tspan>', "Fredoka One", 54, "#2a3f5f",
                  extra='stroke="#fff" stroke-width="6" paint-order="stroke"'))
    b.append(text(300, 146, "GUESS THE WORD BEFORE THE MOUSE ARRIVES", "Nunito", 14, "#6a88aa", 900, ls=3))
    b.append(f'<g filter="url(#k-drop-s)">{rect(40, 180, 520, 170, "#fff8e1", 22, "stroke=\"#f5c842\" stroke-width=\"4\"")}</g>')
    b.append('<path d="M110 300 H470" stroke="#6a88aa" stroke-width="4" stroke-dasharray="4 12" stroke-linecap="round"/>')
    b.append(emoji(200, 300, "🐭", 70) + emoji(500, 300, "🧀", 80))
    b.append('<path d="M150 296 q -24 -10 -40 6" fill="none" stroke="#9b6cd8" stroke-width="3"/>')
    # blanks
    word = "B_N_N_"
    real = "BANANA"
    for k, ch in enumerate(word):
        x = 90 + k * 72
        b.append(rect(x, 400, 60, 74, "#fff", 12, 'stroke="#d0e8f0" stroke-width="3"') + f'<line x1="{x+12}" y1="460" x2="{x+48}" y2="460" stroke="#2a3f5f" stroke-width="4"/>')
        if ch != "_":
            b.append(text(x + 30, 452, ch, "Fredoka One", 44, "#2a3f5f"))
    # keyboard
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    used_ok = set("BN")
    used_bad = set("TSO")
    for r, row in enumerate(rows):
        w = 46
        x0 = (600 - len(row) * (w + 6)) / 2
        for c, ch in enumerate(row):
            x, y = x0 + c * (w + 6), 520 + r * 62
            fill = "#4ccc6a" if ch in used_ok else ("#c8d6e2" if ch in used_bad else "#fff")
            ink = "#fff" if ch in used_ok else ("#8aa0b8" if ch in used_bad else "#2a3f5f")
            b.append(f'<g filter="url(#k-drop-s)">{rect(x, y, w, 54, fill, 10, "stroke=\"#d0e8f0\" stroke-width=\"2\"")}</g>' + text(x + w/2, y + 37, ch, "Fredoka One", 26, ink))
    b.append(text(300, 760, "CHANCES  ● ● ● ● ● ● ○ ○ ○", "Nunito", 18, "#38a854", 900, ls=2))
    return svg(d, "".join(b))


def scattergories():
    d = rad("bg", [(0, "#1e1e38"), (1, "#0d0d1a")], cy="35%")
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(f'<circle cx="84" cy="104" r="30" fill="#7c3aed"/>' + text(126, 124, "Scattergories", "Inter", 62, "#f1f5f9", 900, "start", -1))
    b.append(text(300, 170, "SPIN THE LETTER · RACE THE CLOCK", "Inter", 15, "#94a3b8", 800, ls=4))
    cx, cy = 190, 330
    for k in range(26):
        a = math.radians(k * 360 / 26 - 90)
        b.append(text(f"{cx+112*math.cos(a):.1f}", f"{cy+112*math.sin(a)+6:.1f}", chr(65 + k), "Inter", 17, "#a855f7" if chr(65+k) != "B" else "#f59e0b", 800))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="92" fill="#16162a" stroke="#7c3aed" stroke-width="6"/>'
             f'<circle cx="{cx}" cy="{cy}" r="92" fill="none" stroke="#a855f7" stroke-width="6" filter="url(#k-glow-s)"/>')
    b.append(text(cx, cy + 34, "B", "Inter", 100, "#f59e0b", 900))
    b.append('<circle cx="450" cy="330" r="80" fill="none" stroke="#1e1e38" stroke-width="12"/>'
             '<circle cx="450" cy="330" r="80" fill="none" stroke="#06b6d4" stroke-width="12" stroke-dasharray="380 503" transform="rotate(-90 450 330)" stroke-linecap="round"/>'
             + text(450, 344, "2:00", "Inter", 40, "#f1f5f9", 900))
    cats = [("Things in a bathroom", "bathtub"), ("Ice cream flavors", "banana"), ("Animals", "bear"), ("Jobs", "baker"), ("Countries", "")]
    for k, (c, a) in enumerate(cats):
        y = 480 + k * 60
        b.append(rect(50, y, 500, 48, "#16162a", 12, 'stroke="#1e1e38" stroke-width="2"')
                 + f'<circle cx="80" cy="{y+24}" r="15" fill="#7c3aed"/>' + text(80, y + 30, k + 1, "Inter", 16, "#fff", 800)
                 + text(108, y + 31, c, "Inter", 19, "#cbd5e1", 600, "start") + text(530, y + 31, a, "Caveat", 28, "#10b981", 700, "end"))
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
    b = [rect(0, 0, 600, 800, "#0d0d0d")]
    b.append(text(50, 140, "STOP", "Black Han Sans", 120, "#f0ede6", anchor="start"))
    b.append(text(50, 270, "TWIST", "Black Han Sans", 120, "#f0e040", anchor="start"))
    b.append(rect(54, 286, 330, 10, "#ff5c3a", 3))
    b.append(text(52, 330, "SCATTERGORIES WITH A TWIST", "DM Sans", 15, "#888", 700, "start", 5))
    # stop sign
    b.append(f'<g transform="translate(500 110) rotate(12) scale(.78)" filter="url(#k-drop)"><polygon points="{_oct(0,0,92)}" fill="#ff5c3a" stroke="#fff" stroke-width="7"/>'
             + text(0, 16, "STOP!", "Black Han Sans", 42, "#fff") + "</g>")
    b.append(rect(52, 368, 120, 120, "#f0e040", 18) + text(112, 462, "M", "Black Han Sans", 92, "#0d0d0d"))
    b.append(rect(190, 384, 360, 88, "#161616", 14, 'stroke="#ff5c3a" stroke-width="3"') + text(210, 418, "TWIST:", "DM Sans", 15, "#ff5c3a", 800, "start", 3)
             + text(210, 452, "two words, double points", "DM Sans", 22, "#f0ede6", 600, "start"))
    cats = [("👤 Name", "Maria"), ("🐾 Animal", "monkey"), ("🍔 Food", "mango"), ("🌍 Place", "Madrid"), ("🎬 Movie", ""), ("✨ Adjective", "messy")]
    for k, (c, a) in enumerate(cats):
        r, col = divmod(k, 2)
        x, y = 52 + col * 254, 512 + r * 82
        b.append(rect(x, y, 240, 70, "#161616", 12, 'stroke="#2a2a2a" stroke-width="2"') + text(x + 16, y + 28, c, "DM Sans", 16, "#888", 700, "start")
                 + text(x + 16, y + 58, a or "…", "Caveat", 30, "#f0e040" if a else "#444", 700, "start"))
    return svg("", "".join(b))


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
    d = rad("bg", [(0, "#1a1e28"), (1, "#0d0f14")], cy="30%") + lin("gold", [(0, "#f6d77a"), (1, "#e07040")], x2=1, y2=0)
    b = [rect(0, 0, 600, 800, "url(#bg)")]
    b.append(text(300, 112, "Think on", "Syne", 62, "#f4f5f8", 800))
    b.append(text(300, 190, "your Feet", "Syne", 62, "url(#gold)", 800))
    b.append(text(300, 236, "NAME ONE FOR EVERY CATEGORY", "DM Sans", 15, "#6b7180", 800, ls=4))
    cats = ["Fruit", "Sport", "Job", "Color", "Country", "Animal", "Clothes", "Verb", "Drink"]
    done = {0: "#3ecf8e", 2: "#5090f0", 4: "#3ecf8e", 6: "#5090f0", 7: "#3ecf8e"}
    for k, c in enumerate(cats):
        r, col = divmod(k, 3)
        x, y = 50 + col * 172, 280 + r * 104
        dc = done.get(k)
        b.append(rect(x, y, 156, 88, dc + "22" if dc else "#161a23", 14, f'stroke="{dc or "#2a3045"}" stroke-width="{3 if dc else 2}"')
                 + text(x + 78, y + 54, c, "DM Sans", 24, "#f4f5f8" if dc else "#9aa3b6", 700))
        if dc:
            b.append(f'<circle cx="{x+138}" cy="{y+16}" r="11" fill="{dc}"/>' + text(x + 138, y + 21, "✓", "DM Sans", 13, "#0d0f14", 900))
    for k, (team, col, frac) in enumerate([("TEAM 1", "#3ecf8e", .62), ("TEAM 2", "#5090f0", .3)]):
        y = 620 + k * 60
        b.append(text(50, y + 20, team, "DM Sans", 16, col, 800, "start", 2) + rect(150, y + 4, 330, 20, "#161a23", 10) + rect(150, y + 4, 330 * frac, 20, col, 10)
                 + text(550, y + 21, "✕" * (k + 1), "DM Sans", 20, "#e07040", 900, "end"))
    b.append(footer("2–6 TEAMS · CEFR FILTER", "DM Sans", "#f0c040", 14, 4, 780, 800))
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
