#!/usr/bin/python
input = open('input/4.txt','r')
lines = input.readlines()
input.close()

# naive solution - check every word in a passphrase against every other word.

valid = 0
for passphrase in lines:
    isValid = True
    phrase = passphrase.split()
    for i in range(len(phrase)):
        for j in range(i+1, len(phrase)):
            if phrase[i] == phrase[j]:
                isValid = False
                break
    # if we're at the end of the phrase and isValid is still true,
    # this passphrase is valid
    if isValid == True:
        valid += 1

print valid, "passphrases are valid"
