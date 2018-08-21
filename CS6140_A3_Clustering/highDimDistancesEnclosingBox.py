# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:24:22 2018

@author: Alex
"""

import numpy as np
from scipy.special import factorial
from math import pi
import timeit

start_time = timeit.default_timer()

# Set dimension
d = 4

# Initialize values
vBall = 0
vBox = 0
z = 0
r = 1
i = 0
diff = np.zeros((1000,1))
c = np.zeros((1000,1))
diff[0] = pi
highLim = 1E40
tol = 0.01

# Calculate gamma function
#z = int(d/2) + 1
#gamma = factorial((z-1), exact=True )
# 1, 1.33 and 2 are the gamma results for dimensions 2, 3, 4
gamma = np.array((1,1.33,2))

#for r in range(0,10,0.25):
for d in range(2,5):
    while diff[i] >= tol and diff[i] <= highLim:    
        #vBall = (((pi)**(d/2))/(gamma[d-2]))*(r**d)
        #vBox = (2*r)**d 
        vBall = ((pi)**(d/2))/(gamma[d-2])
        vBox = (2*c[i])**d
        c[i+1] = c[i] + 0.001
        i += 1
        diff[i] = abs(vBall - vBox)
        if diff[i] > 0.90*highLim:
            resultFlag = "Blow Up"
        else:
            resultFlag = "Success"
    

    

# timeit statement
elapsed = timeit.default_timer() - start_time
print('Results:', resultFlag)
print('Execution time (t):', elapsed)
print('Expansion factor (c):', c)


# %% Plot Diff
import matplotlib.pyplot as plt

lastEl = 808
subset1 = diff[0:lastEl,:]
c1 = c[0:lastEl,:]
plt.plot(c1,subset1)

plt.grid(True, which='both')
plt.title("Smallest Enclosing Box (3-d)")
plt.xlabel("Expansion Factor (c)")
plt.ylabel("Ball Box Volume Difference")
plt.show()
