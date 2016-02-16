# Chapter 3 Catching exceptions using try and except

inp = raw_input('Enter Fahrenheit Temperature:')
try:
	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print cel
except:
	print 'Please enter a number'

# Chapter 5 The Difference between continue and break
'''
If the user types done, the break statement exits the loop. Otherwise the program echoes whatever
the user types and goes back to the top of the loop.
All the lines are printed except the one that starts with the hash sign because when
the continue is executed, it ends the current iteration and jumps back to the while
statement to start the next iteration, thus skipping the print statement.
'''

while True:
	line = raw_input('> ')
	if line[0] == '#' :
		continue
	if line == 'done':
		break
	print line
print 'Done!'

# Chapter 6 String
'''
One common task is to remove white space (spaces, tabs, or newlines) from the
beginning and end of a string using the strip method.
You will note that startswith requires case to match, so sometimes we take a line
and map it all to lowercase before we do any checking using the lower method.
'''

line.strip()
line.lower()
ine.startswith('p')

'''
First, we will find the position of the at-sign in the string. Then we will find the
position of the first space after the at-sign. And then we will use string slicing to
extract the portion of the string which we are looking for.
'''

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos)
print sppos
host = data[atpos+1:sppos]
print host

'''
Format operator
'''

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
