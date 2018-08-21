# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:07:46 2018

@author: Alex Palomino
"""

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import matplotlib 

row = 0
doc = np.empty
xDiff = []
yDiff = []
combos = []

doc = np.loadtxt('C1.txt')
doc = np.delete(doc,0,1)

s = plt.scatter(doc[:,0],doc[:,1],marker="x")
plt.title("21 Clusters (Original)")
plt.xlabel("x-coord")
plt.ylabel("y-coord")
plt.show()

#plt.title('Hierarchical Clustering Dendrogram (truncated)')
#plt.xlabel('sample index or (cluster size)')
#plt.ylabel('distance')
#dendrogram(
#    Z1,
#    truncate_mode='lastp',  # show only the last p merged clusters
#    p=4,  # show only the last p merged clusters
#    leaf_rotation=90.,
#    leaf_font_size=12.,
#    show_contracted=True,  # to get a distribution impression in truncated branches
#)
#plt.show()