#!/usr/bin/python

# This time, just count pieces of garbage INSIDE <>s, including excess
# <'s but excluding the < and > that delineate the garbage. Ignore !s.

stream = open('input/9.txt','r').read()

garbageSeen = 0

justSawBang = False  # should I ignore this char?
inGarbage = False    # will be used to decide whether to count garbage

for char in stream:
        if justSawBang == True:    # skip this character entirely
                justSawBang = False
        elif char == '!':
                justSawBang = True
        elif char == '<':
                if inGarbage:
                        garbageSeen += 1 # stray < inside garbage
                else:
                        inGarbage = True
        elif char == '>':
                inGarbage = False
        elif inGarbage:   # arbitrary char in garbage stream
                garbageSeen += 1

print garbageSeen
