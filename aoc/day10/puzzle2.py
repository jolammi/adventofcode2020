"""TODO: Implement puzzle2"""
# import traceback
# # import itertools
# import copy
# from pprint import pprint
# WINDOW_SIZE = 25
#
#
# def read_data():
#     with open("input_.txt", "r") as handle:
#         data = [int(i.strip("\n")) for i in handle.readlines()]
#         data_set = set(data)
#         data_set.add(0)
#         data_set.add(max(data_set)+3)
#         print(data_set)
#     return data_set
#
#
# def parse_adapters(data):
#     sets = set()
#     sets.add(frozenset(data))
#     print(sets)
#     while True:
#         for idx, curr in enumerate(sets):
#             # print(idx)
#             # print()
#
#             curr = list(curr)
#             print(curr)
#             this_loop = []
#             for index, val in enumerate(list(curr)):
#                 # print(val, list(curr))
#                 try_list = copy.deepcopy(curr)
#                 this_loop.append(frozenset(try_list))
#                 # print(index, val)
#                 if (index == 0) or (index == len(curr)-1):
#                     continue
#                 if (curr[index + 1] - curr[index - 1]) <= 3:
#                     try_list = copy.deepcopy(curr)
#                     assert list(try_list) == list(curr)
#                     # if frozenset(try_list) not in sets:
#                     this_loop.append(frozenset(try_list))
#                     try_list.remove(val)
#                     # if frozenset(try_list) not in sets:
#                     this_loop.append(frozenset(try_list))
#                     # print(try_list)
#                     # print(sets)
#                     # print()
#                     # print(frozenset(curr))
#         # print(this_loop)
#         for i in this_loop:
#             sets.add(i)
#         this_loop = []
#         pprint(sets)
#         # print(len(sets))
#         input()
#         # one_jolt_diff = 0
#         # three_jolt_diff = 0
#         # current = 0
#         # while data:
#         #     diff = min(data) - current
#         #     if diff == 1:
#         #         one_jolt_diff += 1
#         #     elif diff == 3:
#         #         three_jolt_diff += 1
#         #     current = min(data)
#         #     data.remove(current)
#         # print(one_jolt_diff, three_jolt_diff +1)
#         # return one_jolt_diff, three_jolt_diff+1
#
#
# if __name__ == "__main__":
#     try:
#         data = read_data()
#         one_jolt, three_jolt = parse_adapters(data)
#         # assert first_faulty == 177777905
#         print(f"One-jolt difference multiplied by three-jolt differences is {one_jolt*three_jolt}")
#     except Exception:
#         print("Please learn how to code")
#         traceback.print_exc()
