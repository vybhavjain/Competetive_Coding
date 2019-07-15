n = int(input())

s = []
peak = []
trough = []

for i in range(n):
    t = int(input())
    s.append(t)
i = 0
flag = 2
while i < n-1:
    if s[i] < s[i+1] and flag != 0 :
        trough.append(i)
        flag = 0
    if s[i] > s[i+1] and flag != 1:
        peak.append(i)
        flag = 1
    i = i + 1

if flag == 0:
    peak.append(i)
else:
    trough.append(i)
#print(s,peak,trough)

difference = []

for i in range(len(peak)-1):
    difference.append(peak[i+1] - peak[i])
for i in range(len(trough)-1):
    difference.append(trough[i+1] - trough[i])
print(max(difference))
