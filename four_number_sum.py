def fourNumberSum(array, targetSum):
    result = []  # 合計が目標値と一致する組み合わせを格納するリスト
    array.sort()  # 配列をソートして順序を整える
    for i in range(len(array) - 3):  # 4つの要素の組み合わせを探すため、最後から4番目の要素までループ
        for j in range(
            i + 1, len(array) - 2
        ):  # iより後ろの要素との組み合わせを考えるため、i+1から最後から3番目の要素までループ
            left = j + 1  # 左側のポインタをjの次の位置に設定
            right = len(array) - 1  # 右側のポインタを配列の最後に設定
            while left < right:
                total_sum = (
                    array[i] + array[j] + array[left] + array[right]
                )  # 4つの要素の合計を計算
                if total_sum == targetSum:
                    result.append(
                        [array[i], array[j], array[left], array[right]]
                    )  # 合計が目標値と一致する場合、組み合わせをリストに追加
                    right -= 1  # 右側のポインタを減少させる（より小さい値を試すため）
                    left += 1  # 左側のポインタを増加させる（より大きい値を試すため）
                elif total_sum > targetSum:
                    right -= 1  # 合計が目標値より大きい場合、右側のポインタを減少させる
                else:
                    left += 1  # 合計が目標値より小さい場合、左側のポインタを増加させる
    return result  # 合計が目標値と一致する組み合わせのリストを返す


# テスト
if __name__ == "__main__":
    array = [7, 6, 4, -1, 2]
    targetsum = 16
    print(fourNumberSum(array, targetsum))
