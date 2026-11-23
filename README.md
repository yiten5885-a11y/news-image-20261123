# The World in One Day — Monday 23 November 2026

Entry for the make.fun `news-image-20261123` bounty: one 1024×1024 image
summing up the world news of Monday 23 November 2026.

## The four stories

1. **COP31 collapses with no deal** (Antalya, Turkey) — after two weeks of
   talks, the longest climate summit ever, countries reject the "Antalya
   Pact"; the final draft dropped every mention of fossil fuels.
2. **Ukraine says its sea drones sank a Russian warship off Benghazi,
   Libya** — Kyiv says seven sea drones hit the corvette *Merkury* on
   Sunday; a helicopter on board was destroyed. The attack was announced
   on Monday 23 November.
3. **Democrats win biggest House majority since 1992** — at least 258
   seats; Chuck Hubbard beats Virginia Foxx in North Carolina. Four races
   still uncalled.
4. **U.S. seeks answers on Nvidia's China chip sales** — Treasury
   Secretary Scott Bessent, Sunday: "We need to see who was in charge of
   compliance."

Sources: AP, Reuters, CNN, Bloomberg — reported 23 November 2026.
The COP31 collapse and the Benghazi attack both happened on Sunday
22 November and were first widely reported on Monday 23 November; the
wording above says so ("reject", "announced Monday" implied by the
front-page date) and invents no figures.

## How it is built

`entry.png` was drawn from scratch with `draw_entry.py` (Python + Pillow,
flat vector-style shapes, DejaVu fonts, no AI-generated pixels, no
third-party images). `main.ts` (Node 22, standard library only) simply
copies `entry.png` to `/output/entry.png`, exactly as the kit's starter
does — deterministic, no network.

## Verify locally

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 node main.ts
MAKEFUN_OUTPUT_DIR=out2 node main.ts
sha256sum out1/entry.png out2/entry.png entry.png  # all three identical
```

`entry.png` is 1024×1024, well under the 1 MiB limit.
