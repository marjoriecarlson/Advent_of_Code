#!/usr/bin/python

genA = 516
genB = 190

matches = 0
for i in range(5000000):
    while True:
        genA = (genA * 16807) % 2147483647
        if genA % 4 == 0:
            break
    
    while True:
        genB = (genB * 48271) % 2147483647
        if genB % 8 == 0:
            break

    if (genA & 0xffff) == (genB & 0xffff):
        matches += 1

# solution: how many generated numbers match?
print matches
