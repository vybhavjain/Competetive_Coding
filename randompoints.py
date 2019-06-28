def distance(x1,y1,x2,y2):
    t = (x1-x2)**2 + (y1-y2)**2    
    dist.append(t)

x = []
y = []
dist = []

n = int(input())

for i in range(n):
    x.append(int(input()))

n = int(input())

for i in range(n):
    y.append(int(input()))

for i in range(n-1):
    distance(x[i],y[i],x[i+1],y[i+1])
print(min(dist))
