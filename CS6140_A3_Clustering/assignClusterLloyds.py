# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 07:54:46 2018

@author: Alex Palomino
"""

import numpy as np
from scipy.spatial import distance
import timeit

start_time = timeit.default_timer()


x = np.loadtxt('C2.txt')
x = np.delete(x,0,1)
n = len(x)

k = 3
c = np.zeros((k,2))
phi = np.zeros((n,1))
dst2Center = np.zeros((n,k))
maxCenterCost = np.zeros((k,1))
maxMeanCost = np.zeros((k,1))
xAug = np.zeros((n,3))
xAug[:,0] = x[:,0]
xAug[:,1] = x[:,1]

# Choose initial set of centers
# C initially with points indexed {1,2,3}
#c[0] = x[0]
#c[1] = x[1]
#c[2] = x[2]

# C initially with results of Gonzo 
c[0] = ((-2,14))
c[1] = ((-0.40328,-5.4479))
c[2] = ((-4.06452,4.19390))

diff = 1
runs = 0

#while diff > 0.1:
for R in range(10):
    runs += 1
    # Set initial center assignment for all points
    for j in range(n):
        phi[j] = 1
    
    for j in range(n):
        for i in range(k): 
            dst2Center[j][i] = distance.euclidean(x[j],c[i])

    for j in range(n):
        phi[j] = np.argmin(dst2Center[j,:])+1
    
    xAug[:,2] = phi[:,0]
           
    x1 = np.zeros((n,2))
    x2 = np.zeros((n,2))
    x3 = np.zeros((n,2))
    row1 = 0
    row2 = 0
    row3 = 0
    for j in range(n):
        #for i in range(k):    
            #phi1 = [x for x in phi if x ==1]
        if phi[j] == 1:
            x1[row1] = x[j]
            row1 += 1
        elif phi[j] == 2:
            x2[row2] = x[j]
            row2 += 1
        elif phi[j] == 3:
            x3[row3] = x[j]
            row3 += 1
    x1 = x1[np.all(x1 != 0, axis=1)]
    x2 = x2[np.all(x2 != 0, axis=1)]
    x3 = x3[np.all(x3 != 0, axis=1)]
    x1mean = (np.mean(x1[:,0]),np.mean(x1[:,1]))
    x2mean = (np.mean(x2[:,0]),np.mean(x2[:,1]))
    x3mean = (np.mean(x3[:,0]),np.mean(x3[:,1]))
    dst1 = distance.euclidean(x1mean,c[0])
    dst2 = distance.euclidean(x2mean,c[1])
    dst3 = distance.euclidean(x3mean,c[2])
    
    diff = dst1 + dst2 + dst3
    
    c[0] = x1mean
    c[1] = x2mean
    c[2] = x3mean

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
#plt.scatter(phiCX[0,0],phiCX[0,1],c='k',marker="v")
#plt.scatter(phiCX[1,0],phiCX[1,1],c='k',marker="v")
#plt.scatter(phiCX[2,0],phiCX[2,1],c='k',marker="v")

plt.title("Lloyd's Clustered Data (k = 3)")
plt.xlabel("x-coord")
plt.ylabel("y-coord")
plt.show()
