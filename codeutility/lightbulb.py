
counter = 0

#[2,1,3,5,4]

def checker(n,count,tracker,maxval):
    global counter
    print(n,count,tracker)
    if tracker in n:
        indexval = n.index(tracker)
        count = count + 1
        counter = counter + 1
        tracker = tracker + 1
        checker(n[indexval+1:],count,tracker,maxval)
    elif tracker<maxval and tracker not in n:
        tracker = tracker + 1
        checker(n,count,tracker,maxval)
    
    return counter

#arr = [2,1,3,5,4]
#arr = [2,3,4,1,5]
#arr = [1,3,4,2,5]

print(checker(arr,0,1,len(arr)))