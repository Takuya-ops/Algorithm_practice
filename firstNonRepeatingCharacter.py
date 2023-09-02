from collections import Counter


def firstNonRepeatingCharacter(string):
    sc = Counter(string)
    for i in range(len(string)):
        if sc[string[i]] == 1:
            return i
    return -1
