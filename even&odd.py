# 作成するものは、リストの中の数字を偶数（昇順）、奇数（昇順）に並び替えるもの

# 関数指定の際の引数に、型を明示するために必要
from typing import List

# 与えるものは数字のリスト
# 与えたリストの内容をそのまま引き継ぐので、返り値はNone
# 方針：偶数、奇数のリストを別々に用意してやって、後でくっつける。


def even_first_odd_end(numbers: list) -> None:
    # 偶数、奇数用のリストを用意
    even_list, odd_list = [], []
    # numbers内の数字が２で割った時の余りがゼロのものを偶数のリストに入れてやる。
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)


# 返すものは並び替えを行ったあとのリスト
