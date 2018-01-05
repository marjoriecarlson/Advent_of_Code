#!/usr/bin/python
input = open('input/2.txt','r')
lines = input.readlines()
input.close()

checksum = 0
for line in lines:
    max = -1
    min = 10000
    for value in line.split():
        if int(value) > max:
            max = int(value)
        if int(value) < min:
            min = int(value)
    checksum += (max - min)
print "Checksum:", checksum
