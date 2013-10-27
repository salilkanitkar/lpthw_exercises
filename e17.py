#!/usr/bin/python

""" Exercise 17 """

"""
PreRequisite: The file e17_sample.txt must be present before
running this exercise.
"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
in_file = open(from_file)
in_data = in_file.read()
# To do above two operations on one line: open(from_file).read()

print "The input file is %d bytes long." % len(in_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready? Hit RETURN to Continue CTRL-C to Abort"
raw_input("?")

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."

in_file.close()
out_file.close()

"""
Test Run:
$ ./e17.py e17_sample.txt e17_output.txt
Copying from e17_sample.txt to e17_output.txt
The input file is 19 bytes long.
Does the output file exist? False
Ready? Hit RETURN to Continue CTRL-C to Abort
?
Alright, all done.
"""

