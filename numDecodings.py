class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


class Solution2:
    def numDecordings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            if 1 <= int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


# テスト
solution = Solution()

print(solution.numDecodings("12"))  # 出力: 2通り（AB）、（L）
print(solution.numDecodings("226"))  # 出力: 3通り（BZ）、（VF）、（BBF）
print(solution.numDecodings("06"))  # 出力: 0通り
