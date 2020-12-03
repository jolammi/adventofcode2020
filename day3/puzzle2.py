import traceback
from functools import reduce

RIGHT_AND_DOWN = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.readlines()
        data = [i.strip("\n") for i in data]
    return data


def parse_trees(data, right, down):
    # Indexes are zero-based, but, if the row has for example 11 characters,
    # the 11th index, is the first character of the next list. So len(data[0]).
    row_width = len(data[0])
    index = 0
    trees = 0
    for row in data[::down]:
        if is_tree(row[index]):
            trees += 1
        index = (index + right) % (row_width)
    return trees


def all_rows_equal_length(data):
    lengths = [len(i) for i in data]
    return lengths[:-1] == lengths[1:]


def is_tree(char):
    return char == "#"


if __name__ == "__main__":
    try:
        totals = []
        data = read_data()
        if not all_rows_equal_length(data):
            raise Exception("Rows are not same length. Fix the logic.")
        for right, down in RIGHT_AND_DOWN:
            totals.append(parse_trees(data, right, down))
            print(f"The number of trees encountered on loop {right} right, {down} down is {totals[-1]}")
        print(f"Answer to the queestion, multiplication of trees, is {reduce(lambda x, y: x*y, totals)}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
