#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING input_str as parameter.
#

#from itertools import combinations
def value(string,Dict_values):
    sum_string = 0
    for j in string:
        sum_string = sum_string + Dict_values[j]
    if sum_string % len(string) == 0:
        return 1
    return 0
    
def countSubstrings(input_str):
    # Write your code here
    Dict_values = {'a':1,'b':1,
    'c':2,'d':2,'e':2,
    'f':3,'g':3,'h':3,
    'i':4,'j':4,'k':4,
    'l':5,'m':5,'n':5,
    'o':6,'p':6,'q':6,
    'r':7,'s':7,'t':7,
    'u':8,'v':8,'w':8,
    'x':9,'y':9,'z':9,
    }
    substrings = [value(input_str[i: j],Dict_values) for i in range(len(input_str))for j in range(i + 1, len(input_str) + 1)]
    return sum(substrings)     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_str = input()

    result = countSubstrings(input_str)

    fptr.write(str(result) + '\n')

    fptr.close()

