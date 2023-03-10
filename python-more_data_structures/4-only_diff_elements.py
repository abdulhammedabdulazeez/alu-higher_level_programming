#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create empty sets to store unique elements from both sets
    unique_set_1 = set()
    unique_set_2 = set()
    for elem in set_1:
        if elem not in set_2:
            unique_set_1.add(elem)
    for elem in set_2:
        if elem not in set_1:
            unique_set_2.add(elem)
    return unique_set_1.union(unique_set_2)
