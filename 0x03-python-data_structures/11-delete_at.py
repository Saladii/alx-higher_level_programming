#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx > range(len(my_list)) or idx < 0):
        return my_list
    else:
        del my_list[idx]
    return my_list
