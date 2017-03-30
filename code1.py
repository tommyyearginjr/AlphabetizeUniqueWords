#!/usr/bin/python3.5

from collections import Counter

text = "Don't call me Henry; just call me!"
remove = ";!"

for char in remove:
    text = text.replace(char, "")

wordList = []
wordListX = []
wordListXX = []
wordListXXX = []
properNames = ['Henry']
freqDict = []

wordList.append(text.split(" "))

for word in wordList[0]:
    wordListX.append(word)

for word in wordListX:
    for name in properNames:
        if word != name:
            x=word.lower()
            wordListXX.append(x)

a = Counter(wordListXX)

for i in a:
    freqDict.append(i)

freqDict.sort()

print(freqDict)
