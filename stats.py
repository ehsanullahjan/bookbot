import pathlib
from collections import defaultdict
from typing import Generator


def get_text(pathname: str | pathlib.Path) -> str:
    with open(pathname, mode="r", encoding="utf-8") as f:
        return f.read()


def get_lines(pathname: str | pathlib.Path) -> Generator[str]:
    with open(pathname, mode="r", encoding="utf-8") as f:
        for line in f:
            yield line


def count_words(text: str) -> int:
    return len(text.split())


def calc_char_freq(text: str) -> dict[str, int]:
    freqs = defaultdict(int)
    for char in text:
        freqs[char.lower()] += 1
    return freqs


def to_sorted_records(char_freqs: dict[str, int]) -> list[dict[str, int]]:
    records = [{"char": k, "num": v} for k, v in char_freqs.items()]
    records.sort(key=lambda r: r["num"], reverse=True)
    return records
