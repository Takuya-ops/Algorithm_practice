def spiralTraverse(array):
    sol = []  # 螺旋順に巡回した要素を格納するためのリスト

    while array:  # array リストが空になるまで繰り返す
        sol += array.pop(0)  # array リストの先頭行の要素を sol リストに追加
        array = list(zip(*array))[::-1]  # 残りの行を90度回転して array を更新

    return sol  # 螺旋順に巡回した要素が格納されたリストを返す
