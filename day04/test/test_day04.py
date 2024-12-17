import pytest

from day04.src.day04 import puzzle


@pytest.fixture
def input_path():
    return "day04/test/test_inputs/test_input.txt"


@pytest.fixture
def pattern():
    return "XMAS"


@pytest.fixture
def cross_pattern():
    return "MAS"


@pytest.fixture
def directions():
    return [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


@pytest.fixture
def cross_directions():
    return [(-1,-1), (-1, 1), (1, -1), (1, 1)]


test_positions =  [
    (puzzle.Position(0,1), (3,3), True),
    (puzzle.Position(2,2), (3,3), True),
    (puzzle.Position(2,3), (3,3), False),
    (puzzle.Position(-1, 0), (3, 3), False)
]


test_feasible_directions = [
    (puzzle.Position(0,1), "aa", (3,3), [(0,-1), (1,-1), (1,0), (1,1), (0,1)]),
    (puzzle.Position(0,1), "aaa", (3,3), [(1,0)])
]


@pytest.mark.parametrize("position, size, expected", test_positions)
def test_check_position_in_wordsearch(position, size, expected):
    in_bound = puzzle.check_position_in_wordsearch(position=position, wordsearch_size=size)

    assert in_bound == expected


@pytest.mark.parametrize("position, test_pattern, size, expected", test_feasible_directions)
def test_check_feasible_directions(position, test_pattern, size, expected, directions):
    feasible_directions = puzzle.check_feasible_directions(position=position, max_index=len(test_pattern)-1, wordsearch_size=size, directions=directions)

    assert all(elem in expected for elem in feasible_directions)


def test_check_for_pattern_match(input_path, pattern):
    wordsearch = puzzle.read_wordsearch(input_path=input_path)
    position = puzzle.Position(0, 5)
    direction = (0, 1)

    match = puzzle.check_for_pattern_match(wordsearch=wordsearch, position=position, pattern=list(pattern), direction=direction)
    assert match == True


def test_check_for_cross_pattern_match(input_path, cross_pattern, cross_directions):
    wordsearch = puzzle.read_wordsearch(input_path=input_path)
    position = puzzle.Position(1, 2)

    match = puzzle.check_for_cross_pattern_match(wordsearch=wordsearch, position=position, pattern=list(cross_pattern), directions=cross_directions)
    assert match == True


def test_get_pattern_count_in_wordsearch(input_path, pattern, directions):
    pattern_count = puzzle.get_pattern_count_in_wordsearch(input_path=input_path, pattern=pattern, directions=directions)

    assert pattern_count == 18


def test_get_cross_pattern_count_in_wordsearch(input_path, cross_pattern, cross_directions):
    cross_pattern_count = puzzle.get_cross_pattern_count_in_wordsearch(input_path=input_path, pattern=cross_pattern, directions=cross_directions)

    assert cross_pattern_count == 9
