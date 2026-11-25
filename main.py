"""One-Liner Marathon entry: a single one-line comedy joke.

The joke: heroic fitness stats, an impossible day on the couch,
and one small reveal at the end.
"""

import os

JOKE = (
    "My fitness tracker says I burned 2,314 calories, climbed 40 flights "
    "of stairs, and swam half a mile yesterday, which is remarkable, "
    "because I spent the entire day on the couch. The tracker was on the cat."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
