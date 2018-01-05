#!/usr/bin/python
input = open('input/5.txt','r')
lines = input.readlines()
input.close()

instructions = []
for line in lines:
	instructions.append(int(line))

numInstructions = len(instructions)
numSteps = 0
index = 0

while True:
	numSteps += 1
	instruction = instructions[index]
	instructions[index] += 1
	index += instruction
	if (index < 0 or index >= numInstructions): # outside array
		break
print numSteps, "jumps"
