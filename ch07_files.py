# Chapter 7 Files

# Reading files
'''
If the open is successful, the operating system returns us a file handle. The file
handle is not the actual data contained in the file, but instead it is a "handle" that
we can use to read the data. You are given a handle if the requested file exists and
you have the proper permissions to read the file.

While the file handle does not contain the data for the file, it is quite easy to
construct a for loop to read through and count each of the lines in a file.

When the file is read using a for loop in this manner, Python takes care of splitting
the data in the file into separate lines using the newline character. Python reads
each line through the newline and includes the newline as the last character in the
line variable for each iteration of the for loop.
'''

fhand = open('mbox.txt')
count = 0
for line in fhand:
	count = count + 1
print 'Line Count:', count


'''
If you know the file is relatively small compared to the size of your main memory,
you can read the whole file into one string using the read method on the file
handle.

When the file is read in this manner, all the characters including all of the lines
and newline characters are one big string in the variable inp. Remember that this
form of the open function should only be used if the file data will fit comfortably
in the main memory of your computer.

If the file is too large to fit in main memory, you should write your program to
read the file in chunks using a for or while loop.
'''

fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)

# Searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:') :
		print line

'''
As your file processing programs get more complicated, you may want to structure
your search loops using continue. The basic idea of the search loop is that you
are looking for "interesting" lines and effectively skipping "uninteresting" lines.
And then when we find an interesting line, we do something with that line.
'''

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	# Skip 'uninteresting lines'
	if not line.startswith('From:') :
		continue
	# Process our 'interesting' line
	print line



# Letting the user choose the file name by using the try/except structure
fname = raw_input('Enter the file name: ')

try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

count = 0
for line in fhand:
	if line.startswith('Subject:') :
		count = count + 1
print 'There were', count, 'subject lines in', fname



# Writing files

'''
To write a file, you have to open it with mode 'w' as a second parameter.

If the file already exists, opening it in write mode clears out the old data and starts
fresh, so be careful! If the file doesn’t exist, a new one is created.

The write method of the file handle object puts data into the file.
Again, the file object keeps track of where it is, so if you call write again, it adds
the new data to the end.
We must make sure to manage the ends of lines as we write to the file by explicitly
inserting the newline character when we want to end a line. The print statement
automatically appends a newline, but the write method does not add the newline
automatically.

When you are done writing, you have to close the file to make sure that the last bit
of data is physically written to the disk so it will not be lost if the power goes off.

We could close the files which we open for read as well, but we can be a little
sloppy if we are only opening a few files since Python makes sure that all open
files are closed when the program ends. When we are writing files, we want to
explicitly close the files so as to leave nothing to chance.
'''

fout = open('output.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()
