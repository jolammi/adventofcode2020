import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read()
        data = data.split("\n\n")  # separate documents to their own lists
        data = [i.replace("\n", "") for i in data]  # remove newlines
    return data


def parse_counts(data):
    counts = []
    for chars in data:
        tmp = chars
        for char in chars:
            tmp = tmp.replace(char, "")
            tmp = char + tmp
        counts.append(len(tmp))
    return counts


if __name__ == "__main__":
    try:
        data = read_data()
        counts = parse_counts(data)
        print(f"The sum of the counts is {sum(counts)}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
