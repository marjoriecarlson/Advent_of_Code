#!/usr/bin/python

genA = 516
genB = 190

matches = 0
for i in range(40000000):
    genA = (genA * 16807) % 2147483647
    genB = (genB * 48271) % 2147483647
    if (genA & 0xffff) == (genB & 0xffff):
        matches += 1

# solution: how many generated numbers match?
print matches
