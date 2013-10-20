#!/usr/bin/python

""" Exercise 10 """

tabby_cat = "\tI am tabbed cat."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

"""
Test Run:
$ python e10.py
	I am tabbed cat.
I'm split 
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass
"""

