from typing import List


class Solution:
    def makeEqual(self, words):
        char_count = {}
        for word in words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        for char in char_count:
            if char_count[char] % len(words) != 0:
                return False
        return True


# テスト
sol = Solution()
print(sol.makeEqual(["abc", "aabc", "bc"]))  # True
print(sol.makeEqual(["ab", "a"]))  # False
