import re
import traceback
regex = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-zA-Z]+)")


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.readlines()
        data = [i.strip("\n") for i in data]
    return data


def parse_data(data):
    num_correct = 0
    for row_data in _split_to_rows(data):
        password = row_data["password"]
        letter = row_data["letter"]
        # Below the XOR operator: A or B but not both
        if ((password[row_data["first_index"]] == letter) is not
                (password[row_data["second_index"]] == letter)):
            num_correct += 1

    return num_correct


def _split_to_rows(data):
    for row in data:
        match = regex.match(row)
        row_data = {
            "first_index": int(match.group(1)) - 1,  # substract 1 to use zero based indexes
            "second_index": int(match.group(2)) - 1,  # substract 1 to use zero based indexes
            "letter": match.group(3),
            "password": match.group(4),
        }
        yield row_data


if __name__ == "__main__":
    try:
        data = read_data()
        correct = parse_data(data)
        print(f"The number of correct passwords in the input file is {str(correct)}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
