#!/usr/bin/python

""" Exercise 25 """

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words and then prints the first and last word."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e25.py
Then exercise the functions through the python command interpreter ->
salil@ubuntu:~/git-repo/lpthw_exercises$ python
Python 2.7.3 (default, Apr 10 2013, 05:46:21) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import e25
>>> sentence = "All good things come to those who wait."
>>> words = e25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = e25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> e25.print_first_word(sorted_words)
All
>>> e25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = e25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> e25.print_first_and_last(sentence)
All
wait.
>>> e25.print_first_and_last_sorted(sentence)
All
who
>>> help(e25)

>>> help(e25.break_words)

>>> help(e25.print_first_and_last)

--->> The help(e25.print_first_and_last) prints the info that we have written
in the \"\"\" section

"""

