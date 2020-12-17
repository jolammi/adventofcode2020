# TODO finish puzzle2
import traceback
import re
import copy

def read_data():
    with open("input_.txt", "r") as handle:
        data = handle.read()
        data = data.split(("\n\n"))
        rules_list = data.pop(0).split("\n")
        rules = {}
        for row in rules_list:
            m = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", row)
            rules[m.group(1)] = [(int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))]
            # rules[m.group(1)] = [[int(i) for i in minmax_tuple] for minmax_tuple in rules[m.group(1)]]
        # print(rules)
        my_ticket = [int(i) for i in data.pop(0).replace("your ticket:\n", "").split(",")]
        # print(my_ticket)
        nearby_tickets = data.pop(0).replace("nearby tickets:\n", "").split("\n")
        nearby_tickets = [row.split(",") for row in nearby_tickets]
        nearby_tickets = [[int(i) for i in row] for row in nearby_tickets]
        # print(nearby_tickets)

        return {"rules": rules, "my_ticket": my_ticket, "nearby_tickets": nearby_tickets}


def parse_legit_tickets(data_dict):
    rules = data_dict["rules"]
    nearby_tickets = data_dict["nearby_tickets"]
    err_rate = 0
    only_legit = copy.deepcopy(nearby_tickets)
    for row in nearby_tickets:
        for num in row:
            num_results = []
            for rule in rules.values():
                if not ((rule[0][0] <= num <= rule[0][1]) or (rule[1][0] <= num <= rule[1][1])):
                    num_results.append(False)
                else:
                    num_results.append(True)
            if not any(num_results):
                err_rate += num
                only_legit.remove(row)

    only_legit.append(data_dict["my_ticket"])
    print(only_legit)
    return err_rate


def parse_correct_order(data_dict, legit_tickets):
    pass


if __name__ == "__main__":
    try:
        data_dict = read_data()
        legit_tickets = parse_legit_tickets(data_dict)
        order = parse_correct_order(data_dict, legit_tickets)
        # assert num_spoken == 610
        print(f"The ticket scanning error rate is {error_rate}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
