# 関数の引数に型を明示できるようにする。
from typing import List

# Noneを指定することで、対象のリストを上書きできるようにする。


def even_first_odd_end(numbers: List[int]) -> None:
    # 空のリストを作成する
    even_list, odd_list = [], []
    # リストの始めから見ていき、
    for num in numbers:
        # もし２で割った余りが０ならば、
        if num % 2 == 0:
            # 偶数用のリストに追加する。
            even_list.append(num)
        # それ以外の場合は、
        else:
            # 奇数用のリストに追加する。
            odd_list.append(num)
    # リスト内のすべての要素を、偶数用のリストと奇数用のリストを結合したものに置き換える。
    numbers[:] = even_list + odd_list


# テスト
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_first_odd_end(list1)
    print(list1)
