from typing import List

# 方針：i（はじめ）とj（終わり）から順番に値を見ていき、もしiが偶数でなければiとjの数字を入れ替える。


def even_first_odd_end(numbers: List[int]) -> None:
    i, j = 0, len(numbers) - 1
    # iがjのインデックスを超えるまで処理を続ける。
    while i < j:
        if numbers[i] % 2 == 0:
            # i++（インクリメント表記）はpythonでは使えない。
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # j--（デクリメント表記）はpythonでは使えない。
            j -= 1


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_first_odd_end(list1)
    print(list1)
