# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:59:39 2018

@author: Alex
"""

import numpy as np
from scipy.spatial import distance
import timeit

start_time = timeit.default_timer()

# Open Files
S = open('S0.txt','r')
S = S.readline()
#S = open('S0.txt','r+').read()
#S1 = open('S1.txt','r+').read()

# Establish Domain
m = len(S) # m total elements
n = len(list(set(S))) # from domain of n

# Initalize Values
C = [0]*n # counters
L = [0]*n # labels
k = 9

j = 0

# Open Files
S = open('S0.txt','r+').read()
#S1 = open('S1.txt','r+').read()

# Establish Domain
m = len(S) # m total elements
n = len(list(set(S))) # from domain of n

# Initalize Values
C = [0]*n # counters
L = [0]*n # labels

j = 0

for i in range(m):
    if S[i] == L[j]:
        C[j] += 1    
    else:
        if C[j] == 0:
            L[j] = S[i]
            C[j] = 1    
        else:
            for j in range(n): 
                C[j] -= 1
 
freq = [C,L]
               
# Print Results
print(' ')
print('Characters in Document (m):', m)       
print('Unique Labels in Document (n):', n)       
print('Maximum Frequency in Document (maxC):', max(C))
print('Frequency Counts in Document:', freq)       
print(' ')

# Timeit Statement
elapsed = timeit.default_timer() - start_time
print('Execution time (s): {:f}'.format(elapsed))