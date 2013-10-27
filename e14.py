#!/usr/bin/python

""" Exercise 14 """

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)

"""
Test Run:
$ ./e14.py salil
Hi salil, I'm the ./e14.py script.
I'd like to ask you a few questions.
Do you like me salil?
>Yes
Where do you live salil?
>Pune
What kind of computer do you have salil?
>Lenovo

Alright, so you said 'Yes' about liking me.
You live in 'Pune'. Not sure where that is.
And you have a 'Lenovo' computer. Nice
"""

