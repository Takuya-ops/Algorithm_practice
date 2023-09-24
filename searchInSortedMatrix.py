def searchInSortedMatrix(matrix, target):
    # 2D配列の大きさを取得
    i = 0
    j = len(matrix[0]) - 1
    while i <= len(matrix) - 1 and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]
