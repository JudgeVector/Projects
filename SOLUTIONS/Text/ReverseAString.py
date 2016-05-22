"""
Reverse a String - Enter a string and the program will reverse it and print it out.
"""

def reverse_string(s):
	reverse = ''
	for i in reversed(range(len(s))):
		reverse += s[i]
	return reverse
	
usr_string = str(input('Enter a string to be reversed: '))
print(reverse_string(usr_string))
input('Press enter to exit')