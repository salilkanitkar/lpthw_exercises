#!/usr/bin/python

""" Exercise 35 """

from sys import exit

def is_number(num):
	try:
		int(num)
		return True
	except ValueError:
		return False	

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	# Using the is_number function is a better alternative to the blow 'if "0" in next'
	# to check if the input provided is a number or not. 
	# if "0" in next or "1" in next:
	if is_number(next):
		how_much = int(next)
	else:
		dead("Man, learn to type a number!")

	if how_much < 50:
		print "Nice, you're not greedy. You win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear pissed off and chews your legs off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here, you see the great evil Cthulhu."
	print "He, it, whatever stares at you and go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well, that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and to your left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e35.py
You are in a dark room.
There is a door to your right and to your left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has moved from the door. You can go through it now.
> open door
This room is full of gold. How much do you take?
> 1000
You greedy bastard! Good job!
"""

