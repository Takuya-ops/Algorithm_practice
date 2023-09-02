def selectionSort(array):
    for i in range(len(array)):
        arg_min = min(range(i, len(array)), key=lambda x: array[x])
        array[i], array[arg_min] = array[arg_min], array[i]
    return array
