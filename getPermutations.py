def getPermutations(array):
    def helper(array):
        if len(array) == 1:
            yield array

        for idx, element in enumerate(array):
            remaining = array[:idx] + array[idx + 1 :]
            for sub_perm in helper(remaining):  # "remainig" ではなく "remaining" を使います
                yield [element] + sub_perm

    return list(helper(array))

def getPer