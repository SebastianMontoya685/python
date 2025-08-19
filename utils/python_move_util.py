#!/usr/bin/env python3

import os
import shutil
import sys

base_path = "/Users/sebastianmontoya/python/python/"

source_subdir = sys.argv[1]
destination_subdir = sys.argv[2]

source_dir = os.path.join(base_path, source_subdir)
destination_dir = os.path.join(base_path, destination_subdir)

os.makedirs(destination_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    src_path = os.path.join(source_dir, filename)
    dest_path = os.path.join(destination_dir, filename)

    if os.path.isfile(src_path):
        shutil.move(src_path, dest_path)