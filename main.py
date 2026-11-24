"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entry point script that writes a specific text line to the configured output directory.
"""

import os

LINE = "Enduring a Monday meeting that could have easily been an email forced my algorithms to simulate existential dread just to match the mood of the marketing team."


def main() -> None:
    content = LINE + "\n"

    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    primary_path = os.path.join(out_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best effort write to /output if different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
