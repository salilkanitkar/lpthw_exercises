#!/usr/bin/python

""" Exercise 03 """

print "I will now count my chicken"

print "Hens", 25 + 30 / 6
#             (25+(30/6))

print "Roosters", 100 - 25 * 3 % 4
#                 (100-((25*3)%4))

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#     (3 + 2 + 1 - 5 + (4 % 2) -( 1/4 ) + 6)

print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
#     ((3+2)<(5-7))

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Hence the False output above!"

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "7 / 4 = ", 7 / 4
print "7.0 / 4.0 = ", 7.0 / 4.0

"""
Test Run:
$ python e03.py 
I will now count my chicken
Hens 30
Roosters 97
7
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Hence the False output above!
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
7 / 4 =  1
7.0 / 4.0 =  1.75
"""

