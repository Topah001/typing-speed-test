"""A small terminal typing-speed test with reusable scoring helpers."""
from __future__ import annotations

import argparse
import difflib
import time
from dataclasses import dataclass

PROMPT = "Practice makes progress. Focus on accuracy before speed."


@dataclass(frozen=True)
class Results:
    wpm: float
    accuracy: float
    elapsed_seconds: float


def score_typing(prompt: str, typed: str, elapsed_seconds: float) -> Results:
    """Compute gross WPM and aligned character accuracy, guarding bad durations."""
    elapsed = max(0.0, float(elapsed_seconds))
    if elapsed == 0.0 or not typed:
        wpm = 0.0
    else:
        wpm = len(typed) / 5.0 / (elapsed / 60.0)
    denominator = max(len(prompt), len(typed))
    if denominator == 0:
        accuracy = 100.0
    else:
        matching = sum(block.size for block in difflib.SequenceMatcher(
            None, prompt, typed, autojunk=False
        ).get_matching_blocks())
        accuracy = matching * 100.0 / denominator
    return Results(round(wpm, 2), round(accuracy, 2), round(elapsed, 2))


def run_test(prompt: str = PROMPT) -> Results:
    print("Type the passage below, then press Enter:\n")
    print(prompt)
    start = time.monotonic()
    typed = input("\n> ")
    elapsed = time.monotonic() - start
    return score_typing(prompt, typed, elapsed)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Measure typing speed and accuracy.")
    parser.add_argument("--prompt", default=PROMPT, help="Passage to type")
    args = parser.parse_args(argv)
    if not args.prompt:
        parser.error("prompt must not be empty")
    result = run_test(args.prompt)
    print(f"\nTime: {result.elapsed_seconds:.2f} seconds")
    print(f"Speed: {result.wpm:.2f} WPM")
    print(f"Accuracy: {result.accuracy:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())