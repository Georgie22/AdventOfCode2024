from typing import Type, List
from dataclasses import dataclass


DIRECTIONS = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


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
    

def check_feasible_directions(position: Type[Position], pattern: List, grid_size: tuple, directions: List[tuple]) -> list[tuple]:

    feasible_directions = []

    for d in directions:

        i = position.i + d[0]*(len(pattern)-1)
        j = position.j + d[1]*(len(pattern)-1)
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
                feasible_directions = check_feasible_directions(position=position, pattern=pattern, grid_size=(grid_width, grid_height), directions=directions)

                for d in feasible_directions:
                    match = check_for_pattern_match(grid=grid, position=position, pattern=pattern, direction=d)
                    if match:
                        count += 1

    return count


def main(input_path: str, pattern: str, directions: List[tuple]) -> None:

    # part 1
    pattern_count = get_pattern_count_in_grid(input_path=input_path, pattern=pattern, directions=directions)
    print(pattern_count)


if __name__ == "__main__":
    main(input_path="day04/inputs/input.txt", pattern="XMAS", directions=DIRECTIONS)
