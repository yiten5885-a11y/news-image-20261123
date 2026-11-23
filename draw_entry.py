#!/usr/bin/env python3
"""Draw the 23 Nov 2026 news front page (1024x1024). Deterministic, no network.
Run: python3 draw_entry.py  -> writes entry.png beside this file."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 234)
INK = (25, 25, 25)
RED = (166, 27, 27)
NAVY = (22, 50, 79)
GOLD = (176, 124, 32)
TEAL = (14, 107, 107)
GREY = (90, 86, 76)
SEA = (38, 98, 140)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def block(x, y, w, kicker, headline, deck, hsize=44, dsize=21, kcolor=RED):
    d.text((x, y), kicker, font=SANS_B(19), fill=kcolor)
    y += 30
    for ln in wrap(d, headline, SERIF_B(hsize), w):
        d.text((x, y), ln, font=SERIF_B(hsize), fill=INK)
        y += hsize + 6
    y += 4
    for ln in wrap(d, deck, SANS(dsize), w):
        d.text((x, y), ln, font=SANS(dsize), fill=(52, 50, 44))
        y += dsize + 7
    return y

# ---- masthead ----
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((512, 18), "THE WORLD IN ONE DAY", font=SERIF_B(58), fill=(248, 244, 234), anchor="ma")
d.text((512, 92), "MONDAY  23  NOVEMBER  2026", font=SANS_B(30), fill=(232, 196, 106), anchor="ma")
d.line([0, 148, W, 148], fill=GOLD, width=6)

# ---- lead: COP31 ----
lx, ly, lw = 40, 176, 520
block(lx, ly, lw, "CLIMATE  •  ANTALYA, TURKEY",
      "COP31 collapses with no deal",
      "After two weeks of talks — the longest climate summit ever — countries reject the “Antalya Pact”. The final draft dropped every mention of fossil fuels.",
      hsize=52, dsize=23)
# globe illustration, right of lead
cx, cy, r = 800, 316, 110
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(58, 130, 178), outline=INK, width=4)
d.ellipse([cx - r + 26, cy - r + 30, cx - r + 92, cy - r + 86], fill=(120, 178, 110))
d.ellipse([cx + 8, cy + 18, cx + 82, cy + 78], fill=(120, 178, 110))
d.arc([cx - r, cy - r + 40, cx + r, cy + r - 40], 250, 470, fill=(248, 244, 234), width=3)
d.arc([cx - r + 40, cy - r, cx + r - 40, cy + r], 90, 270, fill=(248, 244, 234), width=3)
# crack
d.line([(cx - 30, cy - 105), (cx - 8, cy - 55), (cx - 34, cy - 8), (cx + 2, cy + 40), (cx - 12, cy + 95)],
       fill=RED, width=9, joint="curve")
d.text((cx, cy + r + 16), "NO DEAL", font=SANS_B(34), fill=RED, anchor="ma")
d.line([40, 496, 984, 496], fill=INK, width=3)

# ---- three columns ----
col_w = 300
xs = [40, 362, 684]
ys = 522

# 1. Libya — ship + drone
x = xs[0]
d.rectangle([x, ys, x + col_w, ys + 150], fill=(214, 232, 240), outline=INK, width=2)
# sea
for i, yy in enumerate([ys + 118, ys + 130, ys + 142]):
    d.arc([x + 8 + i * 20, yy - 12, x + 90 + i * 20, yy + 12], 180, 360, fill=SEA, width=3)
    d.arc([x + 150 + i * 12, yy - 12, x + 230 + i * 12, yy + 12], 180, 360, fill=SEA, width=3)
# ship hull
d.polygon([(x + 70, ys + 78), (x + 240, ys + 78), (x + 218, ys + 112), (x + 92, ys + 112)], fill=(70, 70, 74))
d.rectangle([x + 118, ys + 48, x + 168, ys + 78], fill=(70, 70, 74))
d.line([x + 143, ys + 18, x + 143, ys + 48], fill=INK, width=4)
# explosion starburst
for ang in range(0, 360, 45):
    import math
    a = math.radians(ang)
    d.line([(x + 196, ys + 52), (x + 196 + int(26 * math.cos(a)), ys + 52 + int(26 * math.sin(a)))],
           fill=(226, 122, 24), width=5)
d.ellipse([x + 182, ys + 38, x + 210, ys + 66], fill=(226, 122, 24), outline=RED, width=2)
# drone: small quadcopter with spinning rotors
d.ellipse([x + 238, ys + 20, x + 254, ys + 32], fill=INK)
d.line([x + 230, ys + 26, x + 262, ys + 26], fill=INK, width=3)
d.line([x + 224, ys + 20, x + 238, ys + 20], fill=INK, width=2)
d.line([x + 254, ys + 20, x + 268, ys + 20], fill=INK, width=2)
d.line([x + 246, ys + 32, x + 246, ys + 40], fill=INK, width=2)
block(x, ys + 166, col_w, "WAR AT SEA  •  LIBYA",
      "Ukraine says its sea drones sank a Russian warship off Benghazi",
      "Seven sea drones, Kyiv says; a helicopter on board was destroyed.",
      hsize=29, dsize=18)

# 2. Washington — Capitol + 258
x = xs[1]
d.rectangle([x, ys, x + col_w, ys + 150], fill=(232, 226, 210), outline=INK, width=2)
# capitol dome
d.pieslice([x + 105, ys + 18, x + 195, ys + 92], 180, 360, fill=NAVY)
d.rectangle([x + 112, ys + 82, x + 188, ys + 94], fill=NAVY)
d.rectangle([x + 146, ys + 8, x + 154, ys + 22], fill=NAVY)
d.rectangle([x + 78, ys + 92, x + 222, ys + 100], fill=NAVY)
for cx2 in range(x + 88, x + 216, 26):
    d.rectangle([cx2, ys + 100, cx2 + 12, ys + 128], fill=NAVY)
d.rectangle([x + 70, ys + 128, x + 230, ys + 136], fill=NAVY)
d.text((x + col_w // 2, ys + 8), "", font=SANS_B(10), fill=INK)
block(x, ys + 166, col_w, "WASHINGTON  •  MIDTERMS",
      "Democrats win biggest House majority since 1992",
      "At least 258 seats. Hubbard beats Foxx in North Carolina; four races uncalled.",
      hsize=29, dsize=18)

# 3. Nvidia — chip + magnifier
x = xs[2]
d.rectangle([x, ys, x + col_w, ys + 150], fill=(226, 232, 226), outline=INK, width=2)
# chip
d.rectangle([x + 96, ys + 34, x + 204, ys + 118], fill=(34, 34, 38), outline=GOLD, width=3)
d.rectangle([x + 128, ys + 62, x + 172, ys + 90], fill=(58, 130, 90))
for px in range(x + 112, x + 196, 20):
    d.line([px, ys + 22, px, ys + 34], fill=INK, width=4)
    d.line([px, ys + 118, px, ys + 130], fill=INK, width=4)
for py in range(ys + 50, ys + 106, 20):
    d.line([x + 84, py, x + 96, py], fill=INK, width=4)
    d.line([x + 204, py, x + 216, py], fill=INK, width=4)
# magnifier
d.ellipse([x + 216, ys + 84, x + 272, ys + 140], outline=RED, width=6)
d.line([x + 258, ys + 126, x + 288, ys + 148], fill=RED, width=7)
d.text((x + 244, ys + 94), "?", font=SERIF_B(36), fill=RED, anchor="mm")
block(x, ys + 166, col_w, "TECH  •  CHIPS",
      "U.S. seeks answers on Nvidia’s China chip sales",
      "Bessent, Sunday: “We need to see who was in charge of compliance.”",
      hsize=29, dsize=18)

# ---- footer ----
d.line([40, 958, 984, 958], fill=INK, width=2)
d.text((512, 968), "Sources: AP  •  Reuters  •  CNN  •  Bloomberg  —  reported 23 November 2026",
       font=SANS(18), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png")
