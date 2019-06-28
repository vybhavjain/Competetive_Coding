list_a = [10,0,15,2,45]
list_b = [10,0,20,25,1]

list_c = list(zip(list_a, list_b))

print(list_c)
#    return(sorted(tup, key = lambda x: x[1]))   
a = sorted(list_c ,key = lambda x: x[1])  
print(a)

list_c.sort(key = lambda x: x[0])  
print(list_c)
