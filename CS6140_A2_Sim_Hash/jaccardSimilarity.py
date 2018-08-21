
# Initialize Doc X Values
gramReadX = []
charsX = []

# Open File X
docX = open("D3.txt","r")

for line in docX:
    for c in line:
        charsX.append(c)

for c in range(len(charsX)-1):
    gramX = charsX[c] + charsX[c+1]
    gramReadX.append(gramX)

# Initialize Doc Y Values
gramReadY = []
charsY = []

# Open File Y
docY = open("D4.txt","r")

for line in docY:
    for c in line:
        charsY.append(c)

for c in range(len(charsY)-1):
    gramY = charsY[c] + charsY[c+1]
    gramReadY.append(gramY)


intersection = len(set.intersection(*[set(gramReadX), set(gramReadY)]))
union = len(set.union(*[set(gramReadX), set(gramReadY)]))
JS = intersection/float(union)

print("JS: {}".format(JS))