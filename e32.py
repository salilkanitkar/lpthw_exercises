#!/usr/bin/python

""" Exercise 32 """

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

# Printing mixed lists - so have to use %r
for i in change:
	print "I got %r" % i

elements = []

# The below loop that adds numbers to 'elements'
# one by one is not required.
# Alternatively, it can be done in one line as below -
# elements = range(0, 6)

for i in range(0, 6):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i 

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e32.py
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
"""

