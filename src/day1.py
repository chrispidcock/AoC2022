"""Day 1: Calorie Counting"""
from src.funcs import file_manager


filename = "day1.txt"
f = file_manager.read_file(filename)


def top_3(cals, top_cals):
    top_cals.append(cals)
    top_cals = sorted(top_cals, reverse=True)
    top_cals = top_cals[:3]
    return top_cals


cur_cals = 0
top_cals = []
for line in f:
    if len(line) == 0:
        top_cals = top_3(cur_cals, top_cals)
        cur_cals = 0
        continue
    cur_cals += int(line)

print(f"top_cals = {top_cals}")
print(f"cals_total = {sum(top_cals)}")
