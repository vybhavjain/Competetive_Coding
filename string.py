n=int(input())
#print(n)
#work = []
flag = 1 
for i in range(n):
    flag = 1
    work = []
    count = 0
    k=input()
    l=input()
    l1 = len(l)
    l5 = len(k)
    if l in k:
        print('yes')
        print('0')
        flag = 0
    else :
        for t in range(l5):
            count = 0
            l2 = 0
            a = t
            while a < l5 and l[l2] != k[a]:
                a = a+1
            while a < l5 and l2 < l1 and l[l2] == k[a]:
                l2 = l2+1
                a = a+1
            while a < l5 and l2 < l1:
                a = a+1
                count = count+1
                while a < l5 and l2 < l1 and l[l2] == k[a] :
                    l2 = l2+1
                    a = a+1
            if l2 == l1 and count != 0:
                work.append(count)
                #print('Yes')
                #print(count)
            else :
                #print('No')
                l2 = l1
    if len(work) != 0 :
        print('Yes')
        print(min(work))
        flag =1
    elif len(work) == 0 and flag == 1:
        print('No')
