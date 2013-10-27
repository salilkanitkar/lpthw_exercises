#!/usr/bin/python

""" Exercise 16 """

"""
PreRequisite: The file e16_sample.txt must be present before
running this exercise.
"""

from sys import argv

script, filename = argv

print "We are going to erase file %r" % filename
print "If you don't want that - hit CTRL-C (^C)."
print "If you do want that - hit RETURN."
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
# Opening the file in 'w' mode essentially truncates it anyway!

print "Truncating the file... Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Alternatively, to do the above write operation in one call to write() ->
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally we close it"
target.close()

"""
Test Run:
$ ./e16.py e16_sample.txt
We are going to erase file 'e16_sample.txt'
If you don't want that - hit CTRL-C (^C).
If you do want that - hit RETURN.
?
Opening the file...
Truncating the file... Goodbye!
Now I'm going to ask you for three lines.
line1: Mary had a little lamb.
line2: It's fleece was white as snow.
line3: It was also tasty.
I'm going to write these to the file.
And finally we close it
"""

