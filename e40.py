#!/usr/bin/python

""" Exercise 40 """

# __init__ method: Constructor for the Python class

class Song(object):
# The 'object' is parenthesis here is basically the superclass

	def __init__(self, lyrics):
		self.lyrics = lyrics
# 'self' is rrequired because without it, you can not tell if you are creating a new local
# variable called 'lyrics'

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy B'Day to you",
				   "I don't want to get sued",
				   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
					    "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e40.py
Happy B'Day to you
I don't want to get sued
So I'll stop right there.
They rally around the family
With pockets full of shells
"""

