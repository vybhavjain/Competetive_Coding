S = "0081"

total = 0
sum_total = 0

for i in S:
    sum_total = sum_total + int(i)


for i in S:
    temp = sum_total 
    temp = temp - int(i)
    for value in range(10):
        if value!= int(i):
            if (temp+value) % 3 == 0:
                total = total + 1


if int(S) % 3 == 0:
    total = total + 1                

print(total)