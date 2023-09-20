def oneEdit(stringOne, stringTwo):
    # 文字列の長さの差を計算
    length_difference = abs(len(stringOne) - len(stringTwo))

    # 長さの差が2以上ある場合、2つの文字列は絶対に1文字の編集で一致しない
    if length_difference >= 2:
        return False

    if len(stringOne) == len(stringTwo):
        return replaceFunction(stringOne, stringTwo)
    elif len(stringOne) < len(stringTwo):
        return addFunction(stringOne, stringTwo)
    else:
        return addFunction(stringTwo, stringOne)


def replaceFunction(stringOne, stringTwo):
    diff_count = 0
    for i in range(len(stringOne)):
        if stringOne[i] != stringTwo[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    return True


def addFunction(shorter, longer):
    short_index = 0
    long_index = 0
    diff_count = 0

    while short_index < len(shorter) and long_index < len(longer):
        if shorter[short_index] != longer[long_index]:
            diff_count += 1
            if diff_count > 1:
                return False
            long_index += 1
        else:
            short_index += 1
            long_index += 1

    return True


# テスト
print(oneEdit("pale", "ple"))  # True
print(oneEdit("pales", "pale"))  # True
print(oneEdit("pale", "bale"))  # True
print(oneEdit("pale", "bake"))  # False
