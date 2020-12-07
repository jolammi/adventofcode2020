import traceback

ROWS = 128
ROW_DEPTH = 7
SEAT_DEPTH = 3
COLUMNS = 8


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.readlines()
        data = [i.strip("\n") for i in data]
        return data


def parse_highest_index(data):
    biggest = 0
    for bp_code in data:
        row_number = parse_number_from_instructions(
            chars=bp_code[:ROW_DEPTH],
            min_index=0,
            max_index=ROWS - 1,
            index_range=ROWS,
            lower="F",
            upper="B")
        seat = parse_number_from_instructions(
            chars=bp_code[ROW_DEPTH:],
            min_index=0,
            max_index=COLUMNS - 1,
            index_range=COLUMNS,
            lower="L",
            upper="R")
        index = row_number * 8 + seat
        if index > biggest:
            biggest = index
    return(biggest)


def parse_number_from_instructions(chars, min_index, max_index, index_range, lower, upper):
    num_min = min_index
    num_max = max_index  # zero-based indexing
    num_range = index_range

    for char in chars:
        if char == lower:
            num_max = num_max - num_range/2
            num_range = num_range / 2
        elif char == upper:
            num_min = num_min + num_range/2
            num_range = num_range / 2

    if num_max == num_min:
        return int(num_max)
    else:
        raise Exception("Parsing was unsuccessful, please fix")


if __name__ == "__main__":
    try:
        data = read_data()
        highest = parse_highest_index(data)
        print(f"The highest index in the data is {highest}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
