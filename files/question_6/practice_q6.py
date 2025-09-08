#!/usr/bin/env python3

import sys
import re
from pathlib import Path

# Reading the lines from both files.
with open(sys.argv[1], "r") as file1:
    lines1 = file1.readlines()

with open(sys.argv[2], "r") as file2:
    lines2 = file2.readlines()

# Manually reversing the lines from one of the files.
lines2.reverse()

print(lines1)
print(lines2)

if lines1 == lines2:
    print("Mirrored")
else:
    print("Not mirrored")