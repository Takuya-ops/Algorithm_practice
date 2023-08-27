def largestRange(array):
    nums = set(array)
    maxLength = 0
    bestRange = []

    for num in array:
        if num - 1 not in nums:
            i = num
            while i in nums:
                i += 1
            currentLength = i - num
            if currentLength > maxLength:
                maxLength = currentLength
                bestRange = [num, i - 1]
    return bestRange
