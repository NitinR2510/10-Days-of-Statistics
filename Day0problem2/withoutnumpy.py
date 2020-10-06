# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 03:24:48 2020

@author: Nitin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = input()
X = X.split(" ")
for i in range(N):
    X[i] = int(X[i])
W = input()
W = W.split(" ")
for i in range(N):
    W[i] = int(W[i])
M = [ ]
for i in range(N):
    M.append(X[i]*W[i])
m1 = sum(M)/sum(W)
print("%0.1f"%m1)