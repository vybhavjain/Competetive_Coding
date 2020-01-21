t = int(input())

for i in range(t):
    c,n = input().split(" ")
    c = int(c)
    n = int(n)
    total = (n*(n+1))//2
    remainder = (c - total ) % n
    if c-total > 0:
        print(remainder)
    else : 
        print(c)
