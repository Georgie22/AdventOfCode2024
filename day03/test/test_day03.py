import pytest

from day03.src.day03 import puzzle


@pytest.fixture
def corrupted_memory():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


@pytest.fixture
def instructions():
    return ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]


@pytest.fixture
def product_pairs():
    return [[2, 4], [5, 5], [11, 8], [8, 5]]


@pytest.fixture
def enabled_instructions():
    return ["mul(2,4)", "mul(8,5)"]


@pytest.fixture
def enabled_product_pairs():
    return [[2, 4], [8, 5]]


def test_find_instructions(corrupted_memory, instructions):
    input_instructions = puzzle.find_instructions(corrupted_memory=corrupted_memory)

    assert input_instructions == instructions


def test_find_enabled_instructions(corrupted_memory, enabled_instructions):
    input_enabled_instructions = puzzle.find_enabled_instructions(corrupted_memory=corrupted_memory)

    assert input_enabled_instructions == enabled_instructions


def test_get_product_pairs(instructions, product_pairs, enabled_instructions, enabled_product_pairs):
    input_product_pairs = puzzle.get_product_pairs(instructions=instructions)
    input_enabled_product_pairs = puzzle.get_product_pairs(instructions=enabled_instructions)

    assert input_product_pairs == product_pairs
    assert input_enabled_product_pairs == enabled_product_pairs


def test_calculate_sum_of_products(product_pairs, enabled_product_pairs):
    sum_of_product = puzzle.calculate_sum_of_products(product_pairs=product_pairs)
    enabled_sum_of_product = puzzle.calculate_sum_of_products(product_pairs=enabled_product_pairs)

    assert sum_of_product == 161
    assert enabled_sum_of_product == 48