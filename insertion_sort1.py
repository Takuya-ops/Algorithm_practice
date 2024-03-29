from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    #  リストの長さの取得（インデックス番号を取得するため）
    len_numbers = len(numbers)
    # インデックス番号１〜最後までループ
    for i in range(1, len_numbers):
        temp = numbers[i]
        # iの前の数字がj
        j = i - 1
        # jが0以上でtemp（jのindexの次の値）よりも大きい場合、
        while j >= 0 and numbers[j] > temp:
            # 前後を入れ替える（j+1はiでもOK？）
            numbers[j+1] = numbers[j]

            j -= 1

        numbers[j+1] = temp

    return numbers


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 100) for _ in range(10)]
    print(insertion_sort(nums))
