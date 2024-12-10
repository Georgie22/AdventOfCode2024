import re
from typing import List


# Regex expression notes
# ==============================================
# . matches any single character except newline
# + matches one or more occurences
# ^ matches the start of the line
# $ matches the end of the line
# \ used to treat special characters as literals
# d{x,y} matches x - y digit values e.g d{1,2} - 1 or 2 digit values
# [0-9] matches any digit


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        return file.readlines()
    

def get_corrupted_memory(input_path: str) -> str:

    corrupted_memory_lines = read_file_lines(input_path=input_path)
    corrupted_memory = "".join(corrupted_memory_lines)

    return corrupted_memory
  

def find_instructions(corrupted_memory: str) -> list[str]:

    instructions =  re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted_memory)

    return instructions


def find_enabled_instructions(corrupted_memory: str) -> list[str]:

    dont_splits = re.split(r"don't\(\)", corrupted_memory)

    enabled_instructions = []

    # the memory starts enabled as default
    # so any instructions in the first split (before the first don't() condition) are automatically enabled
    initial_instructions = find_instructions(dont_splits[0])
    enabled_instructions.extend(initial_instructions)

    # any instructions after don't() are ignored unless a do() condition is found. Instructions after do() are enabled
    for split in dont_splits[1:]:
        do_split = re.split(r"do\(\)", split)
        if len(do_split) == 1:
            # no do condition found
            continue
        else:
            # accomodate for possibly more than one do() found
            for split in do_split[1:]:
                instructions = find_instructions(split)
                enabled_instructions.extend(instructions)

    return enabled_instructions


def get_product_pairs(instructions: List[str]) -> list[list[int]]:

    product_pairs = []
    for instruction in instructions:
        numbers = re.findall("[0-9]+", instruction)
        pair = [int(value) for value in numbers]
        product_pairs.append(pair)

    return product_pairs


def calculate_sum_of_products(product_pairs: List[List[int]]) -> int:

    products = [values[0]*values[1] for values in product_pairs]
    sum_of_products = sum(products)

    return sum_of_products


def run_program(input_path: str, enable_conditions: bool = False) -> int:

    corrupted_memory = get_corrupted_memory(input_path=input_path)
    if enable_conditions:
         instructions = find_enabled_instructions(corrupted_memory)
    else:
        instructions = find_instructions(corrupted_memory=corrupted_memory)
    product_pairs = get_product_pairs(instructions=instructions)
    sum_of_products = calculate_sum_of_products(product_pairs=product_pairs)

    return sum_of_products


def main(input_path: str) -> None:

    # part 1
    sum_of_products = run_program(input_path=input_path)
    print(sum_of_products)

    # part 2
    enabled_sum_of_products = run_program(input_path=input_path, enable_conditions=True)
    print(enabled_sum_of_products)


if __name__ == "__main__":
    main(input_path = "day03/inputs/input.txt")