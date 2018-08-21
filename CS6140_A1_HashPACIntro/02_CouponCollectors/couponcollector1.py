#from numba import jit

#@jit(nopython=True)
def couponcollector1(n, nMax, m, timeExec):
    # Generate random numbers in the domain [n] until two have the same value. How many
    # random trials did this take? We will use k to represent this value.
    # Consider a domain size of n = 4000


    # import libraries
    import timeit
    import random
    import numpy as np

    start_time = timeit.default_timer()

    trials = []  # stores number of trials to collision for each experiment

    # find number of trials to encounter collision. Repeat m times.
    for n in range(1, nMax):
        print(n)
        k = 0  # number of trials k
        flag = 'FALSE'
        r = np.empty(nMax)
        #r = []
        while flag == 'FALSE':
            k += 1
            r[n] =(random.randint(1, nMax))
            print(r[n])
            #print(len(set(r)))
            if len(set(r)) == n:
                flag = 'TRUE'
                trials.append(k)

    elapsed = timeit.default_timer() - start_time
    timeExec.append(elapsed)
    # empirical estimation of expected trials before collision
    completeSet = sum(trials) / m

    return trials, completeSet, r, k, timeExec