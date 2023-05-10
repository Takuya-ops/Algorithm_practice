from typing import List

# 値を足し合わせる部分のアルゴリズム（出力はリストに入ったままの状態）


def pascal_triangle(depth: int) -> List[List[int]]:
    # 各深さ毎のリストを作成する（深くなる毎に1が追加されていく）
    data = [[1] * (i + 1) for i in range(depth)]
    # 和を計算できるようになるのは、深さが２以降
    for line in range(2, depth):
        # １つ上の層の値を足したものに置き換える。
        for i in range(1, line):
            data[line][i] = data[line-1][i-1] + data[line-1][i]
    return data

# トライアングル形式で表示させる関数


def print_pascal(data: List[int]) -> None:
    # 桁数に応じたスペースを付与させる（一番深いリストの中で最大の値と取り出す）
    max_digit = len(str(max(data[-1])))
    # widthを偶数にしてやる
    width = max_digit + (max_digit % 2) + 2
    for index, line in enumerate(data):
        # リスト内の数字のみを取り出す
        numbers = "".join([str(i).center(width, " ") for i in line])
        # 深さに応じてインデントを変える
        print((" " * int(width/2)) * (len(data) - index), numbers)


# テスト
if __name__ == "__main__":
    # 改行して表示させる
    print_pascal(pascal_triangle(11))
