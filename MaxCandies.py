
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxCandies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY bags
#  2. LONG_INTEGER candiesLimit
#

def maxCandies(bags, candiesLimit):
    # Write your code here
    bags.sort()
    sum2 = 0
    while bags[len(bags) - 1] > candiesLimit:
        bags.pop(len(bags) - 1)
    if candiesLimit in bags:
        return candiesLimit
    maximum = []
    s =len(bags)
    print(bags)
    for i in range(s):
        sum2 = bags[len(bags) - 1]
        j = len(bags) - 2
        while sum2 < candiesLimit and j >= 0:
            while sum2 + bags[j] > candiesLimit and j >= 0:
                j = j - 1
            if j == -1 :
                break
            sum2 = sum2 + bags[j]
            j = j - 1
        maximum.append(sum2)
        bags.pop(len(bags) - 1)
    #print(maximum)
    return max(maximum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bags_count = int(input().strip())

    bags = []

    for _ in range(bags_count):
        bags_item = int(input().strip())
        bags.append(bags_item)

    candiesLimit = int(input().strip())

    result = maxCandies(bags, candiesLimit)

    fptr.write(str(result) + '\n')

    fptr.close()

