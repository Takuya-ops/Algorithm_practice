from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        # Count the number of 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        special_count = 0
        # Identify and count special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1

        return special_count


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    mat1 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    # Expected output: 1
    print("Test Case 1:", solution.numSpecial(mat1))

    # Test case 2
    mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # Expected output: 3
    print("Test Case 2:", solution.numSpecial(mat2))

    # Test case 3
    mat3 = [[1, 0], [0, 1], [0, 0]]
    # Expected output: 2
    print("Test Case 3:", solution.numSpecial(mat3))
