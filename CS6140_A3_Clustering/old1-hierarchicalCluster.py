# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:07:46 2018

@author: Alex Palomino
"""

import numpy as np
import itertools
from scipy.spatial import distance

k = 0
doc = np.empty

doc = np.loadtxt('C1.txt')
#doc = np.delete(doc,0,1)

numrows = len(doc) 

dst = np.zeros((numrows,numrows))

#Build distance matrix
for col in range(len(doc)):
    ptA = (doc[col][1], doc[col][2])
    
    for row in range(len(doc)):
        ptB = (doc[row][1], doc[row][2])
        dst[row][col] = distance.euclidean(ptA,ptB)
        if dst[row][col] == 0:
            dst[row][col] = 100
    
    minDstTemp = (min(dst[:,col]))
    minDstTempPrv = (min(dst[:,col-1]))
    loc = np.argwhere(dst[:,col] == minDstTemp)
    #pts = np.delete(pts,1,0)
    if minDstTemp == (min(dst[:,col-1])):
        doc[loc][0] = k
        doc[col][0] = k
    else:
        k+=1
        doc[loc][0] = k
        doc[col][0] = k
 
                    
            