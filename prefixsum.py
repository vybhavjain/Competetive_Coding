import random
import math

count = 0
n = int(input())
#print(n)
for i in range(1000000):
    count = 0
    array2 = []
    array1 = random.sample(range(1,10000), n)
#array1 = [9,7,20,13]
    array2.append(array1[0])  
    for i in range(1, n):
        x = array2[i-1] + array1[i]
        array2.append(x)
        #print(array1)
        #print(array2)

    for i in array2:
        if (math.sqrt(i)-int(math.sqrt(i)) == 0):
            count = count+1
    if count == n:
        print(array1)
        #print(array2)
        break

if count!=n:
    print(-1)    
