#!/usr/bin/env python3
import sys
from collections import Counter

def main():
    for line in sys.stdin:
        clean_line = line.strip().split()
        valid_words = []
        for word in clean_line:
            counts = Counter(word.lower())
            values = counts.values()
            if any(value > 1 for value in values):
                valid_words.append(word)
        print(" ".join(valid_words))
if __name__ == "__main__":
    main()