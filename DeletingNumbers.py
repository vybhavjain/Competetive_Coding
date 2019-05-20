n,k = input().split(" ")
n = int(n)
k = int(k)

arr = []
arr = input().split(" ")

for i in range(n):
    arr[i] = int(arr[i])
    
middle = (n+1)//2
if k > middle:
    for t in range(k-middle):
        arr.append(0)
max1 = 0
max2 = 0
final_max = 0
k = k-1
for i in range(k):
    if arr[middle-i]>max1:
        max1 = arr[middle-i]
        #print(max1)
for i in range(k):
    if arr[middle+i]>max2:
        max2 = arr[middle+i]
        #print(max2)
print(max(max1,max2,arr[middle]))
