#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    add_list = []
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            add_list.append(True)
        else:
            add_list.append(False)
    return add_list
