# 一回のリストのループ中に数の逆転があったら、その値を適切な位置まで移動させる
from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        # 現在の最小の値を保持しておく
        temp = numbers[i]
        j = i - 1
        # 適切な位置まで移動させる
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(insertion_sort(nums))
