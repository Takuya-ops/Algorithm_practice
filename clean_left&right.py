def subarraySort(array):
    leftvalue = -1
    rightvalue = -1
    maxvalue = array[0]

    for i in range(1, len(array)):
        if array[i] < maxvalue:
            leftvalue = i
        else:
            maxvalue = array[i]

    minvalue = array[len(array) - 1]

    for i in reversed(range(0, len(array))):
        if array[i] > minvalue:
            rightvalue = i
        else:
            minvalue = array[i]

    return [rightvalue, leftvalue]
