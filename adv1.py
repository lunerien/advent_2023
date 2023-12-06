import re
from typing import List
from enum import Enum


def main_adv1() -> int:
    with open("input_adv1", encoding="utf-8", mode="r") as input_file:
        sum_out = 0
        for line in input_file.readlines():
            res = extract_numbers_from_line(line)
            sum_out += res
        #     if len(arr) == 0:
        #         raise ValueError
        #     out_val = int(str(arr[0]) + str(arr[len(arr) - 1]))
        #     sum_out += out_val
        #     print(line, arr, "sum", out_val, "end_sum", sum_out)
        return sum_out


def extract_numbers_from_line(line: str) -> int:
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    regex_first = re.compile(r".*?(one|two|three|four|five|six|seven|eight|nine|\d).*")
    regex_last = re.compile(r".*(one|two|three|four|five|six|seven|eight|nine|\d).*?")
    match_first = regex_first.match(line).groups()[0]
    match_last = regex_last.match(line).groups()[0]
    try:
        num_first = digits[match_first]
    except KeyError:
        num_first = int(match_first)

    try:
        num_last = digits[match_last]
    except KeyError:
        num_last = int(match_last)

    return int(str(num_first) + str(num_last))


if __name__ == "__main__":
    print("adv1 out sum:", main_adv1())
