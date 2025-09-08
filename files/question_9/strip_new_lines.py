#!/usr/bin/env python3

import sys
import re
from pathlib import Path

# Function to find the index of the last space in a line
def index_of_last_space(line: str, max_length: int):
    final_space_index = -1
    for i, char in enumerate(line[:max_length]):
        if char.isspace():
            final_space_index = i
    return final_space_index

# Function to find the index of the first space in a line
def index_of_first_space(line: str, max_length: int):
    for i, char in enumerate(line[max_length - 1:], start=max_length - 1):
        if char.isspace():
            return i

# Function to insert a newline into a line at a given index
def insert_newline_into_index(line: str, index: int):
    return line[:index] + "\n" + line[index + 1:]

# Main function to read the file and write back to the same file
def main():
    lines_list = []

    # Reading from hello.txt
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        for line in lines:
            new_lines = line.strip()
            lines_list.append(new_lines)

        

    for i, line in enumerate(lines_list):
        print(f"{i}: {line}")

    # Writing back to the same file
    with open(sys.argv[1], "w") as file:
        for line in lines_list:
            file.write(f"{line}\n")

if __name__ == "__main__":
    main()