def isMonotonic(array):
    c = True  # 単調増加を示すフラグ
    d = True  # 単調減少を示すフラグ
    for i in range(len(array) - 1):
        # 配列内の要素を順番に比較し、単調増加かどうかを判定
        c = c and array[i] <= array[i + 1]
        # 配列内の要素を順番に比較し、単調減少かどうかを判定
        d = d and array[i] >= array[i + 1]
    # 単調増加または単調減少のいずれかが成り立つ場合、単調であると判断
    return c or d


# テスト
if __name__ == "__main__":
    array1 = [-1, -5, -10, -1100, -1100, -1101]
    array2 = [-1, -5, 10, -1100, -1100, -1101]
    print(isMonotonic(array1))
    print(isMonotonic(array2))
