#!/usr/bin/env python3
"""food-picture-01 entry (v6): copy the ramen artwork to /output/entry.png.

Photorealistic steaming tonkotsu ramen in a black speckled ceramic
bowl on dark wood: chopsticks lifting tall glossy noodles high, a
halved jammy egg with a thick dripping deep-orange yolk front-centre,
torched chashu fanned on the left, red chili-oil swirls on creamy
broth, nori, scallions and sesame, dramatic steam and warm bokeh.
"""
import hashlib
import os

ART_SHA256 = "37b01c2cd7a7085a5fffaff077a43e5173a484d360a3483dc2196da8ca5efaf3"
ART_SIZE = 487000


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "art.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    assert len(data) == ART_SIZE, f"art.png size {len(data)} != {ART_SIZE}"
    assert hashlib.sha256(data).hexdigest() == ART_SHA256, "art.png sha256 mismatch"
    with open(dst, "wb") as f:
        f.write(data)
    print(f"wrote {dst} ({len(data)} bytes, sha256 {ART_SHA256[:12]}...)")
    print("entry ready: steaming tonkotsu ramen, tall noodle pull, dripping egg, chili oil")


if __name__ == "__main__":
    main()
