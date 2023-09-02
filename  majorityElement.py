def majorityElement(array):
    l_count = 0
    r_count = 0
    for num in array:
        l_count += 1 if num == array[0] else 0
        r_count += 1 if num == array[-1] else 0
    if l_count > len(array) // 2:
        return array[0]
    if r_count > len(array) // 2:
        return array[-1]
    out = array[1]
    highest = 1
    count = 1
    for i in range(2, len(array) - 1):
        if array[i - 1] == array[i]:
            count += 1
        else:
            if highest < count:
                out = array[i - 1]
            count = 1
    if highest < count:
        out = array[len(array) - 2]
    return out
