#!/usr/bin/env python3

import re

text = "Order ID: 57329, Status: Shipped"

match = re.search(r"\d+", text)
start_pos = match.start()
end_pos = match.end()
print(f"{match.group()}, {start_pos}, {end_pos}")