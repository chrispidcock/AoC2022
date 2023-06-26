from src import day4 as d4


def test_process_assignment_entire_overlap_end():
    is_inclosed = d4.process_assignment_entire_overlap("6-6,4-6")
    assert is_inclosed is True


def test_process_assignment_entire_overlap_single_enclosed():
    is_inclosed = d4.process_assignment_entire_overlap("6-6,4-7")
    assert is_inclosed is True


def test_process_assignment_entire_overlap_double_enclosed():
    is_inclosed = d4.process_assignment_entire_overlap("6-7,4-9")
    assert is_inclosed is True


def test_process_assignment_entire_overlap_large_overlap():
    is_inclosed = d4.process_assignment_entire_overlap("3-8,4-9")
    assert is_inclosed is False


def test_process_assignment_entire_overlap_single_overlap():
    is_inclosed = d4.process_assignment_entire_overlap("3-4,4-9")
    assert is_inclosed is False


def test_process_assignment_entire_overlap_no_overlap():
    is_inclosed = d4.process_assignment_entire_overlap("1-3,4-9")
    assert is_inclosed is False




def test_process_assignment_overlap_end():
    is_overlapping = d4.process_assignment_overlap("6-6,4-6")
    assert is_overlapping is True


def test_process_assignment_overlap_single_enclosed():
    is_overlapping = d4.process_assignment_overlap("6-6,4-7")
    assert is_overlapping is True


def test_process_assignment_overlap_double_enclosed():
    is_overlapping = d4.process_assignment_overlap("6-7,4-9")
    assert is_overlapping is True


def test_process_assignment_overlap_large_overlap():
    is_overlapping = d4.process_assignment_overlap("3-8,4-9")
    assert is_overlapping is True


def test_process_assignment_overlap_single_overlap():
    is_overlapping = d4.process_assignment_overlap("3-4,4-9")
    assert is_overlapping is True


def test_process_assignment_overlap_no_overlap():
    is_overlapping = d4.process_assignment_overlap("1-3,4-9")
    assert is_overlapping is False


def test_process_assignment_overlap_no_overlap_swapped():
    is_overlapping = d4.process_assignment_overlap("4-9,1-3")
    assert is_overlapping is False
