t = int(input())

for j in range(t):
    n=int(input())
    sum = 0
    fact = 1
    if n >3 and n%2 ==1:
        print('YES')
    elif n+1 % 3 ==0:
        print('YES')
    else:
        for i in range(1,n+1):
            fact = fact*i
            sum = sum + i
        if fact%sum ==0:
            print('YES')
        else:
            print('NO')
