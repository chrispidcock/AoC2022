"""Day 2: Rock Paper Scissors

https://adventofcode.com/2022/day/2
"""
from enum import Enum

from src.funcs import file_manager


filename = "day2.txt"
f = file_manager.read_file(filename)


class Shape(bytes, Enum):
    ROCK = (0, 1, 2)
    PAPER = (1, 2, 0)
    SCISSORS = (2, 3, 1)

    def __new__(cls, shape, points, beats):
        obj = bytes.__new__(cls, [shape])
        obj.shape = shape
        obj.points = points
        obj._beats = beats
        obj._value_ = shape
        return obj

    def beats(self) -> "Shape":
        ordinal = self._value_ - 1
        if ordinal < 0:
            ordinal = len(Shape) - 1
        return Shape(ordinal)

    def loses(self) -> "Shape":
        ordinal = self._value_ + 1
        if ordinal >= len(Shape):
            ordinal = 0
        return Shape(ordinal)


class Outcome(bytes, Enum):
    LOSE = (0, 0)
    DRAW = (1, 3)
    WIN = (2, 6)

    def __new__(cls, outcome, points):
        obj = bytes.__new__(cls, [outcome])
        obj._value_ = outcome
        obj.points = points
        return obj


shape_map: dict[str, Shape]  = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}


def calculate_outcome(shape_1: Shape, shape_2: Shape) -> Outcome:
    if shape_1 == shape_2:
        return Outcome.DRAW
    if shape_1.beats() == shape_2:
        return Outcome.WIN
    return Outcome.LOSE


def calculate_shape(shape: Shape, outcome: Outcome) -> Shape:
    match outcome:
        case Outcome.DRAW:
            return shape
        case Outcome.LOSE:
            return shape.beats()
        case Outcome.WIN:
            return shape.loses()


def extract_input_shapes(input_str: str) -> list[str, str]:
    return input_str.split(" ")


def part1(input_list: list) -> int:
    total_score = 0
    for input in input_list:
        p1, p2 = extract_input_shapes(input)
        outcome = calculate_outcome(shape_map[p2], shape_map[p1])
        total_score += outcome.points + shape_map[p2].points
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
        total_score += outcome_map[p2].points + shape_to_play.points
    return total_score


total_score = part1(f)
print(total_score)
total_score = part2(f)
print(total_score)
