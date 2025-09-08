#!/usr/bin/env python3

import sys
import re
from pathlib import Path

def count_chars_excluding_newline(line: str):
    index = 0
    for char in line:
        if char != "\n":
            index += 1   
    return index   

def does_line_have_spaces(line: str):
      if " " in line:
          return True
      else:
          return False
      
def does_line_have_spaces_in_first_n_chars(line: str, max_length: int):
    for i, char in enumerate(line[:max_length]):
        if char == " ":
            return True
    return False

def index_of_last_space_in_first_n_chars(line: str, max_length: int):
    index = -1
    for i, char in enumerate(line[:max_length]):
        if char == " ":
            index = i
    return index

def index_of_first_space(line: str):
    for i, char in enumerate(line):
        if char == " ":
            return i
    return -1

def insert_newline_into_index(line: str, index: int):
    return line[:index] + "\n" + line[index + 1:]

def main():
    max_length = int(sys.argv[1])
    filename = sys.argv[2]

    # Reading from the file and finding those lines >= n
    final_lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            clean_line_length = count_chars_excluding_newline(line)
            if clean_line_length <= max_length or not does_line_have_spaces(line):
                final_lines.append(line)
                i += 1
                continue

            if does_line_have_spaces_in_first_n_chars(line, max_length):
                index = index_of_last_space_in_first_n_chars(line, max_length)
            else:
                index = index_of_first_space(line)

            # Split at the space
            first_part = line[:index] + "\n"
            second_part = line[index+1:].lstrip()  # Remove leading space

            final_lines.append(first_part)
            if i + 1 < len(lines):
                lines[i+1] = second_part + " " + lines[i+1].lstrip()
            else:
                final_lines.append(second_part + "\n")
            i += 1  # Always increment, since the next line will be processed with the overflow
    with open(filename, "w") as file:
        for i, line in enumerate(final_lines):
            if i < len(final_lines) - 1:
                file.write(line.rstrip('\n') + '\n')
            else:
                file.write(line.rstrip('\n'))

if __name__ == "__main__":
    main()