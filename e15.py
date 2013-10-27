#!/usr/bin/python

""" Exercise 15 """

"""
PreRequisite: The file e15_sample.txt must be present before
running this exercise.
"""
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r" % filename
print txt.read()

txt.close()

print "Type the filename again:"
filename_again = raw_input(">")

txt_again = open(filename_again)
print txt_again.read()

txt_again.close()

"""
Test Run:
$ ./e15.py e15_sample.txt
Here's your file 'e15_sample.txt'
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

Type the filename again:
>e15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

"""

