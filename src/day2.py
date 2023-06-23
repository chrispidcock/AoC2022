"""Day 2: Rock Paper Scissors

https://adventofcode.com/2022/day/2
"""
from enum import Enum

from src.funcs import file_manager


filename = "day2.txt"
f = file_manager.read_file(filename)


class Shape(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Outcome(Enum):
    LOSE = "lose"
    DRAW = "draw"
    WIN = "win"


shape_map: dict[str, Shape]  = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}
winning_hand_map: dict[Shape, Shape] = {
    Shape.ROCK: Shape.SCISSORS,
    Shape.SCISSORS: Shape.PAPER,
    Shape.PAPER: Shape.ROCK,
}
outcome_points: dict[Outcome, int] = {
    Outcome.LOSE: 0,
    Outcome.DRAW: 3,
    Outcome.WIN: 6,
}
shape_points: dict[Shape, int] = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}


def calculate_outcome(shape_1: Shape, shape_2: Shape) -> Outcome:
    if shape_1 == shape_2:
        return Outcome.DRAW
    if winning_hand_map[shape_1] == shape_2:
        return Outcome.WIN
    return Outcome.LOSE


def calculate_shape(shape: Shape, outcome: Outcome) -> Shape:
    match outcome:
        case Outcome.DRAW:
            return shape
        case Outcome.LOSE:
            return winning_hand_map[shape]
        case Outcome.WIN:
            return shape_to_lose(shape)


def shape_to_lose(shape: Shape) -> Shape:
    for key, val in winning_hand_map.items():
        if val == shape:
            return key


def extract_input_shapes(input_str: str) -> list[str, str]:
    return input_str.split(" ")


def part1(input_list: list) -> int:
    total_score = 0
    for input in input_list:
        p1, p2 = extract_input_shapes(input)
        outcome = calculate_outcome(shape_map[p2], shape_map[p1])
        total_score += outcome_points[outcome] + shape_points[shape_map[p2]]
    return total_score

def part2(input_list: list) -> int:
    outcome_map = {
        "X": Outcome.LOSE,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN,
    }
    total_score = 0
    for input in input_list:
        p1, p2 = extract_input_shapes(input)
        shape_to_play = calculate_shape(shape_map[p1], outcome_map[p2])
        total_score += outcome_points[outcome_map[p2]] + shape_points[shape_to_play]
    return total_score


total_score = part1(f)
print(total_score)
total_score = part2(f)
print(total_score)
