# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:32:03 2019

@author: VYBHAV JAIN
"""

number = int(input())

for i in range(number):
    count = 0
    s = []
    n1,k1 = input().split()
    n1 = int(n1)
    k1 = int(k1)
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])    
    k2 = 2*k1
    for i in range(n1):
        if s[i] >=(k2):
            s[i] = s[i] - k2
            count = count + 1
    for i in range(n1):
        if s[i] >(k1):
            s[i] = 0
            count = count + 1
    for i in range(n1):
        if s[i] == (k1):
            s[i] = 0
            count = count + 0.5
    s.append(0)    
    s.sort()
    s.reverse()
    for i in range(n1):
        if s[i] + s[i+1] >= (k1):
            s[i] = 0
            s[i+1] = 0
            count = count + 1
            #s.sort()
           # s.reverse()
    for i in range(n1):
        if s[i] > 0:
            s[i] = 0
            count = count + 0.5
    if(count%1 ==0):
        print(int(count))
    else:
        print(int(count+0.5))
    #print(s)
    
