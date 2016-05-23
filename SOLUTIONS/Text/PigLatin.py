"""
Pig Latin - Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 
Read Wikipedia for more information on rules.
"""

def pig_latin(s):
	token_phrase = s.split()
	new_phrase = ''
	for i in range(0,len(token_phrase)):
		if token_phrase[i][0] in {'a', 'e', 'i', 'o', 'u'}:
			token_phrase[i] += 'yay'
		else:
			token_phrase[i] += token_phrase[i][0] + 'ay'
			token_phrase[i] = token_phrase[i][:0] + token_phrase[i][1:]
		new_phrase += token_phrase[i] + ' '
	return new_phrase
	
print(pig_latin(input('Enter a word or phrase to convert to pig latin: ')))
input('Press enter to exit')