from collections import Counter
def wordcount(text):
	words = text.split()
	return words
def charcount(text):
	lwords = text.lower()
	charcountdic = Counter(lwords)
	return charcountdic