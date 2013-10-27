#!/usr/bin/python

""" Exercise 12 """

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

age = int(age)
weight = int(weight)

print "So you are %d old, %s tall and you weigh %d" %\
      (age, height, weight)

"""
Test Run:
$ ./e12.py
How old are you? 27
How tall are you? 5'4"
How much do you weigh? 60
So you are 27 old, 5'4" tall and you weigh 60
"""

