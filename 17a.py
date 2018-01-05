numSteps = 370
numIters = 2017

index = 0
buf = [0]

for nextValue in range(1, numIters + 1):
    # advance the index
    index = (index + numSteps) % len(buf)

    # add the next consecutive val at that index
    if index == (len(buf) - 1): # if at end, just append nextValue
        buf.append(nextValue)

    else:
        temp = buf[index+1:]     # save values AFTER current index
        buf[index+1] = nextValue # add nextValue right after index
        buf.append(0)            # append garbage to ++ buf length
        buf[index+2:] = temp     # restore stored vals after nextValue

    # increment the index to point at the val we added
    index += 1

# solution = what *follows* the last-inserted value -- so, at index+1
print buf[index+1]
