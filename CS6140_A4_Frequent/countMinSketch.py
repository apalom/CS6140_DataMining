# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import timeit
import hashlib

start_time = timeit.default_timer()

# Open Files
Sraw = open('S1.txt','r')
S = Sraw.readline()

# Initialize Values
dic = {}
k = 10 #counters
t = 5 #hash functions

# Initialize Dictionary
for i in range(1,t+1):
    for j in range(1,k+1):
        dic[str(i) + '-' + str(j)] = 0
 
# Count Min Sketch Hashes       
for char in S:
    #h = hashlib.sha256()
    h = hashlib.sha256(str(hash(char)).encode('utf-8'))
    count = []
    
    for salt in range(1,t+1):
        h.update(str(salt).encode('utf-8')) 
        count.append(int(h.hexdigest(), 16) % k + 1)
    
    for val in range(t):
        dic[str(val+1) + '-' + str(count[val])] += 1

# Estimated counts for 'a', 'b', 'c'            
val = 0
i = 0
salt = 0
count = []
for i in 'abc':
    #h1 = hashlib.sha256()
    h1 = hashlib.sha256(str(hash(i)).encode('utf-8'))
    count = []
    
    for salt in range(1,t+1):
        h1.update(str(salt).encode('utf-8')) 
        count.append(int(h1.hexdigest(), 16) % k + 1)
      
    for val in range(t):
        count.append(dic[str(val+1) + '-' + str(count[val])])
        
    print('Character Count '+ str(i) + ': ' + str(min(count[t:k])))
    

# Timeit Statement
elapsed = timeit.default_timer() - start_time
print('')
print('Execution time (s): {:f}'.format(elapsed))
        
            
            
       
            
            
            
