# Chapter 12 Network Programming

'''
Python program that makes a connection to a web server and follows the
rules of the HTTP protocol to requests a document and display what the server
sends back.
'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
	data = mysock.recv(512)
	if ( len(data) < 1 ) :
		break
	print data

mysock.close()


#Retrieving an image over HTTP
'''
send and receive data over HTTP using the socket library
'''

import socket
import time
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
count = 0
picture = "";

while True:
	data = mysock.recv(5120)
	if ( len(data) < 1 ) : break
	# time.sleep(0.25)
	count = count + len(data)
	print len(data),count
	picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n");
print 'Header length',pos
print picture[:pos]
# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")
fhand.write(picture);
fhand.close()


'''
Retrieving web pages with urllib
Once the web page has been opened with urllib.urlopen, we can treat it like a
file and read through it using a for loop.
When the program runs, we only see the output of the contents of the file. The
headers are still sent, but the urllib code consumes the headers and only returns
the data to us.
Again, once we have opened the web page, we can read it like a local file.
'''

import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
	print line.strip()


'''
Our regular expression looks for strings that start with "href="http://", followed by
one or more characters (".+?"), followed by another double quote. The question
mark added to the ".+?" indicates that the match is to be done in a "non-greedy"
fashion instead of a "greedy" fashion. A non-greedy match tries to find the small-
est possible matching string and a greedy match tries to find the largest possible
matching string.
'''

import urllib
import re
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
	print link



'''
We will use urllib to read the page and then use BeautifulSoup to extract the
href attributes from the anchor (a) tags.
The program prompts for a web address, then opens the web page, reads the data
and passes the data to the BeautifulSoup parser, and then retrieves all of the anchor
tags and prints out the href attribute for each tag.
'''

import urllib
from bs4 import BeautifulSoup
# from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
print tags

for tag in tags:
	print tag.get('href', None)
	# Look at the parts of a tag
	# print 'TAG:',tag
	# print 'URL:',tag.get('href', None)
	# print 'Content:',tag.contents[0]
	# print 'Attrs:',tag.attrs


'''
Sometimes you want to retrieve a non-text (or binary) file such as an image or
video file. The data in these files is generally not useful to print out, but you can
easily make a copy of a URL to a local file on your hard disk using urllib.
The pattern is to open the URL and use read to download the entire contents of
the document into a string variable (img) then write that information to a local file.

However if this is a large audio or video file, this program may crash or at least
run extremely slowly when your computer runs out of memory. In order to avoid
running out of memory, we retrieve the data in blocks (or buffers) and then write
each block to your disk before retrieving the next block. This way the program can
read any size file without using up all of the memory you have in your computer.

In this example, we read only 100,000 characters at a time and then write those
characters to the cover.jpg file before retrieving the next 100,000 characters of
data from the web.
'''

import urllib
img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'w')
size = 0

while True:
	info = img.read(100000)
	if len(info) < 1 : break
	size = size + len(info)
	fhand.write(info)

print size,'characters copied.'
fhand.close()
