import traceback
import copy


def read_data():
    with open("input.txt", "r") as handle:
        data = [i.strip("\n") for i in handle.readlines()]
    data = [i.split(" ") for i in data]
    for lst in data:
        lst[1] = int(lst[1])
    return data


def iterate_change(data):
    for idx in range(len(data)):
        prog_input = copy.deepcopy(data)
        if prog_input[idx][0] == "jmp":
            prog_input[idx][0] = "nop"
        elif prog_input[idx][0] == "nop":
            prog_input[idx][0] = "jmp"
        retval = run_program(prog_input)
        if retval:
            return retval


def run_program(data):
    accumulator = 0
    idx = 0
    done_action_indexes = set()
    while idx not in done_action_indexes:
        done_action_indexes.add(idx)
        try:
            action = data[idx][0]
            if action == "acc":
                accumulator += data[idx][1]
                idx += 1
            elif action == "jmp":
                idx += data[idx][1]
            elif action == "nop":
                idx += 1
        except IndexError:
            return accumulator
    return None


if __name__ == "__main__":
    try:
        data = read_data()
        acc_val = iterate_change(data)
        assert acc_val == 2092
        print(f"The value of the accumulator when the program terminater normally is {acc_val}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
