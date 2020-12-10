"""
This solution is highly unoptimal. After spending hours and hours trying to figure it out, \
I am currently happy with the 10 second parsing on my gen8 i5 laptop.
"""
import traceback
import time


def read_data():
    with open("input.txt", "r") as handle:
        data = [i.strip("\n") for i in handle.readlines()]
    data = [i.replace(" bags contain ", ":") for i in data]
    data = [i.replace("bags", "") for i in data]
    data = [i.replace("bag", "") for i in data]
    data = [i.strip(" .") for i in data]
    data = [i.replace(" , ", ",") for i in data]
    data = [i.replace(" ", "") for i in data]
    data = [i.split(":") for i in data]
    data = [{key: value.split(",")} for key, value in data]
    for dic in data:
        for key, value in dic.items():
            new_value = []
            for color in value:
                if color == "noother":
                    dic[key] = 1
                    continue
                amount, color_name = color[:1], color[1:]
                new_value.extend([color_name]*int(amount))
                dic[key] = new_value
    data_dic = {}
    for dic in data:
        key = list(dic.keys()).pop()
        data_dic[key] = dic[key]
    return data_dic


def parse_bags(data):
    whole_chain = data["shinygold"]
    int_list = []
    lone_list = []
    while True:
        try:
            for index, color in enumerate(whole_chain):
                if all(isinstance(x, int) for x in whole_chain):
                    return(len(int_list))
                int_list = []
                if type(color) != int:
                    if type(color) == list:
                        raise TypeError
                    whole_chain[index] = data[color]
                    if type(data[color]) != int:
                        whole_chain.append(1)

                    for idx, elem in enumerate(list(whole_chain)):
                        if type(elem) == int:
                            int_list.append(elem)
        except TypeError:
            for idx, elem in enumerate(list(whole_chain)):
                if type(elem) == int:
                    int_list.append(elem)
                    whole_chain.remove(elem)
                if type(elem) == str:
                    lone_list.append(elem)
                    whole_chain.remove(elem)
            whole_chain = [item for sublist in whole_chain for item in sublist]
            whole_chain.extend(int_list)
            whole_chain.extend(lone_list)
            int_list = []
            lone_list = []


if __name__ == "__main__":
    try:
        print(__doc__)
        t1 = time.time()

        data = read_data()
        print("Parsing, this may take a while...\n")
        bags = parse_bags(data)
        assert bags == 11310

        print(f"The amount of bags required inside the shiny gold bag is {bags}\n")
        print("Parsing the solution took ", round(time.time()-t1, 2), " seconds")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
