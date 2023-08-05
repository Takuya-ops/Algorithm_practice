# sortedSquaredArray関数の定義。整数の配列を受け取り、二乗して昇順にソートした新しい配列を返す。
def sortedSquaredArray(array):
    # sortedSquaresという名前の新しいリストを作成し、arrayと同じ長さで0で初期化する。
    sortedSquares = [0 for _ in array]

    # arrayの要素を順番に処理するためのforループ
    for idx in range(len(array)):
        # 現在処理中の要素の値をvalue変数に代入する。
        value = array[idx]

        # sortedSquaresリストの対応する位置にvalueの二乗を格納する。
        sortedSquares[idx] = value * value

    # すべての要素の二乗がsortedSquaresリストに格納されたら、リストを昇順でソートする。
    sortedSquares.sort()

    # ソートされたsortedSquaresリストを返す。
    return sortedSquares


# テスト
if __name__ == "__main__":
    array = [-4, -2, 0, 2, 4]
    print(sortedSquaredArray(array))
