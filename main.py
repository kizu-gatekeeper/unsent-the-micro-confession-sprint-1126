"""Entry for make.fun: Unsent: The Micro-Confession Sprint.

A To: line plus the one line that was typed and never sent.
"""
import os

LINE = "To: my dad\ni kept the voicemail where you forgot my name mid-sentence. i play it when i need to remember why i stopped calling first"
MAX_CHARS = 260


def write_entry(out_dir):
    parts = LINE.split("\n")
    if len(parts) != 2 or not parts[0].startswith("To:") or not parts[1].strip():
        raise ValueError("entry must be a To: line plus one unsent line")
    if not LINE.strip() or len(LINE) > MAX_CHARS or len(parts[1]) > 200:
        raise ValueError("entry exceeds the character limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
