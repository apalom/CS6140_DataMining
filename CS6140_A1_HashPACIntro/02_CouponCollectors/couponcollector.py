#from numba import jit

#@jit(nopython=True)
def couponcollector(n, nMax, m, timeExec):
    # Generate random numbers in the domain [n] until two have the same value. How many
    # random trials did this take? We will use k to represent this value.
    # Consider a domain size of n = 4000


    # import libraries
    import timeit
    import random
    import numpy as np

    start_time = timeit.default_timer()

    trials = []  # stores number of trials to collision for each experiment

    # find number of trials to encounter complete set. Repeat m times.
    for i in range(m):
        k = 0  # number of trials k
        flag = 'FALSE'
        #r = np.empty(nMax)
        r = []
        while flag == 'FALSE':
            k += 1
            r.append(random.randint(1, n))
            #print(r)
            #print(len(set(r)))
            if len(set(r)) == n:
                flag = 'TRUE'
                trials.append(k)

    elapsed = timeit.default_timer() - start_time
    timeExec.append(elapsed)
    # empirical estimation of expected trials before collision
    completeSet = sum(trials) / m

    return trials, completeSet, r, k, timeExec