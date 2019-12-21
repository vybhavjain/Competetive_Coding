def firstOccurrence(s, x):
    # Write your code here
    o = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r = 999
    t = 999
    for i in range(26):
        x1 = x
        x1 = x1.replace("*", o[i])
        print (x1)
        t = s.find(x1)
        if t != -1:
            r = t
    if r == 999:
        r = -1
    print(r)
    return r
