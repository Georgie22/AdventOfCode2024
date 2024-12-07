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
  

def find_instructions(input_path: str) -> list[str]:

    corrupted_memory_lines = read_file_lines(input_path=input_path)
    corrupted_memory = "".join(corrupted_memory_lines)
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted_memory)

    return instructions


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


def main(input_path: str) -> None:

    # part 1
    instructions = find_instructions(input_path=input_path)
    product_pairs = get_product_pairs(instructions=instructions)
    sum_of_products = calculate_sum_of_products(product_pairs=product_pairs)
    print(sum_of_products)


if __name__ == "__main__":
    main("day03/inputs/input.txt")