class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        MOD = 10**9 + 7

        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1

        count = 0
        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        count = (count + dp[move - 1][i][j]) % MOD
                    if i == m - 1:
                        count = (count + dp[move - 1][i][j]) % MOD
                    if j == 0:
                        count = (count + dp[move - 1][i][j]) % MOD
                    if j == n - 1:
                        count = (count + dp[move - 1][i][j]) % MOD
                    dp[move][i][j] = (
                        (dp[move - 1][i - 1][j] if i > 0 else 0)
                        + (dp[move - 1][i + 1][j] if i < m - 1 else 0)
                        + (dp[move - 1][i][j - 1] if j > 0 else 0)
                        + (dp[move - 1][i][j + 1] if j < n - 1 else 0)
                    ) % MOD
        return count


sol = Solution()
# 例1
m, n, maxMove, startRow, startColumn = 2, 2, 2, 0, 0
print(sol.findPaths(m, n, maxMove, startRow, startColumn))

# 例2
m, n, maxMove, startRow, startColumn = 1, 3, 3, 0, 1
print(sol.findPaths(m, n, maxMove, startRow, startColumn))
