class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # ナイトが各数字から移動できる数字のマッピング
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        # DPテーブルの初期化
        dp = [1] * 10

        # n回のジャンプをシミュレート
        for _ in range(n - 1):
            new_dp = [0] * 10
            for i in range(10):
                for move in moves.get(i, []):
                    new_dp[move] = (new_dp[move] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD


# テスト用のコード
sol = Solution()
print(sol.knightDialer(1))  # 10
print(sol.knightDialer(2))  # 20
print(sol.knightDialer(3131))  # 136006598
