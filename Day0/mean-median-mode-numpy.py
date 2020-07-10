# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 01:38:53 2020

@author: Nitin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N = int(input())
A  =input()
A = A.split(" ")
for i in range(N):
    A[i] = int(A[i])
A.sort()
A = np.array(A)
#mean and median
print("%0.1f"%np.mean(A))
print("%0.1f"%np.median(A))
#mode
uni, occ = np.unique(A, return_counts=True)
k = occ.max()
possible = [ ]
for i in range(len(uni)):
    if occ[i] == k:
        possible.append(uni[i])
possible.sort()
print("%0.1f"%(possible[0])) 
