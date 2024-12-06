import pytest

from src.day01puzzle import part1

@pytest.fixture
def input_path():
    return "day01/test/test_inputs/part1_test.txt"

@pytest.fixture
def list1():
    return [3, 4, 2, 1, 3, 3]

@pytest.fixture
def list2():
    return [4, 3, 5, 3, 9, 3]


def test_process_input(input_path, list1, list2):
    inputs = part1.process_input(input_path=input_path)

    assert len(inputs) == 2
    assert inputs[0] == list1
    assert inputs[1] == list2


def test_calculate_distance_sum(list1, list2):
    distance_sum = part1.calculate_distance_sum(list1=list1, list2=list2)

    assert distance_sum == 11
