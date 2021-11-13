import math 
def CountSquares(a, b): 
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1) 
  
n=int(input())

for i in range(n):
    k,l=input().split()
    k=int(k)
    l=int(l)
    res=CountSquares(k,l)
    print(res)
