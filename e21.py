#!/usr/bin/python

""" Exercise 21 """

def add(a, b):
	print "Adding %d and %d:" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d and %d:" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d and %d:" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d and %d:" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(50, 5)
weight = multiply(10, 5)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ:%d" % (age, height, weight, iq)

# Here is a puzzle

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

"""
Test Run:
$ ./e21.py
Let's do some math with just functions!
Adding 30 and 5:
Subtracting 50 and 5:
Multiplying 10 and 5:
Dividing 100 and 2:
Age: 35, Height: 45, Weight: 50, IQ:50
Dividing 50 and 2:
Multiplying 50 and 25:
Subtracting 45 and 1250:
Adding 35 and -1205:
That becomes:  -1170 Can you do it by hand?
"""

