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
    plane = []
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
        plane.append((row_number, seat))
    return(parse_own_seat(plane))


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


def parse_own_seat(plane):
    # plane list has elements in fomat (row_number, seat_number)
    empty_seats = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            if (i, j) not in plane:
                # extract seats that are missing from the plane list to an own list
                empty_seats.append((i, j))
    own_seat = empty_seats.copy()
    for seat in empty_seats:
        # check if the next or previous seat is missing from the plane seats list; if so, the seat can be discarded
        if ((seat[0] + 1 not in [row for row, _ in plane]) or (seat[0] - 1 not in [row for row, _ in plane])):
            own_seat.remove(seat)
    row, seat = own_seat.pop()
    return row * 8 + seat


if __name__ == "__main__":
    try:
        data = read_data()
        seat_id = parse_highest_index(data)
        print(f"The ID of my seat is {seat_id}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
