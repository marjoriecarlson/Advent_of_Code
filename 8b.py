#!/usr/bin/python
from collections import defaultdict

# read in an instruction
# parse: reg name, inc/dec, amount, if reg op val
# find both registers; if nonexistent; add to register dict with val = 0
# check the if condition; if true, do the op
# move on to next line

input = open('input/8.txt','r')
lines = input.readlines()
input.close()

registers = {}
maxValSeen = 0

for line in lines:  # execute each instruction in turn
        instruction  = line.split()

        # figure out which register to modify; create it if needed
        modRegister = instruction[0]
        if modRegister not in registers:
                registers[modRegister] = 0

        # figure out which register to compare; create it if needed
        compRegister = instruction[4]
        if compRegister not in registers:
                registers[compRegister] = 0
        compValue = registers[compRegister]

        comparator  = instruction[5]
        comparand   = int(instruction[6])

        # check if the condition is met
        conditionMet = False
        if comparator == "<":
                conditionMet = (compValue < comparand)
        if comparator == ">":
                conditionMet = (compValue > comparand)
        if comparator == "<=":
                conditionMet = (compValue <= comparand)
        if comparator == ">=":
                conditionMet = (compValue >= comparand)
        if comparator == "==":
                conditionMet = (compValue == comparand)
        if comparator == "!=":
                conditionMet = (compValue != comparand)

        # if the condition is met, add or subtract the value from modRegister
        if conditionMet:
                modValue = int(instruction[2])
                if (instruction[1] == "inc"):
                        registers[modRegister] += modValue
                else:
                        registers[modRegister] -= modValue
                # check if largest value seen
                if registers[modRegister] > maxValSeen:
                        maxValSeen = registers[modRegister]


# at the end: figure out which register has the largest value
print "largest register value:", maxValSeen
