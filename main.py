"""One-Liner Laughs entry: write a single funny line to /output/entry.txt.

The joke: a ghosting setup that lands on an unexpected tech twist --
the ex is not haunting the narrator, she is his cloud backup.
"""

import os

JOKE = (
    "I tried to ghost my ex, but she tracks my location, my Spotify, "
    "and my trauma \u2014 turns out she's my cloud backup."
)


def main() -> None:
    # The gate is 1-200 characters: fail loudly here instead of
    # shipping an entry the sealed scorer would refuse.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise SystemExit(f"joke is {len(JOKE)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
