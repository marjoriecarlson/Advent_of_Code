#!/usr/bin/python
input = open('input/7.txt','r')
programs = input.readlines()
input.close()

# there are many children that aren't parents, but
# the root is the only parent that's not also a child

parentNodes = []
childNodes = []

for program in programs:
        info = program.split()
        if len(info) > 2:  # ignore leaf nodes
                # first element is own name; add self to parentNodes
                parentNodes.append(info[0])

                # info[3:] are the child nodes; strip their commas and add to childNodes
                childNodes.extend([child.strip(',') for child in info[3:]])



for parent in parentNodes:
        if parent not in childNodes:
                print "Root is", parent
