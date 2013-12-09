#!/usr/bin/python

""" Exercise 37 """

def symbol_tryOuts():
	print "Lets try out a few Python symbols"
	
	print "1. and: and should be used instead of && in an if statement"
	a = 0
	b = 0
	if a == 0 and b == 0:
		print "and used instead of &&"

	print "2. del: Used to delte values form a list or an entire variable"
	a = [0, 1, 2, 3, 4]
	print a
	del(a[0])
	print a
	del(a[1:3])
	print a

	print "3. from: Used as - from <some module> import <some func>"

	print "4. not: 'if not' checks for truth value and '!=' checks for equality."

	print "5. as: The as keywork is used in the try-except blocks"
	usage_str = """The usage is: ->
	try:
		[] + 3
	except (ExceptionType1, ExceptionType2) as x:
		print \"Caught exeption\"
	The above except clause is less ambigous than saying \"except (ExceptionType1, ExceptionType2), x\"
	"""
	print usage_str

	global_symbol_str = """6. global: The global keyword indicates that the variable will be 'global' within that module.
	While assigning value to a global variable, you have to use global keyword before that var name,
	otherwise, a new local variable will be created.
	Eg ->
	
	def foo():
		var1 = 1
		global var2 = 2 
		print var1 + var2

	def foo1():
		print var2 -> The global var2 will be printed
		global var2 = 3 -> The global var2 var's value is changed
		var2 = 4 --> Here, a new local variable var2 will be created and assigned the value
	"""
	print global_symbol_str

	with_symbol_str = """7. with: The with symbol is used for automatic management of the resources used within a python block.
	Eg ->
	with open('output.txt', 'w') as fileObj:
		fileObj.write('Some text')

	The above 'with' statement will automatically close the file when the 'with' block of code exits.
	The with keyworkd guarantes that the file will be closed irrespective of how the nested block of code exist.
	If an exception occurs - it will close the file before the exception handler is involved.
	If the nested block contains a 'return', 'break' or 'continue' statement, it will close the file
	before any of those statements are hit and executed.
	"""
	print with_symbol_str

	assert_symbol_str = """8. assert: The assert statement indicates that the condition following the assert
	keyword must be evaluated. If it evaluates to True, further execution continues.
	If it evalueates to False, python interpreter raises the AssertionError exception.
	"""
	print assert_symbol_str

	pass_symbol_str = """9. pass: The 'pass' keyword in python is basically the NOOP equivalent.
	E.g -
	if a <= b:
		pass  # This is a no-op.
	"""
	print pass_symbol_str

	yield_symbol_str = """10. yield: The yiels python symbol is pretty complicated. You have to know about iterator, iterable and generator to fully understand the yield statement.
	StackOverflow Thread: http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained
	iterable objects: Any object that can be used in a for loop like list, file, string etc.
	iterator object: Any object that implements the next() method returning the next element and when
	there are no more next elements to return, it will raise the StopIteration exception.
	built-in iter function: Takes an iterable object and returns an iterator
	function iter internally calls the __iter__: The __iter__ makes an object iterable. The __iter__ returns
	an iterator.
	generator: Generator simpliefies the creation of iterator. The generator function generates a generator.
	When a generator function is called, the generator object is returned without even beginning the execution
	of generator function. When next method is called on the returned Generator object the first time, it starts
	the execution of generator function until it reaches the yield statement and returns the yield'ed value.
	"""
	print yield_symbol_str

	finally_symbol_str = """ 11. finally: The finally is a clause in python try-catch construct
	It always gets executed before leving the try statement block - whether an exception has occurred or not.
	"""
	print finally_symbol_str

	lambda_symbol_str = """ 12. lambda: lambda is just a way of defining functions inline.
	Eg -
	a = lambda x:x + 1
	print a(1)
	>> 2
	lambda provides a way to have functions passed around.
	"""
	print lambda_symbol_str

def constant_tryOuts():
	none_constant_str = """ 1. none: The None constant is used to represent the absence of a value.
	"""
	print none_constant_str

symbol_tryOuts()
constant_tryOuts()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e37.py

"""

