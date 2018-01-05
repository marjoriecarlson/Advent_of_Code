#!/usr/bin/python

lengths = [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100]

# make an array of 256 numbers, 0-255
rope = []
for i in range(256):
        rope.append(i)

index = 0
skipSize = 0

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

# answer required: product of first two list items
print rope[0] * rope[1]
