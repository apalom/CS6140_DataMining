
import numpy as np
import random

import timeit

start_time = timeit.default_timer()
timeExec = []

# Initialize Doc X Values
gramReadX = []
charsX = []

# Open File X
docX = open("D1.txt","r")
for line in docX:
    for c in line:
        charsX.append(c)

for c in range(len(charsX)-2):
    gramX = charsX[c] + charsX[c+1] + charsX[c+2]
    gramReadX.append(gramX)

# Print Doc X Gram Results
kGramX = list(set(gramReadX))
print("kGramX: {}".format(kGramX))
uniqueX = len(set(gramReadX))
print("UniqueX: {}".format(uniqueX))

# Initialize Doc Y Values
gramReadY = []
charsY = []

# Open File Y
docY = open("D2.txt","r")
for line in docY:
    for c in line:
        charsY.append(c)

for c in range(len(charsY)-2):
    gramY = charsY[c] + charsY[c+1] + charsY[c+2]
    gramReadY.append(gramY)

# Print Doc Y Gram Results
kGramY = list(set(gramReadY))
print("kGramY: {}".format(kGramY))
uniqueY = len(set(gramReadY))
print("UniqueY: {}".format(uniqueY))

#t = [20, 60, 150, 300, 600]

tMax = 15000
matches = np.zeros((tMax, uniqueY))
open('output.txt', 'w').close()
f = open( 'output.txt', 'w' )
for t in range(tMax):
    random.shuffle(kGramX)
    random.shuffle(kGramY)

    for i in range(uniqueY):

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

