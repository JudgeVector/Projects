"""
Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
"""
f = 'string.txt'
my_string = open(f, 'r').read()
split_str = my_string.split()
print('The phrase: (' + my_string + ') contains ' + str(len(split_str)) + ' words.')