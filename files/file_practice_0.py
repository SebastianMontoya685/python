#!/usr/bin/env python3

import os
import sys
import re
from pathlib import Path

# Read a file and print the second line
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines[1])

# Write to a file
with open("log.txt", "w") as file:
    file.write("Log started\n")

# Append to a file
with open("log.txt", "a") as file:
    file.write("Session resumed\n")

# Checking for file existence using the os & path modules
if os.path.exists("log.txt"):
    print("File exists")
else:
    print("File does not exist")

file = "log.txt"
if Path(file).exists():
    print("File exists")
else:
    print("File does not exist")


# Practicing with creating and deleting files and directories using os and Path
# Using the os module
os.mkdir("data/output", parents=True, exist_ok=True)
os.remove("output")

# Using the Path module
Path("data/output").mkdir(parents=True, exist_ok=True)
Path("data/output").unlink("output")