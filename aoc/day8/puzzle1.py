import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = [i.strip("\n") for i in handle.readlines()]
    data = [i.split(" ") for i in data]
    for lst in data:
        lst[1] = int(lst[1])
    return data


def run_program(data):
    accumulator = 0
    idx = 0
    done_action_indexes = []
    while True:
        if idx in done_action_indexes:
            return accumulator
        else:
            done_action_indexes.append(idx)
        action = data[idx][0]
        if action == "acc":
            accumulator += data[idx][1]
            idx += 1
        elif action == "jmp":
            idx += data[idx][1]
        elif action == "nop":
            idx += 1


if __name__ == "__main__":
    try:
        data = read_data()
        acc_val = run_program(data)
        print(f"The value of the accumulator when starting the second round is {acc_val}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
