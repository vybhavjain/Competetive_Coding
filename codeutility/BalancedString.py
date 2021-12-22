# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def checkstring(s):
    for letter in s:
        if letter.upper() == letter :
            #upper_flag = True
            if letter.lower() not in s:
                return False
        else :
            if letter.upper() not in s:
                return False
    return True

def solution(S):
    # write your code in Python 3.6
    substrings = []
    length = 300
    final_length = len(S) 

    for i in range(0,final_length):
        for j in range(i,final_length):
            substrings.append(S[i:j+1])

    for word in substrings:
        if checkstring(word):
            if len(word) < length:
                length = len(word)
                
    if length == 300 :
        length = -1 
    
    return length

    pass
