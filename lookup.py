import wordgen
import random
import fileinput

dictionary = open("dictionary.txt", 'a+')
dictionary.seek(0)
text = dictionary.read().strip().split()
alldefs = list(text)
allwords = list(text)
del text[1::2]
del allwords[::2]
dictionary.seek(2)

def check(w):
    if w in text:
        print(alldefs[alldefs.index(w)+1])
        return False
    else:
        return True

def getWord(query):
    if check(query.replace(" ", "-").lower()):
        dictionary.seek(0)
        newword = wordgen.wordgen()
        while newword in allwords:
            print("Alert: 001")
            newword = wordgen.wordgen()
        dictionary.seek(2)
        dictionary.write("\n" + query.replace(" ", "-") + "\t\t" + newword)
        print(newword)
        return newword

#depreciated
def changePhonemes():
    for word in allwords:
        if "h" in word:
            syl = wordgen.consonants[random.randint(0, len(wordgen.consonants)-1)]
            newWord = word.replace("h", syl)
            #print(word + "\t\t" + newWord) #diagnostic

#print(modQuery("some-word").lower())
def getAndPrintWord():
    print("Input English Word -> ", end=" ")
    request = str.lower(input())
    print(request, " -> ", end=" ")
    getWord(request)

getAndPrintWord()
