import re
from itertools import combinations
from typing import List


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        return file.readlines()
    

def get_rules(input_path: str) -> list[str]:

    lines = read_file_lines(input_path=input_path)
    lines = "".join(lines)
    rules = re.findall(r"[0-9]+\|[0-9]+", lines)

    return rules


def get_updates(input_path: str) -> list[list[str]]: 

    lines = read_file_lines(input_path=input_path)
    rules = get_rules(input_path=input_path)
    updates = [line.split()[0] for line in lines[len(rules):] if len(line) > 1]
    updates = [re.findall(r"[0-9]+", u) for u in updates]

    return updates


def check_rules_followed(rules: List[str], update: List[str]) -> bool:

    page_combinations = list(combinations(update, 2))
    page_orders = ["|".join(pc) for pc in page_combinations]
    following = all(pc in rules for pc in page_orders)

    if following:
        return True
    else:
        return False


def reorder_update(rules: List[str], update: List[str]) -> list[str]: 

    rule_pages = [re.findall(r"[0-9]+", rule) for rule in rules]

    # for each page in update - find the pages to print after
    for page in update: 
        pages_to_print_after = []
        for rp in rule_pages:
            if page == rp[0]:
                pages_to_print_after.append(rp[1])

        # retrieve indices of pages to print after. If they are not all larger than page index, reset page index to minimum of smallest. 
        pages_to_print_after_indices = [update.index(p) for p in pages_to_print_after if p in update]
        old_page_index = update.index(page)
        if not all(old_page_index < i for i in pages_to_print_after_indices):
            new_page_index = min(pages_to_print_after_indices)
            update.insert(new_page_index, update.pop(old_page_index))

    return update


def get_update_middle_page(update: List[str]) -> int:

    middle_page = int(update[len(update)//2])
    
    return middle_page


def sum_update_middle_pages(rules: List[str], updates: List[List[str]]) -> tuple[int]:

    correct_update_pages = []
    reordered_update_pages = []
    for update in updates:
        following = check_rules_followed(rules=rules, update=update)
        if following:
            middle_page = get_update_middle_page(update)
            correct_update_pages.append(middle_page)
        else: 
            update = reorder_update(rules=rules, update=update)
            middle_page = get_update_middle_page(update)
            reordered_update_pages.append(middle_page)

    correct_update_sum = sum(correct_update_pages)
    reordered_update_sum = sum(reordered_update_pages)

    return correct_update_sum, reordered_update_sum


def main(input_path: str) -> None:
    rules = get_rules(input_path=input_path)
    updates = get_updates(input_path=input_path)

    # part 1 and part 2
    correct_update_sum, reordered_update_sum = sum_update_middle_pages(rules=rules, updates=updates)
    print(correct_update_sum)
    print(reordered_update_sum)


if __name__ == "__main__":
    main("day05/inputs/input.txt")