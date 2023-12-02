from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Count the frequency of each character in chars
        chars_count = {}
        for char in chars:
            chars_count[char] = chars_count.get(char, 0) + 1

        # Function to check if a word can be formed by characters from chars
        def can_form(word):
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1
                if word_count[char] > chars_count.get(char, 0):
                    return False
            return True

        return sum(len(word) for word in words if can_form(word))


# Test cases
solution = Solution()
test_cases = [
    (["cat", "bt", "hat", "tree"], "atach"),  # 6
    (["hello", "world", "leetcode"], "welldonehoneyr"),  # 10
]

results = [solution.countCharacters(words, chars) for words, chars in test_cases]
print(results)
