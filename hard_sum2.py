sum1 = 0
n = int(input())

arr = [1,9]
def bitvalue(number):
    sum3=0
    for i in range(1,number):   
        sum3 += i|number
    sum5 = (sum3*2)+number
    arr.append(sum5+arr[number-2])
 
def something(finalnumb):
    x=2
    while(x< finalnumb):
        bitvalue(x+1)
        x= x+1 
something(n)
print(arr[n-1])
