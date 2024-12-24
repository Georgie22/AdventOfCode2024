import operator
import itertools

from typing import List


def read_file_lines(input_path: str) -> list[str]:

    with open(input_path, "r") as file:
        lines = file.readlines()
    
    return lines


def read_calibration_equations(input_path: str) -> list[tuple]:

    equations = read_file_lines(input_path=input_path)

    calibration_equations = []
    for equation in equations:
        
        # split terms in equation by ":" (result term : terms to apply operations to)
        terms = equation.split(":")
        result_term = int(terms[0])
        operation_terms = [int(t) for t in terms[1].split()]

        # store equation terms in a tuple. (result_term, [operation_terms])
        calibration_equations.append((result_term, operation_terms))
    
    return calibration_equations


def check_operation_sequence(terms: List, operation_sequence: List) -> int:

    accumulator = terms[0]
    for f, term in zip(operation_sequence, terms[1:]):
        accumulator = f(accumulator, term)      # operation performed with previous output and next term in iterable

    return accumulator


def get_calibrated_result(calibration_equation: tuple, operators: List) -> int:

    result = calibration_equation[0]
    terms = calibration_equation[1]

    # find the possible operation sequences
    possible_operations = itertools.product(operators, repeat=len(terms)-1)

    # for each operation sequence check if the equation calibrates (i.e equals the result term). If yes return the result term.
    for operation_sequence in possible_operations:
        accumulator = check_operation_sequence(terms=terms, operation_sequence=operation_sequence)
        if accumulator == result:
            return result
    
    # if the equation is not calibrated return zero
    return 0
            

def get_total_calibration_result(calibration_equations: List[tuple], operators: List) -> int:

    """
    Return the sum of the result terms for calibrated equations.
    """

    calibration_results = []

    for equation in calibration_equations:
        result = get_calibrated_result(calibration_equation=equation, operators=operators)
        calibration_results.append(result)

    total_calibration_result = sum(calibration_results)

    return total_calibration_result


def main(input_path: str) -> None:

    calibration_equations = read_calibration_equations(input_path=input_path)

    # Part 1
    total_calibration_result = get_total_calibration_result(calibration_equations=calibration_equations, operators=[operator.mul, operator.add])
    print(total_calibration_result)


if __name__ == "__main__":
    main(input_path="day07/inputs/input.txt")
