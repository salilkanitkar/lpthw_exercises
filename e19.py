#!/usr/bin/python

""" Exercise 19 """

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket\.n"

print "We can just give the function numbers directly"
cheese_and_crackers(20, 30)

print "OR, we can use variables"
amount_of_cheese = 20
amount_of_crackers = 30
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math while calling the function:"
cheese_and_crackers(20 + 10, 30 + 20)

print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 30)

"""
Test Run:
$ ./e19.py
We can just give the function numbers directly
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket\.n
OR, we can use variables
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket\.n
We can even do math while calling the function:
You have 30 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket\.n
And we can combine the two variables and math:
You have 40 cheeses!
You have 60 boxes of crackers!
Man that's enough for a party!
Get a blanket\.n
"""

