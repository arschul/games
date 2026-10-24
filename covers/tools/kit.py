"""Shared helpers for cover SVGs (600x800)."""
import math, random
from xml.sax.saxutils import escape as _esc

W, H = 600, 800


def esc(s):
    return _esc(str(s), {'"': "&quot;"})


def svg(defs, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs>{FILTERS}{defs}</defs>{body}</svg>')


FILTERS = '''
<filter id="k-glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="k-glow-s" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.5"/></filter>
<filter id="k-drop" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity=".45"/></filter>
<filter id="k-drop-s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity=".4"/></filter>
'''


def font(f):
    return f"'{f}'" if " " in f or f[0].isdigit() else f


def text(x, y, s, f, size, fill, weight=400, anchor="middle", ls=0, extra="", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font(f)}" font-size="{size}" '
            f'font-weight="{weight}" letter-spacing="{ls}" fill="{fill}"{st} {extra}>{s}</text>')


def glow_text(x, y, s, f, size, fill, glow, weight=400, ls=0, extra="", anchor="middle"):
    return (text(x, y, s, f, size, glow, weight, anchor, ls, 'filter="url(#k-glow)" opacity=".85" ' + extra)
            + text(x, y, s, f, size, fill, weight, anchor, ls, extra))


def lin(id_, stops, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def rad(id_, stops, cx="50%", cy="40%", r="75%"):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'


def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def emoji(x, y, ch, size, extra=""):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Noto Color Emoji" font-size="{size}" {extra}>{ch}</text>'


def stars(seed, n, color="#fff", y1=800, size=(1, 2.4), op=(.2, .8)):
    r = random.Random(seed)
    return "".join(
        f'<circle cx="{r.uniform(0, 600):.0f}" cy="{r.uniform(0, y1):.0f}" r="{r.uniform(*size):.1f}" fill="{color}" opacity="{r.uniform(*op):.2f}"/>'
        for _ in range(n))


def footer(s, f, color, size=14, ls=4, y=780, weight=700):
    return text(300, y, s, f, size, color, weight, ls=ls)


def hexpts(cx, cy, r, rot=0):
    return " ".join(f"{cx + r*math.cos(math.radians(60*k+rot)):.1f},{cy + r*math.sin(math.radians(60*k+rot)):.1f}" for k in range(6))


def chip(x, y, w, h, label, f, size, bg, ink, stroke=None, rx=None, weight=700):
    rx = h / 2 if rx is None else rx
    st = f'stroke="{stroke}" stroke-width="2"' if stroke else ""
    return rect(x, y, w, h, bg, rx, st) + text(x + w/2, y + h/2 + size*0.36, label, f, size, ink, weight)
