def merge(arr, temp, left, mid, right):  

    i, j, k, inv_count = left, mid, left, 0
      
    while (i <= mid - 1) and (j <= right):  
      
        if arr[i] <= arr[j]: 
            temp[k] = arr[i] 
            k, i = k + 1, i + 1
          
        else: 
            temp[k] = arr[j] 
            k, j = k + 1, j + 1

            inv_count = inv_count + (mid - i)  

    while i <= mid - 1:  
        temp[k] = arr[i] 
        k, i = k + 1, i + 1

    while j <= right:  
        temp[k] = arr[j] 
        k, j = k + 1, j + 1

    for i in range(left, right + 1):  
        arr[i] = temp[i]  
  
    return inv_count  

def _mergeSort(arr, temp, left, right):  
    inv_count = 0
    if right > left:  

        mid = (right + left) // 2

        inv_count = _mergeSort(arr, temp, left, mid)  
        inv_count += _mergeSort(arr, temp, mid + 1, right)  
        inv_count += merge(arr, temp, left, mid + 1, right)  
      
    return inv_count  

def mergeSort(arr, array_size):  
  
    temp = [None] * array_size  
    return _mergeSort(arr, temp, 0, array_size - 1)  

def possibleSortingBy3SizeSubarray(arr, N):  
    numberOfInversion = mergeSort(arr, N)  
    return (numberOfInversion % 2 == 0)  
  
n = int(input())
for i in range(n):
    size = int(input())
    k = []
    k = input().split(" ")
    for i in range(size):
        k[i] = int(k[i])
    if possibleSortingBy3SizeSubarray(k, size):  
        print("YES") 
    else: 
        print("NO") 
