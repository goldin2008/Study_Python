##Extracting data using regular expressions

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
we are looking for substrings that start with a single lowercase letter,
uppercase letter, or number "[a-zA-Z0-9]", followed by zero or more non-blank
characters ("\S*"), followed by an at-sign, followed by zero or more non-blank
characters ("\S*"), followed by an uppercase or lowercase letter. Note that we
switched from "+" to "*" to indicate zero or more non-blank characters since "[azA-
Z0-9]" is already one non-blank character. Remember that the "*" or "+"
applies to the single character immediately to the left of the plus or asterisk.
'''

'''
Instead of calling search(), we add parentheses around the part of the regular
expression that represents the floating-point number to indicate we only want
findall() to give us back the floating-point number portion of the matching
string.
'''

'''
Translating our regular expression, we are looking for lines that start with  "Details: ",
followed by any number of characters ( ".* "), followed by  "rev= ", and then
by one or more digits. We want to find lines that match the entire expression but
we only want to extract the integer number at the end of the line, so we surround
 "[0-9]+ " with parentheses.
'''

import re

hand = open('t.txt')

for line in hand:
	line = line.rstrip()
	x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
# 	x = re.findall('ˆX\S*: ([0-9.]+)', line)
# 	x = re.findall('ˆDetails:.*rev=([0-9]+)', line)
	if len(x) > 0 :
		print x
		
