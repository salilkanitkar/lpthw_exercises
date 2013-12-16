#!/usr/bin/python

""" Exercise 43 """

from sys import exit
from random import randint

class Scene(object):

   def enter(self):
      print "This scene is not yet configured. Subclass it and implement enter()"
      exit(1)

class Engine(object):

   def __init__(self, scene_map):
      print "Engine __init__ has scene_map: ", scene_map
      self.scene_map = scene_map

   def play(self):
      current_scene = self.scene_map.opening_scene()
      print "Play's first scene: ", current_scene

      while True:
         print "\n---------"
         next_scene_name = current_scene.enter()
         print "next_scene: ", next_scene_name
         current_scene = self.scene_map.next_scene(next_scene_name)
         print "map returns new scene: ", current_scene

class Death(Scene):

   quips = [
            "You died. You kind of suck at this.",
            "Your mom would be proud, if she were smarter.",
            "Such a loser.",
            "I have a small puppy that's better at this."
           ]

   def enter(self):
         print Death.quips[randint(0, len(self.quips)-1)]
         exit(1)

class CentralCorridor(Scene):

   def enter(self):
      print "You are running down the central corridor to the Weapons Armory when"
      print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
      print "flowing around hi hate-filled body. He is blocking the door to the Armory."
      print "Input either - \"shoot!\", \"dodge!\" or \"tell a joke\""

      action = raw_input("> ")

      if action == "shoot!":
         return 'death'

      elif action == "dodge!":
         return 'death'

      elif action == "tell a joke":
         return 'laser_weapon_armory'

      else:
         return 'central_corridor'

class LaserWeaponArmory(Scene):

   def enter(self):
      print "You are now in LasorWeaponArmory. There is a neutron bomb in front of you."
      print "You need a code to unlock it. Code is 3 digits."
      print "You get 10 guesses for the code."

      code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))

      guess = raw_input("> ")
      guesses = 0

      while guess != code and guesses < 10:
         print "BZZZDD - wrong guess!"
         guesses += 1
         guess = raw_input("> ")

      if guess == code:
         return 'the_bridge'

      else:
         return 'death'

class TheBridge(Scene):

   def enter(self):
      print "You have two options - \"throw the bomb\" or \"slowly place the bomb\""

      action = raw_input("> ")

      if action == "throw the bomb":
         return 'death'

      elif action == "slowly place the bomb":
         return 'escape_pod'

      else:
         return 'the_bridge'

class EscapePod(Scene):

   def enter(self):
         print "You have to choose between one of 5 pods."

         good_pod = randint(1,5)
         guess = raw_input("[pod #]> ")

         if int(guess) != good_pod:
            return 'death'

         else:
            return 'finished'

class Map(object):

   scenes = {
             'central_corridor': CentralCorridor(),
             'laser_weapon_armory': LaserWeaponArmory(),
             'the_bridge': TheBridge(),
             'escape_pod': EscapePod(),
             'death': Death()
            }

   def __init__(self, start_scene):
      self.start_scene = start_scene
      print "start_scene __init__ : ", self.start_scene

   def next_scene(self, scene_name):
      val = Map.scenes.get(scene_name)
      print "next_scene returns: ", val
      return val ## This line was not there - the bug fix I say!

   def opening_scene(self):
      return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e43.py
start_scene __init__ :  central_corridor
Engine __init__ has scene_map:  <__main__.Map object at 0x986342c>
next_scene returns:  <__main__.CentralCorridor object at 0x986332c>
Play's first scene:  <__main__.CentralCorridor object at 0x986332c>

---------
You are running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around hi hate-filled body. He is blocking the door to the Armory.
Input either - "shoot!", "dodge!" or "tell a joke"
> tell a joke
next_scene:  laser_weapon_armory
next_scene returns:  <__main__.LaserWeaponArmory object at 0x986334c>
map returns new scene:  <__main__.LaserWeaponArmory object at 0x986334c>

---------
You are now in LasorWeaponArmory. There is a neutron bomb in front of you.
You need a code to unlock it. Code is 3 digits.
You get 10 guesses for the code.
> 111
BZZZDD - wrong guess!
> 112
BZZZDD - wrong guess!
> 112
BZZZDD - wrong guess!
> 456
BZZZDD - wrong guess!
> 435
BZZZDD - wrong guess!
> 67
BZZZDD - wrong guess!
> 789
BZZZDD - wrong guess!
> 567
BZZZDD - wrong guess!
> 456
BZZZDD - wrong guess!
> 456
BZZZDD - wrong guess!
> 34
next_scene:  death
next_scene returns:  <__main__.Death object at 0x98633ac>
map returns new scene:  <__main__.Death object at 0x98633ac>

---------
You died. You kind of suck at this.

"""

