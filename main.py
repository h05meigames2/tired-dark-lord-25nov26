"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one ~100-word monologue from Lord Ashenmar, Dark Lord of the
Tower of Ashes, to /output/entry.txt. His exhaustion shows only in
pauses, postponements and deflections -- never in the words themselves.
"""

import os

MONOLOGUE = (
    "I have ruled from the Tower of Ashes for thirty years, and the "
    "throne still pinches. The ravens bring me reports I never asked "
    "for. My minions stack their paperwork — permits for plagues, "
    "forms in triplicate — beside a cold cup of tea. Every eclipse "
    "ritual, postponed. Every hero, arriving at the worst possible "
    "hour, sword gleaming, monologue longer than mine. I should blot "
    "out the sun today. I should. Instead, I shall feed the ravens, "
    "sign one form, and save the apocalypse for tomorrow. The world "
    "can wait. My chair, at last, does not."
)

FORBIDDEN = ("tired", "weary", "exhausted", "sleepy")


def main():
    text = MONOLOGUE.strip()
    assert 1 <= len(text) <= 600, f"length {len(text)} out of range"
    lowered = text.lower()
    for word in FORBIDDEN:
        assert word not in lowered, f"forbidden word present: {word}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
