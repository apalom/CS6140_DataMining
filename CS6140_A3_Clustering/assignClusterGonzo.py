# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:08:57 2018

@author: Alex
"""

import numpy as np
from scipy.spatial import distance
import timeit

start_time = timeit.default_timer()

x = np.loadtxt('C2.txt')
x = np.delete(x,0,1)

k = 3
n = len(x)

dstPhiC = np.empty
dstTmp = np.empty
dst2Center = np.zeros((n,k))
phi = np.zeros((n,1))
maxD = np.zeros((k,1))
c = np.zeros((k,2))
centerCost = np.zeros((n,k))
phiCX = np.zeros((k,2))
maxCenterCost = np.zeros((k,1))
maxMeanCost = np.zeros((k,1))

c[0] = (x[0][0],x[0][1])

for j in range(0,n):
    phi[j] = 1

for i in range(1,k+1):
    m = 0
    c[i-1] = (x[0][0],x[0][1])
    
    # Update cluster center to further point
    for j in range(0,n):
        dstPhiCtmp = distance.euclidean(x[j],c[int(phi[j]-1)])
        
        if dstPhiCtmp > m:
            m = dstPhiCtmp
            c[i-1] = x[j]
    maxD[i-1] = m
    # Assign point to cluster if within phiC distance         
    for j in range(0,n):   
        dstPhiCtmp = distance.euclidean(x[j],c[int(phi[j]-1)])
        dstXjCi = distance.euclidean(x[j],c[i-1])
        
        if dstPhiCtmp > dstXjCi:
            phi[j] = i
    
# Calculate distances and costs
for j in range(0,n):
    for i in range(1,k+1):
        ptX = x[j]
        center = c[i-1]
        dst2Center[j][int(phi[j]-1)]= distance.euclidean(ptX,center) 

        maxCenterCost[i-1] = np.amax(dst2Center[:,i-1])
        maxMeanCost[i-1] = np.sqrt((1/n)*np.sum(np.square(dst2Center[:,i-1]))) 
    
# timeit statement
elapsed = timeit.default_timer() - start_time
print('Execution time:', elapsed)

# %% Scatter Plot
import matplotlib.pyplot as plt

k1 = []
k2 = []
k3 = []

for j in range(0,n):
    if phi[j] == 1:
        k1.append(j)
    if phi[j] == 2:
        k2.append(j)
    if phi[j] == 3:
        k3.append(j)

#s = plt.scatter(x[:,0],x[:,1],marker="x")

plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')

plt.scatter(x[k1,0], x[k1,1], c='r',marker=".")
plt.scatter(x[k2,0], x[k2,1], c='g',marker=".")
plt.scatter(x[k3,0], x[k3,1], c='b',marker=".")
plt.scatter(c[0,0],c[0,1],c='k',marker="x")
plt.scatter(c[1,0],c[1,1],c='k',marker="x")
plt.scatter(c[2,0],c[2,1],c='k',marker="x")
plt.scatter(phiCX[0,0],phiCX[0,1],c='k',marker="v")
plt.scatter(phiCX[1,0],phiCX[1,1],c='k',marker="v")
plt.scatter(phiCX[2,0],phiCX[2,1],c='k',marker="v")

plt.title("Clustered Data (k = 3) Outlier Removed")
plt.xlabel("x-coord")
plt.ylabel("y-coord")
plt.show()