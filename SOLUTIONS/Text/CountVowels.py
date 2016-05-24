"""
Count Vowels - Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found.
"""

vowels = ['a','e','i','o','u']
vowel_count = [0,0,0,0,0]
def count_vowels(s):
	for i in range(0, len(s)):
		if s[i] in vowels:
			for j in range(0, len(vowels)):
				if s[i] is vowels[j]:
					vowel_count[j] += 1
					
	total = 0
	for v in range(0, len(vowel_count)):
		total += vowel_count[v]
		print(vowels[v] + ' : ' + str(vowel_count[v]))
	return total
	
print('Total number of vowels: ' + str(count_vowels(input('Enter a word or phrase to count the vowels: ').lower())))
