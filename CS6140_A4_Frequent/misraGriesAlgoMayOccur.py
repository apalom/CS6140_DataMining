# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:32:42 2018

@author: Alex
"""

import numpy as np
import timeit

start_time = timeit.default_timer()

# Open Files
S = open('S1.txt','r')
S = S.readline()

# Establish Domain
m = len(S) # m total elements
n = len(list(set(S))) # from domain of n

dic = {}
k = 9

# Misra-Gries Algorithm
for i in S:
    r = np.random.uniform(0,1) 
    if (i in dic):
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

L = list(dic.keys())
C = list(dic.values())
dic1 = sorted(dic.values(), reverse = True)

# Frugal Quantiles
q = 0.8 # quantil
label = 0
for i in S:
    if i in L:
        r = np.random.uniform(0,1)
        if (dic[i] > label) and (r > 1-q):
            label += 1
        if (dic[i] < label) and (r > q):
            label -= 1


maxCount = max(dic.values())
mostFreq = [key for key,val in dic.items() if val == maxCount]

# Print Results
print(' ')
print('Document:, S1.txt')
print('Characters in Document:', len(S))       
print('Unique Labels in Document:', k)       
print('Counters and Labels:', dic)
print(' ')
print('Most Frequent Item in Document:', mostFreq)
print('Maximum Frequency in Document:', maxCount)
print('Objects Occuring > 20% of the time:', label)
    
print(' ')

# Timeit Statement
elapsed = timeit.default_timer() - start_time
print('Execution time (s): {:f}'.format(elapsed))