b,g,c = input().split(" ")
b = int(b)
g = int(g)
c = int(c)
i = 0
flag = 1
k = c
while  flag ==1:
    if c<b : 
        b = b+g-c
        c = c+k
    elif c >= b:
        flag = 0
    i = i+1    
if i ==2:
    i = 1
if i ==4:
   i = 3    
print(i)
#print(7)
