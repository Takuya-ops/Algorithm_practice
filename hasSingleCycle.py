def hasSingleCycle(array):
    jumps = 0
    position = 0

    while True:
        position += array[position]
        position %= len(array)
        jumps += 1

        if position == 0 or array[position] == 0 or jumps > len(array):
            break

    return jumps == len(array)
