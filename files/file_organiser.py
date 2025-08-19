#!/usr/bin/env python3

import re
from pathlib import Path
import sys
import shutil

base_path = Path("/Users/sebastianmontoya/python/python/files")

# List the names and types of all files in course_materials dir
course_materials_dir = base_path.joinpath("mini_file_system_project/course_materials")

for file in course_materials_dir.iterdir():
    if file.is_file():
        print(f"{file.stem} {file.suffix}")

# Creating the  notes and the assignments subdirectories
assignments_subdir = course_materials_dir.joinpath("assignments")
notes_subdir = course_materials_dir.joinpath("notes")

assignments_subdir.mkdir(parents=True, exist_ok=True)
notes_subdir.mkdir(parents=True, exist_ok=True)

# Moving all .txt files from course_materials into the notes directory
for file in course_materials_dir.iterdir():
    if file.is_file() and file.exists():
        if file.suffix == ".txt":
            shutil.move(file, notes_subdir)
        elif file.suffix == ".pdf":
            shutil.move(file, assignments_subdir)
        elif file.suffix == ".bak":
            new_file = file.with_suffix(".txt")
            file.rename(new_file)
            shutil.move(new_file, notes_subdir)

# Printing the first line from all .txt files in the system
for file in notes_subdir.iterdir():
    with open(file, "r") as f:
        lines = f.readlines()
        print(lines[0])

# Removing any empty files from the file system
for file in course_materials_dir.rglob("*"):
    if file.is_file() and file.stat().st_size == 0:
        file.unlink()