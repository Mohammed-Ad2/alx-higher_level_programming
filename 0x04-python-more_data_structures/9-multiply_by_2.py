#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    new_dict = a_dictionary.copy()
    for k, v in new_dict.items():
        new_dict[k] *= 2
    return new_dict
