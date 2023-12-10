from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict


class File:
    @dataclass
    class Element:
        class Type(Enum):
            NUM = 1,
            CHAR = 2

        type_of: Type
        index_start: int
        index_end: int
        value: str

    @dataclass
    class Line:
        number: int
        numbers: List
        symbols: Dict

    def __init__(self, file_name: str):
        self.lines = []
        with open(file_name, mode="r", encoding="utf-8") as file_to_read:
            for index, line in enumerate(file_to_read):
                numbers, symbols = self._process_line(line)
                print("line: ", index)
                print(numbers)
                print(symbols)
                self.lines.append(self.Line(number=index, numbers=numbers, symbols=symbols))
        print(self.lines)

    def _process_line(self, str_line):
        local_numbers = []
        local_symbols = {}
        act_elem = ""
        for index, el in enumerate(str_line):
            try:
                int(el)
                act_elem += el
            except ValueError:
                if act_elem != "":
                    local_numbers.append(
                        self._save_num(act_elem, index - 1))
                    act_elem = ""
                if el != "." and el != "\n":
                    local_symbols[index] = self._save_symbol(index)
        return local_numbers, local_symbols

    def _save_num(self, buff: str, loc: int):
        print(" -", buff, loc - len(buff) + 1, loc)
        return self.Element(type_of=self.Element.Type.NUM,
                            index_start=loc - len(buff),
                            index_end=loc,
                            value=buff)

    def _save_symbol(self, index):
        print(" - symbol", index)
        return self.Element(type_of=self.Element.Type.CHAR,
                            index_start=index,
                            index_end=index,
                            value="#")


def main_day3(file: str):
    sum = 0
    array_of_nums = []
    array_of_signs = []
    processed_file = File(file)
    return sum


if __name__ == "__main__":
    assert (val := main_day3("input_day3_test")) == 4361, f"Return should be 4361 but was {val}"
