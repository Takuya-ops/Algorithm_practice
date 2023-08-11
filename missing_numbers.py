def missingNumbers(nums):
    # 正の無限大の値を2つリストに追加しておくことで、ループ処理を簡略化する
    nums += [float("inf"), float("inf")]

    # 数値を変換して欠けている整数の位置を示す
    for index in range(len(nums) - 2):
        visited_index = abs(nums[index]) - 1  # 数値の絶対値から1引いた値が、位置を示す
        nums[visited_index] *= -1  # 指定された位置の数値を負に変換することで、その位置が存在することを示す

    missing = []
    # 正の数が残っている位置が、欠けている整数を示す
    for index, num in enumerate(nums):
        if num > 0:  # 正の数が残っている位置が、欠けている整数を示す
            missing.append(index + 1)  # インデックス+1が欠けている整数として追加される
    return missing


if __name__ == "__main__":
    nums = [1, 3]
    print(missingNumbers(nums))
