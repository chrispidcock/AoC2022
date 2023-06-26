from src import day4 as d4


def test_process_assignment_text_end():
    is_inclosed = d4.process_assignment_text("6-6,4-6")
    assert is_inclosed is True


def test_process_assignment_text_single_enclosed():
    is_inclosed = d4.process_assignment_text("6-6,4-7")
    assert is_inclosed is True


def test_process_assignment_text_double_enclosed():
    is_inclosed = d4.process_assignment_text("6-7,4-9")
    assert is_inclosed is True


def test_process_assignment_text_large_overlap():
    is_inclosed = d4.process_assignment_text("3-8,4-9")
    assert is_inclosed is False


def test_process_assignment_text_single_overlap():
    is_inclosed = d4.process_assignment_text("3-4,4-9")
    assert is_inclosed is False


def test_process_assignment_text_no_overlap():
    is_inclosed = d4.process_assignment_text("1-3,4-9")
    assert is_inclosed is False
