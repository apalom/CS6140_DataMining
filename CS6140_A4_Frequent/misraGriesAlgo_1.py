# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:32:42 2018

@author: Alex
"""

import numpy as np
from scipy.spatial import distance
import timeit

start_time = timeit.default_timer()

# Open Files
S = open('S2.txt','r')
S = S.readline()

dic = {}
k = 9

for i in S:
    if i in dic:
        dic[i] += 1
    elif (len(dic) < k):
        dic[i] = 1
    else:
        d = ''
        for key,val in dic.items():
            if val == 0:
                d = key
        if d != '':
            del dic[d]
            dic[i] = 1
        else:
            for key,val in dic.items():
                dic[key] -= 1
        d = ''
        

maxCount = max(dic.values())
mostFreq = [key for key,val in dic.items() if val == maxCount]

# Print Results
print(' ')
print('Document: S2.txt')
print('Characters in Document:', len(S))       
print('Unique Labels in Document:', k)       
print('Counters and Labels:', dic)
print(' ')
print('Most Frequent Item in Document:', mostFreq)
print('Maximum Frequency in Document:', maxCount)
    
print(' ')

# Timeit Statement
elapsed = timeit.default_timer() - start_time
print('Execution time (s): {:f}'.format(elapsed))