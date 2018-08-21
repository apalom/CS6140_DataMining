
# import libraries
import matplotlib.pyplot as plt
import numpy as np



m = 30
nMax = 210 + 1

# initialize variables
timeExec = []
trials = []
nStep = []

for n in range(1, m):
    # function call
    from couponcollector1 import couponcollector1
    [trials, completeSet, r, k, timeExec] = couponcollector1(n, nMax, m, timeExec)
    print(n)
    nStep.append(n)

# print results
print('Domain range (n): {}'.format(n))
print("Experiment repititions (m): %d" % len(trials))
print('Random Trials to Complete Set (k): {}'.format(k))
print('Expected trials to complete set (k): {:.2f}'.format(completeSet))
# print('Complet Set (r): {}'.format(set(r)))
print('Total Execution Time (s): {:.4f}'.format(sum(timeExec)))

# timeit statement
print('Execution time', timeExec)

# plot time trials
plt.plot(nStep,timeExec)
plt.ylim((0))
plt.xlabel("Domain (n)")
plt.ylabel("Time (s)")
plt.title("Coupon Collector Time Trials n = {}".format(m))
plt.grid(True)
plt.show()

# Prepare for CDF Plot
data_size = len(trials)

# Set bins edges
data_set = sorted(set(trials))
bins = np.append(data_set, data_set[-1] + 1)

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(trials, bins=bins, density=False)

counts = counts.astype(float) / data_size

# Find the cdf
cdf = np.cumsum(counts)

# Plot the cdf
plt.plot(bin_edges[0:-1], cdf, linestyle='--', marker=".", color='b')
plt.ylim((0))
plt.xlabel("Trials (k)")
plt.ylabel("CDF")
plt.title("Coupon Collector CDF")
plt.grid(True)
#plt.show()