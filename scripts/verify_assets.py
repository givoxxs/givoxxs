#!/usr/bin/env python3
"""
verify_assets.py
Automated Asset Budget & Branch Hygiene Verifier for Milestone 1.
Ensures zero budget overages and confirms all required assets are present.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "assets"

# Budget thresholds (in bytes)
HERO_LIMIT = 500 * 1024       # 512,000 bytes (500 KB)
KURA_LIMIT = 150 * 1024       # 153,600 bytes (150 KB)
TOTAL_LIMIT = 1200 * 1024     # 1,228,800 bytes (1.2 MB)

REQUIRED_ASSETS = {
    "hero_living_diorama.webp": ("hero", HERO_LIMIT),
    "hero_living_diorama_light.webp": ("hero", HERO_LIMIT),
    "kura_calibrating.webp": ("kura", KURA_LIMIT),
    "kura_curious.webp": ("kura", KURA_LIMIT),
    "kura_standby.webp": ("kura", KURA_LIMIT),
    "preview_skills_distillation.png": ("preserved", 150 * 1024),
    "preview_giao_archive.png": ("preserved", 600 * 1024),
}

BANNED_FILES = [
    "banner_ghibli.png", "banner_mecha.png", "banner_rpg.png", "banner_simulation_desk.png",
    "jjk_gojo_domain.gif", "jjk_hollow_purple.gif", "jjk_sukuna.gif",
    "mascot_bear_boba.gif", "mascot_bunny_speed.gif", "mascot_capoo_multitask.gif",
    "mascot_cyber_hacker.gif", "mascot_peach_typing.gif", "mascot_retro_robot.gif"
]

def verify():
    if not ASSETS_DIR.exists():
        print(f"FAIL: Assets directory {ASSETS_DIR} not found.")
        sys.exit(1)

    errors = 0
    total_size = 0
    found_files = list(ASSETS_DIR.glob("*"))

    print("=" * 70)
    print("ASSET BUDGET & INTEGRITY VERIFICATION REPORT")
    print("=" * 70)

    # 1. Check for banned files
    for banned in BANNED_FILES:
        if (ASSETS_DIR / banned).exists():
            print(f"❌ FAIL: Legacy bloat file still present: {banned}")
            errors += 1

    # 2. Check required files and individual sizes
    for fname, (cat, limit) in REQUIRED_ASSETS.items():
        fpath = ASSETS_DIR / fname
        if not fpath.exists():
            print(f"❌ FAIL: Required asset missing: {fname}")
            errors += 1
            continue
        
        size = fpath.stat().st_size
        total_size += size
        kb = size / 1024

        if size > limit:
            print(f"❌ FAIL: {fname:35s} {size:8d} B ({kb:6.1f} KB) > Limit {limit//1024} KB")
            errors += 1
        else:
            print(f"✅ PASS: {fname:35s} {size:8d} B ({kb:6.1f} KB) <= Limit {limit//1024} KB")

    # 3. Check for unexpected stray files
    for f in found_files:
        if f.name not in REQUIRED_ASSETS and f.is_file():
            print(f"⚠️  WARN: Unrecognized file in assets/: {f.name} ({f.stat().st_size / 1024:.1f} KB)")
            total_size += f.stat().st_size

    total_kb = total_size / 1024
    total_mb = total_size / (1024 * 1024)

    print("-" * 70)
    print(f"Total Assets Payload: {total_size:,} bytes ({total_kb:.2f} KB / {total_mb:.2f} MB)")
    print(f"Total Budget Ceiling: {TOTAL_LIMIT:,} bytes (1,200.00 KB / 1.17 MB)")

    if total_size > TOTAL_LIMIT:
        print(f"❌ FAIL: Total asset size ({total_mb:.2f} MB) exceeds 1.2 MB limit by {total_size - TOTAL_LIMIT:,} bytes!")
        errors += 1
    else:
        print(f"✅ PASS: Total payload ({total_mb:.2f} MB) is within the 1.2 MB budget.")

    print("=" * 70)
    if errors > 0:
        print(f"VERIFICATION RESULT: FAILED ({errors} errors detected)")
        sys.exit(1)
    else:
        print("VERIFICATION RESULT: ALL CHECKS PASSED")
        sys.exit(0)

if __name__ == "__main__":
    verify()
