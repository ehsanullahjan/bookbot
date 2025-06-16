import pathlib
import sys
from stats import (
    calc_char_freq,
    count_words,
    get_text,
    to_sorted_records,
)


def print_report(pathname: str | pathlib.Path) -> None:
    text = get_text(pathname)
    word_count = count_words(text)
    records: list[dict[str, int]] = to_sorted_records(calc_char_freq(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathname}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for record in records:
        char, freq = record["char"], record["num"]
        if char.isalpha():
            print(f"{char}: {freq}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    pathname = sys.argv[1]
    print_report(pathname)


main()
