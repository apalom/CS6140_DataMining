import random
import numpy as np
import collections

# initialize variables
trials = 0
prob = 0
bits = 9
word = []
dec = 0
trialMax = 10

# domain and solution
maxN = 1000
correctProb = 1/maxN

r = np.zeros(maxN)

for trials in range (trialMax):

    for n in range(0, maxN):
        dec = 0
        word = np.zeros(maxN)
        word = np.random.randint(2, size=bits)
        #print(word)
        for i in range(0, bits):
            dec += word[i] * (2 ** (bits - 1 - i))
        r[n] = dec
        print(r)

    [unique, counts] = np.unique(r, return_counts=True)
    make = dict(zip(unique, counts))
    selector = random.randint(1, len(make))
    choose = list(make)[selector]
    count = make[choose]
    prob = count / maxN
    trials += 1
    if prob == correctProb:
        print('Success')
        break

    if trials == 10:
        print('FAIL')


# print results
print('Random Numbers Generated (r): {}'.format(r))
print('Selected Number for Probability Check (choose): {}'.format(choose))
print('Count Instances of Selected Number (count): {}'.format(count))
print('Probabililty (prob): {}'.format(prob))
print('Trials to Solution (trials): {}'.format(trials))