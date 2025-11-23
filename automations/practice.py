


import os
import sys
import time
import random
import requests
import json
import csv
# import pandas as pd
# import numpy as np

def list_users(users):
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")

def get_users():
    url = "https://jsonplaceholder.typicode.com/users";
    response = requests.get(url);

    return response.json();

def main():
    response = get_users();
    list_users(response);


if __name__ == "__main__":
    main();