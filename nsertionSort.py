def insertionSort(array):
    for idx in range(len(array)):
        while idx > 0 and array[idx] < array[idx - 1]:
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            idx -= 1
    return array
