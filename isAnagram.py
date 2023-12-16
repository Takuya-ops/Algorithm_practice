class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 文字列をソートして比較
        return sorted(s) == sorted(t)


# 使用例
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # 出力: True
print(solution.isAnagram("rat", "car"))  # 出力: False
