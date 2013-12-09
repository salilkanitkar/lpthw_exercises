#!/usr/bin/python

""" Exercise 39 """

# Create a mpping of state to abbreviation
states = {
	'Oregon'    : 'OR',
	'Florida'   : 'FL',
	'California': 'CA',
	'New York'  : 'NY',
	'Michigan'  : 'MI'
}

# Create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: " , states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has:  ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s and has the city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None) # The 'None' specifies the value if get does not return anything ... 

if not state:
	print "Sorry, no texas"

# Get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city

# Dict vs List: List is used when an ordering of the items is required, otherwise dict is fine.

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e39.py
----------
NY State has:  New York
OR State has:  Portland
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
----------
Michigan has:  Detroit
Florida has:   Jacksonville
----------
California is abbreviated as CA
Michigan is abbreviated as MI
New York is abbreviated as NY
Florida is abbreviated as FL
Oregon is abbreviated as OR
----------
FL has city Jacksonville
CA has city San Francisco
MI has city Detroit
OR has city Portland
NY has city New York
----------
California is abbreviated as CA and has the city San Francisco
Michigan is abbreviated as MI and has the city Detroit
New York is abbreviated as NY and has the city New York
Florida is abbreviated as FL and has the city Jacksonville
Oregon is abbreviated as OR and has the city Portland
----------
Sorry, no texas
The city for the state 'TX' is: Does not exist
"""

