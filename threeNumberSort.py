def threeNumberSort(array, order):
    index = 0
    for i in range(2):
        val = order[i]
        for j in range(len(array)):
            if array[j] == val:
                array[j], array[index] = array[index], array[j]
                index += 1
    return array
