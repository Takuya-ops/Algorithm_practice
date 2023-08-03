from typing import List


def order_chagne_by_indexes_v1(chars: List[str], indexes: List[int]) -> str:
    # 与えられた文字の数の長さを持つからのリストを作る。
    tmp = [None] * len(chars)
    # index番号の値のインデックスな同じ場合は、tmpの値を置き換える
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    return "".join(tmp)


if __name__ == "__main__":
    w = ["h", "y", "n", "p", "t", "o"]
    i = [3, 1, 5, 0, 2, 4]
    print(order_chagne_by_indexes_v1(w, i))
