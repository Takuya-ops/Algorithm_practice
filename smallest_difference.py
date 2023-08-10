def smallestDifference(arrayOne, arrayTwo):
    # 与えられた2つの配列を昇順にソート
    arrayOne.sort()
    arrayTwo.sort()

    # 初期値を設定
    smallest, pair = float("inf"), []  # 最小の差と対応するペアを初期化
    oneIdx, twoIdx = 0, 0  # 配列のインデックスを初期化

    # 配列の要素を比較して最小の差と対応するペアを求める
    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        numOne, numTwo = arrayOne[oneIdx], arrayTwo[twoIdx]
        current = abs(numOne - numTwo)  # 現在の差の絶対値を計算
        if current < smallest:
            smallest = current
            pair = [numOne, numTwo]  # 最小の差のペアを更新
        if numOne > numTwo:
            twoIdx += 1  # numOne > numTwo の場合、numTwoを次に進める
        else:
            oneIdx += 1  # numOne <= numTwo の場合、numOneを次に進める

    return pair  # 最小の差を持つペアを返す


if __name__ == "__main__":
    arrayOne = [10, 0, 20, 25, 2000]
    arrayTwo = [1005, 1006, 1014, 1032, 1031]
    print(smallestDifference(arrayOne, arrayTwo))
