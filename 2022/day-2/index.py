import os
from functools import reduce


def read_input_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input.txt")

    with open(file_path, "r") as file:
        lines = file.readlines()

    return lines

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


"""
  A Y
  B X
  C Z
"""

# A -> Rock (1), B -> Paper (2), C -> Scissors (3) || -> Opponent
# X -> loose, Y -> draw, Z -> win


options = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
}


def process_line(total, line):
    opponent, player = line.split()

    return total + options[opponent][player]


def main():
    file_data = read_input_file()
    res = reduce(process_line, file_data, 0)

    print(res)


main()
