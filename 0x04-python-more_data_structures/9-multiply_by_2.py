#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_value = a_dictionary.copy()
    for i in a_dictionary:
        a_value[i] = 2 * a_dictionary[i]
    return a_value
