import random
import numpy as np

word = []

bits = 9
word = np.random.randint(2, size=bits)
dec = 0

for i in range(0,bits):
    print(i)
    dec += word[i]*(2**(bits-1-i))

print(word)
print(dec)



