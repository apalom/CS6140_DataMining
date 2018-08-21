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
wx = np.zeros((n,1))
Px = np.zeros((n,1))
PxDist = np.zeros((n,1))
dst2Center = np.zeros((n,k))
phi = np.zeros((n,1))
c = np.zeros((k,2))
centerCost = np.zeros((n,1))
phiCX = np.zeros((k,2))
maxTrials = 50
maxCenterCost = np.zeros((k,maxTrials))
maxMeanCost = np.zeros((k,maxTrials))

c[0] = (x[0][0],x[0][1])

for trials in range(0,maxTrials):
    for j in range(0,n):
        phi[j] = 1
        
    c[0] = (x[0][0],x[0][1])
    
    for i in range(1,k+1):
        m = 0
        #c[i-1] = (x[0][0],x[0][1])
         
        # Calculate distances 
        for j in range(0,n):
            ptX = x[j]
            center = c[i-1]
            dst2Center[j][int(phi[j]-1)]= distance.euclidean(ptX,center) 
            #if dst2Center[j][int(phi[j]-1)] == 0.0:
            #    dst2Center[j][int(phi[j]-1)] = 100
                       
        # Update cluster center using K-means++
        for j in range(0,n):
            phiCidx = int(np.argmin(dst2Center[:,0]))
            phiCX[i-1] = x[phiCidx]
            wx[j] = distance.euclidean(x[j],c[i-1])**2      
            
        W = np.sum(wx[:,0])  
        r = np.random.uniform()      
            
        for j in range(0,n):
            Px[j] = wx[j]/W
              
        for j in range(1,n):
            PxDist[j] = PxDist[j-1] + Px[j]
        
        for j in range(1,n):     
            if r > PxDist[j-1] and r <= PxDist[j]:
                m = distance.euclidean(x[j],c[i-1])
                c[i-1] = x[j]
            
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
    
            maxCenterCost[i-1][trials] = np.amax(dst2Center[:,i-1])
            maxMeanCost[i-1][trials] = np.sqrt((1/n)*np.sum(np.square(dst2Center[:,i-1])))
    
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

plt.title("K-Means++ Clustered Data (k = 3)")
plt.xlabel("x-coord")
plt.ylabel("y-coord")
plt.show()

# %% Cost CDF Plots

n_bins = 25

maxCenterCostC1 = np.sort(maxCenterCost[0,:])
maxCenterCostC2 = np.sort(maxCenterCost[1,:])
maxCenterCostC3 = np.sort(maxCenterCost[2,:])

# Plot Max Center Cost
fig, ax = plt.subplots(figsize=(12, 6))
n, bins, patches = ax.hist(maxCenterCostC1, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 1')

n, bins, patches = ax.hist(maxCenterCostC2, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 2')

n, bins, patches = ax.hist(maxCenterCostC3, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 3')

ax.grid(True)
ax.legend(loc=2)
ax.set_title('3-Center Cost CDF (50 runs)')
ax.set_xlabel('Max Center Cost')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

maxMeanCostC1 = np.sort(maxMeanCost[0,:])
maxMeanCostC2 = np.sort(maxMeanCost[1,:])
maxMeanCostC3 = np.sort(maxMeanCost[2,:])

# Plot Max Mean Cost
fig, ax = plt.subplots(figsize=(12, 6))
n, bins, patches = ax.hist(maxMeanCostC1, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 1')

n, bins, patches = ax.hist(maxMeanCostC2, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 2')

n, bins, patches = ax.hist(maxMeanCostC3, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 3')

ax.grid(True)
ax.legend(loc=2)
ax.set_title('3-Mean Cost CDF (50 runs)')
ax.set_xlabel('Max Mean Cost')
ax.set_ylabel('Likelihood of occurrence')

plt.show()
