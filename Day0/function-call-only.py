# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 01:39:30 2020

@author: Nitin
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(A):
    m1 = sum(A)/len(A)
    return m1
def median(A):
    A.sort()
    if len(A)%2!=0:
        m2 = A[(len(A)-1)//2]
    else:
        m2 = (A[(len(A)-1)//2]+ A[(len(A)+1)//2])/2
    return m2
def mode(A):
    A.sort()
    B = [ ]
    C = [ ]
    D = [ ]
    for i in range(len(A)):
        if A[i] not in C:
            C.append(A[i])
            B.append(A.count(A[i]))
        k = max(B)
    for i in range(len(B)):
        if B[i] == k:
            D.append(C[i])
    D.sort()
    m3 = D[0]
    return m3

N = int(input())
A  =input()
A = A.split(" ")
for i in range(N):
    A[i] = int(A[i])
A.sort()
print("%0.1f"%mean(A))
print("%0.1f"%median(A))
print("%0.1f"%mode(A))
