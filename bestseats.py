def bestSeat(seats):
    if 0 not in seats:
        return -1

    longest = float("-inf")
    indexes = []
    startIdx = 1

    while startIdx < len(seats):
        if seats[startIdx] == 0:
            endIdx = startIdx
            while endIdx < len(seats) and seats[endIdx] == 0:
                endIdx += 1
            length = endIdx - startIdx
            if length > longest:
                indexes = [startIdx, endIdx - 1]
                longest = endIdx - startIdx
        startIdx += 1
    return sum(indexes) // 2
