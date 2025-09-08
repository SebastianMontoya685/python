#!/usr/bin/env python3
import sys
from collections import Counter


def main():
    for line in sys.stdin:
        clean_line = line.strip().split()
        for word in clean_line:
            character_counts = Counter(word.lower())
            values = character_counts.values()
            if all(value == 1 for value in values):
                print(word)

if _name__ == "__main__":
    main()