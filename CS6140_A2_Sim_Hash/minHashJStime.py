
import numpy as np
import random
import timeit

start_time = timeit.default_timer()

# Number of k Gram
k = 3

# Initialize
timeExec = []
gramReadX = []
gramReadY = []
flag = 'False'

#t = [20, 60, 150, 300, 600]

with open("D1.txt","r") as X:
    while True:
        c = X.read(k)
        gramReadX.append(c)
        if not c:
          break
kGramX = list(set(gramReadX))
print("kGramX: {}".format(kGramX))
uniqueX = len(set(gramReadX))
print("UniqueX: {}".format(uniqueX))

with open("D2.txt", "r") as Y:
        while True:
            c = Y.read(k)
            gramReadY.append(c)
            if not c:
                break
kGramY = list(set(gramReadY))
print("kGramY: {}".format(kGramY))
uniqueY = len(set(gramReadY))
print("UniqueY: {}".format(uniqueY))

tMax = 15000
matches = np.zeros((tMax, len(kGramY)))
f = open( 'output.txt', 'w' )
for t in range(tMax):
    random.shuffle(kGramX)
    random.shuffle(kGramY)

    for i in range(393):

        if kGramX[i] == kGramY[i]:
            matches[t][i] = 1
            f.write(repr(matches[t][i]) + '\n')
        else:
            matches[t][i] = 0
            f.write(repr(matches[t][i]) + ' ')

f.close()

print("Sum: {}".format(np.sum(matches)))

JS = (1/tMax)*np.sum(matches)

print("JS: {}".format(JS))

elapsed = timeit.default_timer() - start_time
timeExec.append(elapsed)

# timeit statement
print('Execution time', timeExec)
