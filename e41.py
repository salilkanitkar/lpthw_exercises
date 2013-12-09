#!/usr/bin/python

""" Exercise 41 """

# Rename this file as oop_test.py to run successfully.

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"

"""
Test Run:
Run the program once to ensure no errors are in the program
$ cp e41.py oop_test.py 
$ ./oop_test.py 
class Bead(object):
	def __init__(self, beam)
> class Bead has-a __init__ that takes self and beam parameters.
ANSWER:  class Bead has-a __init__ that takes self and beam parameters.


class Army(object):
	def crack(self, agreement)
> class Army has-a crack that takes self ans agreement parameters.
ANSWER:  class Army has-a function named crack that takes self and agreement parameters.


class Bee(Bone):
> Make a class named Bee that is-a Bone.
ANSWER:  Make a class named Bee that is-a Bone.

brick.crate(butto, copy, chain)
> From brick get the crate function, and call it with parameters self, butto, copy, chain
ANSWER:  From brick get the crate function, and call it with parameters self, butto, copy, chain.


blade.bait = 'basket'
> From blade get the bait attribute and set it to 'basket'
ANSWER:  From blade get the bait attribute and set it to 'basket'.


apparel = Calendar()
> Set apparelt to an instance of class Calendar.
ANSWER:  Set apparel to an instance of class Calendar.


cow = Ball()
> Set cow to an instance of class Ball.
ANSWER:  Set cow to an instance of class Ball.


crate.driving = 'drain'
> From crate get the driving attribute and set it to 'drain'.
ANSWER:  From crate get the driving attribute and set it to 'drain'.


class Approval(object):
	def __init__(self, approval)
> class Approval has-a __init__that takes self and approval parameters.
ANSWER:  class Approval has-a __init__ that takes self and approval parameters.


cellar.apple(detail, chess, drug)
> From cellar get the apple function, and call it with parameters self, detail, chess, drug.
ANSWER:  From cellar get the apple function, and call it with parameters self, detail, chess, drug.


class Cook(Bean):
> Make a class named Cook that is-a Bean.
ANSWER:  Make a class named Cook that is-a Bean.


class Degree(object):
	def agreement(self, cave, art)
> 
Bye

Using the enlighs option that does the reverse of above operation -
$ cp e41.py oop_test.py 
$ ./oop_test.py "english"
class Addition has-a __init__ that takes self and crate parameters.
> class Addition: def __init__(self, crate)
ANSWER:  class Addition(object):
	def __init__(self, crate)


From desire get the cushion function, and call it with parameters self, amusement, attempt, band.
> desire.cushion(self, amusement, attempt, band)
ANSWER:  desire.cushion(amusement, attempt, band)


class Berry has-a function named condition that takes self and daughter, downtown, cactus parameters.
> class Berry(object):
ANSWER:  class Berry(object):
	def condition(self, daughter, downtown, cactus)


From arm get the balance attribute and set it to 'cloud'.
> arm.balance = 'cloud'
ANSWER:  arm.balance = 'cloud'


Make a class named Discussion that is-a Burst.
> class Discussion(Burst):
ANSWER:  class Discussion(Burst):


Set corn to an instance of class Cemetery.
> corn = Cemetery()
ANSWER:  corn = Cemetery()


class Approval has-a function named bell that takes self and change, dirt parameters.
> class Approval(object): def bell(self, change, dirt)
ANSWER:  class Approval(object):
	def bell(self, change, dirt)


Set division to an instance of class Discovery.
> division = Discovery()
ANSWER:  division = Discovery()


Make a class named Belief that is-a Baseball.
> class Belief(Baseball):
ANSWER:  class Belief(Baseball):


From celery get the addition function, and call it with parameters self, airport, cent, bomb.
> celery.addition(self, airport, cent, bomb)
ANSWER:  celery.addition(airport, cent, bomb)


From approval get the berry attribute and set it to 'bear'.
> approval.berry = 'bear'
ANSWER:  approval.berry = 'bear'


class Cream has-a __init__ that takes self and beetle parameters.
> 
Bye

"""

