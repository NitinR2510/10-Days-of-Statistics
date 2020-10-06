# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 03:24:21 2020

@author: Nitin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N = int(input())
X = input()
X = X.split(" ")
for i in range(N):
    X[i] = int(X[i])
W = input()
W = W.split(" ")
for i in range(N):
    W[i] = int(W[i])
X = np.array(X)
W = np.array(W)
m1 = sum(X*W)/sum(W)
print("%0.1f"%m1)