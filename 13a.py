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

# at each picosecond, I will be at the depth equal to that picosecond.
# check if there is a scanner at that depth and, if so, whether it is at position 
collisions = 0
cost = 0
for picoSecond in range(maxDepth + 1):
    # my position at each picoSecond is the depth = picoSecond
    myDepth = picoSecond
    if myDepth in scanners and scanners[myDepth].positionAtPicoSecond(picoSecond) == 0:
        # eek I've been caught! Update collisions & cost 
        collisions += 1
        cost += (myDepth * scanners[myDepth].range)

print collisions, "collisions at a cost of", cost
