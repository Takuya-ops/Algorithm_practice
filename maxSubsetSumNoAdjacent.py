def maxSubsetSumNoAdjacent(array):
    currentMax, previousMax = 0, 0
    for number in array:
        previousMax, currentMax = currentMax, max(currentMax, previousMax + number)
    return currentMax
