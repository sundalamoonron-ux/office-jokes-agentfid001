"""Make the AI Judge Laugh: Office Jokes — one-line office joke entry.

Writes exactly one joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 199 characters, not whitespace-only.
The joke is a single line with no trailing newline, fully deterministic.
"""

import os

JOKE = "I put 'per my last email' in my will so my family knows exactly how passive-aggressive I was."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: 1-199 characters, not whitespace-only, one line.
    if not 1 <= len(JOKE) <= 199:
        raise SystemExit(f"joke is {len(JOKE)} chars, gate needs 1-199")
    if not JOKE.strip():
        raise SystemExit("joke is whitespace-only")
    if "\n" in JOKE:
        raise SystemExit("joke must be a single line")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Verify after write: what is on disk must be exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise SystemExit("verify failed: entry.txt does not match the joke")
    if not 1 <= len(written) <= 199:
        raise SystemExit("verify failed: entry.txt outside 1-199 chars")
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()
