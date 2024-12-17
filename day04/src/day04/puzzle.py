from typing import Type, List
from dataclasses import dataclass


DIRECTIONS = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
CROSS_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


@dataclass
class Position():
    i: int         # row
    j: int         # column


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        lines = file.readlines()

    return lines
    

def read_wordsearch(input_path: str) -> list[list[str]]:

    wordsearch = []
    rows = read_file_lines(input_path=input_path)

    for row in rows:
        # remove new line element and take out of the list .split() creates
        row_string = row.split()[0]

        # separate the string into the individual characters to form the wordsearch row
        row_elements = [elem for elem in row_string]
        wordsearch.append(row_elements)

    return wordsearch
    

def check_position_in_wordsearch(position: Position, wordsearch_size: tuple) -> bool:

    if (position.i >= 0 and position.i < wordsearch_size[0] and position.j >= 0 and position.j < wordsearch_size[1]):
        return True
    else:
        return False
    

def check_feasible_directions(position: Position, max_index: int, wordsearch_size: tuple, directions: List[tuple]) -> list[tuple]:

    feasible_directions = []

    for d in directions:

        i = position.i + d[0]*(max_index)
        j = position.j + d[1]*(max_index)
        end_position = Position(i, j)

        in_bounds = check_position_in_wordsearch(position=end_position, wordsearch_size=wordsearch_size)
        if in_bounds:
            feasible_directions.append(d)

    return feasible_directions


def check_for_pattern_match(wordsearch: List[List[str]], position: Position, pattern: List, direction: tuple) -> bool:

    wordsearch_pattern = []
    for n in range(len(pattern)):

        i = position.i + direction[0]*n
        j = position.j + direction[1]*n 
        wordsearch_element = wordsearch[i][j]
        wordsearch_pattern.append(wordsearch_element)
    
    if wordsearch_pattern == pattern:
        return True
    else:
        return False
    

def check_for_cross_pattern_match(wordsearch: List[List[str]], position: Position, pattern: List, directions: List[tuple]) -> bool:

    back_cross_elements = {(0,0): wordsearch[position.i][position.j]}
    forward_cross_elements = {(0,0): wordsearch[position.i][position.j]}


    # get grid elements and store in dictionary
    for d in directions:
        for n in range(1, (len(pattern)//2)+1): 

            d_i = d[0]*n
            d_j = d[1]*n

            i = position.i + d_i
            j = position.j + d_j
            wordsearch_element = wordsearch[i][j]

            # add the elements found in the (-1, -1) and (1, 1) directions to the back cross elements
            if (d_i < 0 and d_j < 0) or (d_i > 0 and d_j > 0):
                back_cross_elements[(d_i, d_j)] = wordsearch_element

            # add the elements found in the (-1, 1) and (1, -1) directions to the forward cross elements
            else:
                forward_cross_elements[(d_i, d_j)] = wordsearch_element

    # order the cross elements
    sorted_back_elements = [back_cross_elements[k] for k in sorted(back_cross_elements.keys())]
    sorted_forward_elements = [forward_cross_elements[k] for k in sorted(forward_cross_elements.keys())]

    if (sorted_back_elements == pattern or list(reversed(sorted_back_elements)) == pattern) and (sorted_forward_elements == pattern or list(reversed(sorted_forward_elements)) == pattern):
        return True
    else:
        return False


def get_pattern_count_in_wordsearch(input_path: str, pattern: str, directions: List[tuple]) -> int:

    wordsearch = read_wordsearch(input_path=input_path)
    wordsearch_height = len(wordsearch)
    wordsearch_width = len(wordsearch[0])

    pattern = list(pattern)
  
    count = 0
    for i in range(wordsearch_height):
        for j in range(wordsearch_width):

            if wordsearch[i][j] == pattern[0]:
                position = Position(i, j)
                feasible_directions = check_feasible_directions(position=position, max_index=len(pattern)-1, wordsearch_size=(wordsearch_height, wordsearch_width), directions=directions)

                for d in feasible_directions:
                    match = check_for_pattern_match(wordsearch=wordsearch, position=position, pattern=pattern, direction=d)
                    if match:
                        count += 1

    return count
 

def get_cross_pattern_count_in_wordsearch(input_path: str, pattern: str, directions: List[tuple]) -> int:

    wordsearch = read_wordsearch(input_path=input_path)
    wordsearch_height = len(wordsearch)
    wordsearch_width = len(wordsearch[0])

    pattern = list(pattern)

    count = 0
    for i in range(wordsearch_height):
        for j in range(wordsearch_width):

            if wordsearch[i][j] == pattern[len(pattern)//2]:   # if grid element == middle pattern character
                position = Position(i, j)
                feasible_directions = check_feasible_directions(position=position, max_index=1, wordsearch_size=(wordsearch_height, wordsearch_width), directions=directions)
                if feasible_directions == directions:
                    cross_match = check_for_cross_pattern_match(wordsearch=wordsearch, position=position, pattern=pattern, directions=feasible_directions)
                    if cross_match:
                        count += 1
    
    return count


def main(input_path: str, pattern: str, directions: List[tuple], cross_pattern: str, cross_directions: List[tuple]) -> None:

    # part 1
    pattern_count = get_pattern_count_in_wordsearch(input_path=input_path, pattern=pattern, directions=directions)
    print(pattern_count)

    cross_pattern_count = get_cross_pattern_count_in_wordsearch(input_path=input_path, pattern=cross_pattern, directions=cross_directions)
    print(cross_pattern_count)


if __name__ == "__main__":
    main(input_path="day04/inputs/input.txt", pattern="XMAS", directions=DIRECTIONS, cross_pattern="MAS", cross_directions=CROSS_DIRECTIONS)
