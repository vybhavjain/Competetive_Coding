n = int(input())
k1 = int(input())
A = list(map(int,input().split(" ")))
out = []
for i in range(0,n):
    for j in range(1,n):
        if j + i <=n:
            sum2 = 0
            trial = A[i:j+i]
            max1 = max(trial)
            for k in range(len(trial)):
                sum2 = sum2 + max1 - trial[k]
            #print(trial,sum2,len(trial))
            if sum2<=k1:
                out.append(len(trial))
print(max(out))
        
