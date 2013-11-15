#!/usr/bin/python

""" Exercise 33 """

def while_loop_test(limit, increment):
	i = 0
	numbers = []

	while i < limit:
		print "At the top i is: %d" % i
		numbers.append(i)

		i = i + increment
		print "numbers so far: ", numbers
		print "At the bottom i is: %d" % i

	print "The numbers: "

	for num in numbers:
		print num

limit = 4
increment = 1
print "Testing the while loop with limit: %d and increment: %d" %  (limit, increment)
while_loop_test(limit, increment)

limit = 100
increment = 15
print "Testing the while loop with limit: %d and increment: %d" % (limit, increment)
while_loop_test(limit, increment)

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e33.py
Testing the while loop with limit: 4 and increment: 1
At the top i is: 0
numbers so far:  [0]
At the bottom i is: 1
At the top i is: 1
numbers so far:  [0, 1]
At the bottom i is: 2
At the top i is: 2
numbers so far:  [0, 1, 2]
At the bottom i is: 3
At the top i is: 3
numbers so far:  [0, 1, 2, 3]
At the bottom i is: 4
The numbers: 
0
1
2
3
Testing the while loop with limit: 100 and increment: 15
At the top i is: 0
numbers so far:  [0]
At the bottom i is: 15
At the top i is: 15
numbers so far:  [0, 15]
At the bottom i is: 30
At the top i is: 30
numbers so far:  [0, 15, 30]
At the bottom i is: 45
At the top i is: 45
numbers so far:  [0, 15, 30, 45]
At the bottom i is: 60
At the top i is: 60
numbers so far:  [0, 15, 30, 45, 60]
At the bottom i is: 75
At the top i is: 75
numbers so far:  [0, 15, 30, 45, 60, 75]
At the bottom i is: 90
At the top i is: 90
numbers so far:  [0, 15, 30, 45, 60, 75, 90]
At the bottom i is: 105
The numbers: 
0
15
30
45
60
75
90
"""

