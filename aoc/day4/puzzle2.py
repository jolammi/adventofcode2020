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
        if passport_is_valid(dic):
            valid += 1
    return valid


def passport_is_valid(dic):
    if passport_has_needed_fields(dic):
        return passport_fields_are_valid(dic)


def passport_has_needed_fields(dic):
    needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return needed_keys.issubset(set(dic.keys()))


def passport_fields_are_valid(dic):
    rules = {
        "byr": {
            "length": 4,
            "min": 1920,
            "max": 2002
        },
        "iyr": {
            "length": 4,
            "min": 2010,
            "max": 2020
        },
        "eyr": {
            "length": 4,
            "min": 2020,
            "max": 2030
        },
        "hgt": {
            "endings": ["cm", "in"],
            "in_min": 59,
            "in_max": 76,
            "cm_min": 150,
            "cm_max": 193
        },
        "hcl": {
            "firstchar": "#",
            "length": 7,
            "accepted": "abcdefghijklmnopqrstuvwxyz1234567890"
        },
        "ecl": {
            "accepted": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        },
        "pid": {
            "length": 9
        },
    }
    check_results = [
        year_is_valid("byr", dic, rules),
        year_is_valid("iyr", dic, rules),
        year_is_valid("eyr", dic, rules),
        hgt_is_valid(dic, rules),
        hcl_is_valid(dic, rules),
        ecl_is_valid(dic, rules),
        pid_is_valid(dic, rules),
    ]
    return(all(val is True for val in check_results))


def year_is_valid(field, dic, rules):
    val = dic[field]
    year_rules = rules[field]
    if not is_number(val):
        return False
    if len(val) != year_rules["length"]:
        return False
    if not year_rules["min"] <= int(val) <= year_rules["max"]:
        return False
    return True


def hgt_is_valid(dic, rules):
    hgt = dic["hgt"]
    hgt_rules = rules["hgt"]
    if not hgt.endswith(tuple(rules["hgt"]["endings"])):
        return False
    if (hgt.endswith("cm") and not hgt_rules["cm_min"] <= int(hgt.strip("cm")) <= hgt_rules["cm_max"]):
        return False
    if (hgt.endswith("in") and not hgt_rules["in_min"] <= int(hgt.strip("in")) <= hgt_rules["in_max"]):
        return False
    return True


def hcl_is_valid(dic, rules):
    hcl = dic["hcl"]
    hcl_rules = rules["hcl"]
    if not hcl.startswith(hcl_rules["firstchar"]):
        return False
    if not len(hcl) == 7:
        return False
    for char in hcl[1:]:
        if char not in list(hcl_rules["accepted"]):
            return False
    return True


def ecl_is_valid(dic, rules):
    ecl = dic["ecl"]
    if ecl not in rules["ecl"]["accepted"]:
        return False
    return True


def pid_is_valid(dic, rules):
    pid = dic["pid"]
    if len(pid) != rules["pid"]["length"]:
        return False
    for i in pid:
        if i not in list("1234567890"):
            return False
    return True


def is_number(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    try:
        data = read_data()
        valid = parse_passports(data)
        print(f"There are {valid} valid passports in the data.")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
