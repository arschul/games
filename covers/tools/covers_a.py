"""Cover generators — batch A (pilot). Each function returns a 600x800 SVG string."""
import math

SVG_OPEN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="600" height="800">'


def wrap(defs, body):
    return f'{SVG_OPEN}<defs>{defs}</defs>{body}</svg>'


# ------------------------------------------------------------------ Beam of Ra
def beam_of_ra():
    defs = '''
    <radialGradient id="sky" cx="50%" cy="22%" r="80%">
      <stop offset="0" stop-color="#3a2a12"/><stop offset=".45" stop-color="#17130e"/><stop offset="1" stop-color="#0a0806"/>
    </radialGradient>
    <radialGradient id="sun" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#ffe9a8"/><stop offset=".55" stop-color="#e8b94e"/><stop offset="1" stop-color="#a67c22"/>
    </radialGradient>
    <linearGradient id="goldtxt" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff1c2"/><stop offset=".5" stop-color="#e8b94e"/><stop offset="1" stop-color="#a67c22"/>
    </linearGradient>
    <linearGradient id="silver" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f4f4f6"/><stop offset="1" stop-color="#8d929c"/>
    </linearGradient>
    <linearGradient id="red" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f06a55"/><stop offset="1" stop-color="#8e2316"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.5"/></filter>
    <filter id="drop"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000" flood-opacity=".6"/></filter>
    '''
    b = ['<rect width="600" height="800" fill="url(#sky)"/>']
    # sun disc + rays
    rays = []
    for k in range(24):
        a = k * math.pi / 12
        x1, y1 = 300 + 128 * math.cos(a), 170 + 128 * math.sin(a)
        x2, y2 = 300 + 300 * math.cos(a), 170 + 300 * math.sin(a)
        rays.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    b.append(f'<g stroke="#e8b94e" stroke-opacity=".13" stroke-width="10" stroke-linecap="round">{"".join(rays)}</g>')
    b.append('<circle cx="300" cy="170" r="118" fill="url(#sun)" opacity=".9"/>')
    b.append('<circle cx="300" cy="170" r="118" fill="none" stroke="#fff1c2" stroke-opacity=".35" stroke-width="2"/>')
    b.append('<circle cx="300" cy="170" r="98" fill="none" stroke="#5f3f04" stroke-opacity=".35" stroke-width="1.5" stroke-dasharray="3 6"/>')
    # title
    b.append('<g filter="url(#drop)">'
             '<text x="300" y="196" text-anchor="middle" font-family="Cinzel" font-weight="900" font-size="76" '
             'fill="url(#goldtxt)" stroke="#2b1d06" stroke-width="2.5" paint-order="stroke" letter-spacing="2">Beam of Ra</text></g>')
    b.append('<text x="300" y="320" text-anchor="middle" font-family="Inter" font-weight="700" font-size="15" '
             'letter-spacing="5" fill="#c2b393">LASER · MIRRORS · STRATEGY</text>')
    # board
    x0, y0, cs, cols, rows = 60, 350, 60, 8, 7
    b.append(f'<rect x="{x0-10}" y="{y0-10}" width="{cs*cols+20}" height="{cs*rows+20}" rx="10" fill="#1d1912" stroke="#4b3f2c" stroke-width="2"/>')
    for r in range(rows):
        for c in range(cols):
            fill = "#262017" if (r + c) % 2 == 0 else "#1f1a12"
            b.append(f'<rect x="{x0+c*cs}" y="{y0+r*cs}" width="{cs}" height="{cs}" fill="{fill}" stroke="#3a3122" stroke-width="1"/>')
    # tinted home columns
    b.append(f'<rect x="{x0}" y="{y0}" width="{cs}" height="{cs*rows}" fill="#c0392b" opacity=".08"/>')
    b.append(f'<rect x="{x0+cs*(cols-1)}" y="{y0}" width="{cs}" height="{cs*rows}" fill="#cfd4dc" opacity=".06"/>')
    cx = lambda c: x0 + cs * c + cs / 2
    cy = lambda r: y0 + cs * r + cs / 2
    h = 23

    def pyramid(c, r, corner, grad):
        X, Y = cx(c), cy(r)
        pts = {
            "tl": [(X-h, Y-h), (X+h, Y-h), (X-h, Y+h)],
            "tr": [(X-h, Y-h), (X+h, Y-h), (X+h, Y+h)],
            "bl": [(X-h, Y-h), (X-h, Y+h), (X+h, Y+h)],
            "br": [(X+h, Y-h), (X+h, Y+h), (X-h, Y+h)],
        }[corner]
        p = " ".join(f"{a:.1f},{b_:.1f}" for a, b_ in pts)
        # mirrored hypotenuse highlighted
        hyp = [q for q in pts if not (q[0] == (X-h if "l" in corner else X+h) and q[1] == (Y-h if "t" in corner else Y+h))]
        return (f'<polygon points="{p}" fill="url(#{grad})" stroke="#1a1208" stroke-width="2" filter="url(#drop)"/>'
                f'<line x1="{hyp[0][0]:.1f}" y1="{hyp[0][1]:.1f}" x2="{hyp[1][0]:.1f}" y2="{hyp[1][1]:.1f}" '
                f'stroke="#e9fff1" stroke-width="3.5" stroke-linecap="round"/>')

    # beam path: sphinx (1,6) up -> mirror (1,1) -> right -> (5,1) -> down -> (5,4) -> right -> pharaoh (7,4)
    path = [(cx(1), cy(6) - 18), (cx(1), cy(1)), (cx(5), cy(1)), (cx(5), cy(4)), (cx(7) - 16, cy(4))]
    pts = " ".join(f"{a:.1f},{c:.1f}" for a, c in path)
    b.append(f'<polyline points="{pts}" fill="none" stroke="#0aa543" stroke-width="16" stroke-linejoin="round" filter="url(#glow)" opacity=".9"/>')
    b.append(f'<polyline points="{pts}" fill="none" stroke="#5cff8f" stroke-width="5" stroke-linejoin="round"/>')
    b.append(f'<polyline points="{pts}" fill="none" stroke="#eafff0" stroke-width="1.6" stroke-linejoin="round"/>')
    # mirrors
    b.append(pyramid(1, 1, "tl", "silver"))
    b.append(pyramid(5, 1, "tr", "silver"))
    b.append(pyramid(5, 4, "bl", "silver"))
    # decoys
    b.append(pyramid(3, 3, "br", "red"))
    b.append(pyramid(6, 6, "tl", "red"))
    b.append(pyramid(2, 4, "tr", "silver"))
    b.append(pyramid(3, 0, "bl", "red"))
    # anubis-like blocks (rounded shields)
    for (c, r, g) in [(4, 5, "silver"), (6, 2, "red"), (0, 3, "red")]:
        b.append(f'<rect x="{cx(c)-20}" y="{cy(r)-22}" width="40" height="44" rx="12" fill="url(#{g})" stroke="#1a1208" stroke-width="2" filter="url(#drop)"/>'
                 f'<rect x="{cx(c)-12}" y="{cy(r)-22}" width="24" height="9" rx="3" fill="#1a1208" opacity=".35"/>')
    # sphinx (laser source)
    X, Y = cx(1), cy(6)
    b.append(f'<circle cx="{X}" cy="{Y}" r="22" fill="url(#silver)" stroke="#1a1208" stroke-width="2" filter="url(#drop)"/>'
             f'<rect x="{X-6}" y="{Y-30}" width="12" height="16" rx="3" fill="#2b241a"/>'
             f'<circle cx="{X}" cy="{Y}" r="7" fill="#5cff8f"/>')
    # pharaoh hit + burst
    X, Y = cx(7), cy(4)
    burst = []
    for k in range(12):
        a = k * math.pi / 6 + .2
        burst.append(f'<line x1="{X+26*math.cos(a):.1f}" y1="{Y+26*math.sin(a):.1f}" x2="{X+44*math.cos(a):.1f}" y2="{Y+44*math.sin(a):.1f}"/>')
    b.append(f'<g stroke="#ffe9a8" stroke-width="3" stroke-linecap="round" opacity=".9">{"".join(burst)}</g>')
    b.append(f'<circle cx="{X}" cy="{Y}" r="34" fill="#5cff8f" opacity=".35" filter="url(#glow)"/>')
    b.append(f'<circle cx="{X}" cy="{Y}" r="22" fill="url(#red)" stroke="#1a1208" stroke-width="2"/>'
             f'<path d="M{X-12} {Y-6} L{X-6} {Y-16} L{X} {Y-8} L{X+6} {Y-16} L{X+12} {Y-6} Z" fill="#e8b94e" stroke="#5f3f04" stroke-width="1.5"/>'
             f'<rect x="{X-10}" y="{Y-4}" width="20" height="14" rx="3" fill="#e8b94e" stroke="#5f3f04" stroke-width="1.5"/>')
    # footer
    b.append('<text x="300" y="784" text-anchor="middle" font-family="Inter" font-weight="600" font-size="13" letter-spacing="3" fill="#7a6a4c">2 PLAYERS OR TEAMS</text>')
    return wrap(defs, "".join(b))


