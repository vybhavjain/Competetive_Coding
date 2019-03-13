number = int(input())

n = []
m = []
k = []
l = []
w = []
for i in range(number):
    n1,m1 = input().split()
    n.append(int(n1))
    m.append(int(m1))
    for j in range(int(m1)):
        k1,l1,w1 = input().split()
        k.append(int(k1))
        l.append(int(l1))
        w.append(int(w1))
    wkl = list(zip(*sorted(zip(k,l,w))))[0]
    #wkl.sort()
    print(wkl)
