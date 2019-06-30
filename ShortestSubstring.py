    #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortestSubstring(s):
    unique = []
    for i in range(len(s)):
        if s[i] not in unique:
            unique.append(s[i])
    length = len(unique)
    #s1 = ""
    lens = []
    #print(unique)
    for i in range(len(s) - length + 1):
        for j in range(i+length,len(s)+1):
            s1 = s[i:j]
            flag = 0
            for k in range(len(unique)):
                if unique[k] not in s1:
                    flag = 1
                    break
            if flag == 0:
                lens.append(len(s1))
                break
    if len(lens) == 0 :
        lens.append(0)
    return min(lens)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortestSubstring(s)

    fptr.write(str(result) + '\n')

    fptr.close()
