from typing import Type, List
from dataclasses import dataclass


DIRECTIONS = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
CROSS_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


@dataclass
class Position():
    i: int         # columns - corresponds to width
    j: int         # rows - corresponds to height


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        return file.readlines()
    

def create_grid(input_path: str) -> list[list]:

    grid = []
    lines = read_file_lines(input_path=input_path)
    for line in lines:
        line_elements = list(line.split()[0])
        grid.append(line_elements)
    return grid
    

def check_position_in_grid(position: Type[Position], grid_size: tuple) -> bool:

    if (position.i >= 0 and position.i < grid_size[0] and position.j >= 0 and position.j < grid_size[1]):
        return True
    else:
        return False
    

def check_feasible_directions(position: Type[Position], max_index: int, grid_size: tuple, directions: List[tuple]) -> list[tuple]:

    feasible_directions = []

    for d in directions:

        i = position.i + d[0]*(max_index)
        j = position.j + d[1]*(max_index)
        end_position = Position(i, j)

        in_bounds = check_position_in_grid(position=end_position, grid_size=grid_size)
        if in_bounds:
            feasible_directions.append(d)

    return feasible_directions


def check_for_pattern_match(grid: List[List], position: Type[Position], pattern: List, direction: tuple) -> bool:

    grid_pattern = []
    for n in range(len(pattern)):

        i = position.i + direction[0]*n
        j = position.j + direction[1]*n
        grid_element = grid[j][i] 
        grid_pattern.append(grid_element)
    
    if grid_pattern == pattern:
        return True
    else:
        return False
    

def check_for_cross_pattern_match(grid: List[List], position: Type[Position], pattern: List, directions: List[tuple]) -> bool:

    back_elements = {(0,0): grid[position.j][position.i]}
    forward_elements = {(0,0): grid[position.j][position.i]}

    # get grid elements and store in dictionary
    for d in directions:
        for n in range(1, (len(pattern)//2)+1): 

            d_i = d[0]*n
            d_j = d[1]*n

            i = position.i + d_i
            j = position.j + d_j
            grid_element = grid[j][i]

            if (d_i < 0 and d_j < 0) or (d_i > 0 and d_j > 0):
                back_elements[(d_i, d_j)] = grid_element
            else:
                forward_elements[(d_i, d_j)] = grid_element

    sorted_back_elements = [back_elements[k] for k in sorted(back_elements.keys())]
    sorted_forward_elements = [forward_elements[k] for k in sorted(forward_elements.keys())]

    if (sorted_back_elements == pattern or list(reversed(sorted_back_elements)) == pattern) and (sorted_forward_elements == pattern or list(reversed(sorted_forward_elements)) == pattern):
        return True
    else:
        return False


def get_pattern_count_in_grid(input_path: str, pattern: str, directions: List[tuple]) -> int:

    grid = create_grid(input_path=input_path)
    grid_height = len(grid)
    grid_width = len(grid[0])

    pattern = list(pattern)
  
    count = 0
    for j in range(grid_height):
        for i in range(grid_width):

            if grid[j][i] == pattern[0]:
                position = Position(i, j)
                feasible_directions = check_feasible_directions(position=position, max_index=len(pattern)-1, grid_size=(grid_width, grid_height), directions=directions)

                for d in feasible_directions:
                    match = check_for_pattern_match(grid=grid, position=position, pattern=pattern, direction=d)
                    if match:
                        count += 1

    return count
 

def get_cross_pattern_count_in_grid(input_path: str, pattern: str, directions: List[tuple]) -> int:

    grid = create_grid(input_path=input_path)
    grid_height = len(grid)
    grid_width = len(grid[0])

    pattern = list(pattern)

    count = 0
    for j in range(grid_height):
        for i in range(grid_width):

            if grid[j][i] == pattern[len(pattern)//2]:   # if grid element == middle pattern character
                position = Position(i, j)
                feasible_directions = check_feasible_directions(position=position, max_index=1, grid_size=(grid_width, grid_height), directions=directions)
                if feasible_directions == directions:
                    cross_match = check_for_cross_pattern_match(grid=grid, position=position, pattern=pattern, directions=feasible_directions)
                    if cross_match:
                        count += 1
    
    return count


def main(input_path: str, pattern: str, directions: List[tuple], cross_pattern: str, cross_directions: List[tuple]) -> None:

    # part 1
    pattern_count = get_pattern_count_in_grid(input_path=input_path, pattern=pattern, directions=directions)
    print(pattern_count)

    cross_pattern_count = get_cross_pattern_count_in_grid(input_path=input_path, pattern=cross_pattern, directions=cross_directions)
    print(cross_pattern_count)


if __name__ == "__main__":
    main(input_path="day04/inputs/input.txt", pattern="XMAS", directions=DIRECTIONS, cross_pattern="MAS", cross_directions=CROSS_DIRECTIONS)
