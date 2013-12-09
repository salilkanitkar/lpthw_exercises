#!/usr/bin/python

""" Exercise 42 """

## There is a class called 'object' from which every class should inherit from

## Animal is-a object
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a __init__
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a __init__
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a __init__
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name,salary):
		## Employee has-a __init__
		super(Employee, self).__init__(name)
	
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("rover")

## Satan is-a Cat
satan = Cat("satan")

## Mary is-a Person
mary = Person("mary")

## Mary has a Cat called satan
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has a pet Dog called rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e42.py

"""

