def patternMatcher(pattern, string):
    # パターンが空または文字列よりも長い場合は、マッチング不可能なので空のリストを返す
    if len(pattern) == 0 or len(pattern) > len(string):
        return []

    # パターンの最初の文字を取得
    firstLetterA = pattern[0]
    amountOfA = 0
    amountOfB = 0
    firstIdxB = -1

    # パターン内の各文字をチェックしてAとBの数を数える
    for i in range(len(pattern)):
        if pattern[i] == firstLetterA:
            amountOfA += 1
        else:
            # 最初のB文字のインデックスを記録
            if firstIdxB == -1:
                firstIdxB = i
            amountOfB += 1

    # Bが存在しない場合
    if amountOfB == 0:
        lenA = len(string) // amountOfA
        # stringをAの数で均等に分割できる場合、分割して返す
        if lenA * amountOfA == len(string):
            if firstLetterA == "x":
                return [string[:lenA], ""]
            else:
                return ["", string[:lenA]]
        return []

    # Bが存在する場合
    for lenA in range(1, len(string)):
        lenB = getLenB(lenA, amountOfA, amountOfB, len(string))
        if lenB == -1:
            continue

        idxB = firstIdxB * lenA
        stringA = string[:lenA]
        stringB = string[idxB : idxB + lenB]
        potentialMatch = "".join(
            [stringA if char == firstLetterA else stringB for char in pattern]
        )
        # パターンに対する文字列の一致をチェック
        if potentialMatch == string:
            if firstLetterA == "x":
                return [stringA, stringB]
            else:
                return [stringB, stringA]
    return []


def getLenB(lenA, amountOfA, amountOfB, totalLength):
    # B文字列の長さを計算して返す
    v = (totalLength - (amountOfA * lenA)) / amountOfB
    return int(v) if v.is_integer() else -1


# テスト
if __name__ == "__main__":
    pattern = "xxyxxy"
    string = "gogopowerrangergogopowerranger"
    print(patternMatcher(pattern, string))
