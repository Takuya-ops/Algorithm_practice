def runLengthEncoding(string):
    ret = ""
    stck = [string[0]]
    for s in string[1:]:
        if stck[-1] == s and len(stck) < 9:
            stck.append(s)
        else:
            ret += str(len(stck)) + stck[-1]
            stck = [s]
    ret += str(len(stck)) + stck[-1]
    return ret
