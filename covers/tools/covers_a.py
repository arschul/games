"""Cover generators — batch A (pilot). Each function returns a 600x800 SVG string."""
import math

SVG_OPEN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 800" width="600" height="800">'


def wrap(defs, body):
    return f'{SVG_OPEN}<defs>{defs}</defs>{body}</svg>'


# ------------------------------------------------------------------ Beam of Ra
def beam_of_ra():
    """Scorching desert noon; a green laser bounces off a stepped pyramid and a scarab into a pharaoh mask."""
    defs = (
        '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3c675"/><stop offset=".55" stop-color="#fbe3ad"/><stop offset="1" stop-color="#fff3d6"/></linearGradient>'
        '<radialGradient id="sun" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fffef5"/><stop offset=".25" stop-color="#fff6d0"/><stop offset=".6" stop-color="#ffd27a" stop-opacity=".55"/><stop offset="1" stop-color="#ffc86a" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="d1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#efc488"/><stop offset="1" stop-color="#e2ad6b"/></linearGradient>'
        '<linearGradient id="d2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e6aa62"/><stop offset="1" stop-color="#cf914b"/></linearGradient>'
        '<linearGradient id="d3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d48f45"/><stop offset="1" stop-color="#a86a2c"/></linearGradient>'
        '<linearGradient id="lime" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#dfe5ee"/><stop offset="1" stop-color="#8c97a8"/></linearGradient>'
        '<linearGradient id="limeD" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c9d1dd"/><stop offset="1" stop-color="#6c7789"/></linearGradient>'
        '<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff3c4"/><stop offset=".45" stop-color="#e8bb4f"/><stop offset="1" stop-color="#8a5f12"/></linearGradient>'
        '<linearGradient id="mirror" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a6f1ff"/><stop offset=".4" stop-color="#ffffff"/><stop offset="1" stop-color="#7fd0ee"/></linearGradient>'
        '<radialGradient id="shell" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#ffb39f"/><stop offset=".45" stop-color="#d9472f"/><stop offset="1" stop-color="#5e1208"/></radialGradient>'
        '<radialGradient id="plinth" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#ff9e86"/><stop offset=".5" stop-color="#c2412d"/><stop offset="1" stop-color="#5e1208"/></radialGradient>'
        '<linearGradient id="skin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9b07a"/><stop offset="1" stop-color="#a8673a"/></linearGradient>'
        '<clipPath id="nemes"><path d="M450 336 C 520 336 536 392 534 430 L 560 520 L 506 520 L 498 456 L 402 456 L 394 520 L 340 520 L 366 430 C 364 392 380 336 450 336 Z"/></clipPath>'
        '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>'
        '<filter id="drop" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="4" dy="9" stdDeviation="6" flood-color="#3a1d05" flood-opacity=".45"/></filter>'
    )
    b = ['<rect width="600" height="800" fill="url(#sky)"/>']
    rays = []
    for k in range(20):
        a = k * math.pi / 10
        rays.append(f'<line x1="{300+120*math.cos(a):.1f}" y1="{150+120*math.sin(a):.1f}" x2="{300+520*math.cos(a):.1f}" y2="{150+520*math.sin(a):.1f}"/>')
    b.append(f'<g stroke="#fff1c4" stroke-opacity=".5" stroke-width="22" stroke-linecap="round">{"".join(rays)}</g>')
    b.append('<circle cx="300" cy="150" r="230" fill="url(#sun)"/>')

    def dune(base, amp, k, ph, fill, crest=None):
        pts = [(x, base + amp * math.sin(x * k + ph) + amp * .4 * math.sin(x * k * 2.7 + ph * 2)) for x in range(-10, 611, 10)]
        out = '<path d="M-10 800 ' + " ".join(f"L{x} {y:.1f}" for x, y in pts) + f' L610 800 Z" fill="{fill}"/>'
        if crest:
            out += '<path d="M' + " L".join(f"{x} {y:.1f}" for x, y in pts) + f'" fill="none" stroke="{crest}" stroke-width="3"/>'
        return out
    b.append(dune(372, 10, .012, 1.1, "url(#d1)"))
    for (x, base, s) in [(92, 382, 74), (176, 386, 44), (514, 378, 60)]:
        b.append(f'<path d="M{x-s} {base} L{x} {base-s*.9} L{x+s} {base} Z" fill="#e3ad6b"/><path d="M{x} {base-s*.9} L{x+s} {base} L{x+s*.25} {base} Z" fill="#c98e4c"/>')
    b.append(dune(470, 16, .009, 2.3, "url(#d2)", "#fff0c8"))
    b.append(dune(640, 20, .007, .4, "url(#d3)", "#ffe0a8"))
    b.append('<text x="300" y="214" text-anchor="middle" font-family="Rakkas" font-size="104" fill="#8f2412" '
             'stroke="#fff3d0" stroke-width="7" paint-order="stroke" filter="url(#drop)">Beam of Ra</text>')
    path = [(-10, 620), (150, 620), (150, 430), (392, 430)]
    pts = " ".join(f"{x},{y}" for x, y in path)
    b.append(f'<polyline points="{pts}" fill="none" stroke="#0aa543" stroke-width="22" stroke-linejoin="round" filter="url(#glow)"/>')
    b.append(f'<polyline points="{pts}" fill="none" stroke="#5cff8f" stroke-width="8" stroke-linejoin="round"/>')
    b.append(f'<polyline points="{pts}" fill="none" stroke="#f0fff4" stroke-width="2.5" stroke-linejoin="round"/>')
    # stepped pyramid, mirror on the long face (faces up-left)
    X, Y, h = 150, 620, 62
    g = ['<g filter="url(#drop)">',
         f'<path d="M{X+h} {Y-h} L{X+h} {Y+h} L{X-h} {Y+h} Z" fill="#3d4757"/>',
         f'<path d="M{X+h} {Y-h} L{X} {Y} L{X+h} {Y+h} Z" fill="url(#limeD)"/>',
         f'<path d="M{X+h} {Y+h} L{X} {Y} L{X-h} {Y+h} Z" fill="url(#lime)"/>']
    for f in (.28, .5, .72, .9):
        s = h * f
        g.append(f'<path d="M{X+s} {Y-s} L{X+s} {Y+s} L{X-s} {Y+s}" fill="none" stroke="#000" stroke-opacity=".3" stroke-width="2"/>')
    c = h * .27
    g.append(f'<path d="M{X+c} {Y-c} L{X} {Y} L{X+c} {Y+c} Z" fill="#a8761c"/><path d="M{X+c} {Y+c} L{X} {Y} L{X-c} {Y+c} Z" fill="url(#gold)"/>')
    g.append(f'<line x1="{X+h*.97}" y1="{Y-h*.97}" x2="{X-h*.97}" y2="{Y+h*.97}" stroke="#0a141e" stroke-opacity=".7" stroke-width="15" stroke-linecap="round"/>'
             f'<line x1="{X+h*.97}" y1="{Y-h*.97}" x2="{X-h*.97}" y2="{Y+h*.97}" stroke="url(#mirror)" stroke-width="10" stroke-linecap="round"/></g>')
    b.append("".join(g))
    # scarab: beetle along its mirror diagonal
    X, Y = 150, 430
    sc = [f'<g transform="translate({X} {Y}) rotate(-45)" filter="url(#drop)">']
    for u, k in ((-24, -16), (2, 0), (28, 16)):
        for sg in (-1, 1):
            sc.append(f'<path d="M{u} {sg*22} L{u+k*.5} {sg*38} L{u+k*1.1+4} {sg*46}" fill="none" stroke="#2b1a0c" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    sc.append('<path d="M-60 0 C -60 -16 -48 -18 -44 -14 L -40 0 L -44 14 C -48 18 -60 16 -60 0 Z" fill="#2a1d0e" stroke="#e3b24a" stroke-width="2"/>')
    sc.append('<ellipse cx="-30" cy="0" rx="14" ry="26" fill="url(#shell)" stroke="#e3b24a" stroke-width="3"/>')
    sc.append('<ellipse cx="16" cy="0" rx="38" ry="33" fill="url(#shell)" stroke="#e3b24a" stroke-width="3"/>')
    sc.append('<path d="M-6 -16 C 14 -26 36 -20 44 -10 M-6 16 C 14 26 36 20 44 10" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2.5"/>')
    sc.append('<line x1="-78" y1="0" x2="78" y2="0" stroke="#0a141e" stroke-opacity=".7" stroke-width="13" stroke-linecap="round"/>'
              '<line x1="-78" y1="0" x2="78" y2="0" stroke="#e6fbff" stroke-width="8" stroke-linecap="round"/></g>')
    b.append("".join(sc))
    # pharaoh mask, hit by the beam
    burst = []
    for k in range(14):
        a = k * math.pi / 7 + .15
        burst.append(f'<line x1="{450+96*math.cos(a):.1f}" y1="{430+96*math.sin(a):.1f}" x2="{450+136*math.cos(a):.1f}" y2="{430+136*math.sin(a):.1f}"/>')
    b.append(f'<g stroke="#fff6c8" stroke-width="7" stroke-linecap="round" opacity=".95">{"".join(burst)}</g>')
    b.append('<circle cx="450" cy="430" r="104" fill="#5cff8f" opacity=".35" filter="url(#glow)"/>')
    b.append('<circle cx="450" cy="432" r="92" fill="url(#plinth)" stroke="#e3b24a" stroke-width="6" filter="url(#drop)"/>')
    nem = 'M450 336 C 520 336 536 392 534 430 L 560 520 L 506 520 L 498 456 L 402 456 L 394 520 L 340 520 L 366 430 C 364 392 380 336 450 336 Z'
    b.append(f'<path d="{nem}" fill="#f1d27a"/>')
    b.append('<g clip-path="url(#nemes)" stroke="#1d1a17" stroke-width="10">' + "".join(f'<line x1="{450+k*15}" y1="320" x2="{450+k*22}" y2="530"/>' for k in range(-8, 9)) + '</g>')
    b.append(f'<path d="{nem}" fill="none" stroke="#3a2607" stroke-width="3"/>')
    b.append('<ellipse cx="450" cy="420" rx="40" ry="52" fill="url(#skin)" stroke="#5a3418" stroke-width="2.5"/>')
    b.append('<rect x="408" y="372" width="84" height="11" fill="url(#gold)"/>')
    b.append('<path d="M450 340 Q 464 356 456 376 L 444 376 Q 436 356 450 340 Z" fill="#ffd25a" stroke="#5a3d06" stroke-width="2"/>')
    b.append('<g stroke="#140c06" stroke-width="4" stroke-linecap="round" fill="none"><path d="M414 396 Q 426 388 438 394"/><path d="M462 394 Q 474 388 486 396"/></g><g fill="#fff" stroke="#140c06" stroke-width="3"><ellipse cx="427" cy="412" rx="9" ry="10"/><ellipse cx="473" cy="412" rx="9" ry="10"/></g><g fill="#140c06"><circle cx="428" cy="414" r="4"/><circle cx="472" cy="414" r="4"/><ellipse cx="450" cy="447" rx="7" ry="9"/></g>')
    b.append('<rect x="441" y="468" width="18" height="40" rx="6" fill="#1d1a17" stroke="#f1d27a" stroke-width="2.5"/>')
    # scorpion strolling over the sand
    sp = ['<g transform="translate(386 712) scale(1.6)" fill="#3a230f" stroke="#3a230f" stroke-linecap="round">',
          '<ellipse cx="-4" cy="8" rx="46" ry="9" fill="#000" fill-opacity=".18" stroke="none"/>']
    for k in range(4):
        for sg in (-1, 1):
            bx = 6 - k * 7
            sp.append(f'<path d="M{bx} {sg*4} L{bx-3+sg*2} {sg*13} L{bx-8+sg*3} {sg*20}" fill="none" stroke-width="2.6"/>')
    for sg in (-1, 1):
        sp.append(f'<path d="M10 {sg*4} L20 {sg*11} L30 {sg*10}" fill="none" stroke-width="3.2"/><ellipse cx="35" cy="{sg*10}" rx="7" ry="4.5" stroke="none"/>')
    sp.append('<ellipse cx="4" cy="0" rx="12" ry="8" stroke="none"/>' + "".join(f'<ellipse cx="{-8-k*6}" cy="0" rx="{7-k*.5}" ry="{8.5-k*.6}" stroke="none"/>' for k in range(5)))
    tail = []
    for k in range(7):
        u = k / 6
        a = math.pi * .95 * u
        tail.append((-36 - math.sin(a) * 24, -(1 - math.cos(a)) * 17))
    sp.append("".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{6.4-k*.55:.1f}" stroke="none"/>' for k, (x, y) in enumerate(tail)))
    tx, ty = tail[-1]
    sp.append(f'<ellipse cx="{tx+4:.1f}" cy="{ty+1:.1f}" rx="5.5" ry="4" fill="#7a3a12" stroke="none"/><path d="M{tx+8:.1f} {ty+2:.1f} Q {tx+13:.1f} {ty+3:.1f} {tx+13:.1f} {ty+8:.1f}" fill="none" stroke-width="2.2"/></g>')
    b.append("".join(sp))
    b.append('<text x="300" y="776" text-anchor="middle" font-family="Figtree" font-weight="800" font-size="22" fill="#fff3d0">Laser and mirrors · 2 players or teams</text>')
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
