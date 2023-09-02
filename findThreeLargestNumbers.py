def findThreeLargestNumbers(array):
    output = [float("-inf")] * 4
    for num in array:
        output[0] = num
        output.sort()
    return output[-3:]
