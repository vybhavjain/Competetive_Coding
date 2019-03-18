n = int(input())
a = []
b = []
c = []
d = []
for i in range(n):
    a1,b1,c1 = input().split()
    a.append(int(a1))
    b.append(int(b1))
    c.append(int(c1))

for i in range(n):
    d1= (b[i])^2 - 4*a[i]*c[i]
    if d1>0:
        d.append(d1)
    if d1==0:
        d.append(d1)
print(len(d))
