def moveElementToEnd(array, toMove):
    # 一時的なインデックスを初期化
    tmp = 0

    # リスト内の各要素に対してループ処理を開始
    for i in range(len(array)):
        # 現在の要素が移動させたい要素でない場合
        if array[i] != toMove:
            # 現在の要素と一時的な位置にある要素を入れ替え
            array[i], array[tmp] = array[tmp], array[i]
            # 一時的な位置を次の要素に更新
            tmp += 1

    # 要素の移動が終了したリストを返す
    return array


# テスト
if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    print(moveElementToEnd(array, toMove))
