import math
t = int(input())

for i in range(t):
    n = int(input())
    pos =  math.ceil(math.log2(n))
    p   = pow(2, pos-1)
    print(p-1)
