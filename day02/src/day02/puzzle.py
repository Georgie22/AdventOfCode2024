from typing import List
from itertools import combinations


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        return file.readlines()
    

def get_reports(input_path: str) -> list[list[int]]:

    lines = read_file_lines(input_path=input_path)

    reports = []
    for line in lines:
        line_elements = line.split()
        report_line = [int(elem) for elem in line_elements]
        reports.append(report_line)

    return reports


def get_report_element_differences(report: List[int]) -> list[int]:

    beginning = report[:-1]
    end = report[1:]
    differences = [e_elem - b_elem for b_elem, e_elem in zip(beginning, end)]

    return differences


def check_safety(report: List[int]) -> bool:

    element_differences = get_report_element_differences(report=report)
    increasing = all(difference > 0 for difference in element_differences)
    decreasing = all(difference < 0 for difference in element_differences)
    in_bounds = all(1 <= abs(difference) < 4 for difference in element_differences)

    if increasing and in_bounds:
        return True
    elif decreasing and in_bounds:
        return True
    else:
        return False


def check_safety_with_dampner(report: List[int]) -> bool:

    safe = check_safety(report=report)
    if not safe:
        dampner_reports = combinations(report, len(report)-1)
        safe = any([check_safety(report=d_report) for d_report in dampner_reports])
    
    return safe


def calculate_safe_report_count(input_path: str, dampner: bool = False) -> int:

    reports = get_reports(input_path=input_path)
    safe_count = 0
    for report in reports:
        if dampner:
            safe = check_safety_with_dampner(report=report)
        else:
            safe = check_safety(report=report)
        if safe:
            safe_count += 1
    return safe_count


def main(input_path: str) -> None:

    # part 1
    safe_count = calculate_safe_report_count(input_path=input_path)
    print(safe_count)

    # part 2
    safe_count_with_dampner = calculate_safe_report_count(input_path=input_path, dampner=True)
    print(safe_count_with_dampner)


if __name__ == "__main__":
    main("day02/inputs/input.txt")
