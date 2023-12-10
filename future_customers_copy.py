class Solution:
    def transpose(self, matrix):
        transposed = []
        for i in range(len(matrix[0])):
            new_row = [matrix[j][i] for j in range(len(matrix))]
            transposed.append(new_row)
        return transposed


# テスト
sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = sol.transpose(matrix1)
print(output)
