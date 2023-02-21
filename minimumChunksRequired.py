#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimumChunksRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER totalPackets
#  2. 2D_LONG_INTEGER_ARRAY uploadedChunks
#

def numpacks(num_elem):
    i = num_elem
    packs = 0
    v = []
    while num_elem > 0:
        packs = packs + 1
        v.append(int(num_elem % 2))
        num_elem = int(num_elem/2)
    print("packs is",i, len(v), "v is",v)
    return sum(v)
            
def minimumChunksRequired(totalPackets, uploadedChunks):
    # Write your code here
    uploadedChunks.sort()
    last = 1
    min_packets = 0
    #print(uploadedChunks)
    for i in range(len(uploadedChunks)):
        start = uploadedChunks[i][0];
        end = uploadedChunks[i][1]
        num_elem = start - last
        last = end + 1
        print(start,end,last)
        min_packets = min_packets + numpacks(num_elem)
    
    if(len(uploadedChunks)):
        left = totalPackets - uploadedChunks[len(uploadedChunks)-1][1]
        if (left):
            min_packets = min_packets + numpacks(left)
    else:
        return numpacks(totalPackets)        
    return min_packets
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    totalPackets = int(input().strip())

    uploadedChunks_rows = int(input().strip())
    uploadedChunks_columns = int(input().strip())

    uploadedChunks = []

    for _ in range(uploadedChunks_rows):
        uploadedChunks.append(list(map(int, input().rstrip().split())))

    result = minimumChunksRequired(totalPackets, uploadedChunks)

    fptr.write(str(result) + '\n')

    fptr.close()

