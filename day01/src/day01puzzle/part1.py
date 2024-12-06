import os
from typing import List


def read_file_lines(input_path: str) -> list[str]:

    full_input_path = os.path.abspath(input_path)
    with open(full_input_path, "r") as file:
        return file.readlines()


def process_input(input_path: str) -> tuple[List[int], List[int]]:
    
    lines = read_file_lines(input_path=input_path)

    list1 = []
    list2 = []

    for line in lines:
        line_elements = line.split()
        list1.append(int(line_elements[0]))
        list2.append(int(line_elements[1]))
    return list1, list2


def calculate_distance_sum(list1: List, list2: List) -> int:
    
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    distances = [abs(elem1 - elem2) for elem1 ,elem2 in zip(sorted_list1, sorted_list2)]
    sum_distance = sum(distances)

    return sum_distance


def main(input_path: str) -> None:
    list1, list2 = process_input(input_path=input_path)
    sum_distance = calculate_distance_sum(list1, list2)
    print(sum_distance)


if __name__ == "__main__":
    main(input_path="day01/test/test_inputs/part1_test.txt")
