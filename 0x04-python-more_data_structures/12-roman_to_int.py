#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    prev_value = 0
    for char in roman_string:
        if char in roman_numerals:
            value = roman_numerals[char]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value

    return result
