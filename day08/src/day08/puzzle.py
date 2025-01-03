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


def check_node_on_map(node: Node, map_size: tuple[int, int]) -> bool:

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


def get_antinodes_from_antenna_pair(antennas: tuple[Node, Node], step: tuple, map_size: tuple[int, int]) -> list[tuple]:

    antinode_0 = Node(antennas[0].i - step[0], antennas[0].j - step[1])
    antinode_1 = Node(antennas[1].i + step[0], antennas[1].j + step[1])

    # check the antinodes are on the map
    valid_antinodes = []
    for antinode in (antinode_0, antinode_1):
        antinode_on_map = check_node_on_map(node=antinode, map_size=map_size)
        if antinode_on_map:
            valid_antinodes.append((antinode.i, antinode.j))

    return valid_antinodes


def get_antenna_antinodes(map: List[List], harmonics: bool = False) -> set[tuple]:

    map_height = len(map)
    map_width = len(map[0])

    # locate the antennas
    antennas_d = get_antenna_nodes_and_frequencies(map=map)

    antinodes = set()
    # get the possible resonant antenna pairs
    for antenna_nodes in antennas_d.values():
        antenna_pairs = itertools.combinations(iterable=antenna_nodes, r=2)

        for resonant_pair in list(antenna_pairs):

            # calculate the i, j distances between the antennas in a resonant pair
            di = resonant_pair[1].i - resonant_pair[0].i
            dj = resonant_pair[1].j - resonant_pair[0].j

            if not harmonics:
                # find the antinodes one step away from each antenna (in the appropriate directions)
                pair_antinodes = get_antinodes_from_antenna_pair(antennas=resonant_pair, step=(di,dj), map_size=(map_height, map_width))
                antinodes.update(pair_antinodes)

            else:
                # add the resonant attennas as antinodes
                antinodes.update([(antenna.i, antenna.j) for antenna in resonant_pair])
                antinodes_found = True

                # initialise step_size
                n = 1
                
                # while antinodes are found, increase step size to find new antinodes (further from the antennas)
                while antinodes_found:
                    pair_antinodes = get_antinodes_from_antenna_pair(antennas=resonant_pair, step=(n*di, n*dj), map_size=(map_height, map_width))
                    if len(pair_antinodes) > 0:
                        antinodes.update(pair_antinodes)
                    else:
                        antinodes_found = False
                    n += 1

    return antinodes
 

def main(input_path: str) -> None:
    map = read_map(input_path=input_path)

    # part 1
    antinodes = get_antenna_antinodes(map=map)
    antinode_count = len(antinodes)
    print(antinode_count)

    # part 2
    harmonic_antinodes = get_antenna_antinodes(map=map, harmonics=True)
    harmonic_antinode_count = len(harmonic_antinodes)
    print(harmonic_antinode_count)
    

if __name__ == "__main__":
    main(input_path="day08/inputs/input.txt")

