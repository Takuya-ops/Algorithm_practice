def semordnilap(words):
    arr = []
    map = {}
    for word in words:
        map[word] = 1
        reverse = word[::-1]
        if reverse in map and reverse != word:
            arr.append([word, reverse])
    return arr
