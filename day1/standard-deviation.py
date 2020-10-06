# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:22:14 2020

@author: Nitin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(A):
    u = sum(A)/len(A)
    return u
def std(A):
    u = mean(A)
    B = []
    for i in range(len(A)):
        v = (A[i]-u)**2
        B.append(v)
    sd = ((sum(B))/len(A))**0.5
    return sd

N = int(input())
A = input().split(" ")
for i in range(N):
    A[i] = int(A[i])
print("%0.1f"%std(A))

