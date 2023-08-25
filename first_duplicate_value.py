def firstDuplicateValue(array):
    hash = {}
    for item in array:
        if hash.get(item):
            return item
        hash[item] = True
    return -1
