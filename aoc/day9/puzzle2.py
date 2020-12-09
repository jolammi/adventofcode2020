import traceback
import itertools
WANTED_NUMBER = 177777905


def read_data():
    with open("input.txt", "r") as handle:
        data = [int(i.strip("\n")) for i in handle.readlines()]
    return data


def parse_encryption_weakness(data):
    sum_range_list = parse_sum_range(data)
    smallest, biggest = parse_smallest_and_biggest(sum_range_list)
    return smallest+biggest


def parse_smallest_and_biggest(sum_range):
    return min(sum_range), max(sum_range)


def parse_sum_range(data):
    for WINDOW_SIZE in range(len(data)):
        for index in range(WINDOW_SIZE, len(data)):
            window = data[index - WINDOW_SIZE: index]
            combination = [combo for combo in itertools.combinations(window, WINDOW_SIZE)
                           if sum(combo) == WANTED_NUMBER]
            if combination:
                combination = combination.pop()
                if len(combination) > 1:
                    return(combination)


if __name__ == "__main__":
    try:
        data = read_data()
        encr_weakness = parse_encryption_weakness(data)
        assert encr_weakness == 23463012
        print(f"The encryption weakness is {encr_weakness}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
