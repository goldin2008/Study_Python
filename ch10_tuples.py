# Chapter 10 Tuples
# encoding=utf8

t = tuple()
print t

#  Comparing tuples

'''
Decorate a sequence by building a list of tuples with one or more sort keys preceding
the elements from the sequence,
Sort the list of tuples using the Python built-in sort, and
Undecorate by extracting the sorted elements of the sequence.

For example, suppose you have a list of words and you want to sort them from
longest to shortest.
DSU: Abbreviation of “decorate-sort-undecorate”, a pattern that involves building
a list of tuples, sorting, and extracting part of the result.
'''

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()

for word in words:
    t.append((len(word), word))

t.sort(reverse=True)
res = list()

for length, word in t:
    res.append(word)

print res

l = list()
l.append(1)
l.append('a')
print l

# Tuple assignment
'''
Stylistically when we use a tuple on the left side of the assignment statement, we
omit the parentheses, but the following is an equally valid syntax.
The return value from split is a list with two elements; the first element is assigned
to uname, the second to domain.
'''
m = [ 'have', 'fun' ]
x, y = m
print x
print y

(a, b) = m
print a
print b

addr = 'monty@python.org'
uname, domain = addr.split('@')
print uname
print domain

#  Dictionaries and tuples
'''
Dictionaries have a method called items that returns a list of tuples, where each
tuple is a key-value pair.
As you should expect from a dictionary, the items are in no particular order.
However, since the list of tuples is a list, and tuples are comparable, we can now
sort the list of tuples. Converting a dictionary to a list of tuples is a way for us to
output the contents of a dictionary sorted by key.
'''

d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t
t.sort()
print t

# Multiple assignment with dictionaries
'''
Combining items, tuple assignment, and for, you can see a nice code pattern for
traversing the keys and values of a dictionary in a single loop.
This loop has two iteration variables because items returns a list of tuples and
key, val is a tuple assignment that successively iterates through each of the keyvalue
pairs in the dictionary.
If we combine these two techniques, we can print out the contents of a dictionary
sorted by the value stored in each key-value pair.
To do this, we first make a list of tuples where each tuple is (value, key). The
items method would give us a list of (key, value) tuples—but this time we
want to sort by value, not key. Once we have constructed the list with the value key
tuples, it is a simple matter to sort the list in reverse order and print out the new, sorted list.
'''

for key, val in d.items():
    print val, key

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
    l.append( (val, key) )

print l
l.sort(reverse=True)
print l

# The most common words
'''
The first part of the program which reads the file and computes the dictionary
that maps each word to the count of words in the document is unchanged. But
instead of simply printing out counts and ending the program, we construct a list
of (val, key) tuples and then sort the list in reverse order.
Since the value is first, it will be used for the comparisons. If there is more than
one tuple with the same value, it will look at the second element (the key), so
tuples where the value is the same will be further sorted by the alphabetical order
of the key.
At the end we write a nice for loop which does a multiple assignment iteration
and prints out the ten most common words by iterating through a slice of the list
(lst[:10]).
So now the output finally looks like what we want for our word frequency analysis.

The fact that this complex data parsing and analysis can be done with an easy-tounderstand
19-line Python program is one reason why Python is a good choice as
a language for exploring information.
'''
import string
fhand = open('romeo-full.txt')
# print fhand
# print fhand.read()
counts = dict()

for line in fhand:
    line = line.translate(None, string.punctuation)
    # print line
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()

for key, val in counts.items():
    lst.append( (val, key) )
    lst.sort(reverse=True)

for key, val in lst[:10] :
    print key, val


# Using tuples as keys in dictionaries
'''
Because tuples are hashable and lists are not, if we want to create a composite
key to use in a dictionary we must use a tuple as the key.
We would encounter a composite key if we wanted to create a telephone directory
that maps from last-name, first-name pairs to telephone numbers. Assuming
that we have defined the variables last, first, and number, we could write a
dictionary assignment statement as follows.
The expression in brackets is a tuple. We could use tuple assignment in a for loop
to traverse this dictionary.
This loop traverses the keys in directory, which are tuples. It assigns the elements
of each tuple to last and first, then prints the name and corresponding
telephone number.

directory[last,first] = number
'''

directory = dict()
directory['Yu','Lei'] = 119
print directory

for last, first in directory:
    print first, last, directory[last,first]


# Sequences: strings, lists, and tuples—Oh My!

'''
Summary for data structure

Strings are immutable
Lists are mutalbe
Tuples are immutable

In many contexts, the different kinds of sequences (strings, lists, and tuples) can
be used interchangeably. So how and why do you choose one over the others?
To start with the obvious, strings are more limited than other sequences because
the elements have to be characters. They are also immutable. If you need the
ability to change the characters in a string (as opposed to creating a new string),
you might want to use a list of characters instead.

Lists are more common than tuples, mostly because they are mutable. But there
are a few cases where you might prefer tuples：
1. In some contexts, like a return statement, it is syntactically simpler to
create a tuple than a list. In other contexts, you might prefer a list.
2. If you want to use a sequence as a dictionary key, you have to use an immutable
type like a tuple or string.
3. If you are passing a sequence as an argument to a function, using tuples
reduces the potential for unexpected behavior due to aliasing.

Because tuples are immutable, they don’t provide methods like sort and reverse,
which modify existing lists. However Python provides the built-in functions
sorted and reversed, which take any sequence as a parameter and return a new
sequence with the same elements in a different order.

hashable: A type that has a hash function. Immutable types like integers, floats,
and strings are hashable; mutable types like lists and dictionaries are not.
'''
