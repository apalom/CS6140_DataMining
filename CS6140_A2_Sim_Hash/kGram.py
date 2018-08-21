# Number of k Gram
# How many distinct k-grams are there for each document with each type of k-gram?
# Initialize List
gramRead = []
chars = []
doc = open("D2.txt","r")

for line in doc:
    for c in line:
        chars.append(c)

for c in range(len(chars)-2):
    gram = chars[c] + chars[c+1] + chars[c+2]
    gramRead.append(gram)
    print(c)

print("All kGrams: {}".format(gramRead))
print("Set of kGrams: {}".format(set(sorted(gramRead))))
print("Number of kGrams: {}".format(len(set(gramRead))))