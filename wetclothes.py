n,m,g = input().split(" ")

n = int(n)
m = int(m)
g = int(g)

count = 0
picked = 0
t = []
t = input().split(" ")

for i in range(n):
    t[i] = int(t[i])

a = []
a = input().split(" ")

for i in range(m):
   a[i] = int(a[i])

t1 = []
#print(n,m,g)
#print(t)
#print(a)
for x in range(n-1):
    t1.append(t[x+1]-t[x])
#print(t1)    
a.sort()
t1.sort()
#print(a)    
t1.append(10001)
a.append(10002)
while len(t1) != 1:
    while a[0] <=t1[0] :
        a.pop(0)
        picked = picked +1
    count = count + 1
    t1.pop(0)
print(picked)
