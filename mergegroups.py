n = int(input())
a = [int(x) for x in input().split()]
for s in range(len(a)):
    a[s] = [a[s]]
q = int(input())
for i in range(q):
    p = []
    #sample = [int(x) for x in input().split(" ")]
    sample = input().split(" ")
    for q in range(len(sample)):
        sample[q] = int(sample[q])
    if sample[0] == 2:
        x = sample[1] - 1
        if len(a[x]) == 1:
            print(0)
        else:
            p = a[x]
            p.sort()
            diff = p[-1] - p[-2]
            print(diff)
    else:
        x = sample[1] - 1
        y = sample[2] - 1
        for l in range(len(a[y])):
            if a[y][l] not in a[x]:
                a[x].append(a[y][l])
        a[y] = a[x]
