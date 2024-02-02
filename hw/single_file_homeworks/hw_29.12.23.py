# list1 = [3, 9, 12]
# list2 = [4, 7, 3]
# list3 = []
#
# len_list = len(list1)
#
# if len(list1) == len(list2):
#     for i in range(len_list):
#         list3.append(list1[i] + list2[i])
# else:
#     print("Error!")
#
# print(f"{list1} + {list2} = {list3}")

# забыл что нужно использовать map, поэтому с опозданием. Sorry(

list1 = [3, 9, 12]
list2 = [4, 7, 3]

list3 = list(map(lambda x, y: x + y, list1, list2))

print(f"{list1} + {list2} = {list3}")
