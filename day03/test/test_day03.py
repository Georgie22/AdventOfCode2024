import pytest

from day03.src.day03 import puzzle


@pytest.fixture
def input_path():
    return "day03/test/test_inputs/test_input.txt"


@pytest.fixture
def instructions():
    return ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']


@pytest.fixture
def product_pairs():
    return [[2, 4], [5, 5], [11, 8], [8, 5]]


def test_find_instructions(input_path, instructions):
    input_instructions = puzzle.find_instructions(input_path=input_path)

    assert input_instructions == instructions


def test_get_product_pairs(instructions, product_pairs):
    input_product_pairs = puzzle.get_product_pairs(instructions=instructions)

    assert input_product_pairs == product_pairs


def test_calculate_sum_of_products(product_pairs):
    sum_of_product = puzzle.calculate_sum_of_products(product_pairs=product_pairs)

    assert sum_of_product == 161