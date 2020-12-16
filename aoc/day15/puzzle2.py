import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read().strip("\n").split(",")
        data = [int(i) for i in data]
    return data


def get_wanted_spoken_number(data, num_range):
    data.extend([None]*(num_range-len(data)))
    num_infos = {}
    for index, value in enumerate(data):
        if value is not None:
            num_infos[value] = [index]
            continue
        num = data[index - 1]
        appears_so_far = num_infos[num]
        if len(appears_so_far) == 1:
            data[index] = 0
            num_infos[0].append(index)
            continue
        this = index - 1 - appears_so_far[-2]
        data[index] = this
        try:
            num_infos[this].append(index)
        except KeyError:
            num_infos[this] = [index]
    return(data[num_range-1])


if __name__ == "__main__":
    try:
        print("This loop may run for a little while, why don't you grab a glass of water or something?")
        data = read_data()
        num_spoken = get_wanted_spoken_number(data, 30000000)
        assert num_spoken == 1407
        print(f"The 30000000th number spoken is {num_spoken}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
