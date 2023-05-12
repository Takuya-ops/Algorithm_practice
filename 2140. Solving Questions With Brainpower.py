from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # ポイントとスキップ数の組の数
        n = len(questions)
        # 組の数の分だけ０を持つリストを作成
        dp = [0] * n
        # 作成したリストの末尾を、与えられた配列（question）の末尾の組の1つ目の値で置き換える。（ポイントのみを作成したリストに入れる）
        dp[-1] = questions[-1][0]
        # 0~2のインデックスについてもポイントを入れる（最後の組については、スキップできないため含めない）
        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]

            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]


if __name__ == "__main__":
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(Solution().mostPoints(questions))