# ------------------------------------------------------------------ Jeopardy
def jeopardy():
    defs = '''
    <radialGradient id="bg" cx="50%" cy="0%" r="110%">
      <stop offset="0" stop-color="#1a3fff"/><stop offset=".45" stop-color="#0a1fd4"/><stop offset="1" stop-color="#04083a"/>
    </radialGradient>
    <linearGradient id="tile" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0d1fb8"/><stop offset="1" stop-color="#060e8a"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff3a6"/><stop offset=".45" stop-color="#ffcc00"/><stop offset="1" stop-color="#c9a000"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity=".22"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <filter id="sh"><feDropShadow dx="0" dy="5" stdDeviation="0" flood-color="#020430" flood-opacity="1"/></filter>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="10"/></filter>
    '''
    b = ['<rect width="600" height="800" fill="url(#bg)"/>']
    # spotlights
    b.append('<polygon points="120,0 170,0 330,800 -40,800" fill="url(#beam)"/>')
    b.append('<polygon points="430,0 480,0 640,800 270,800" fill="url(#beam)"/>')
    # title
    b.append('<text x="300" y="138" text-anchor="middle" font-family="Anton" font-size="104" fill="#ffcc00" opacity=".55" filter="url(#glow)" letter-spacing="2">JEOPARDY!</text>')
    b.append('<text x="300" y="138" text-anchor="middle" font-family="Anton" font-size="104" fill="url(#gold)" '
             'stroke="#020430" stroke-width="5" paint-order="stroke" filter="url(#sh)" letter-spacing="2">JEOPARDY!</text>')
    b.append('<text x="300" y="182" text-anchor="middle" font-family="Oswald" font-weight="500" font-size="19" letter-spacing="7" fill="#aabfff">THE ULTIMATE CLASSROOM EDITION</text>')
    # board
    cats = ["ANIMALS", "FLAGS", "VERBS", "FOOD", "WORLD"]
    x0, y0, w, gap = 34, 222, 100, 6
    hh, rh = 64, 88
    b.append(f'<rect x="{x0-10}" y="{y0-10}" width="{5*w+4*gap+20}" height="{hh+5*rh+5*gap+20}" rx="8" fill="#020430"/>')
    taken = {(1, 0), (3, 2), (0, 3), (4, 1), (2, 4)}
    for c, name in enumerate(cats):
        x = x0 + c * (w + gap)
        b.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{hh}" fill="url(#tile)" stroke="#1a3fff" stroke-width="1.5"/>')
        b.append(f'<text x="{x+w/2}" y="{y0+hh/2+7}" text-anchor="middle" font-family="Oswald" font-weight="600" font-size="19" fill="#fff" letter-spacing="1">{name}</text>')
        for r in range(5):
            y = y0 + hh + gap + r * (rh + gap)
            b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{rh}" fill="url(#tile)" stroke="#1a3fff" stroke-width="1.5"/>')
            if (c, r) in taken:
                continue
            if (c, r) == (2, 2):
                b.append(f'<rect x="{x+3}" y="{y+3}" width="{w-6}" height="{rh-6}" fill="#ffcc00" opacity=".18"/>')
            b.append(f'<text x="{x+w/2}" y="{y+rh/2+16}" text-anchor="middle" font-family="Anton" font-size="44" '
                     f'fill="url(#gold)" stroke="#020430" stroke-width="3" paint-order="stroke">{(r+1)*100}</text>')
    b.append('<text x="300" y="784" text-anchor="middle" font-family="Oswald" font-weight="500" font-size="15" letter-spacing="5" fill="#aabfff">2–6 TEAMS · PICK A CATEGORY</text>')
    return wrap(defs, "".join(b))


# ------------------------------------------------------------------ Battle Pets
FIRE_PET = """
......b.....b...
.....bab...bab..
.....baab.baab..
....baaaabaaaab.
...baaaaaaaaaab.
...baawkaaawkab.
...baakkaaakkab.
..bccaaaaaaaaab.
..bcccaaabbaaab.
...bccaaaaaaab..
ff..baaaaaaaab..
fyf.baaaaaaaab..
.fyfbaa.bab.bab.
..ffbb..bb..bb..
"""


def pixel_sprite(art, x0, y0, px, pal, flip=False):
    rows = [r for r in art.strip("\n").split("\n")]
    width = max(len(r) for r in rows)
    out = []
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch == "." or ch not in pal:
                continue
            ii = (width - 1 - i) if flip else i
            out.append(f'<rect x="{x0+ii*px}" y="{y0+j*px}" width="{px}" height="{px}" fill="{pal[ch]}"/>')
    return "".join(out)


def battle_pets():
    defs = '''
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffe14a"/><stop offset=".55" stop-color="#9fe08a"/><stop offset="1" stop-color="#3fc7ff"/>
    </linearGradient>
    <radialGradient id="arena" cx="50%" cy="60%" r="60%">
      <stop offset="0" stop-color="#1f2640"/><stop offset="1" stop-color="#0b0e1a"/>
    </radialGradient>
    <pattern id="grid" width="16" height="16" patternUnits="userSpaceOnUse">
      <path d="M16 0H0V16" fill="none" stroke="#323a5c" stroke-width="1" opacity=".45"/>
    </pattern>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>
    '''
    b = ['<rect width="600" height="800" fill="url(#arena)"/>', '<rect width="600" height="800" fill="url(#grid)"/>']
    # pixel stars
    import random
    rnd = random.Random(7)
    for _ in range(40):
        x, y = rnd.randrange(0, 600, 4), rnd.randrange(0, 260, 4)
        b.append(f'<rect x="{x}" y="{y}" width="4" height="4" fill="#eef1fb" opacity="{rnd.choice([.25,.4,.7])}"/>')
    # title
    b.append('<text x="300" y="118" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="46" fill="#000" opacity=".6" transform="translate(5 5)">BATTLE</text>')
    b.append('<text x="300" y="118" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="46" fill="url(#title)">BATTLE</text>')
    b.append('<text x="300" y="186" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="46" fill="#000" opacity=".6" transform="translate(5 5)">PETS</text>')
    b.append('<text x="300" y="186" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="46" fill="url(#title)">PETS</text>')
    b.append('<text x="300" y="228" text-anchor="middle" font-family="\'DM Sans\'" font-weight="700" font-size="14" letter-spacing="5" fill="#8089b3">EFL ELEMENTAL SHOWDOWN</text>')
    # HP bars
    def hp(x, label, col, frac):
        return (f'<text x="{x}" y="300" font-family="\'Press Start 2P\'" font-size="12" fill="{col}">{label}</text>'
                f'<rect x="{x}" y="310" width="200" height="18" fill="#161b2e" stroke="{col}" stroke-width="3"/>'
                f'<rect x="{x+4}" y="314" width="{192*frac:.0f}" height="10" fill="#5fd97a"/>'
                f'<rect x="{x+4+192*frac:.0f}" y="314" width="{192*(1-frac):.0f}" height="10" fill="#ff5e6a" opacity=".5"/>')
    b.append(hp(40, "P1 EMBERFOX", "#f5c84a", .72))
    b.append(hp(360, "P2 TIDEPUP", "#8c6cff", .45))
    # ground shadows
    b.append('<ellipse cx="150" cy="590" rx="110" ry="16" fill="#000" opacity=".45"/>')
    b.append('<ellipse cx="450" cy="590" rx="110" ry="16" fill="#000" opacity=".45"/>')
    fire = {"a": "#ff5e3a", "b": "#5a1608", "c": "#ffb08a", "w": "#ffffff", "k": "#160606", "f": "#ffe14a", "y": "#ff9a2a"}
    water = {"a": "#3fc7ff", "b": "#0a3a5c", "c": "#bdeeff", "w": "#ffffff", "k": "#04121e", "f": "#8ce6ff", "y": "#ffffff"}
    b.append('<circle cx="150" cy="490" r="90" fill="#ff5e3a" opacity=".22" filter="url(#glow)"/>')
    b.append('<circle cx="450" cy="490" r="90" fill="#3fc7ff" opacity=".22" filter="url(#glow)"/>')
    b.append(pixel_sprite(FIRE_PET, 150 - 8 * 14, 590 - 14 * 14 - 2, 14, fire))
    b.append(pixel_sprite(FIRE_PET, 450 - 8 * 14, 590 - 14 * 14 - 2, 14, water, flip=True))
    # VS bolt
    b.append('<polygon points="312,388 268,470 298,470 280,540 336,448 304,448 324,388" fill="#ffe14a" stroke="#0b0e1a" stroke-width="4"/>')
    b.append('<text x="300" y="610" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="34" fill="#0b0e1a" transform="translate(4 4)">VS</text>')
    b.append('<text x="300" y="610" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="34" fill="#eef1fb">VS</text>')
    # type chips
    types = [("FIRE", "#ff5e3a"), ("WATER", "#3fc7ff"), ("NATURE", "#5fd97a"), ("ELECTRIC", "#ffe14a"), ("STONE", "#c9a36a")]
    x = 30
    for name, col in types:
        w = 24 + len(name) * 9.6
        b.append(f'<rect x="{x}" y="660" width="{w:.0f}" height="30" fill="{col}22" stroke="{col}" stroke-width="2.5"/>'
                 f'<text x="{x+w/2:.0f}" y="680" text-anchor="middle" font-family="\'Press Start 2P\'" font-size="9.5" fill="{col}">{name}</text>')
        x += w + 8
    # dialogue box
    b.append('<rect x="30" y="712" width="540" height="62" fill="#161b2e" stroke="#eef1fb" stroke-width="3"/>'
             '<text x="48" y="740" font-family="\'Press Start 2P\'" font-size="11" fill="#eef1fb">PAST SIMPLE: "She ___ home."</text>'
             '<text x="48" y="762" font-family="\'Press Start 2P\'" font-size="11" fill="#5fd97a">▶ went    ate    goed</text>')
    return wrap(defs, "".join(b))


# ------------------------------------------------------------------ Spelling Bee
def hexagon(cx, cy, r, attrs):
    pts = " ".join(f"{cx + r*math.cos(math.pi/180*(60*k)):.1f},{cy + r*math.sin(math.pi/180*(60*k)):.1f}" for k in range(6))
    return f'<polygon points="{pts}" {attrs}/>'


def bee():
    defs = '''
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0" stop-color="#fffdf5"/><stop offset="1" stop-color="#fdeec4"/>
    </radialGradient>
    <linearGradient id="honey" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFD24D"/><stop offset="1" stop-color="#E69F00"/>
    </linearGradient>
    <filter id="sh"><feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#b07800" flood-opacity=".28"/></filter>
    <filter id="tsh"><feDropShadow dx="0" dy="4" stdDeviation="0" flood-color="#b36b00" flood-opacity="1"/></filter>
    '''
    b = ['<rect width="600" height="800" fill="url(#bg)"/>']
    # faint honeycomb
    r = 34
    for row in range(-1, 15):
        for col in range(-1, 11):
            cx = col * r * 1.5
            cy = row * r * math.sqrt(3) + (r * math.sqrt(3) / 2 if col % 2 else 0)
            b.append(hexagon(cx, cy, r - 2, 'fill="none" stroke="#FFB800" stroke-opacity=".16" stroke-width="2"'))
    # title
    b.append('<text x="300" y="118" text-anchor="middle" font-family="\'Fredoka One\'" font-size="80" fill="url(#honey)" stroke="#fff" stroke-width="8" paint-order="stroke" filter="url(#tsh)">Spelling Bee</text>')
    b.append('<text x="300" y="202" text-anchor="middle" font-family="\'Fredoka One\'" font-size="70" fill="url(#honey)" stroke="#fff" stroke-width="8" paint-order="stroke" filter="url(#tsh)">Showdown</text>')
    b.append('<text x="300" y="246" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="16" letter-spacing="4" fill="#2D2D2D">THE ULTIMATE WORD TOURNAMENT</text>')
    # letter hive: S P E L L I N G (center E)
    R = 70
    cx0, cy0 = 300, 480
    ring = ["S", "P", "L", "I", "N", "G"]
    cols = ["#FF6B6B", "#38BDF8", "#84CC16", "#A855F7", "#4ECDC4", "#FF6B6B"]
    for k, ch in enumerate(ring):
        a = math.pi / 180 * (60 * k - 90)
        x, y = cx0 + R * math.sqrt(3) * math.cos(a), cy0 + R * math.sqrt(3) * math.sin(a)
        b.append('<g filter="url(#sh)">' + hexagon(x, y, R - 6, f'fill="#fff" stroke="{cols[k]}" stroke-width="6" stroke-linejoin="round"') + '</g>')
        b.append(f'<text x="{x:.1f}" y="{y+24:.1f}" text-anchor="middle" font-family="\'Fredoka One\'" font-size="66" fill="#2D2D2D">{ch}</text>')
    b.append('<g filter="url(#sh)">' + hexagon(cx0, cy0, R - 6, 'fill="url(#honey)" stroke="#E69F00" stroke-width="6" stroke-linejoin="round"') + '</g>')
    b.append(f'<text x="{cx0}" y="{cy0+24}" text-anchor="middle" font-family="\'Fredoka One\'" font-size="66" fill="#fff">E</text>')
    # flight path + bee
    b.append('<path d="M70 690 C 150 600, 60 560, 120 470 S 90 330, 170 300" fill="none" stroke="#2D2D2D" stroke-opacity=".35" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>')
    bx, by = 470, 680
    b.append(f'<g transform="translate({bx} {by}) rotate(-14)">'
             '<ellipse cx="-8" cy="-40" rx="30" ry="22" fill="#e9f7ff" stroke="#38BDF8" stroke-width="3" opacity=".9" transform="rotate(-25 -8 -40)"/>'
             '<ellipse cx="22" cy="-42" rx="26" ry="19" fill="#e9f7ff" stroke="#38BDF8" stroke-width="3" opacity=".9" transform="rotate(20 22 -42)"/>'
             '<ellipse cx="0" cy="0" rx="58" ry="40" fill="#FFB800" stroke="#2D2D2D" stroke-width="5"/>'
             '<path d="M-22 -37 Q -30 0 -22 37 L -8 39 Q -16 0 -8 -39 Z" fill="#2D2D2D"/>'
             '<path d="M8 -39 Q 0 0 8 39 L 22 37 Q 14 0 22 -37 Z" fill="#2D2D2D"/>'
             '<polygon points="-58,0 -76,-6 -76,6" fill="#2D2D2D"/>'
             '<circle cx="38" cy="-8" r="9" fill="#2D2D2D"/><circle cx="41" cy="-11" r="3" fill="#fff"/>'
             '<path d="M30 10 Q 40 18 50 8" fill="none" stroke="#2D2D2D" stroke-width="4" stroke-linecap="round"/>'
             '<path d="M40 -36 Q 46 -60 60 -62" fill="none" stroke="#2D2D2D" stroke-width="4" stroke-linecap="round"/><circle cx="62" cy="-62" r="5" fill="#2D2D2D"/>'
             '</g>')
    b.append('<text x="300" y="776" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="15" letter-spacing="3" fill="#8a6a1a">2–16 PLAYERS · A1 TO B2</text>')
    return wrap(defs, "".join(b))


# ------------------------------------------------------------------ Airtight
def airtight():
    defs = '''
    <linearGradient id="desk" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2a221a"/><stop offset="1" stop-color="#14100c"/>
    </linearGradient>
    <pattern id="grain" width="600" height="14" patternUnits="userSpaceOnUse">
      <path d="M0 7 Q 150 3 300 8 T 600 6" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="2"/>
    </pattern>
    <linearGradient id="folder" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e3d5ae"/><stop offset="1" stop-color="#cdbb8c"/>
    </linearGradient>
    <filter id="drop"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#000" flood-opacity=".55"/></filter>
    <filter id="small"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000" flood-opacity=".35"/></filter>
    <filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="3"/></filter>
    '''
    b = ['<rect width="600" height="800" fill="url(#desk)"/>', '<rect width="600" height="800" fill="url(#grain)"/>']
    # lamp light
    b.append('<radialGradient id="lamp" cx="40%" cy="35%" r="60%"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".22"/><stop offset="1" stop-color="#ffe2a0" stop-opacity="0"/></radialGradient>')
    b.append('<rect width="600" height="800" fill="url(#lamp)"/>')
    # folder
    b.append('<g transform="rotate(-2 300 430)" filter="url(#drop)">'
             '<path d="M50 140 h150 l20 -26 h110 l20 26 h200 v610 h-500 z" fill="#c2b494"/>'
             '<rect x="44" y="150" width="512" height="610" rx="6" fill="url(#folder)"/>'
             '<rect x="60" y="166" width="480" height="578" fill="none" stroke="#a8946655" stroke-width="2"/>'
             '</g>')
    # case-file tab label
    b.append('<g transform="rotate(-2 300 430)">'
             '<text x="275" y="133" text-anchor="middle" font-family="\'Special Elite\'" font-size="15" fill="#5a5142" letter-spacing="3">CASE FILE</text>'
             '</g>')
    # title
    b.append('<text x="84" y="250" font-family="\'Special Elite\'" font-size="84" fill="#241f18" transform="rotate(-2 300 430)">AIRTIGHT<tspan fill="#b3261e">.</tspan></text>')
    b.append('<text x="88" y="286" font-family="\'DM Mono\'" font-size="15" fill="#5a5142" transform="rotate(-2 300 430)">the alibi game — precinct nº 7</text>')
    # polaroids
    def polaroid(x, y, rot, label, shirt):
        return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#small)">'
                '<rect x="-80" y="-96" width="160" height="192" fill="#f6efdc"/>'
                '<rect x="-68" y="-84" width="136" height="136" fill="#3b3f4a"/>'
                '<circle cx="0" cy="-30" r="30" fill="#16181f"/>'
                f'<path d="M-52 52 Q -50 4 0 2 Q 50 4 52 52 Z" fill="{shirt}"/>'
                '<text x="0" y="-22" text-anchor="middle" font-family="\'Special Elite\'" font-size="36" fill="#cfc4a8">?</text>'
                f'<text x="0" y="80" text-anchor="middle" font-family="\'Special Elite\'" font-size="17" fill="#241f18">{label}</text>'
                '</g>')
    b.append(polaroid(170, 440, -6, "SUSPECT A", "#16181f"))
    b.append(polaroid(430, 450, 5, "SUSPECT B", "#16181f"))
    # pins + red string with a broken clue between
    b.append('<path d="M172 350 C 240 420, 330 330, 428 362" fill="none" stroke="#b3261e" stroke-width="3"/>')
    b.append('<path d="M172 350 C 220 520, 300 560, 300 600" fill="none" stroke="#b3261e" stroke-width="3"/>')
    b.append('<path d="M428 362 C 400 520, 320 560, 300 600" fill="none" stroke="#b3261e" stroke-width="3"/>')
    for (x, y) in [(172, 350), (428, 362), (300, 600)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#b3261e" stroke="#5a0f0a" stroke-width="2"/><circle cx="{x-2}" cy="{y-2}" r="2.5" fill="#ffb3a8"/>')
    # note card with contradictory times
    b.append('<g transform="translate(300 652) rotate(-3)" filter="url(#small)">'
             '<rect x="-128" y="-38" width="256" height="76" fill="#f6efdc"/>'
             '<line x1="-118" y1="-6" x2="118" y2="-6" stroke="#a8c0d8" stroke-width="1"/>'
             '<line x1="-118" y1="18" x2="118" y2="18" stroke="#a8c0d8" stroke-width="1"/>'
             '<text x="-112" y="-12" font-family="\'Special Elite\'" font-size="17" fill="#241f18">A: "We left at 8:15"</text>'
             '<text x="-112" y="12" font-family="\'Special Elite\'" font-size="17" fill="#241f18">B: "We left at 9:30"</text>'
             '<path d="M-118 26 q 120 -8 236 0" fill="none" stroke="#b3261e" stroke-width="3"/>'
             '</g>')
    # stamp
    b.append('<g transform="translate(420 724) rotate(-8)" filter="url(#rough)" opacity=".85">'
             '<rect x="-108" y="-26" width="216" height="52" rx="6" fill="none" stroke="#b3261e" stroke-width="5"/>'
             '<text x="0" y="10" text-anchor="middle" font-family="\'Special Elite\'" font-size="27" fill="#b3261e" letter-spacing="4">CONFIDENTIAL</text>'
             '</g>')
    # paper clip
    b.append('<path d="M478 118 v-40 a14 14 0 0 1 28 0 v86 a20 20 0 0 1 -40 0 v-70" fill="none" stroke="#9aa0a8" stroke-width="5" stroke-linecap="round"/>')
    b.append('<text x="300" y="788" text-anchor="middle" font-family="\'DM Mono\'" font-size="13" letter-spacing="3" fill="#c9963f">TWO SUSPECTS · ONE ALIBI</text>')
    return wrap(defs, "".join(b))


# ------------------------------------------------------------------ Castle Roads
def castle_roads():
    T = 150
    defs = '''
    <pattern id="grass" width="12" height="12" patternUnits="userSpaceOnUse">
      <rect width="12" height="12" fill="#5d8a3c"/>
      <path d="M2 10 l2 -5 M8 11 l1 -4 M6 4 l1 -3" stroke="#4b7430" stroke-width="1.4" stroke-linecap="round"/>
    </pattern>
    <pattern id="brick" width="16" height="10" patternUnits="userSpaceOnUse">
      <rect width="16" height="10" fill="#a4543a"/>
      <path d="M0 5 H16 M8 0 V5 M0 5 V10 M16 5 V10" stroke="#7a3624" stroke-width="1.2"/>
    </pattern>
    <filter id="tile"><feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity=".45"/></filter>
    <filter id="drop"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".6"/></filter>
    <linearGradient id="bevel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".3"/>
    </linearGradient>
    '''
    # tiles: (row, col): dict(roads=set, city=set, mon=bool, meeple=color)
    M = {
        (0, 0): dict(mon=True),
        (0, 1): dict(city="SE"), (0, 2): dict(city="SW"), (0, 3): dict(roads="S"),
        (1, 0): dict(roads="S"), (1, 1): dict(city="NE"), (1, 2): dict(city="NW"), (1, 3): dict(roads="NS"),
        (2, 0): dict(roads="NS"), (2, 1): dict(roads="ES"), (2, 2): dict(roads="EW"), (2, 3): dict(roads="NW"),
        (3, 0): dict(roads="NE"), (3, 1): dict(roads="NEW"), (3, 2): dict(roads="EW"), (3, 3): dict(roads="WS"),
        (4, 0): dict(), (4, 1): dict(mon=True), (4, 2): dict(city="S"), (4, 3): dict(roads="NS"),
        (5, 0): dict(city="E"), (5, 1): dict(city="WN"), (5, 2): dict(city="N"), (5, 3): dict(roads="N"),
    }
    meeples = {(1, 1): "#e2552f", (2, 2): "#2f6fd6", (4, 1): "#e2552f", (5, 1): "#f0bf55", (1, 3): "#2f6fd6"}
    edge_mid = {"N": (T/2, 0), "S": (T/2, T), "E": (T, T/2), "W": (0, T/2)}
    city_shape = {
        "N": f"M0 0 H{T} Q {T/2} {T*0.55} 0 0 Z",
        "S": f"M0 {T} H{T} Q {T/2} {T*0.45} 0 {T} Z",
        "E": f"M{T} 0 V{T} Q {T*0.45} {T/2} {T} 0 Z",
        "W": f"M0 0 V{T} Q {T*0.55} {T/2} 0 0 Z",
    }
    corner = {
        frozenset("SE"): f"M{T} 0 V{T} H0 Q {T*0.2} {T*0.2} {T} 0 Z",
        frozenset("SW"): f"M0 0 V{T} H{T} Q {T*0.8} {T*0.2} 0 0 Z",
        frozenset("NE"): f"M0 0 H{T} V{T} Q {T*0.2} {T*0.8} 0 0 Z",
        frozenset("NW"): f"M0 {T} V0 H{T} Q {T*0.8} {T*0.8} 0 {T} Z",
    }
    b = ['<rect width="600" height="800" fill="#10161e"/>']
    ox, oy = 0, -50
    for (r, c), t in M.items():
        x, y = ox + c * T, oy + r * T
        g = [f'<g transform="translate({x} {y})">', f'<rect x="1.5" y="1.5" width="{T-3}" height="{T-3}" rx="5" fill="url(#grass)"/>']
        city = t.get("city", "")
        wall = {
            "N": f"M{T} 0 Q {T/2} {T*0.55} 0 0", "S": f"M{T} {T} Q {T/2} {T*0.45} 0 {T}",
            "E": f"M{T} {T} Q {T*0.45} {T/2} {T} 0", "W": f"M0 {T} Q {T*0.55} {T/2} 0 0",
            frozenset("SE"): f"M0 {T} Q {T*0.2} {T*0.2} {T} 0", frozenset("SW"): f"M{T} {T} Q {T*0.8} {T*0.2} 0 0",
            frozenset("NE"): f"M{T} {T} Q {T*0.2} {T*0.8} 0 0", frozenset("NW"): f"M{T} 0 Q {T*0.8} {T*0.8} 0 {T}",
        }
        keys = [frozenset(city)] if (len(city) == 2 and frozenset(city) in corner) else list(city)
        for k in keys:
            d = corner[k] if isinstance(k, frozenset) else city_shape[k]
            g.append(f'<path d="{d}" fill="url(#brick)"/>')
            g.append(f'<path d="{wall[k]}" fill="none" stroke="#e8dcc0" stroke-width="7" stroke-linecap="round"/>')
            g.append(f'<path d="{wall[k]}" fill="none" stroke="#5b4a32" stroke-width="2.5" stroke-dasharray="7 6"/>')
        roads = t.get("roads", "")
        segs = []
        if len(roads) == 2 and roads[0] + roads[1] not in ("NS", "SN", "EW", "WE"):
            (x1, y1), (x2, y2) = edge_mid[roads[0]], edge_mid[roads[1]]
            segs.append(f"M{x1} {y1} Q {T/2} {T/2} {x2} {y2}")
        else:
            for e in roads:
                ex, ey = edge_mid[e]
                end = (T/2, T/2) if len(roads) != 2 else None
                if len(roads) == 2:
                    segs = [f"M{edge_mid[roads[0]][0]} {edge_mid[roads[0]][1]} L{edge_mid[roads[1]][0]} {edge_mid[roads[1]][1]}"]
                    break
                segs.append(f"M{ex} {ey} L{T/2} {T/2}")
        for d in segs:
            g.append(f'<path d="{d}" fill="none" stroke="#5b4a32" stroke-width="22" stroke-linecap="round"/>')
            g.append(f'<path d="{d}" fill="none" stroke="#e6dcc4" stroke-width="15" stroke-linecap="round"/>')
        if len(roads) in (1, 3):
            g.append(f'<rect x="{T/2-15}" y="{T/2-15}" width="30" height="26" rx="3" fill="#c9b48a" stroke="#5b4a32" stroke-width="3"/>'
                     f'<path d="M{T/2-19} {T/2-13} L{T/2} {T/2-30} L{T/2+19} {T/2-13} Z" fill="#a4543a" stroke="#5b4a32" stroke-width="3"/>')
        if t.get("mon"):
            g.append(f'<rect x="{T/2-26}" y="{T/2-14}" width="52" height="40" rx="3" fill="#e6dcc4" stroke="#5b4a32" stroke-width="3"/>'
                     f'<path d="M{T/2-32} {T/2-12} L{T/2} {T/2-40} L{T/2+32} {T/2-12} Z" fill="#a4543a" stroke="#5b4a32" stroke-width="3"/>'
                     f'<rect x="{T/2-7}" y="{T/2+6}" width="14" height="20" rx="7" fill="#5b4a32"/>'
                     f'<path d="M{T/2} {T/2-58} v18 M{T/2-7} {T/2-50} h14" stroke="#5b4a32" stroke-width="3"/>')
        g.append(f'<rect x="1.5" y="1.5" width="{T-3}" height="{T-3}" rx="5" fill="url(#bevel)"/>')
        g.append(f'<rect x="1.5" y="1.5" width="{T-3}" height="{T-3}" rx="5" fill="none" stroke="#1d232b" stroke-opacity=".55" stroke-width="2"/>')
        if (r, c) in meeples:
            col = meeples[(r, c)]
            mx, my = (T*0.7, T*0.62) if t.get("roads") else (T*0.5, T*0.45)
            g.append(f'<g transform="translate({mx} {my})" filter="url(#tile)">'
                     f'<path d="M0 -24 a9 9 0 1 1 0.1 0 Z M-6 -14 h12 l12 8 l-3 6 l-8 -3 l7 26 h-11 l-3 -12 l-3 12 h-11 l7 -26 l-8 3 l-3 -6 Z" '
                     f'fill="{col}" stroke="#1d232b" stroke-width="2.5" stroke-linejoin="round"/></g>')
        g.append("</g>")
        b.append(f'<g filter="url(#tile)">{"".join(g)}</g>')
    # title panel
    b.append('<g filter="url(#drop)"><rect x="50" y="300" width="500" height="186" rx="16" fill="#1d2530" fill-opacity=".94" stroke="#f0bf55" stroke-width="3"/></g>')
    b.append('<rect x="62" y="312" width="476" height="162" rx="10" fill="none" stroke="#f0bf55" stroke-opacity=".35" stroke-width="1.5"/>')
    b.append('<text x="300" y="400" text-anchor="middle" font-family="Cinzel" font-weight="700" font-size="66" fill="#f0bf55">Castle Roads</text>')
    b.append('<text x="300" y="442" text-anchor="middle" font-family="Inter" font-weight="500" font-size="17" fill="#aab5c3">Build the map one tile at a time</text>')
    b.append('<rect x="0" y="752" width="600" height="48" fill="#10161e" opacity=".82"/>'
             '<text x="300" y="783" text-anchor="middle" font-family="Inter" font-weight="700" font-size="14" letter-spacing="4" fill="#f0bf55">TILE LAYING · 2–5 PLAYERS</text>')
    return wrap(defs, "".join(b))


COVERS = {
    "beam-of-ra": beam_of_ra,
    "jeopardy": jeopardy,
    "battle-pets": battle_pets,
    "bee": bee,
    "airtight": airtight,
    "castle-roads": castle_roads,
}
