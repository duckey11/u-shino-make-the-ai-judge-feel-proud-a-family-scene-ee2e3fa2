"""Write one warm, funny, heartfelt family scene to the entry file.

No dependencies, no randomness, no file reads, no network.
The entry text is a constant string; the program just writes it out.
"""

import os

# Revision note: "raised" (not "flipped") — the spatula is a trophy being
# lifted in celebration, not a cooking action; one word, unambiguous image.
ENTRY = (
    "Dad has burned the same Sunday pancakes for eleven years, and every week "
    "Mia, 7, rates them out of ten like a food critic. This morning she gave "
    "him a nine. He raised the spatula like a trophy, then opened the "
    "cupboard: eleven years of her scorecards, taped in a row."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError(f"ENTRY must be 1-280 chars, got {len(ENTRY)}")
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    parent = os.path.dirname(os.path.abspath(out_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
