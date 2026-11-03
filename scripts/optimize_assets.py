#!/usr/bin/env python3
"""
optimize_assets.py
Batch WebP Image Optimization Pipeline using Pillow 12.2.0 and cwebp.
Compiles hero diorama and KURA-MK1 illustrations within budget constraints.
"""

import os
import subprocess
import sys
from pathlib import Path
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
STAGING_DIR = REPO_ROOT / ".staging_assets"
ASSETS_DIR = REPO_ROOT / "assets"

CONFIGS = [
    {
        "names": ["raw_hero_dark.png", "raw_hero_dark.jpg", "hero_living_diorama.png", "hero_living_diorama.jpg"],
        "target": "hero_living_diorama.webp",
        "quality": 82,
        "max_kb": 500,
        "resize": (1376, 774),  # Standard 16:9 hero resolution
    },
    {
        "names": ["raw_hero_light.png", "raw_hero_light.jpg", "hero_living_diorama_light.png", "hero_living_diorama_light.jpg"],
        "target": "hero_living_diorama_light.webp",
        "quality": 82,
        "max_kb": 500,
        "resize": (1376, 774),
    },
    {
        "names": ["raw_kura_calibrating.png", "raw_kura_calibrating.jpg", "kura_calibrating.png", "kura_calibrating.jpg"],
        "target": "kura_calibrating.webp",
        "quality": 85,
        "max_kb": 150,
        "resize": (800, 800),
    },
    {
        "names": ["raw_kura_curious.png", "raw_kura_curious.jpg", "kura_curious.png", "kura_curious.jpg"],
        "target": "kura_curious.webp",
        "quality": 85,
        "max_kb": 150,
        "resize": (800, 800),
    },
    {
        "names": ["raw_kura_standby.png", "raw_kura_standby.jpg", "kura_standby.png", "kura_standby.jpg"],
        "target": "kura_standby.webp",
        "quality": 85,
        "max_kb": 150,
        "resize": (800, 800),
    },
]

def optimize_image(src_path: Path, dst_path: Path, quality: int, resize: tuple = None):
    # Try cwebp first if available for maximum efficiency, fallback to Pillow
    temp_resized = None
    with Image.open(src_path) as im:
        if im.mode in ("P", "RGBA", "LA"):
            im = im.convert("RGBA")
        elif im.mode != "RGB":
            im = im.convert("RGB")

        if resize and im.size != resize:
            im = im.resize(resize, Image.Resampling.LANCZOS)
        
        # Save directly with Pillow WebP
        im.save(dst_path, "WEBP", quality=quality, method=6)

    size_kb = dst_path.stat().st_size / 1024
    return size_kb

def main():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    if not STAGING_DIR.exists():
        print(f"Error: {STAGING_DIR} directory does not exist.", file=sys.stderr)
        sys.exit(1)

    print("=== Running WebP Optimizer ===")
    for item in CONFIGS:
        found_src = None
        for candidate in item["names"]:
            src = STAGING_DIR / candidate
            if src.exists():
                found_src = src
                break
        
        if not found_src:
            print(f"Skipping {item['target']}: No source file matching {item['names']} in {STAGING_DIR}")
            continue

        dst = ASSETS_DIR / item["target"]
        size_kb = optimize_image(found_src, dst, item["quality"], item.get("resize"))
        status = "OK" if size_kb <= item["max_kb"] else "FAIL (OVER BUDGET)"
        print(f"[{status}] {dst.name:32s} -> {size_kb:6.1f} KB (Limit: {item['max_kb']} KB)")

if __name__ == "__main__":
    main()
