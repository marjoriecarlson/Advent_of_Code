#!/usr/bin/python

# Basic insight: if a move follows a move in the opposite direction,
# you can just cancel them both out. Also, any move can be combined with
# two other neighboring moves, e.g., a move north + a move southwest is
# equivalent to one move northwest. If you cancel out/combine moves as
# much as possible, you will end up with the minimum number of uncombinable
# moves.

class MoveClass(object):
    def __init__(self):
        self.north = 0
        self.south = 0
        self.northwest = 0
        self.northeast = 0
        self.southwest = 0
        self.southeast = 0

    def moveNorth(self):
        if self.south > 0:
            self.south -= 1
        elif self.southwest > 0:
            self.southwest -= 1
            self.northwest += 1
        elif self.southeast > 0:
            self.southeast -= 1
            self.northeast += 1
        else:
            self.north += 1
        
    def moveSouth(self):
        if self.north > 0:
            self.north -= 1
        elif self.northwest > 0:
            self.northwest -= 1
            self.southwest += 1
        elif self.northeast > 0:
            self.northeast -= 1
            self.southeast += 1
        else:
            self.south += 1
        
    def moveNorthWest(self):
        if self.southeast > 0:
            self.southeast -= 1
        elif self.south > 0:
            self.south -= 1
            self.southwest += 1
        elif self.northeast > 0:
            self.northeast -= 1
            self.north += 1
        else:
            self.northwest += 1
        
    def moveNorthEast(self):
        if self.southwest > 0:
            self.southwest -= 1
        elif self.south > 0:
            self.south -= 1
            self.southeast += 1
        elif self.northwest > 0:
            self.northwest -= 1
            self.north += 1
        else:
            self.northeast += 1
        
    def moveSouthWest(self):
        if self.northeast > 0:
            self.northeast -= 1
        elif self.north > 0:
            self.north -= 1
            self.northwest += 1
        elif self.southeast > 0:
            self.southeast -= 1
            self.south += 1
        else:
            self.southwest += 1
        
    def moveSouthEast(self):
        if self.northwest > 0:
            self.northwest -= 1
        elif self.north > 0:
            self.north -= 1
            self.northeast += 1
        elif self.southwest > 0:
            self.southwest -= 1
            self.south += 1
        else:
            self.southeast += 1

    def totalSteps(self):
        return (self.north + self.south + self.northwest +
                self.northeast + self.southwest + self.southeast)

    def __str__(self):
        return ("N  "  + str(self.north) +
               " S  " + str(self.south) +
               "\nNW " + str(self.northwest) +
               " NE " + str(self.northeast) +
               "\nSW " + str(self.southwest) +
               " SE " + str(self.southeast))

input = open('input/11.txt','r')
moves = input.read().split(",")

path = MoveClass()
maxSteps = 0
for move in moves:
    if move == "n":
        path.moveNorth()
    elif move == "s":
        path.moveSouth()
    elif move == "nw":
        path.moveNorthWest()
    elif move == "ne":
        path.moveNorthEast()
    elif move == "sw":
        path.moveSouthWest()
    else:
        path.moveSouthEast()
    if maxSteps < path.totalSteps(): # update maxsteps on every move
        maxSteps = path.totalSteps()

print path
print "Total steps:", path.totalSteps(), "max steps:", maxSteps
