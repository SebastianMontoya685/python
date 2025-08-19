#!/usr/bin/env python3

usernames = ["john", "amy99", "user_1", "Bob!", "admin123", "kate"]

filtered_usernames = list(filter(lambda username: len(username) > 5 and username.isalnum(), usernames))