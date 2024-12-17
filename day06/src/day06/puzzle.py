from dataclasses import dataclass
from typing import Type, List


@dataclass
class Position():
    i: int          # rows
    j: int          # columns


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        return file.readlines()


def read_map(input_path:str) -> list[list]:

    map =[]
    lines = read_file_lines(input_path=input_path)
    for line in lines:
        line_elements = list(line.split()[0])
        map.append(line_elements)
    return map


def check_position_is_on_map(position: Position, map_size: tuple) -> bool:

    if (position.i >= 0 and position.i < map_size[0] and position.j >= 0 and position.j < map_size[1]):
        return True
    else:
        return False


def get_new_guard_position(guard: str, position: Type[Position]) -> Type[Position]:

    if guard == "^":
        i = position.i - 1
        j = position.j
    elif guard == ">":
        i = position.i
        j = position.j + 1
    elif guard == "v":
        i = position.i + 1
        j = position.j
    else:
        i = position.i
        j = position.j - 1 

    new_position = Position(i, j)
    
    return new_position


def get_new_guard_direction(guard: str) -> str:

    if guard == "^":
        guard = ">"
    elif guard == ">":
        guard = "v"
    elif guard == "v":
        guard = "<"
    else:
        guard = "^"
    
    return guard


def get_guard_positions(map: List[List], guard: str) -> list[Type[Position]]:

    map_height = len(map)
    map_width = len(map[0])

    starting_position = [(i, j.index(guard)) for i, j in enumerate(map) if "^" in j][0]
    position = Position(starting_position[0], starting_position[1])
    position_on_map = True

    guard_positions = [position]
    while position_on_map:
      
        new_position = get_new_guard_position(guard=guard, position=position)
        new_position_on_map = check_position_is_on_map(position=new_position, map_size=(map_height, map_width))

        if new_position_on_map:
            if map[new_position.i][new_position.j] != "#":
                position = new_position
                guard_positions.append(position)
            else:
                guard = get_new_guard_direction(guard=guard)
        else:
            position_on_map = False

    return guard_positions


def sum_distinct_guard_positions(map: List[List], guard:str) -> int:

    guard_positions = [(pos.i, pos.j) for pos in get_guard_positions(map=map, guard=guard)]
    distinct_guard_positions = list(set(guard_positions))
    guard_position_sum = len(distinct_guard_positions)

    return guard_position_sum


def main(input_path: str, guard: str) -> None:

    map = read_map(input_path=input_path)
    guard_position_sum = sum_distinct_guard_positions(map=map, guard=guard)
    print(guard_position_sum)


if __name__ == "__main__":
    main("day06/inputs/input.txt", guard="^")