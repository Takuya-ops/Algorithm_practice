from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        # ここ以下の処理について復習
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


if __name__ == "__main__":
    # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    import random
    nums = [random.randint(0, 1000) for _ in range(50)]
    print("-------------元のリスト-------------")
    print(nums)
    print("-------------------------------------")
    print("-------------ソート後のリスト---------------")
    print(insertion_sort(nums))
    print("-------------------------------------")
