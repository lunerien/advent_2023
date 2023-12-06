import re
from collections import Counter
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
            print(line)
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
                    if game_num == 80:
                        print(type_ob, quantity)
                    counter.update({type_ob: quantity})
                print(counter.most_common())

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
            print("is valid: ", is_valid)
            print("------------------------")
        return valid_counter


if __name__ == "__main__":
    print("Adv day 2 valid: ", main_adv2())
