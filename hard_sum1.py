sum1 = 0
n = int(input())

arr = [1,9]
 
def something(finalnumb):
    x=2
    while(x < finalnumb):
        sum3=0
        for i in range(1,x+1):   
            sum3 += i|x+2
        sum4 = sum3*2
        sum5 = sum4+x+1
        arr.append(sum5+arr[x-1])
        x= x+1 
something(n)
print(arr[n-1])
