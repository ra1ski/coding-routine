"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    input_length = len(input_array)

    low = 0
    high = input_length - 1

    while low <= high:
        middle_index = (low+high) // 2

        middle_value = input_array[middle_index]

        if middle_value == value:
            return middle_index
        else:
            if middle_value < value:
                low = middle_index + 1
            else:
                high = middle_index - 1
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29, 30]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
