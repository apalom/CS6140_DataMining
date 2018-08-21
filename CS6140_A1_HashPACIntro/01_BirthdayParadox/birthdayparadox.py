
def birthdayparadox(n, m, timeExec):
    # Generate random numbers in the domain [n] until two have the same value. How many
    # random trials did this take? We will use k to represent this value.
    # Consider a domain size of n = 4000


    # import libraries
    import timeit
    import random

    start_time = timeit.default_timer()

    trials = []  # stores number of trials to collision for each experiment

    # find number of trials to encounter collision. Repeat m times.
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

    elapsed = timeit.default_timer() - start_time
    timeExec.append(elapsed)

    # empirical estimation of expected trials before collision
    preCollision = sum(trials) / m

    return trials, preCollision, timeExec
