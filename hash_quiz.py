from typing import List, Tuple, Optional


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num


if __name__ == "__main__":
    l = [11, 8, 5, 4, 5]
    # 合計した時の値の指定（2つ）
    t = 16
    print(get_pair(l, t))
    print(get_pair_half_sum(l))
