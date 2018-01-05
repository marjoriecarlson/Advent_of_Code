# BROKEN!



#!/usr/bin/python

dancers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def spin(num):
    global dancers
    cutoff = len(dancers) - num
    return dancers[cutoff:] + dancers[:cutoff]

def exchange(index1, index2):
    global dancers
    swapTemp = dancers[index1]
    dancers[index1] = dancers[index2]
    dancers[index2] = swapTemp

def printDancers():
    global dancers
    print ''.join(dancers)

input = open('input/16.txt','r')
lines = input.readlines()
input.close()

patternsSeen = [dancers]

for i in range(6000):
    for line in lines:
        if line[0] == 's':
            dancers = spin(int(str(line[1:])))
        else:
            a, b = line[1:-1].split('/')
            if line[0] == 'x':
                exchange(int(a), int(b))
            else:
                exchange(dancers.index(a), dancers.index(b))
#    print dancers
    if dancers not in patternsSeen:
        patternsSeen.append(dancers)
    else:
        print "CYCLE FOUND!", len(patternsSeen)
        print dancers
        break
print "No cycle found."
