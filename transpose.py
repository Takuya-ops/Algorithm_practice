class Solution:
    def transpose(self, matrix):
        # Transposing the matrix
        transposed = []
        for i in range(len(matrix[0])):
            new_row = [matrix[j][i] for j in range(len(matrix))]
            transposed.append(new_row)
        return transposed


# Creating an instance of the Solution class
solution = Solution()

# Testing the method with the provided examples
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output1 = solution.transpose(matrix1)

matrix2 = [[1, 2, 3], [4, 5, 6]]
output2 = solution.transpose(matrix2)

print(output1, output2)
