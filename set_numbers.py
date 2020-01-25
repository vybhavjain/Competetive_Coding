import math

t = int(input())

for i in range(t):
    n = int(input())
    x =  math.log2(n)
    pos = math.ceil(x)
    if math.log2(n+1) % 1 == 0:
        print(n)
    elif x%1 !=0:
        p   = pow(2, pos-1)
        print(p-1)
    else:
        print(n-1)
