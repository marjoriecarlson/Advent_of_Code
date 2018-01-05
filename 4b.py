#!/usr/bin/python
input = open('input/4.txt','r')
lines = input.readlines()
input.close()

valid = 0
for passphrase in lines:
    anagrammedPhrase = []

    # let's assume it's valid, then subtract it if we find otherwise
    valid += 1

    for word in passphrase.split():            
        # turn word into array & sort to make it its alphabetized anagram
        wordAsArray = list(word)
        wordAsArray.sort()
        anagrammedWord = ''.join(wordAsArray)

        # if it's then the same as some other word in the phrase that has
        # already been alphabetized, then they are anagrams of each other
        if anagrammedWord in anagrammedPhrase:
            valid -= 1
            break
        else:
            anagrammedPhrase.append(anagrammedWord)
        # if it's still valid at the end of the phrase, increment valid phrases

print valid, "passphrases are valid"
