def longestPeak(array):
    currPeak, maxPeak = 0, 0
    isIncreasing = False
    isDecreasing = False

    for i in range(1, len(array)):
        prevNumber = array[i - 1]
        currNumber = array[i]

        if currNumber > prevNumber:
            if isDecreasing:
                maxPeak = max(currPeak, maxPeak)
                currPeak = 1
                isDecreasing = False
            if isIncreasing:
                currPeak += 1
            else:
                isIncreasing = True
                currPeak = 2
        elif currNumber < prevNumber:
            if isIncreasing:
                currPeak += 1
                isDecreasing = True
            else:
                isDecreasing = False
        else:
            if isDecreasing:
                maxPeak = max(currPeak, maxPeak)
            currPeak = 0
            isIncreasing = False
            isDecreasing = False

    if isDecreasing:
        maxPeak = max(currPeak, maxPeak)

    return maxPeak
