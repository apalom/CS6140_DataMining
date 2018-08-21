# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:51:04 2018

@author: Alex
"""

import numpy as np
import math
from matplotlib import pyplot as plt

print(math.pi)
a=(math.pi)**0.5
d=2
b=[]
c=np.zeros((10,1))
x=np.zeros((10,1))
for d in range(2,22,2):
    b=(math.factorial(d/2))**(1/d)
    g=d/2
    x[int(g)-1]=g
    c[int(g)-1]=(a/b)
    


plt.figure(figsize=(10, 5))           
plt.scatter(2*x, c, c='r')
plt.show()