class Solution:
    def maxScore(self, s: str) -> int:
        total_zeros = s.count("0")
        total_ones = s.count("1")

        max_score = 0
        count_zeros, count_ones = 0, total_ones

        for i in range(len(s) - 1):
            if s[i] == "0":
                count_zeros += 1
            else:
                count_ones -= 1

            current_score = count_zeros + count_ones
            max_score = max(max_score, current_score)

        return max_score


# クラスの定義
class Solution2:
    # メソッドの定義
    def maxScore(self, s: str) -> int:
        total_zeros = s.count("0")
        total_ones = s.count("1")

        max_score = 0
        count_zeros, count_ones = 0, total_ones

        for i in range(len(s) - 1):
            if s[i] == "0":
                count_zeros += 1
            else:
                count_ones -= 1

            current_score = count_zeros + count_ones
            max_score = max(max_score, current_score)

        return max_score

class Solution3:
    def maxScore(self, s: str) -> int:
        total_zeros = s.count("0")
        total_ones = s.count("1")
        
        max_score = 0
        count_zeros, count_ones = 0, total_ones
        
        for i in range(len(s) - 1):
            if s[i] == "0":
                count_zeros += 1
            else:
                count_ones -= 1
            
            current_score = count_zeros + count_ones
            max_score = max(max_score, current_score)
            
)
# テスト
sol = Solution()
result1 = sol.maxScore("011101")
result2 = sol.maxScore("00111")
result3 = sol.maxScore("1111")

print(result1, result2, result3)
