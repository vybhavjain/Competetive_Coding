# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:48:12 2019

@author: VYBHAV JAIN
"""

n1,m1,p1 = input().split()
n1 = int(n1)
m1 = int(m1)
p1 = int(p1)

a = []
b = []

#for i in range(n1):
a = input().split()
for i in range(n1):
    a[i] = int(a[i])
b = input().split()
for i in range(m1):
    b[i] = int(b[i])
sum = 0
for i in range(n1):
    for j in range(m1):
        t= i*i*j*j*j
        sum = sum +a[i]*b[j]*(pow(p1,t))
print(sum%490019)
