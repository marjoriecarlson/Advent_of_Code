#!/usr/bin/python

input = open('input/10.txt','r')
lines = input.read()
input.close()

# create lengths by converting input to ASCII values and appending 5 given values
lengths = []
for char in lines:
        lengths.append(ord(char))  # add ascii value to lengths
lengths.extend([17, 31, 73, 47, 23])

# make an array of 256 numbers, 0-255
rope = []
for i in range(256):
        rope.append(i)

# these are preserved between the 64 hash runs
index = 0
skipSize = 0

#64 times with same lengths input
for i in range(64):
        # create a hash by reversing subchunks of the array of the lengths specified above.
        # on each iteration, the index moves by the previous subchunk's length + a skipSize
        # that gets larger on each iteration.
        for length in lengths:
                endOfChunk = index + length

                # simple case: the entire chunk is in the array, no wrapping required
                # slice it, reverse it, copy it back in
                if endOfChunk <= len(rope):
                        sublist = rope[index:endOfChunk]
                        sublist.reverse()
                        rope[index:endOfChunk] = sublist

                # hard case: have to wrap back around to the beginning of the array
                else:
                        # create the chunk by slicing the end chunk and beginning chunk
                        sublist = rope[index:]
                        lenOfEndChunk = len(sublist)
                        lenOfBegChunk = length - len(sublist)
                        sublist.extend(rope[0:lenOfBegChunk])

                        #reverse the chunk, then copy it back into the end and beg. chunks
                        sublist.reverse()
                        rope[index:] = sublist[0:lenOfEndChunk]
                        rope[0:lenOfBegChunk] = sublist[lenOfEndChunk:]

                # index increments by length plus an increasing skipSize, and wraps
                index = (index + length + skipSize) % len(rope)
                skipSize += 1

# rope[] is now the sparse hash; we ^ it together to get the final hash

finalHash = ""
for i in range(0, 256, 16):
        thisBlock = rope[i:i+16]
        thisBlockHash = 0

        for j in range(16):
                thisBlockHash ^= thisBlock[j]
        hexHash = hex(thisBlockHash)
        if len(hexHash) == 3: # append hash digits,
                              # prepending 0 if it's one-digit
                finalHash += ('0')
                finalHash += (hexHash[2])
        else:
                finalHash += (hexHash[2:])

print finalHash
