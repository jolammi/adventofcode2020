import traceback
import itertools
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
        mem_adress_list = list(format(int(matches.group(1)), "036b"))
        mask = list(self.mask)
        for index, (mem_adress_bit, mask_bit) in enumerate(zip(mem_adress_list, mask)):
            if mask_bit == "1":
                mem_adress_list[index] = "1"
            if mask_bit == "0":
                pass  # just a reminder for no operation on 0
            if mask_bit == "X":
                mem_adress_list[index] = "X"
        for address in self._parse_mem_adresses(mem_adress_list):
            self.memory[address] = int(matches.group(2))

    def _parse_mem_adresses(self, mem_adress_list):
        floating_indexes = [i for i, x in enumerate(mem_adress_list) if x == "X"]
        bits = list(itertools.product([0, 1], repeat=mem_adress_list.count("X")))
        for bit_tuple in bits:
            mem_adress_copy = mem_adress_list.copy()
            for bit_char, floating_index in zip(bit_tuple, floating_indexes):
                mem_adress_copy[floating_index] = str(bit_char)
            yield "".join(mem_adress_copy)


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
        assert values_sum == 4254673508445
        print(f"The sum of all values left in memory after completion is {values_sum}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
