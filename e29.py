#!/usr/bin/python

""" Exercise 29 """

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs"

if people <= dogs:
	print "People are less than or equal to dogs"

if people == dogs:
	print "People are dogs"

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e29.py
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs
People are less than or equal to dogs
People are dogs
"""

