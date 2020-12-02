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
        occurrences = row_data["password"].count(row_data["letter"])
        if (row_data["min_occurrences"] <= occurrences <= row_data["max_occurrences"]):
            num_correct += 1

    return num_correct

def _split_to_rows(data):
    for row in data:
        match = regex.match(row)
        row_data = {
            "min_occurrences": int(match.group(1)),
            "max_occurrences": int(match.group(2)),
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
