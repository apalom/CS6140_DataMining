# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:13:32 2018

@author: Alex
"""

import numpy as np
from scipy.spatial import distance
import timeit

start_time = timeit.default_timer()

x = np.loadtxt('C2.txt')
x = np.delete(x,0,1)
n = len(x)

xAug = np.zeros((n,3))
xAug[:,0] = x[:,0]
xAug[:,1] = x[:,1]

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
runs = 0

c[0] = (x[0][0],x[0][1])

for trials in range(0,maxTrials):
    for j in range(0,n):
        phi[j] = 1
    
    for i in range(1,k+1):
        m = 0
        c[i-1] = (x[0][0],x[0][1])
         
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
    
    # Lloyds Algo 
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

    #Calculate distances and costs
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

# %% Cost CDF Plots
import matplotlib.pyplot as plt

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
