"""Day 4: Camp Cleanup

https://adventofcode.com/2022/day/4
"""
from src.funcs import file_manager


input_strings = file_manager.read_file("day4.txt")


def process_assignment_entire_overlap(input: str) -> bool:
    str1, str2 = input.split(',')
    rng1_min, rng1_max = str1.split('-')
    rng2_min, rng2_max = str2.split('-')
    if (int(rng1_min) <= int(rng2_min) and int(rng1_max) >= int(rng2_max)) \
        or (int(rng2_min) <= int(rng1_min) and int(rng2_max) >= int(rng1_max)):
            return True
    return False


def process_assignment_overlap(input: str) -> bool:
    str1, str2 = input.split(',')
    rng1_min, rng1_max = str1.split('-')
    rng2_min, rng2_max = str2.split('-')
    if (int(rng1_min) <= int(rng2_min) <= int(rng1_max)) \
        or (int(rng2_min) <= int(rng1_min) <= int(rng2_max)):
            return True
    return False


def part1(input_list: list[str]) -> int:
    total = 0
    for entry in input_list:
        total += 1 if process_assignment_entire_overlap(entry) else 0
    return total


part_1_total = part1(input_strings)

print(f"{part_1_total=}")


def part2(input_list: list[str]) -> int:
    total = 0
    for entry in input_list:
        total += 1 if process_assignment_overlap(entry) else 0
    return total


part_2_total = part2(input_strings)

print(f"{part_2_total=}")

