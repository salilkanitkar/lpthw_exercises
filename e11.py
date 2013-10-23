#!/usr/bin/python

""" Exercise 11 """

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you are %r old, %r tall and %r heavy." % (age, height, weight)


"""
Test Run:
$ python e10.py
How old are you? 27
How tall are you? 5'3"
How much do you weigh? 160
So you are '27' old, '5\'3"' tall and '160' heavy.
"""

