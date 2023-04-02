from typing import List

# 返り値はインデックス番号


def linear_search(numbers: List[int], value: int) -> int:
    # numbersリスト内のインデックス番号を取り出す
    for i in range(0, len(numbers)):
        # もしnumbers内の値が、valueの値と同じならば、
        if numbers[i] == value:
            # そのインデックス番号を返す
            return i
    # リストに存在していなければ-1を返す
    return -1


if __name__ == '__main__':
    nums = [1, 4, 6, 7, 10, 13, 17, 20]
    print("この数字のインデックス番号は、")
    print(linear_search(nums, 13))
