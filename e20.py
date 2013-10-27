#!/usr/bin/python

""" Exercise 20 """

"""
PreRequisite: A file e20_sample.txt must be already present before
		      running this exercise.
"""

from sys import argv

script, input_file = argv

def print_all(f):
	f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print "LineNum: %d %s" % (line_count, f.readline())

current_file = open(input_file)

print "First, let's print the whole file"
print_all(current_file)

print "Now, lets rewind - back to the beginning of the file"
rewind(current_file)

print "Lets print first three lines"
line_count = 1
print_a_line(line_count, current_file)
line_count += 1
print_a_line(line_count, current_file)
line_count += 1
print_a_line(line_count, current_file)

"""
Test Run:
$ ./e20.py e20_sample.txt
First, let's print the whole file
Now, lets rewind - back to the beginning of the file
Lets print first three lines
LineNum: 1 This is Line1.

LineNum: 2 This is Line2.

LineNum: 3 This is Line3.

"""

