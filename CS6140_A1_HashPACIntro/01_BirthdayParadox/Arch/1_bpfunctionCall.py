
# import libraries
import matplotlib.pyplot as plt

# initialize variables
timeExec = []
trials = []
nStep = []

# funtion call
from birthdayparadox import birthdayparadox

m = 300
nMax = 4000
for n in range(1,nMax):
    [trials, preCollision, timeExec] = birthdayparadox(n,m,timeExec)
    nStep.append(n)

# print results
print('Domain range (n): {}'.format(n))
print("Total trials run (m): %d" % len(trials))
print('Expected trials to collision (k): {:.2f}'.format(preCollision))
print('Total Execution Time (s): {:.4f}'.format(sum(timeExec)))

# timeit statement
print('Execution time', timeExec)

# plot
plt.plot(nStep,timeExec)
plt.ylim((0))
plt.xlabel("Domain (n)")
plt.ylabel("Time (s)")
plt.title("Birthday Paradox Time Trials n = {}".format(nMax))
plt.grid(True)
plt.show()