#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as a:
        print("Exception: {}".format(a), file=sys.stderr)
        return None
