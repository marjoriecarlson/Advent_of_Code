#!/usr/bin/python

registers = {}
lastSound = 0
programCounter = 0
success = False

def checkInitialized(register):
    global registers
    if register not in registers:
        registers[register] = 0

def getValueOf(value): #input could be a # or a register to dereference
    global registers
    try:
        return int(value)
    except: # if it's not a number, it must be a reg
        if value in registers:
            return registers[value]
        return 0
    
def snd(register):
    global lastSound, registers
    lastSound = registers[register]

def rcv(register):
    global lastSound, registers, success
    if registers[register] != 0:
        print lastSound, "recovered!"
        success = True

def math(operation, register, value):
    global registers

    if operation == "set":
        registers[register] = value
    elif operation == "add":
        registers[register] += value
    elif operation == "mul":
        registers[register] *= value
    elif operation == "mod":
        registers[register] %= value
    else:
        print "ERROR", operation, register, value

def jump(register, value):
    global programCounter, registers
    if registers[register] > 0:
        programCounter += (value - 1)  # -1 because it will then increment

def execute(instruction):
    global programCounter
    operation = instruction[0]
    register = instruction[1]
    checkInitialized(register)
    
    if operation == "snd":
        snd(register)

    elif operation == "rcv":
        rcv(register)

    else: # has second arg, which may be numeric or a register
        value = getValueOf(instruction[2])
        if operation == "jgz":
            jump(register, value)
        else: # math operation: set, add, mul or mod
            math(operation, register, value)


file = open('input/18.txt','r')
lines = file.readlines()

# assemble a list of instructions
instructions = []
for line in lines:
    instructions.append(line.split())

while programCounter >= 0 and programCounter < len(instructions) and success == False:
    execute(instructions[programCounter])
    programCounter += 1 # go to next instruction
