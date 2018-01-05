#!/usr/bin/python
input = open('input/4.txt','r')
lines = input.readlines()
input.close()

valid = 0
for passphrase in lines:
	isValid = True
	splitPhrase = passphrase.split()
	splitPhrase.sort()
	for i in range(len(splitPhrase)-1):
		if splitPhrase[i] == splitPhrase[i+1]:
			isValid = False
			break
	if isValid == True:
		valid += 1

print valid
