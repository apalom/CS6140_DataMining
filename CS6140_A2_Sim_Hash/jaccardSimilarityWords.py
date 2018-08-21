
# Initialize Doc X
gramReadX = []
allWordX = []
charsX = []

docX = open("D3.txt","r")

for line in docX:
    for word in line.split():
        allWordX.append(word)

for w in range(len(allWordX)-1):
    gram = allWordX[w] + allWordX[w+1]
    gramReadX.append(gram)

# Initialize Doc Y
gramReadY = []
allWordY = []
charsY = []

docY = open("D4.txt","r")

for line in docY:
    for word in line.split():
        allWordY.append(word)

for w in range(len(allWordY)-1):
    gram = allWordY[w] + allWordY[w+1]
    gramReadY.append(gram)

intersection = len(set.intersection(*[set(gramReadX), set(gramReadY)]))
union = len(set.union(*[set(gramReadX), set(gramReadY)]))
JS = intersection/float(union)

print("JS: {}".format(JS))