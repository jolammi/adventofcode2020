import traceback
import re


class Program:
    def __init__(self, data):
        self.data = data
        self.current_mask = None
        self.memory = {}

    def run_program(self):
        for row in self.data:
            instruction, matches = self.parse_instruction(row)
            {
                "update_mask": self.update_mask,
                "save_value": self.save_value
            }.get(instruction)(matches)

    def parse_instruction(self, row):
        regexes = [
            (r"mask = ([10X]+)", "update_mask"),
            (r"mem\[(\d+)\] = (\d+)", "save_value"),
        ]
        for regex in regexes:
            m = re.match(regex[0], row)
            if m:
                return regex[1], m

    def update_mask(self, matches):
        self.mask = matches.group(1)

    def save_value(self, matches):
        # TODO: This would be way wiser to do with bitwise operations. Please implement.
        value_to_save = list(format(int(matches.group(2)), "036b"))
        mask = list(self.mask)
        for index, (value_bit, mask_bit) in enumerate(zip(value_to_save, mask)):
            if mask_bit == "1":
                value_to_save[index] = "1"
            if mask_bit == "0":
                value_to_save[index] = "0"
        self.memory[matches.group(1)] = int("".join(value_to_save), 2)


def read_data():
    with open("input.txt", "r") as handle:
        data = [i.strip("\n") for i in handle.readlines()]
    return data


if __name__ == "__main__":
    try:
        data = read_data()
        program = Program(data)
        program.run_program()
        values_sum = sum(program.memory.values())
        assert values_sum == 18630548206046
        print(f"The sum of all values left in memory after completion is {values_sum}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
