with open("puzzle1_input.txt", "r") as handle:
    data = handle.readlines()
data = [i.strip("\n") for i in data]
for i in data:
    for j in reversed(data):
        if int(i)+int(j) == 2020:
            print(i)
            print(j)
            # 765 and 1255
            print(int(i)*int(j))
            # 960075
