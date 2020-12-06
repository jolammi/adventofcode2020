import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read()
        data = data.split("\n\n")  # separate documents to their own lists
        data = [i.replace("\n", " ") for i in data]  # remove newlines
        data = [i.split(" ") for i in data]  # split to sublists on spaces
        data = [[i.split(":") for i in document] for document in data]  # split sublists by ":"
        data = [{lst[0]: lst[1] for lst in document} for document in data]  # construct  dicts from sub-sublists
    return data


def parse_passports(data):
    valid = 0
    for dic in data:
        needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        if needed_keys.issubset(set(dic.keys())):
            valid += 1
    return valid


if __name__ == "__main__":
    try:
        data = read_data()
        valid = parse_passports(data)
        print(f"There are {valid} valid passports in the data.")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
