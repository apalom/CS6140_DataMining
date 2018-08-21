
# import libraries
import matplotlib.pyplot as plt

# initialize variables
timeExec = []
trials = []
nStep = []

# function call
from birthdayparadox import birthdayparadox

m = 10000
nMax = 1000001
for n in range(1, nMax+1, 100000):
    [trials, preCollision, timeExec] = birthdayparadox(n, m, timeExec)
    print(n)
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
plt.ylim([0, 400])
plt.xlabel("Domain (n)")
plt.ylabel("Time (s)")
plt.title("Birthday Paradox Time Trials m = {} ".format(m))
plt.grid(True)
plt.show()