from typing import List

# pivot(リストの末尾)の値のインデックス値を返す関数


def partition(numbers: List[int], low: int, high: int) -> int:
    # i, j, pivot（リストの最後の基準となる値）の定義
    i = low - 1
    # pivotの指定
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

# クイックソート


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            # 小さい方
            _quick_sort(numbers, low, partition_index-1)
            # 大きい方
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


# テスト
if __name__ == "__main__":
    nums = [1, 6, 2, 4, 9, 8, 7]
    print(quick_sort(nums))
