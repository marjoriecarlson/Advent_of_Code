#!/usr/bin/python
input = open('input/2.txt','r')
lines = input.readlines()
input.close()

# Only two numbers in each row CAN evenly divide each other.

checksum = 0
for line in lines:
    for currVal in line.split():
        for compareVal in line.split():
            if currVal != compareVal: # don't divide by itself!
                ratio = float(compareVal)/float(currVal)
                if ratio == int(ratio): # is divisible
                    checksum += int(ratio)
print "Checksum:", checksum
