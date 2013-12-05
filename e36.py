#!/usr/bin/python

""" Exercise 36 """

from sys import exit

def assign_Harry_Persona(DA_person):
   if DA_person == True:
      DA_personas = ["Ron", "Hermione", "Ginny", "Neville", "Luna"]
      print "Input Yes for a character that you want to take up - "
      decision_made = False
      for persona in DA_personas:
         print "Do you want to be %s ?" % persona
         persona_decision = raw_input("Yes/No ? ")
         if persona_decision == "Yes":
            print "Cool - you are now %s " % persona
            dead("This was fun!")
            decision_made = True
            break;
         elif persona_decision == "No":
            print "OK - choose another ..."
         else:
            print "You still haven't figured out that you HAVE to enter Yes or No - Exiting ...."
            dead("You won't probably survive in the Wizarding World anyway....")

      if (decision_made == False):
         print "You ran out of DA members to choose from - you die!"
         dead("Tough Luck dude!")
   else:
      print "You are not in DA - so you get to be only one character - Dudley"
      dead("Meh - this wasn't that great....")
      

def test_Harry():
   print "Team Harry has a few tough questions -"
   DA_person = False

   print "2. Do you want to be a part of Dumbledore's Army (DA) ?"
   DA_decision = raw_input("Yes/No > ")

   if DA_decision == "Yes":
      print "It's not easy being a DA member!\n"
      print "Do you think you have it in you? Last chance - no backing out after this ...."
      DA_decision_confirm = raw_input("Yes/No > ")
      if DA_decision_confirm == "Yes":
         DA_person = True;
      elif DA_decision_confirm == "No":
         print "OK - at least you did not quit later!"
      else:
         dead("Answering with anything other than a resounding Yes is considered a No!")
   elif DA_decision == "No":
      print "OK - let's move on."
   else:
      dead("Please answer with a Yes or No!")

   assign_Harry_Persona(DA_person)

def test_Voldemort():
   print "Team Voldemort has a few tough and evil questions - "

   magic_might_choice = ""

   while magic_might_choice != "Yes":
      print "To prove your evil-ness, you HAVE to answer only one question - till you get it right!"
      print "Is magic might?"
      magic_might_choice = raw_input("Yes/No> ? ")

   dead("OK - you are evil - plain and simple! NoSoupForYou!")

def dead(msg):
   print "Bye Bye - %s" % msg
   exit(0)

def start():
   print "This is a test of your survival in the Wizarding World!"
   print "But first, you have to answer a few questions -"
   print "1. Are you on Harry's team or Voldermort's team? "

   team = raw_input("> ")

   if team == "Harry":
      print "OK - you chose Harry"
      test_Harry()
   elif team == "Voldemort":
      print "Really!?? You have chosen Voldemort"
      test_Voldemort()
   else:
      print "You have to choose one of the two possible teams."
      dead("That got over quickly!")

start()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e36.py
This is a test of your survival in the Wizarding World!
But first, you have to answer a few questions -
1. Are you on Harry's team or Voldermort's team? 
> Harry
OK - you chose Harry
Team Harry has a few tough questions -
2. Do you want to be a part of Dumbledore's Army (DA) ?
Yes/No > Yes
It's not easy being a DA member!

Do you think you have it in you? Last chance - no backing out after this ....
Yes/No > Yes
Input Yes for a character that you want to take up - 
Do you want to be Ron ?
Yes/No ? No
OK - choose another ...
Do you want to be Hermione ?
Yes/No ? No
OK - choose another ...
Do you want to be Ginny ?
Yes/No ? No
OK - choose another ...
Do you want to be Neville ?
Yes/No ? Yes
Cool - you are now Neville 
Bye Bye - This was fun!

"""

