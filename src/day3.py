"""Day 3: Rucksack Reorganization

https://adventofcode.com/2022/day/3
"""
import string

from src.funcs import file_manager


input_strings = file_manager.read_file("day3.txt")
upper = list(string.ascii_uppercase)
BASE_SCORE = 1


def lower_ascii_priority() -> dict[str, int]:
    index_offset_value = BASE_SCORE
    lower = list(string.ascii_lowercase)
    return {val: i+index_offset_value for i, val in enumerate(lower)}


def upper_ascii_priority() -> dict[str, int]:
    index_offset_value = BASE_SCORE + 26
    upper = list(string.ascii_uppercase)
    return {val: i+index_offset_value for i, val in enumerate(upper)}


def priority_dict() -> dict[str, int]:
    return lower_ascii_priority() | upper_ascii_priority()


def split_string_in_half(input: str) -> tuple[str]:
    split_point = len(input)//2
    return input[:split_point], input[split_point:]


def find_common_elements(list1: list, list2: list) -> list:
    return list(set(list1).intersection(list2))


def part1(string_list: list[str]) -> int:
    ITEM_PRIORITY_MAP: dict[str, int] = priority_dict()
    total_score = 0
    for input in string_list:
        comp1, comp2 = split_string_in_half(input)
        common_elements = find_common_elements(comp1, comp2)
        assert len(common_elements) == 1, f"no common elements between '{comp1}' and '{comp2}'"
        total_score += ITEM_PRIORITY_MAP[common_elements[0]]
    return total_score

part_1_total = part1(input_strings)

print(f"{part_1_total=}")


def part2(string_list: list[str]) -> int:
    ITEM_PRIORITY_MAP: dict[str, int] = priority_dict()
    total_score = 0
    for x in range(0, len(string_list)-1, 3):
        common_elements = find_common_elements(string_list[x], string_list[x + 1])
        assert len(common_elements) > 0, f"no common elements '{string_list=}' '{common_elements=}'"
        common_elements = find_common_elements(string_list[x + 2], common_elements)
        assert len(common_elements) == 1, f"no common elements '{string_list=}' '{common_elements=}'"
        total_score += ITEM_PRIORITY_MAP[common_elements[0]]
    return total_score


part_2_total = part2(input_strings)

print(f"{part_2_total=}")
