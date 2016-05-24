"""
Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar"
"""

def reverse_string(s):
	reverse = ''
	for i in reversed(range(len(s))):
		reverse += s[i]
	return reverse

def check_palindrome(s):
	reverse = reverse_string(s)
	if s == reverse:
		return 'It is a palindrome!'
	else:
		return 'It is not a palindrome!'
		
print(check_palindrome(input('Enter a word or phrase to check if it\'s a palindrome: ').lower()))