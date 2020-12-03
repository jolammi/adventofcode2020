import re
import traceback
LEFT = 3
DOWN = 1
regex = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-zA-Z]+)")


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.readlines()
        data = [i.strip("\n") for i in data]
    return data


def parse_trees(data):
    # Indexes are zero-based, but, if the row has for example 11 characters,
    # the 11th index, is the first character of the next list. So len(data[0]).
    row_width = len(data[0])
    index = 0
    trees = 0
    for row in data[::DOWN]:
        if is_tree(row[index]):
            trees += 1
        index = (index + LEFT) % (row_width)
    return trees


def all_rows_equal_length(data):
    lengths = [len(i) for i in data]
    return lengths[:-1] == lengths[1:]


def is_tree(char):
    return char == "#"


if __name__ == "__main__":
    try:
        data = read_data()
        if not all_rows_equal_length(data):
            raise Exception("Rows are not same length. Fix the logic.")
        trees = parse_trees(data)

        print(f"The number of trees encountered is {trees}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
