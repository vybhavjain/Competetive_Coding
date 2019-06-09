def solve (A, Q, K, R, L):
    s = A
    i = L-1
    t = [-1]
    while i <= R-1:
        prefix = 0
        while(s[i] % K == 0 and i<=R-1):
            prefix = prefix + 1
            i = i +1
           # print(s[i])
        t.append(prefix+1)
        i = i+1
    max1 = 0
    r = max(t)
    if r == 1:
        max1 = -1
    else :
        max1 = r
    return max1

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(0,Q):
     L,R,K = list(map(int, input().split()))
     out_ = solve(A, Q, K, R, L)
     print (out_)
