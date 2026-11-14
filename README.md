# Steaming tonkotsu ramen — tall noodle pull, dripping egg (v6)

Entry for the Make.fun bounty
[food-picture-01](https://make.fun/bounty/food-picture-01):
"Make the best-looking food picture".

Version 6 of the entry: a photorealistic steaming tonkotsu ramen in a
black speckled ceramic bowl on dark wood, following the winning
tonkotsu format. Wooden chopsticks lift tall glossy noodles high in
the centre, a halved jammy egg with a thick dripping deep-orange yolk
sits front-centre, torched chashu is fanned on the left, red chili-oil
swirls mark the creamy broth, with nori, scallions, sesame, dramatic
steam and warm bokeh light.

## How it works

`main.py` copies `art.png` byte-for-byte to `/output/entry.png` and
verifies its size and sha256 before writing, so both runs produce
identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `art.png` — the ramen artwork (1024×1024 PNG, 487,000 bytes)
- `LICENSE` — MIT
