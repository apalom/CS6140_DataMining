# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 07:54:46 2018

@author: Alex Palomino
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import timeit

start_time = timeit.default_timer()

# Import data
doc = np.empty
doc = np.loadtxt('C1.txt')
doc = np.delete(doc,0,1)

# Calculate distances and clusters
links = linkage(doc,'complete')
# fcluster(Z, k, criterion='maxclust')

c, coph_dists = cophenet(links, pdist(doc))

elapsed = timeit.default_timer() - start_time
                              
# Plot dendogram of clusters
plt.figure(figsize=(12, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index',fontsize=12)
plt.ylabel('distance',fontsize=12)
dendrogram(links)


# timeit statement
print('Execution time:', elapsed)
print('Correlation coefficient:', c)

# Plot scatter with different colors representing scatter clusters

# SINGLE 
#k1 = [[0,1]]
#k2 = [[2,3]]
#k3 = [[7,8,9,10,11,12,13,14,15,16,17,18,19,20]]

# COMPLETE 
#k1 = [[0,1]]
#k2 = [[7,8,9,10,11,12,13]]
#k3 = [[4,5,6,18,19,20]]

# AVERAGE 
#k1 = [[0,1]]
#k2 = [[2,3]]
#k3 = [[7,8,9,10,11,12,13]]

plt.figure(figsize=(10, 8))
grey = '0.75'
plt.grid(True, which='both')
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.title('Unclustered Scatter')
plt.xlabel('x-coord',fontsize=12)
plt.ylabel('y-coord',fontsize=12)
plt.scatter(doc[:,0], doc[:,1])  # plot all points
#plt.scatter(doc[k1,0], doc[k1,1], c='r')  # plot interesting points in red again
#plt.scatter(doc[k2,0], doc[k2,1], c='g')  # plot interesting points in red again
#plt.scatter(doc[k3,0], doc[k3,1], c='k')  # plot interesting points in red again
plt.show()