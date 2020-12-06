import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read()
        data = data.strip().split("\n\n")  # separate documents to their own lists
        data = [i.split("\n") for i in data]  # remove newlines
    return data


def parse_counts(data):
    counts = []
    for group in data:
        all_str = "".join(group)  # join all answers to a common string which will be iterated
        count_all_yes = 0
        handled = []  # create a list to exclude already handled characters from iteration
        for char in all_str:
            # check if all persons have answered yes to a question but the question hasn't been handled yet
            if (all(char in lst for lst in group) and (char not in handled)):
                handled.append(char)
                count_all_yes += 1
        counts.append(count_all_yes)
    return counts


if __name__ == "__main__":
    try:
        data = read_data()
        counts = parse_counts(data)
        print(f"The sum of the counts is {sum(counts)}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
