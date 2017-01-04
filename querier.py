import wordgen

words = open("words.txt", 'r')
dictionary = open("dict.txt", 'w+')
row = words.readlines()
dictrow = []

def checkDup(word):
    if word not in dictrow:
        print("True")
    else:
        print("False")

def gendict():
    for line in row:
        newword = wordgen.wordgen()
        while newword in dictrow:
            print(line + " is a duplicate")
            newword = wordgen.wordgen()
        dictionary.write(line + newword +"\n\n")
        dictrow.append(newword)

gendict()

#checkDup("AA")
