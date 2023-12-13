from typing import List


class Solution:
    def numSpecial(self, mat: List[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1
        return special_count


if __name__ == "__main__":
    sol = Solution()

    mat1 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    print("テストケース：", sol.numSpecial(mat1))
