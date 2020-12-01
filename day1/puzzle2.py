import sys
with open("puzzle1_input.txt", "r") as handle:
    data = handle.readlines()
data = [i.strip("\n") for i in data]
for i in data:
    for j in reversed(data):
        for k in data:
            if int(i)+int(j)+int(k) == 2020:
                print(i)
                print(j)
                print(k)
                # 855 and 282 and 883
                print(int(i)*int(j)*int(k))
                # 212900130
                sys.exit()
