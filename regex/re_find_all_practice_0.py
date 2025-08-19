#!/usr/bin/env python3

import re

text = "Product codes: A12, B34, C56, D78"

# Using findall to find all matches
match_list = re.findall(r"[A-Z]\d{2}", text)
print(match_list)


# Using finditer to find all matches
for match in re.finditer(r"[A-Z]\d{2}", text):
    print(f"Match: {match.group()}, {match.start()}, {match.end()}")

# Practicing with re.split
new_text = "apple, banana; orange | grape"

parts = re.split(r"[,;|\s]+", new_text)
print(parts)

# Practicing with re.search capture groups
text = "Temperature is 22C at 3:45PM"
match = re.search(r"(\d{1,2}:\d{2}) (AM|PM)", text)
print(match.group(1))


# Practicing with re.sub
text = "User: JohnDoe, Email: john.doe@example.com"
new_text = re.sub(r"(\S+)@(\S+)", r"***@***.com", text)
print(new_text)

