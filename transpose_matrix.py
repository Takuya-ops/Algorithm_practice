def transposeMatrix(matrix):
    return list(zip(*matrix))


# テスト
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(transposeMatrix(matrix))

# # zip関数
# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 92, 78]

# # zip関数で対応する要素をまとめる
# zipped_data = zip(names, scores)

# # zipオブジェクトをリストに変換して表示
# zipped_list = list(zipped_data)
# print(zipped_list)


# # アンパック演算子
# coordinates = (3, 7)

# x, y = coordinates  # タプルの要素を変数にアンパックする
# print("x:", x)
# print("y:", y)
