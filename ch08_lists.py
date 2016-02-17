# Chapter 8 Lists

# Traversing a list

'''
The most common way to traverse the elements of a list is with a for loop. The
syntax is the same as for strings.

This works well if you only need to read the elements of the list. But if you want
to write or update the elements, you need the indices. A common way to do that
is to combine the functions range and len.
'''

for cheese in cheeses:
	print cheese

for i in range(len(numbers)):
	numbers[i] = numbers[i] * 2


# List operations
'''
The + operator concatenates lists,
Similarly, the * operator repeats a list a given number of times.
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c
print a * 4

# List methods
t = ['a', 'b', 'c']
t.append('d')
print t
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print t1
t.sort()
print t


# Deleting elements
t = ['a', 'b', 'c']
x = t.pop(1)
print t
del t[1]
t.remove('b')


# Lists and functions
'''
We make an empty list before the loop starts, and then each time we have a number,
we append it to the list. At the end of the program, we simply compute the sum of
the numbers in the list and divide it by the count of the numbers in the list to come
up with the average.
'''

numlist = list()
while ( True ) :
	inp = raw_input('Enter a number: ')
	if inp == 'done' : break
	value = float(inp)
	numlist.append(value)

average = sum(numlist) / len(numlist)
print 'Average:', average



# Lists and strings
'''
A string is a sequence of characters and a list is a sequence of values, but a list
of characters is not the same as a string. To convert from a string to a list of
characters, you can use list.
The list function breaks a string into individual letters. If you want to break a
string into words, you can use the split method.

You can call split with an optional argument called a delimiter that specifies
which characters to use as word boundaries. The following example uses a hyphen
as a delimiter.

join is the inverse of split. It takes a list of strings and concatenates the elements.
join is a string method, so you have to invoke it on the delimiter and pass
the list as a parameter.

In this case the delimiter is a space character, so join puts a space between words.
To concatenate strings without spaces, you can use the empty string, '', as a
delimiter.
'''

s = 'spam'
t = list(s)
print t

s = 'pining for the fjords'
t = s.split()
print t

s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
print s
print s.split(delimiter)


t = ['pining', 'for', 'the', 'fjords']
delimiter = '@'
delimiter.join(t)
print delimiter
print delimiter.join(t)


# List arguments

'''
It is important to distinguish between operations that modify lists and operations
that create new lists. For example, the append method modifies a list, but the +
operator creates a new list.
This difference is important when you write functions that are supposed to modify
lists. For example, this function does not delete the head of a list.
'''

t1 = [1, 2]
t2 = t1.append(3)
print t1
print t2

t3 = t1 + [3]
print t3
