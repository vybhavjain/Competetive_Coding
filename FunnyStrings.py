n = int(input())
for i in range(n):
    s1 = []
    s2 = []
    ch1 = []
    ch2 = []
    t = input()
    for i in range(len(t)):
        s2.append(t[-i-1])
        s1.append(t[i])
        ch1.append(ord(s1[i]))
        ch2.append(ord(s2[i]))
    s = []
    r = []
    for i in range(len(t)-1):
        s.append(abs(ch1[i]-ch1[i+1]))
        r.append(abs(ch2[i]-ch2[i+1]))
    if s == r:
        print("Funny")
    else:
        print("Not Funny")
