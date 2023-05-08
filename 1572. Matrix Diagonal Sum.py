from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # 正方行列の次元を格納
        n = len(mat)
        ans = 0

        for i in range(n):
            # 一次対角線上の要素を追加
            ans += mat[i][i]
            # 二次対角線上の要素を追加
            ans += mat[n - 1 - i][i]
        # 奇数の正方行列の場合、中心の値が重複してカウントされるため減じる
        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]

        return ans
