from random import randint
import sys

consonants = ['m', 'f', 'r', 'g', 'k', 'kh', 'h', 't', 'p', 'th', 's', 'sh', 'b', 'v', 'd', 'ch', 'l', 'll', 'q', 'zh']
vowels = ['a','e','u','o','i','y']

# dipthongs create:
#  oe, ae, au, etc, double letters are long, y is pronounced as Finnish y

def gensyl(): #generate a syllable
	stype = randint(0,2)
	if stype == 0: #open syllable
		if randint(0,1) == 0: #1 vowel
			vowel = vowels[randint(0,(len(vowels)-1))]
		else: #diphthong
			vowel = vowels[randint(0,(len(vowels)-1))]+vowels[randint(0,(len(vowels)-1))]
		return consonants[randint(0,(len(consonants)-1))]+vowel
	elif stype == 1: #closed syllable
		if randint(0,1) == 0: #1 vowel
			vowel = vowels[randint(0,(len(vowels)-1))]
		else: #diphthong
			vowel = vowels[randint(0,(len(vowels)-1))]+vowels[randint(0,(len(vowels)-1))]
		return consonants[randint(0,(len(consonants)-1))]+vowel+consonants[randint(0,(len(consonants)-1))]
	else:
		if randint(0,1) == 0: #1 vowel
			vowel = vowels[randint(0,(len(vowels)-1))]
		else: #diphthong
			vowel = vowels[randint(0,(len(vowels)-1))]+vowels[randint(0,(len(vowels)-1))]
		return vowel

def genword(n): #generate a full word of n syllables
	word = ""
	for i in range(n):
		word+=gensyl()
	return word

if len(sys.argv) > 1 and sys.argv[1] == "short":
	print(genword(1))
else:
	print(genword(randint(1,3)))