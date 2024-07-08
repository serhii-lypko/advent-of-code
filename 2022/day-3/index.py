import os
from functools import reduce


def read_input_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "input.txt")

    with open(file_path, "r") as file:
        lines = file.readlines()

    return lines

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --


LOWERCASE_PRIORITY_BASELINE_ASCII = 97
UPPERRCASE_PRIORITY_BASELINE_ASCII = 65

LOWERCASE_PRIORITY_BASELINE = 1
UPPERRCASE_PRIORITY_BASELINE = 27


def get_type_symbol_priority(symbol):
    ascii_code = ord(symbol)

    if symbol.isupper():
        return ascii_code - UPPERRCASE_PRIORITY_BASELINE_ASCII + UPPERRCASE_PRIORITY_BASELINE
    else:
        return ascii_code - LOWERCASE_PRIORITY_BASELINE_ASCII + LOWERCASE_PRIORITY_BASELINE


# -- -- -- -- -- -- -- -- -- Part 1 -- -- -- -- -- -- -- -- --

def get_common_type_symbol(items_string):
    midpoint = len(items_string) // 2

    # -- -- Using sorting & two pointers -- --

    left_list = sorted(items_string[:midpoint])
    right_list = sorted(items_string[midpoint:])

    l = len(left_list)

    left_pointer = 0
    right_pointer = 0

    while left_pointer < l or right_pointer < l:
        left_el = left_list[left_pointer]
        right_el = right_list[right_pointer]

        if left_el == right_el:
            return left_el
        elif left_el < right_el:
            left_pointer += 1
        else:
            right_pointer += 1

    # -- -- Using sets -- --

    # left = set(items_string[:midpoint])
    # right = set(items_string[midpoint:])

    # (smaller, bigger) = (left, right) if len(
    #     left) < len(right) else (right, left)

    # for type_symbol in smaller:
    #     if type_symbol in bigger:
    #         type_symbol

# 7763


# -- -- -- -- -- -- -- -- -- Part 2 -- -- -- -- -- -- -- -- --

def split_groups_by_three():
    lines = read_input_file()

    grouped_lines = []

    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        group = [line.strip() for line in group]
        grouped_lines.append(group)

    print(grouped_lines)


def main():
    # common_type_symbol = get_common_type_symbol(
    #     "WVHGHwddqSsNjsjwqVvdwZRCbcJcZTCcsZbLcJJsCZ")

    # file_data = read_input_file()
    # res = reduce(lambda total, curr: total +
    #              get_type_symbol_priority(get_common_type_symbol(curr)),  file_data, 0)

    groups = split_groups_by_three()
    # print(groups)


main()
