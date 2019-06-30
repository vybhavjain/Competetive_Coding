    #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'vowelsubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def vowelsubstring(s):
    # Write your code here
    vowel = ['a','e','i','o','u']
    number = 0
    for i in range(0,len(s)-4):
        for j in range(i+5,len(s)+1):
            flag = 1
            if s[j-1] not in vowel:
                break
            s1 = s[i:j]
            #print(s1)
            for t in s1:
                if t not in vowel:
                    flag = 0
                    break
            if flag == 1:
                if vowel[0]  in s1:
                    if vowel[1] in s1:
                        if vowel[2] in s1:
                            if vowel[3] in s1:
                                if vowel[4] in s1:
                                    number = number + 1
                    
    #print(number)
    return number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = vowelsubstring(s)

    fptr.write(str(result) + '\n')

    fptr.close()
