import os


def read_file_lines(input_path: str) -> list[str]:

    full_input_path = os.path.abspath(input_path)
    with open(full_input_path, "r") as file:
        return file.readlines()
    