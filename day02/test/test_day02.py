import pytest

from day02.src.day02 import puzzle


@pytest.fixture
def input_path():
    return "day02/test/test_inputs/test_input.txt"


@pytest.fixture
def reports():
    return [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]


def test_process_input(input_path, reports):
    input_reports = puzzle.process_input(input_path=input_path)

    assert len(input_reports) == 6
    assert len(input_reports[0]) == 5
    assert input_reports == reports


def test_calculate_safe_report_count(input_path):
    safe_count = puzzle.calculate_safe_report_count(input_path=input_path)

    assert safe_count == 2