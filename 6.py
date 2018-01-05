#!/usr/bin/python

banks = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
redistributions = 0
configsSeen = [banks[:]] # slice for shallow copy

while True:
        # do this every time
        redistributions += 1
        maxBlocks = 0     # contents of fullest bank
        fullestBank = -1  # index of fullest bank

        #find bank with most blocks
        for bank, blocks in enumerate(banks):
                if blocks > maxBlocks:
                        maxBlocks = blocks
                        fullestBank = bank

        # zero out the most-full bank
        banks[fullestBank] = 0

        # iterate through maxBlocks banks starting at one past fullest
        nextBank = fullestBank + 1
        for i in range(nextBank, nextBank + maxBlocks):
                banks[i % 16] += 1   # mod 16 so we wrap

        # check if this configuration has been seen; if so, end
        newConfig = banks[:] # slice for a shallow copy
        if newConfig in configsSeen:
                prevIteration = configsSeen.index(newConfig)
                print "Configuration", newConfig
                print "was seen on iterations", prevIteration, "and", redistributions
                print "Cycle length", redistributions - prevIteration
                break
        else:
                # if not yet seen, it's been seen now!
                configsSeen.append(newConfig)
