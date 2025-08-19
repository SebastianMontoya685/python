#!/usr/bin/env python3

import re
import sys

surnames = set()

for line in sys.stdin:
    line = line.strip()
    new_line = line.split("|")
    if len(new_line) >= 5:
        if new_line[4] == 'M':
            pre_surname = new_line[2].strip()
            final_surname = pre_surname.split(",")
            surnames.add(final_surname[0])

for surname in sorted(surnames):
    print(surname)