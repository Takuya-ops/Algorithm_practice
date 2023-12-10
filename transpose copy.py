class Solution:
    def transpose(self, matrix):
        transposed = []
        # for i in range(len(matrix[0])):
        #     new_row = [matrix[j][i] for j in range(len(matrix))]
        #     transposed.append(new_row)
        # return transposed

        # 内包表記を使わない場合
        for i in range(len(matrix[0])):  # 元の行列の列の数だけ繰り返す
            new_row = []  # 新しい行のための空リスト
            for j in range(len(matrix)):  # 元の行列の各行に対して繰り返す
                new_row.append(matrix[j][i])  # 元の行列の j 行 i 列の要素を新しい行に追加
            transposed.append(new_row)  # 完成した新しい行を転置行列に追加
        return transposed


# Creating an instance of the Solution class
solution = Solution()

# Testing the method with the provided examples
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output1 = solution.transpose(matrix1)
print("転置後の行列：" + str(output1))
