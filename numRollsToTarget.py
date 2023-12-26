class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7  # モジュロ値
        dp = [[0] * (target + 1) for _ in range(n + 1)]  # DPテーブルの初期化
        dp[0][0] = 1  # 基本ケース

        for i in range(1, n + 1):  # サイコロの数について反復処理
            for j in range(1, target + 1):  # すべての可能なターゲットについて反復処理
                for x in range(1, min(k, j) + 1):  # 各サイコロの可能な面について反復処理
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % MOD  # DPテーブルを更新

        return dp[n][target]  # n個のサイコロとターゲット合計での結果を返す


# インスタンスを作成
solution = Solution()

# テスト
print(solution.numRollsToTarget(1, 6, 3))  # 出力: 1
print(solution.numRollsToTarget(2, 6, 7))  # 出力: 6
print(solution.numRollsToTarget(30, 30, 500))  # 出力は大きな数値とモジュロ演算により異なる場合がある
