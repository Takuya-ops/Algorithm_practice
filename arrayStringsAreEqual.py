from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


# テスト
solution = Solution()

test_cases = [
    (["ab", "c"], ["a", "bc"]),  # True
    (["a", "cb"], ["ab", "c"]),  # False
    (["abc", "d", "defg"], ["abcddefg"]),  # True
]

results = [solution.arrayStringsAreEqual(word1, word2) for word1, word2 in test_cases]
print(results)
