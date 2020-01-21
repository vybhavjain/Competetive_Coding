n = int(input())
k1 = int(input())
A = list(map(int,input().split(" ")))
t = 0
for i in range(n,1,-1):
    for j in range(0,n):
        if j + i <=n:
            sum2 = 0
            trial = A[j:j+i]
            max1 = max(trial)
            sum2 = max1*len(trial) - sum(trial)
            if sum2<=k1:
                t = 1
                break
    if t == 1:
        break
print(len(trial))
        
