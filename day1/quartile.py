# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 09:13:22 2020

@author: Nitin
"""
def median(A):
    A.sort()
    if len(A)%2!=0:
        m2 = A[(len(A)-1)//2]
    else:
        m2 = (A[(len(A)-1)//2]+ A[(len(A)+1)//2])/2
    return m2 #this is quartile 2
def quart1(A):
    A.sort()
    B = []
    m1 = median(A)
    for i in range(len(A)):
        if A[i] < m1:
            B.append(A[i])
    q1 = median(B)
    return q1
def quart2(A):
    A.sort()
    B = [ ]
    m1 = median(A)
    for i in range(len(A)):
        if A[i]>m1:
            B.append(A[i])
    q3 = median(B)
    return q3
num = int(input())
A = input().split(" ")
for i in range(num):
    A[i] = int(A[i])
print(int(quart1(A)))
print(int(median(A)))
print(int(quart2(A)))
