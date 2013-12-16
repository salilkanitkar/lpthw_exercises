#!/usr/bin/python

""" Exercise 44 """

class Parent(object):

   def implicit(self):
      print "PARENT implicit()"

   def override(self):
      print "PARENT override()"

   def altered(self):
      print "PARENT altered()"

class Child(Parent):

   def override(self):
      print "CHILD override()"

   def altered(self):
      print "CHILD, Before PARENT altered()"
      super(Child, self).altered()
      print "CHILD, After PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print "\nMethod Resolution Order and the Algorith C3"
print "Avoid Multiple Inheritance!!\n"

class Other(object):

   def implicit(self):
      print "OTHER implicit()"

   def override(self):
      print "OTHER override()"

   def altered(self):
      print "OTHER altered()"

class ChildO(object):

   def __init__(self):
      self.other = Other()

   def implicit(self):
      self.other.implicit()

   def override(self):
      print "CHILDO override()"

   def altered(self):
      print "CHILDO, Before OTHER altered()"
      self.other.altered()
      print "CHILDO, After OTHER altered()"

son = ChildO()

son.implicit()
son.override()
son.altered()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e44.py
PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
PARENT altered()
CHILD, Before PARENT altered()
PARENT altered()
CHILD, After PARENT altered()

Method Resolution Order and the Algorith C3
Avoid Multiple Inheritance!!

OTHER implicit()
CHILDO override()
CHILDO, Before OTHER altered()
OTHER altered()
CHILDO, After OTHER altered()
"""

