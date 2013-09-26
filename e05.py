#!/usr/bin/python

""" Exercise 05 """

name = "Salil"
age = 27
height = 64 # inches
weight = 60 # kgs
eyes = 'Light Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d kgs heavy." % weight
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are %s." % teeth

print "If I add %d, %d, %d I get %d" % (
      age, height, weight, age + height + weight)


"""
Test Run:
$ python e05.py 
Let's talk about Salil.
He's 64 inches tall.
He's 60 kgs heavy.
He's got Light Brown eyes and Black hair.
His teeth are White.
If I add 27, 64, 60 I get 151
"""
