import copy
from typing import List
from dataclasses import dataclass


@dataclass
class Position():
    i: int          # rows
    j: int          # columns


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        lines = file.readlines()
    
    return lines


def read_map(input_path:str) -> list[list]:

    rows = read_file_lines(input_path=input_path)

    map = []
    for row in rows:
        # remove new line element and take out of the list .split() creates
        row_string = row.split()[0]
        # separate row string into the individual characters (that make up the row positions)
        row_elements = [elem for elem in row_string]
        map.append(row_elements)

    return map


def read_starting_position(map: List[List]) -> Position:

    map_height = len(map)

    for i in range(map_height):
        if "^" in map[i]:
            j = map[i].index("^")
            starting_position = Position(i, j)
            break
    
    return starting_position


def check_position_is_on_map(position: Position, map_size: tuple) -> bool:

    if (position.i >= 0 and position.i < map_size[0] and position.j >= 0 and position.j < map_size[1]):
        return True
    else:
        return False


def check_loop(visited_positions: set[tuple, tuple], position: Position, direction: tuple) -> bool:

    if ((position.i, position.j), direction) in visited_positions:
        return True
    else: 
        return False
    

def get_visited_positions(map: List[List], starting_position: Position, starting_direction: tuple) -> tuple[list[tuple], bool]:

    map_height, map_width = (len(map), len(map[0]))

    # store the first position and direction
    direction = starting_direction
    position = starting_position
    visited_positions = {((position.i, position.j), direction)}

    # while current position is on the map
    position_on_map = True
    looping = False
    while position_on_map and not looping:

        # get the next position and check its on map:
        new_position = Position(position.i + direction[0], position.j + direction[1])
        new_position_on_map = check_position_is_on_map(position=new_position, map_size=(map_height, map_width))

        # if new position is on the map
        if new_position_on_map:

            # check we are not looping
            looping = check_loop(visited_positions=visited_positions, position=new_position, direction=direction)
            # if looping, end
            if looping:
                break

            # otherwise check its not an obstacle and mark the position as visted
            elif map[new_position.i][new_position.j] != "#":
                position = new_position
                visited_positions.add(((position.i, position.j), direction))

            # else turn right
            else:
                direction = (direction[1], -direction[0])

        # if new position is not on the map, end
        else:
            position_on_map = False
    
    return visited_positions, looping


def count_loops_possible(map: List[List], starting_position: Position, starting_direction: tuple) -> int:

    original_positions, _ = get_visited_positions(map=map, starting_position=starting_position, starting_direction=starting_direction)

    count = 0
    # for each unique visted position thats not the starting position
    for p in set(p for p, _ in original_positions):
        if p != (starting_position.i, starting_position.j):

            # add an obstruction:
            new_map = copy.deepcopy(map)
            new_map[p[0]][p[1]] = "#"

            # get new visted positions and check for looping
            _, looping = get_visited_positions(map=new_map, starting_position=starting_position, starting_direction=starting_direction)
            if looping:
                count += 1

    return count


def main(input_path: str) -> None:

    # read map and starting position
    map = read_map(input_path=input_path)
    starting_position = read_starting_position(map=map)

    # part 1
    visited_positions, _ = get_visited_positions(map=map, starting_position=starting_position, starting_direction=(-1, 0))
    unique_positions = set([pos for pos, _ in visited_positions])
    print(len(unique_positions))

    # part 2
    loop_count = count_loops_possible(map=map, starting_position=starting_position, starting_direction=(-1,0))
    print(loop_count)


if __name__ == "__main__":
    main(input_path="day06/inputs/input.txt")

