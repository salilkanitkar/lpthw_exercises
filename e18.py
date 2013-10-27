#!/usr/bin/python

""" Exercise 18 """

def print_none():
	print "I got no arguments"

def print_one(arg1):
	print "arg1: %r" % arg1

def print_two(arg1, arg2):
	print "arg1: %r, arg2:%r" % (arg1, arg2)

def print_two_again(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

print_none()
print_one("One")
print_two("One", "Two")
print_two_again("One", "Two")

"""
Test Run:
$ ./e18.py
I got no arguments
arg1: 'One'
arg1: 'One', arg2:'Two'
arg1: 'One', arg2: 'Two'
"""

