def twoNumberSum(array, targetSum):
    storage = set(num for num in array)

    for num in array:
        target = targetSum - num
        if target in storage and target is not num:
            return [num, target]

    return []


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))
