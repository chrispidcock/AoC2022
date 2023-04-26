"""Day 1: Calorie Counting"""
import os

absolute_path = os.path.dirname(__file__)
relative_path = "input.txt"
file_path = os.path.join(absolute_path, relative_path)

def top_3(cals, top_cals):
    top_cals.append(cals)
    top_cals = sorted(top_cals, reverse=True)
    top_cals = top_cals[:3]
    return top_cals

with open(file_path, "r") as f:
    cur_cals = 0
    top_cals = []
    for line in f:
        ln = line.strip()
        if len(ln) == 0:
            top_cals = top_3(cur_cals, top_cals)
            cur_cals = 0
            continue
        cur_cals += int(ln)        

print(f"top_cals = {top_cals}")
print(f"cals_total = {sum(top_cals)}")
