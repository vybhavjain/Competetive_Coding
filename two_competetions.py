A = 100
B = 100

x = 4
y = 11
count = 0
list1 = []
I = []
J = []
for i in range(1,A):
    if i!=x:
        for j in range(B,0,-1):
            t = []
            if j!=y:
                if i*j<x*y:
                    if i not in I and j not in J:
                            count = count+1
                            t.append(i)
                            t.append(j)
                            I.append(i)
                            J.append(j)
                            list1.append(t)
print(len(list1))
print(list1)
