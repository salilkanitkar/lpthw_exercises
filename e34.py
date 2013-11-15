#!/usr/bin/python

""" Exercise 34 """

# Ordinal:  Some sort of ordering is implied.
# Cardinal: No ordering is implied - random access.

# Accessing lists - using array-like indices

elements = ['One', 'Two', 3, 4, 'Five', 6, 'Seven']

print "elements[4]: %r" % elements[4]
print "elements[6]: %r" % elements[6]
print "elements[0]: %r" % elements[0]
print "elements[2]: %r" % elements[2]

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e34.py
elements[4]: 'Five'
elements[6]: 'Seven'
elements[0]: 'One'
elements[2]: 3
"""

