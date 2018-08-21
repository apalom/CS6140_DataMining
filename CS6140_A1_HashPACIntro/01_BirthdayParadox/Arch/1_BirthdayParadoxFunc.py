
def birthdayparadox(n, m):
    # Generate random numbers in the domain [n] until two have the same value. How many
    # random trials did this take? We will use k to represent this value.
    # Consider a domain size of n = 4000

    import timeit

    mysetup = "import random"

    mycode = ''' 
     
    import numpy as np
    import matplotlib.pyplot as plt
    trials = []  # stores number of trials to collision for each experiment
    # Find number of trials to encounter collision. Repeat m times.
    for i in range(m):
        k = 0  # number of trials k
        flag = 'FALSE'
        r = []
        while flag == 'FALSE':
            k += 1
            r.append(random.randint(1, n))
            if len(r) != len(set(r)):
                flag = 'TRUE'
                trials.append(k)
    # Empirical estimation of expected trials before collision
    preCollision = sum(trials) / m
    print('Domain range (n): {}'.format(n))
    print("Total trials run (m): %d" % len(trials))
    print('Expected trials to collision (k): {:.2f}'.format(preCollision))

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
    plt.title("Birthday Paradox CDF")
    plt.grid(True)

    plt.show()

    '''

    # timeit statement
    t = timeit.timeit(setup=mysetup, stmt=mycode, number=1)
    print('Execution time', t)

    return
