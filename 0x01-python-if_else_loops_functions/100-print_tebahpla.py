#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if char % 2 == 1:
        print("{}".format(chr(char).upper()), end="")
    else:
        print("{}".format(chr(char)), end="")
