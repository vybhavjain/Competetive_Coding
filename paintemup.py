t =  int(input())
for k in range(t):
    di  = dict()
    n  = int(input())
    for t in range(n):
        x,y,w,h = input().split(" ")
        x= int(x)
        y= int(y)
        w= int(w)
        h= int(h)
        for i in range(x,x+w):
            for j in range(y,y+h):
                if((i,j) not in di):
                    di[(i,j)]=1
    print(len(di))
