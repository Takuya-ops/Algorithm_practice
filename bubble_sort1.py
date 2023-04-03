# バブルソート：隣同士を比較する → 最後まで繰り返す → 始めに戻り、隣同士を比較 → 最後から２番目まで繰り返す
from typing import List

# 関数の定義(入力：元のリスト、出力：並べ替えた後のリスト)


def bubble_sort(numbers: List[int]) -> List[int]:
    # リストの長さを求める
    len_numbers = len(numbers)
    # リスト内の要素の個数分、インデックス番号を用意する
    for i in range(len_numbers):
        # 隣同士を比較できるのは最後から２番目まで、最後まで行ったらソートをかける範囲をiの分だけ狭める
        for j in range(len_numbers - 1 - i):
            # 大きさを比較する（手前の数値のほうが大きければ、入れ替える）
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# for文を２回使用しているので、O(N^2オーダー)


# テスト
if __name__ == "__main__":
    # テスト用のランダムな数値を作成する
    import random
    nums = [random.randint(0, 100) for _ in range(10)]
    # ソート後のリストをプリントする
    print(bubble_sort(nums))
