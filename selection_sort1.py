# 選択ソート：リストの中から１番小さな数値を探す → 見つけた最小の数値と、リストの始めの数値を入れ替える → これを繰り返す
from typing import List

# 関数の定義：


def selection_sort(numbers: List[int]) -> List[int]:
    # インデックス番号の取り出し
    len_numbers = len(numbers)
    for i in range(len_numbers):
        # インデックス番号を一時的に保持しておく
        min_idx = i
        # 次のインデックス以降の要素を順に見ていく
        for j in range(i+1, len_numbers):
            # 現在保持している値より小さければ、その値のインデックス値を保持する
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        # 一番小さかった値を先頭に持ってくる
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


# テスト
if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for i in range(10)]
    print(selection_sort(nums))
