#!/usr/bin/python
from collections import defaultdict

input = open('input/7.txt','r')
programs = input.readlines()
input.close()

class Node(object):
        name_index = defaultdict(list)
        def __init__(self, name, weight, children):
                self.name = name
                self.weight = int(weight)
                self.childrenNames = children
                self.children = []
                self.totalWeight = -1
                Node.name_index[name] = self

        def linkKids(self): # this must be done after ALL nodes are created
                for child in self.childrenNames:
                        self.children.append(Node.findNode(child))

        def calculateTotalWeight(self): # this must be done after ALL nodes are created
                # if it's already calculated, don't recalculate
                if self.totalWeight > -1:
                        return self.totalWeight

                # if I don't have a list of pointers to my kids, create one
                if not self.children:
                        self.linkKids()

                # my subtree includes my weight
                self.totalWeight = self.weight
                # if I have kids, sum their subtrees' weights with mine
                if self.children:
                        error = False
                        sampleWeight = self.children[0].calculateTotalWeight()
                        for child in self.children:
                                childTotalWeight = child.calculateTotalWeight()
                                self.totalWeight += childTotalWeight
                                if childTotalWeight != sampleWeight:
                                        error = True
                        if error: # this will find the problem subtree!
                                print "\nERROR!!!"
                                for child in self.children:
                                    print child.name, child.calculateTotalWeight()
                                print "\n"

                return self.totalWeight

        def __str__(self):
                string = self.name + " (" + str(self.weight) + "/" + str(self.totalWeight) + ")"
                for child in self.childrenNames:
                        string += ' ' + child
                return string
        __repr__ = __str__

        @classmethod
        def findNode(cls, name):
                return Node.name_index[name]

for program in programs:
        info = program.split()
        self = info[0]
        weight = info[1].strip('(').strip(')')

        if len(info) > 2:  # parent
                node = Node(self, weight, [child.strip(',') for child in info[3:]])
        else: # leaf
                node = Node(self, weight, [])

rootNode = Node.findNode("ykpsek") # ykpsek was found to be root in part a
rootNode.calculateTotalWeight()
print '---'

# the part above showed cumah is the culprit:
# ERROR!!!
# amhaz 1894
# cumah 1903  <------
# zqfvypo 1894
# dribos 1894

print "Cumah's subtree weighs", 1903-1894, "too much."

cumahWeight = Node.findNode('cumah').weight

print "Cumah should weigh", cumahWeight-(1903-1894), "instead of", cumahWeight
