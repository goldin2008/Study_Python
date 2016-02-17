# Chapter 9 Dictionaries

'''
The function dict creates a new dictionary with no items. Because dict is the
name of a built-in function, you should avoid using it as a variable name.

The curly brackets, {}, represent an empty dictionary. To add items to the dictionary,
you can use square brackets

The in operator works on dictionaries; it tells you whether something appears as
a key in the dictionary (appearing as a value is not good enough).

To see whether something appears as a value in a dictionary, you can use the
method values, which returns the values as a list, and then use the in operator.

'''

eng2sp = dict()
print eng2sp
eng2sp['one'] = 'uno'
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print 'one' in eng2sp # True
print 'uno' in eng2sp # False

vals = eng2sp.values()
print 'uno' in vals


# Dictionary as a set of counters
'''
You could create a dictionary with characters as keys and counters as the
corresponding values. The first time you see a character, you would add
an item to the dictionary. After that you would increment the value of an
existing item.
'''

word = 'brontosaurus'
d = dict()
for c in word:
	# if c not in d:
	# 	d[c] = 1
	# else:
	# 	d[c] = d[c] + 1
	d[c] = d.get(c,0) + 1
print d


# Dictionaries and files
'''
We will write a Python program to read through the lines of the file, break each
line into a list of words, and then loop through each of the words in the line and
count each word using a dictionary.
'''

fname = raw_input('Enter the file name: ')

try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
print counts


# Looping and dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
	print key, counts[key]


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
	if counts[key] > 10 :
		print key, counts[key]


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = counts.keys()
print lst
lst.sort()
for key in lst:
	print key, counts[key]


# Advanced text parsing
'''
We can solve both these problems by using the string methods lower,
punctuation, and translate. The translate is the most subtle of the methods.
We use translate to remove all punctuation and lower to force the line to lowercase.
Otherwise the program is unchanged. Note that for Python 2.5 and earlier,
translate does not accept None as the first parameter so use this code instead for
the translate call.
'''

import string # New Code
fname = raw_input('Enter the file name: ')

try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

counts = dict()
for line in fhand:
	line = line.translate(None, string.punctuation) # New Code
	line = line.lower() # New Code
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
print counts
