g = []
p = []
d = []

n =  int(input())
x,y,z = input().split(" ")
x= int(x)
y= int(y)
z= int(z)

for k in range(n):
    g1,p1,d1 = input().split(" ")
    g1= int(g1)
    p1= int(p1)
    d1= int(d1)
    g.append(g1)
    p.append(p1)
    d.append(d1)

def vals(lis,t):
    value = 0
    lis1 = lis
    for i in range(t):
        maxpos = lis.index(max(lis))
        value = lis[maxpos] + value
        #print(lis[maxpos])
        g[maxpos] = 0
        p[maxpos] = 0
        d[maxpos] = 0
    return value

s111 = []
'''
a=vals(g,x)
b=vals(p,y)
c=vals(d,z)
d=a+b+c
s111.append(d)

b=vals(p,y)
c=vals(d,z)
a=vals(g,x)
d=a+b+c
s111.append(d)
'''
c=vals(d,z)
a=vals(g,x)
b=vals(p,y)
d=a+b+c
s111.append(d)

print(max(s111))
