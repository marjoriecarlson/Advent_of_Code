#!/usr/bin/python

class Scanner(object):
    def __init__(self, depth, rnge):
        self.depth = depth
        self.range = rnge

    def positionAtPicoSecond(self, picoSecond):
        lastIndex = self.range - 1
        # the scanner returns to the origin every (2* lastIndex) ps, so we can mod the time
        time = picoSecond % (2 * lastIndex) 
        if (time <= lastIndex): # simple case: outward bound, position = time
            return time
        else: # inward bound, moving opposite direction
            stepsBack = time - lastIndex  # subtract out all forward movements
            return lastIndex - stepsBack  # more steps back = smaller index

    def __str__(self):
        return str(self.depth) + ' ' + str(self.range)


file = open('input/13.txt','r')
lines = file.readlines()

# assemble a dictionary of scanners based on the input
scanners = {}
maxDepth = 0
for line in lines:
    input = line.split(': ')
    depth = int(input[0])
    rnge = int(input[1])
    scanners[depth] = Scanner(depth, rnge)
    if depth > maxDepth:
        maxDepth = depth

# find the smallest delay that leads to no collisions
delay = 0
while True: # each attempt at an increasing delay, until success reached
    myDepth = 0
    for picoSecond in range(delay, delay + maxDepth + 1): # see if we succeed at each picosecond
        if myDepth in scanners and scanners[myDepth].positionAtPicoSecond(picoSecond) == 0:
            break
        else:
            myDepth += 1 # if no collision, increment my depth and keep checking

    # we've left the picosecond loop either because we made it through the puzzle, OR because
    # we had a collision. If success, print successful delay; if failure, increment the delay
    # and try again
    if myDepth > maxDepth:
        print "Success with delay =", str(delay)
        break
    else:
        delay += 1
