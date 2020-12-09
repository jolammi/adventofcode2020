import traceback
# from functools import reduce


def read_data():
    """
    Parses the input file so that only the colors and numbers are left.
    The rows containing data about the shiny gold bag and the bags that contain no other bags is scrapped.
    """
    with open("input_.txt", "r") as handle:
        data = [i.strip("\n") for i in handle.readlines()]
    data = [i.replace(" bags contain ", ":") for i in data]
    data = [i.replace("bags", "") for i in data]
    data = [i.replace("bag", "") for i in data]
    data = [i.strip(" .") for i in data]
    data = [i.replace(" , ", ",") for i in data]
    data = [i.replace(" ", "") for i in data]
    data = [i.split(":") for i in data]
    final_list = []
    for lst in data:
        sublist_split = lst[1].split(",")
        for idx, chars in enumerate(sublist_split):
            chars = chars[:1] + "_" + chars[1:]
            sublist_split[idx] = chars
        final_list.append([lst[0], sublist_split])
    data = final_list.copy()
    for lst in data:
        if "n_oother" in lst[1]:
            lst[1] = 1
        # we aren't interested in what the shint gold bag contains or bags that contain no other bags
        # for chars in list(data):
        #     if ("shiny_gold" in chars) or ("no other" in chars):
        #         while chars in data:
        #             data.remove(chars)
        # data = [" ".join(i) for i in data]replace
    print(data)
    return data


def parse_bags(data):
    handle = []
    for i in data:
        if type(i[1]) == int:
            handle.append(i)
    print(handle)
    for j in handle:
        for i in data:
            if j in i[1]:
                pass
    # bags = 0
    # # total_list = []
    # # for lst in data:
    # #     if lst[0] == "shiny gold":
    # #         for i in lst[1:]:
    # #             for j in range(int(i.split(" ")[0])):
    # #                 total_list.append(" ".join(i.split(" ")[1:]))
    # # while True:
    # #     for chars in list(total_list):
    # #         for lst in data:
    # #             if lst[0] == chars:
    # #                 if lst[1] == "no other":
    # #                     total_list = [i.replace(lst[0], str(1)) for i in total_list]
    # #                     continue
    # #                 for i in lst[1:]:
    # #                     for j in range(int(i.split(" ")[0])):
    # #                         total_list.append(" ".join(i.split(" ")[1:]))

    #     print(total_list)
    #     input()

    # # for
    # print(total_list)
    # iterable = ""
    # to_replace = []
    # for lst in list(data):
    #     if "no other" in lst:
    #         lst[1] = 1
    #         to_replace.append((lst[0], lst[1]))
    #         data.remove(lst)
    # while to_replace:
    #     color, value = to_replace.pop()
    #     for idx, lst in enumerate(list(data)):
    #         for idx2, chars in enumerate(list(lst)):
    #             print(data)
    #             if color in str(chars):

    #                 print(color)
    #                 num = chars.split(" ")[0]
    #                 print(num)
    #                 print(value)
    #                 data[idx][idx2] = int(num)*int(value)
                # lst[1] = 0
                # to_replace.append((lst[0], lst[1]))

    # iter_list = [[1, "shiny gold"]]
    # found = []
    # while iter_list:
    #     to_find = iter_list.pop()
    #     for lst in data:
    #         if lst[0] == to_find[1]:
    #             if lst[1] == "no other":
    #                 continue
    #             parse = lst[1:]
    #             for i in parse:
    #                 i = i.split(" ")
    #                 if i not in found and i not in iter_list:
    #                     iter_list.append((i[0], " ".join(i[1:])))
    #     found.append(to_find)
    # print(iter_list)
    # print(found)

    # colors = 0
    # iterate_list = ["shiny gold"]
    # already_iterated = []
    # while iterate_list:
    #     iterable = iterate_list.pop()
    #     already_iterated.append(iterable)
    #     rows = [s for s in data if iterable in s]
    #     for row in rows:
    #         color = " ".join(row.split(" ")[:2])
    #         if color not in already_iterated and color not in iterate_list:
    #             iterate_list.append(color)
    #             colors += 1
    # assert bags == 36
    # return bags


if __name__ == "__main__":
    try:
        data = read_data()
        bags = parse_bags(data)
        # print(f"The amount of bags required inside the shiny gold bag is {bags}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
