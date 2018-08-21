
import numpy as np
import matplotlib.pyplot as plt

trials = [300, 3000, 5000, 6000, 8000, 10000]
time = [1.960446202, 2.547862608, 3.072099832, 3.215840969, 3.770551227, 4.239583871]

trials = [] # stores number of trials to collision for each experiment
m = 1 # monte carlo
n = 4000 # domain
nMax = 1000000

# Find number of trials to encounter collision. Repeat m times.


# Plot the length
plt.plot(trials,time)
plt.xlabel("Trials (k)")
plt.ylabel("Seconds")
plt.title("Birthday Paradox Time to Execute ")
plt.grid(True)

plt.show()