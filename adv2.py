import re
from collections import Counter, defaultdict
from enum import Enum


class Cubes(Enum):
    red = "red"
    green = "green"
    blue = "blue"


RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


def main_adv2() -> int:
    with open("input_day2", mode="r", encoding="utf-8") as input_file:
        valid_counter = 0
        for line in input_file:
            is_valid = True
            line = line.replace("Game ", "")
            line_split = line.split(":")
            game_num = int(line_split[0])

            throws = line_split[1].split(";")
            for throw in throws:
                regex = re.compile(r"(\d+\s)(red|green|blue)")
                match = regex.findall(throw)

                counter = Counter()
                for el in match:
                    type_ob = Cubes(el[1])
                    quantity = int(el[0])
                    counter.update({type_ob: quantity})
                if counter[Cubes.green] > GREEN_CUBES:
                    is_valid = False
                    break
                if counter[Cubes.red] > RED_CUBES:
                    is_valid = False
                    break
                if counter[Cubes.blue] > BLUE_CUBES:
                    is_valid = False
                    break

            if is_valid:
                valid_counter += game_num
        return valid_counter


def main_adv2_part2(file: str) -> int:
    with open(file, mode="r", encoding="utf-8") as input_file:
        sums = 0
        for line in input_file:
            line = line.replace("Game ", "")
            line_split = line.split(":")

            throws = line_split[1].split(";")
            max_val = defaultdict(int)
            for throw in throws:
                regex = re.compile(r"(\d+\s)(red|green|blue)")
                match = regex.findall(throw)

                for el in match:
                    type_ob = Cubes(el[1])
                    quantity = int(el[0])
                    max_val[type_ob] = max(quantity, max_val[type_ob])
                multi = 1
            for key, val in max_val.items():
                multi *= val
            sums += multi
        return sums


if __name__ == "__main__":
    print("Adv day 2 valid:", main_adv2())
    print("Adv day 2 part 2:", main_adv2_part2("input_day2"))
    print("Adv day 2 part 2 test:", main_adv2_part2("input_2_test") == 2286, main_adv2_part2("input_2_test"),
          "should be 2286")
