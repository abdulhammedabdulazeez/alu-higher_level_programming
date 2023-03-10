#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list with the same elements as the input list
    new_list = [elem for elem in my_list]

    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    # Return the new list with replaced elements
    return new_list
