from typing import List


def partition(numbers: List[int], low: int, high: int) -> int:
    pass


def quick_sort(numbers: List[int]) -> List[int]:
    def _quicksort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            # 小さい方
            _quicksort(numbers, low, partition_index-1)
            # 大きい方
            _quicksort(numbers, partition_index+1, high)


if __name__ == "__main__":
    nums = [7, 2, 1, 9, 4, 6]
    print(quick_sort(nums))
