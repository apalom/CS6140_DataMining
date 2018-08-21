# -*- coding: utf-8 -*-
"""
k-Median Clustering

Created on Fri Feb 23 13:08:57 2018
@author: Alex Palomino
"""

import numpy as np
from scipy.spatial import distance
import timeit

start_time = timeit.default_timer()

x = np.loadtxt('C3.txt')
x = np.delete(x,0,1)

k = 4
n = len(x)

half = int(n/2)
halfIdx = 0
dstPhiC = np.empty
dstTmp = np.empty
wx = np.zeros((n,1))
Px = np.zeros((n,1))
PxDist = np.zeros((n,1))
dst = np.zeros((n,k))
dstCol =  np.zeros((n,1))
dstSort = np.zeros((n,1))
phi = np.zeros((n,1))
c = np.zeros((k,5))
phiCX = np.zeros((k,5))
centerCost = np.zeros((n,1))
maxTrials = 50
cost = np.zeros((k,1))
argMed = 0

#c[0] = (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4])
c[0] = x[0]

for j in range(0,n):
    phi[j] = 1

for i in range(1,k+1):
    m = 0
    c[i-1] = x[0]
    
    # Update cluster center to further point
    for j in range(0,n):
        dstPhiCtmp = distance.euclidean(x[j],c[int(phi[j]-1)])
        dstCol[j] = distance.euclidean(x[j],c[int(phi[j]-1)])
     
    dstSort = np.sort(dstCol,0)
    
    for j in range(0,n):
        argMed = dstSort[half]
        if dstCol[j] == argMed:
            halfIdx = j
            c[i-1] = x[j]
  
    # Assign point to cluster if within phiC distance         
    for j in range(0,n):   
        dstPhiCtmp = distance.euclidean(x[j],c[int(phi[j]-1)])
        dstXjCi = distance.euclidean(x[j],c[i-1])
        
        if dstPhiCtmp > dstXjCi:
            phi[j] = i


# %% Scatter Plot
import matplotlib.pyplot as plt

k1 = []
k2 = []
k3 = []
k4 = []

for j in range(0,n):
    if phi[j] == 1:
        k1.append(j)
    if phi[j] == 2:
        k2.append(j)
    if phi[j] == 3:
        k3.append(j)
    if phi[j] == 4:
        k4.append(j)

#s = plt.scatter(x[:,0],x[:,1],marker="x")

plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')

plt.scatter(x[k1,0], x[k1,1], c='r',marker=".")
plt.scatter(x[k2,0], x[k2,1], c='g',marker=".")
plt.scatter(x[k3,0], x[k3,1], c='b',marker=".")
plt.scatter(x[k4,0], x[k4,1], c='m',marker=".")
plt.scatter(c[0,0],c[0,1],c='k',marker="x")
plt.scatter(c[1,0],c[1,1],c='k',marker="x")
plt.scatter(c[2,0],c[2,1],c='k',marker="x")
plt.scatter(c[3,0],c[3,1], c='k',marker="x")

plt.title("Clustered Data (k = 4)")
plt.xlabel("x-coord")
plt.ylabel("y-coord")
plt.show()            

# %% Scatter Plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k1 = []
k2 = []
k3 = []
k4 = []

for j in range(0,n):
    if phi[j] == 1:
        k1.append(j)
    if phi[j] == 2:
        k2.append(j)
    if phi[j] == 3:
        k3.append(j)
    if phi[j] == 4:
        k4.append(j)

#s = plt.scatter(x[:,0],x[:,1],marker="x")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.grid(True, which='both')
#plt.axvline(x=0, color='k')
#plt.axhline(y=0, color='k')

plt.scatter(x[k1,0], x[k1,1], x[k1,2], c='r',marker=".")
plt.scatter(x[k2,0], x[k2,1], x[k1,2], c='g',marker=".")
plt.scatter(x[k3,0], x[k3,1], x[k1,2], c='b',marker=".")
plt.scatter(x[k4,0], x[k4,1], x[k4,2], c='m',marker=".")


plt.scatter(c[0,0],c[0,1],c='k',marker="x")
plt.scatter(c[1,0],c[1,1],c='k',marker="x")
plt.scatter(c[2,0],c[2,1],c='k',marker="x")
plt.scatter(c[3,0],c[3,1],c='k',marker="x")
#plt.scatter(phiCX[0,0],phiCX[0,1],c='k',marker="v")
#plt.scatter(phiCX[1,0],phiCX[1,1],c='k',marker="v")
#plt.scatter(phiCX[2,0],phiCX[2,1],c='k',marker="v")

plt.title("K-Means++ Clustered Data (k = 3)")
#plt.xlabel("x-coord")
#plt.ylabel("y-coord")
plt.show()

# %% Cost CDF Plots

n_bins = 25

costC1 = np.sort(cost[0,:])
costC2 = np.sort(cost[1,:])
costC3 = np.sort(cost[2,:])
costC4 = np.sort(cost[3,:])

# Plot Max Center Cost
fig, ax = plt.subplots(figsize=(12, 6))
n, bins, patches = ax.hist(costC1, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 1')

n, bins, patches = ax.hist(costC2, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 2')

n, bins, patches = ax.hist(costC3, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 3')

n, bins, patches = ax.hist(costC4, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Center 4')


ax.grid(True)
ax.legend(loc=2)
ax.set_title('4 Cluster Cost CDF (50 runs on C3 Data)')
ax.set_xlabel('Max Center Cost')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

