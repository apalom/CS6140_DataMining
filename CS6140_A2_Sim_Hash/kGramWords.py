# Number of k Gram

# Initialize List
gramRead = []
allWord = []
chars = []
i = 0
doc = open("D4.txt","r")

for line in doc:
    for word in line.split():
        allWord.append(word)

print(allWord)
print(len(allWord))

for w in range(len(allWord)-1):
    gram = allWord[w] + allWord[w+1]
    gramRead.append(gram)
    print(w)

print("All kGrams: {}".format(gramRead))
print("Set of kGrams: {}".format(set(sorted(gramRead))))
print("Number of kGrams: {}".format(len(set(gramRead))))