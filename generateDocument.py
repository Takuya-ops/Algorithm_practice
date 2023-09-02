from collections import Counter


def generateDocument(characters, document):
    return Counter(document) - Counter(characters) == {}
