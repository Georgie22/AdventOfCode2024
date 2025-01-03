import itertools
from dataclasses import dataclass
from typing import List


@dataclass
class Node():
    i: int      # row
    j: int      # column


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        lines = file.readlines()
    
    return lines


def read_map(input_path:str) -> list[list]:

    map_rows = read_file_lines(input_path=input_path)

    map = []
    for row in map_rows:
        # remove new line element and take out of the list .split() creates
        row_string = row.split()[0]
        # separate row string into the individual characters (that make up the row positions)
        row_elements = [elem for elem in row_string]
        map.append(row_elements)

    return map


def check_node_on_map(node: Node, map_size: tuple) -> bool:

    if (node.i >= 0 and node.i < map_size[0] and node.j >= 0 and node.j < map_size[1]):
        return True
    else:
        return False


def get_antenna_nodes_and_frequencies(map: List[List]) -> dict[str, list[Node]]: 

    map_height = len(map)
    map_width = len(map[0])

    antennas = {}
    for i in range(map_height):
        for j in range(map_width):
            map_element = map[i][j]

            if map_element != ".":

                # map_element = antenna frequency. Store frequency with list of nodes as a dictionary pair. {frequency: [Node]}
                if map_element in antennas:
                    antennas[map_element].append(Node(i, j))
                else:
                    antennas[map_element] = [Node(i, j)]

    return antennas


def get_antenna_antinodes(map: List[List]) -> set[tuple]:

    map_height = len(map)
    map_width = len(map[0])
    antennas = get_antenna_nodes_and_frequencies(map=map)
    
    antinodes = set()
    # for each antenna frequency
    for antenna_nodes in antennas.values():

        # get the possible resonant antenna pairs
        antenna_pairs = itertools.combinations(iterable=antenna_nodes, r=2)

        # for each resonant antenna pair determine the di, dj components and calculate the antinodes
        for pair in list(antenna_pairs):
            
            di = pair[1].i - pair[0].i
            dj = pair[1].j - pair[0].j
            antinode_0 = Node(pair[0].i - di, pair[0].j - dj)
            antinode_1 = Node(pair[1].i + di, pair[1].j + dj)

            # check the antinodes are on the map
            for antinode in (antinode_0, antinode_1):
                antinode_on_map = check_node_on_map(node=antinode, map_size=(map_height, map_width))
                if antinode_on_map:
                    antinodes.add((antinode.i, antinode.j))

    return antinodes


def main(input_path: str) -> None:

    # Part 1
    map = read_map(input_path=input_path)
    antinodes = get_antenna_antinodes(map=map)
    antinode_count = len(antinodes)
    print(antinode_count)
    

if __name__ == "__main__":
    main(input_path="day08/inputs/input.txt")

