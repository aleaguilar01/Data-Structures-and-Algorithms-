#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    print(s)
    print(t)
    print(k)
    index = 0

    while index < len(s) and index < len(t):
        if s[index] == t[index]:
            index += 1
        else:
            break

    sliced_s_length = len(s[index:])
    sliced_t_length = len(t[index:])

    sliced_strings_combined = sliced_s_length + sliced_t_length

    if sliced_strings_combined <= k:
        if index == 0 or (index * 2) + sliced_strings_combined < k or (k - sliced_strings_combined) % 2 == 0:
            return "Yes"
    else:
        return "No"


if __name__ == '__main__':

    s = "y"
    t = "yu"
    k = 2

    result = appendAndDelete(s, t, k)

    print(result)