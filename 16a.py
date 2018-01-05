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

input = open('input/16.txt','r')
lines = input.readlines()
input.close()

for line in lines:
    if line[0] == 's':
        dancers = spin(int(str(line[1:])))
    else: # swap dancers specified in args
        a, b = line[1:-1].split('/')
        if line[0] == 'x':
            exchange(int(a), int(b))
        else:
            exchange(dancers.index(a), dancers.index(b))

# solution = configuration of dancers at the end
print ''.join(dancers)=
