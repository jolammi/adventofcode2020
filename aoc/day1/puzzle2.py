import traceback


def read_data():
    with open("input.txt", "r") as handle:
        data = list(set(handle.readlines()))

    data = [i.strip("\n") for i in data]
    return data


def search_occurrences(data):
    for i in data:
        for j in reversed(data):
            for k in data:
                if int(i)+int(j)+int(k) == 2020:
                    return int(i), int(j), int(k)


if __name__ == "__main__":
    try:
        data = read_data()
        i, j, k = search_occurrences(data)
        print(f"The numbers that have a sum of 2020 are {i}, {j}, {k}. "
              f"The answer to the question is {i*j*k}."
              )
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
