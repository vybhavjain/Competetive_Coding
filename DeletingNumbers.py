n,k = input().split(" ")
n = int(n)
k = int(k)

arr = []
arr = input().split(" ")

for i in range(n):
    arr[i] = int(arr[i])
    
middle = (n+1)//2
if k > middle:
    for t in range(middle):
        arr.append(0)
max1 = 0
k = k-1
for i in range(k):
    if arr[middle-i]>max1:
        max1 = arr[middle-i]
for i in range(k):
    if arr[middle+i]>max1:
        max1 = arr[middle+i]
print(max(max1,arr[middle]))
