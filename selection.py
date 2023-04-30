from typing import List


def selection_sort(numbers: List[int]) -> List[int]:
    # リストの長さを取得
    len_numbers = len(numbers)
    for i in range(len_numbers):
        # 現在のインデックス番号の保存
        min_idx = i
        # 現在のインデックス値と次の要素の値を比較し、大小関係が逆転していれば、入れ替える。
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


# テスト
if __name__ == "__main__":
    import random
    # 0~100までのランダムな値を20個出力する。
    num = [random.randint(0, 100) for _ in range(20)]
    print(selection_sort(num))
