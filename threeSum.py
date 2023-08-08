def threeNumberSum(array, targetSum):
    # まず、入力された配列を昇順にソートする。
    array.sort()
    # 返すべき結果を保存する空のリストを作成する。
    res = []

    # 配列の各要素を順番に見ていく。
    for i in range(len(array)):
        # 与えられた数値と他の2つの数値の和がtargetSumになるかをチェックする。
        twoSum(array, i, res, targetSum)
    # すべての組み合わせをチェックした後、結果のリストを返す。
    return res


def twoSum(array, i, res, targetSum):
    # 左のポインタはiの次の位置からスタートする。
    l = i + 1
    # 右のポインタは配列の最後の位置からスタートする。
    r = len(array) - 1

    # 左のポインタが右のポインタより左にある限り、以下のループを実行する。
    while l < r:
        # 現在の3つの数字の和を計算し、targetSumとの比較を行う。
        current_sum = array[i] + array[l] + array[r]

        # もし現在の和がtargetSumより小さいならば
        if current_sum < targetSum:
            # 左のポインタを右に移動して、和を増やす。
            l += 1
        # もし現在の和がtargetSumより大きいならば
        elif current_sum > targetSum:
            # 右のポインタを左に移動して、和を減少させる。
            r -= 1
        # 和がtargetSumと一致する場合
        else:
            # 現在の3つの数字の組み合わせを結果のリストに追加する。
            res.append([array[i], array[l], array[r]])
            # 左のポインタを右に移動して、次の可能な組み合わせを探す。
            l += 1

    # 更新された結果のリストを返す。
    return res


if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, 0, -8, -1]
    targetSum = 0
    print(threeNumberSum(array, targetSum))
