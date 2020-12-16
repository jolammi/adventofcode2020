import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read().strip("\n").split(",")
        data = [int(i) for i in data]
    return data


def get_wanted_spoken_number(data, num_range):
    data.extend([None]*(num_range-len(data)))
    for index, value in enumerate(data):
        if value is not None:
            continue
        num = data[index - 1]
        appears_so_far = [i for i, x in enumerate(data[:index-1]) if x == num]
        if appears_so_far == []:
            data[index] = 0
            continue
        data[index] = index - 1 - appears_so_far[-1]
    return data[2019]


if __name__ == "__main__":
    try:
        data = read_data()
        num_spoken = get_wanted_spoken_number(data, 2020)
        assert num_spoken == 610
        print(f"The 2020th number spoken is {num_spoken}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
