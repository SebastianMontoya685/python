#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split("|")

    new_line = "\t".join(line)
    print(new_line[1:])