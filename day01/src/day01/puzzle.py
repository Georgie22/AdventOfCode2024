from typing import List
from collections import Counter


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        lines = file.readlines()

    return lines


def read_input(input_path: str) -> tuple[List[int], List[int]]:
    
    lines = read_file_lines(input_path=input_path)

    list1 = []
    list2 = []

    # for each line append the first value to one list and the second value to another list
    for line in lines:
        line_elements = line.split()
        list1.append(int(line_elements[0]))
        list2.append(int(line_elements[1]))

    return list1, list2


def calculate_distance_sum(list1: List, list2: List) -> int:
    
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    distances = [abs(elem1 - elem2) for elem1, elem2 in zip(sorted_list1, sorted_list2)]
    sum_distance = sum(distances)

    return sum_distance


def calculate_simularity_score(list1: List, list2: List) -> int: 

    counts = Counter(list2)
    scores = [elem * counts[elem] for elem in list1]
    simularity_score = sum(scores)

    return simularity_score


def main(input_path: str) -> None:
    
    list1, list2 = read_input(input_path=input_path)

    # part 1
    sum_distance = calculate_distance_sum(list1, list2)
    print(sum_distance)

    # part 2
    simularity_score = calculate_simularity_score(list1, list2)
    print(simularity_score)


if __name__ == "__main__":
    main(input_path="day01/inputs/input.txt")
