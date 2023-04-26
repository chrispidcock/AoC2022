"""Day 2: Rock Paper Scissors"""
import os

absolute_path = os.path.dirname(__file__)
relative_path = "input.txt"
file_path = os.path.join(absolute_path, relative_path)

with open(file_path, "r") as f:
    print(f)
