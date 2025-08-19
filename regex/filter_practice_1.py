#!/usr/bin/env python3

people = [("Alice", 25), ("Bob", 17), ("Charlie", 30), ("Diana", 16), ("Eve", 22)]

people_over_18 = list(filter(lambda person: person[1] >= 18, people))