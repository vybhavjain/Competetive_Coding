propagation = int(input())
n = int(input())
height = []
peak = []
for i in range(n):
    t = int(input())
    height.append(t)

for i in range(1,n-1):
    if height[i-1] < height[i]:
        if height[i+1] < height[i]:
            peak.append(i)

count = 0

if propagation > n : 
    print(count)
    
count = n //propagation 

print(count)
