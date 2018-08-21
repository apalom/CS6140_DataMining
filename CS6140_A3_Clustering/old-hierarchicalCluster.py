# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:07:46 2018

@author: Alex Palomino
"""

import numpy as np
from scipy.spatial import distance

row = 0
doc = np.empty

minList = []
minListSet = []

index_min = 0
minDst = 10
doc = np.loadtxt('C1.txt')
#doc = np.delete(doc,0,1)

numrows = len(doc) 

dst = np.zeros((numrows,numrows))

# Build distance matrix
for row in range(numrows):
    ptA = (doc[row][1], doc[row][2])
    
    for col in range(numrows):
        ptB = (doc[col][1], doc[col][2])
        dst[row][col] = distance.euclidean(ptA,ptB)
        if dst[row][col] == 0:
            dst[row][col] = 100

nearestNeighbor = np.zeros((numrows,3))
for col in range(numrows):
    minDstTemp = (min(dst[:,col]))
    if minDstTemp != (min(dst[:,col-1])):
        nearestNeighbor[col,0] = minDstTemp
        pts = np.argwhere(dst == minDstTemp)
        nearestNeighbor[col,1] = pts[0][0]    
        nearestNeighbor[col,2] = pts[0][1]
        
# Find location of minimum distance in distance matrix        
minDst = np.min(dst[np.nonzero(dst)])
if dst[row][col] == minDst:
    minLoc = [row, col]

for row in range(numrows):
    for col in range(numrows):
        if row != col:
            minList.append(dst[row][col])
              
minListSet = list(set(minList))  
minListSet.sort() 


