"""
This is horrible. Yeah, I know it is. After three hours of pure madness I just had to give up
doing anything elegant and just brute-force the solution.
"""
import traceback


def read_data():
    """
    Parses the input file so that only the colors and numbers are left.
    The rows containing data about the shiny gold bag and the bags that contain no other bags is scrapped.
    """
    with open("input.txt", "r") as handle:
        data = [i.strip("\n") for i in handle.readlines()]
        data = [i.replace("bags contain ", ", ") for i in data]
        data = [i.replace("bags", "") for i in data]
        data = [i.replace("bag", "") for i in data]
        # data = [i.strip(" .") for i in data]
        # data = [i.split(" , ") for i in data]
        # we aren't interested in what the shint gold bag contains or bags that contain no other bags
        for chars in list(data):
            if ("shiny_gold" in chars) or ("no other" in chars):
                while chars in data:
                    data.remove(chars)
        # data = [" ".join(i) for i in data]
    return data


def parse_bags(data):
    colors = 0
    iterate_list = ["shiny gold"]
    already_iterated = []
    while iterate_list:
        iterable = iterate_list.pop()
        already_iterated.append(iterable)
        rows = [s for s in data if iterable in s]
        for row in rows:
            color = " ".join(row.split(" ")[:2])
            if color not in already_iterated and color not in iterate_list:
                iterate_list.append(color)
                colors += 1
    assert colors == 316
    return colors


if __name__ == "__main__":
    try:
        data = read_data()
        colors = parse_bags(data)
        print(f"The amount of colors that can contain a shiny gold bag is {colors}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
