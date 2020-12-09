import traceback
import itertools
WINDOW_SIZE = 25


def read_data():
    with open("input.txt", "r") as handle:
        data = [int(i.strip("\n")) for i in handle.readlines()]
    return data


def parse_first_faulty_number(data):
    for index in range(WINDOW_SIZE, len(data)):
        window = data[index - WINDOW_SIZE: index]
        pairs = [pair for pair in itertools.combinations(window, 2) if sum(pair) == data[index]]
        if not pairs:
            return data[index]


if __name__ == "__main__":
    try:
        data = read_data()
        first_faulty = parse_first_faulty_number(data)
        assert first_faulty == 177777905
        print(f"The first number that does not follow the rule is {first_faulty}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
