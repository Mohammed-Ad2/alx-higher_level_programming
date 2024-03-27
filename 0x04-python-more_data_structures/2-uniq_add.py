#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    unique_integers = set()
    total_sum = 0
    for num in my_list:
        if num not in unique_integers:
            unique_integers.add(num)
            total_sum += num
    return total_sum
