import sys
import json
from itertools import permutations 
  
def perm(c): 
     a = list(permutations(c))
     b = []
     for i in range(len(a)):
         k = ''.join(a[i]) 
         b.append(k)
     for i in range(len(a)):
         a[i] = '"' + ''.join(a[i]) + '"'
     print(*a,sep=',')
     b.sort()
     print('"'+b[0]+'"')

line = sys.stdin.readline()
n = int(line[0])

for i in range(n):
  line = sys.stdin.readline()
  c = str(line[0:3])
  t = str(i+1)
  print('#'+t)
  perm(c)
