def isValidSubsequence(array, sequence):
    # インデックス変数を初期化する
    arrIdx = 0  # arrayのインデックスを表す変数
    seqIdx = 0  # sequenceのインデックスを表す変数

    # arrayとsequenceの要素を比較しながらサブシーケンスを検証する
    while arrIdx < len(array) and seqIdx < len(sequence):
        # array[arrIdx]とsequence[seqIdx]が等しい場合、次のsequence要素を検索する
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1  # sequenceのインデックスを次に進める
        arrIdx += 1  # arrayのインデックスを次に進める

    # サブシーケンスの検証結果を返す
    return seqIdx == len(sequence)


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [22, 25, 6]
    print(isValidSubsequence(array, sequence))
