from src import day3 as d3


test_input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]
alphabet_length = 26


def test_lower_ascii_priority():
    lsp = d3.lower_ascii_priority()
    assert lsp["a"] == 1
    assert lsp["z"] == alphabet_length


def test_upper_ascii_priority():
    lsp = d3.upper_ascii_priority()
    assert lsp["A"] == alphabet_length + 1
    assert lsp["Z"] == alphabet_length + alphabet_length


def test_split_string_in_half():
    half1, half2 = d3.split_string_in_half("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert half1 != half2
    assert half1 == "vJrwpWtwJgWr"
    assert half2 == "hcsFMMfFFhFp"


def test_find_common_elements_exist_in_strings():
    str1 = "vJrwpWtwJgWr"
    str2 = "hcsFMMfFFhFp"
    common_elements = d3.find_common_elements(str1, str2)
    assert ["p"] == common_elements


def test_find_common_elements_absent_in_strings():
    str1 = "vJrwWtwJgWr"
    str2 = "hcsFMMfFFhF"
    common_elements = d3.find_common_elements(str1, str2)
    assert [] == common_elements


def test_find_common_elements_exist():
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 5]
    common_elements = d3.find_common_elements(list1, list2)
    assert [1, 2, 3] == common_elements


def test_find_common_elements_absent():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    common_elements = d3.find_common_elements(list1, list2)
    assert [] == common_elements


def test_part1_example():
    input_string_list = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert d3.part1(input_string_list) == 157


def test_part2_example():
    input_string_list = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    assert d3.part2(input_string_list) == 70
