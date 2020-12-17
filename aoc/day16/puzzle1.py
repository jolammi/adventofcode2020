import traceback
import re

def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read()
        data = data.split(("\n\n"))
        rules_list = data.pop(0).split("\n")
        rules = {}
        for row in rules_list:
            m = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", row)
            rules[m.group(1)] = [(int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))]
        my_ticket = [int(i) for i in data.pop(0).replace("your ticket:\n", "").split(",")]
        nearby_tickets = data.pop(0).replace("nearby tickets:\n", "").split("\n")
        nearby_tickets = [row.split(",") for row in nearby_tickets]
        nearby_tickets = [[int(i) for i in row] for row in nearby_tickets]
        return {"rules": rules, "my_ticket": my_ticket, "nearby_tickets": nearby_tickets}


def parse_ticket_scanning_err_rate(data_dict):
    rules = data_dict["rules"]
    nearby_tickets = data_dict["nearby_tickets"]
    err_rate = 0
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

    return err_rate


if __name__ == "__main__":
    try:
        data_dict = read_data()
        error_rate = parse_ticket_scanning_err_rate(data_dict)
        assert error_rate == 24110
        print(f"The ticket scanning error rate is {error_rate}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
