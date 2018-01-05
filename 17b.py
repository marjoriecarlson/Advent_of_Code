numSteps = 370
numIters = 50000000

index = 0
bufsize = 1  # we don't need the whole buffer anymore; just model its size

for nextValue in range(1, numIters + 1):
    # advance the index
    index = (index + numSteps) % bufsize

    # if current index is 0, this iteration changes what follows 0.
    if index == 0:
        print nextValue

    # otherwise, all we care about is that buffersize and index increment.
    bufsize += 1                      
    index += 1
