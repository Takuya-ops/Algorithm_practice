from typing import List


def insertion_sort(numbers: List[int]):
    # numbersの長さを取得
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


def bucket_sort(numbers: List[int]) -> List[int]:
    # リストの中から最大値を取り出す
    max_num = max(numbers)
    # リストの長さを取る
    len_numbers = len(numbers)
    # 作成するバケットの数
    size = max_num // len_numbers
    # バケットの作成
    buckets = [[] for _ in range(size)]

    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bucket_sort(nums))
