def commonCharacters(strings):
    return set.intersection(*[{char for char in string} for string in strings])
