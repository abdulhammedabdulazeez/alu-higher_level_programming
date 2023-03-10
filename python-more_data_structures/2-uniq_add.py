#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    for elem in my_list:
        if elem not in unique_set:
            unique_set.add(elem)

    unique_sum = sum(unique_set)

    # Return the sum of unique integers
    return unique_sum
