from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # 行数と列数を取得
        m, n = len(grid), len(grid[0])

        # 行と列における1の数を計算
        ones_row = [sum(row) for row in grid]
        ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        # 差分行列を生成
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                zeros_row = n - ones_row[i]  # 行における0の数
                zeros_col = m - ones_col[j]  # 列における0の数
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row - zeros_col

        return diff


# テスト用のインスタンスと入力データ
sol = Solution()
test_cases = {
    "test1": [[0, 1, 1], [1, 0, 1], [0, 0, 1]],
    "test2": [[1, 1, 1], [1, 1, 1]],
    "test3": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    "test4": [[0, 0, 0], [0, 0, 0]],
    "test5": [[1, 1], [1, 1], [1, 1]],
}

# テスト実行
test_results = {}
for test_name, grid in test_cases.items():
    test_results[test_name] = sol.onesMinusZeros(grid)

print(test_results)
