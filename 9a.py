#!/usr/bin/python

# Read through a stream of chars; find groups of paired brackets {} {{}{}}.
# Ignore garbage inside <>, including brackets and additional <'s. If you
# encounter an !, ignore the next character.
# Scoring: 1 for outermost {}, add one for however many levels in it is.

stream = open('input/9.txt','r').read()

openParenCount = 0   # keep track of how many open parens await matches
                     # increment when see {, decrement when see }
score = 0

justSawBang = False  # should I ignore this char?
inGarbage = False    # will be used to decide whether to ignore {}s

for char in stream:
        if justSawBang == True:    # skip this character
                justSawBang = False
        elif char == '!':   # bangs count whether in garbage or not
                justSawBang = True
        elif char == '<':
                inGarbage = True
        elif char == '>':
                inGarbage = False
        elif char == '{' and not inGarbage:
                openParenCount += 1
        elif char == '}' and not inGarbage:
                score += openParenCount
                openParenCount -= 1

print score
