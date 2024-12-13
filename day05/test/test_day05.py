import pytest

from day05.src.day05 import puzzle


@pytest.fixture
def input_path():
    return "day05/test/test_inputs/test_input.txt"


@pytest.fixture
def rules(input_path):
    return puzzle.get_rules(input_path=input_path)


@pytest.fixture
def updates(input_path):
    return puzzle.get_updates(input_path=input_path)


def test_check_rules_followed(rules, updates):

    rules_followed = []
    for update in updates:
        following = puzzle.check_rules_followed(rules=rules, update=update)
        rules_followed.append(following)

    assert rules_followed == [True, True, True, False, False, False]
    

def test_reorder_update(rules, updates):

    reordered_updates = []
    for update in updates[3:]:
        update = puzzle.reorder_update(rules=rules, update=update)
        reordered_updates.append(update)

    assert reordered_updates == [
        ["97","75","47","61","53"],
        ["61","29","13"],
        ["97","75","47","29","13"]
    ]


def test_check_get_update_middle_page(updates):

    middle_pages = []
    for update in updates:
        middle_page = puzzle.get_update_middle_page(update=update)
        middle_pages.append(middle_page)

    assert middle_pages == [61,53,29,47,13,75]


def test_sum_update_middle_pages(rules, updates):
    correct_update_sum, reordered_update_sum = puzzle.sum_update_middle_pages(rules=rules, updates=updates)

    assert correct_update_sum == 143
    assert reordered_update_sum == 123
