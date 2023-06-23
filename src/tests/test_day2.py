from src import day2 as d2


def test_calculate_outcome_win():
    assert d2.Outcome.WIN == d2.calculate_outcome(d2.Shape.ROCK, d2.Shape.SCISSORS)


def test_calculate_outcome_draw():
    assert d2.Outcome.DRAW == d2.calculate_outcome(d2.Shape.ROCK, d2.Shape.ROCK)


def test_calculate_outcome_lose():
    assert d2.Outcome.LOSE == d2.calculate_outcome(d2.Shape.SCISSORS, d2.Shape.ROCK)


def test_extract_input_shapes():
    assert d2.extract_input_shapes("B X")[0] == "B"
    assert d2.extract_input_shapes("B X")[1] == "X"


def test_calculate_outcome_example():
    total_score = d2.part1([
        "A Y",
        "B X",
        "C Z",
    ])
    assert 15 == total_score


def test_calculate_outcome_example2():
    total_score = d2.part1([
        "C Z",
    ])
    assert 6 == total_score


def test_calculate_outcome_example3():
    total_score = d2.part1([
        "B X",
    ])
    assert 1 == total_score


def test_calculate_outcome_example4():
    total_score = d2.part1([
        "A Z",
    ])
    assert 3 == total_score
