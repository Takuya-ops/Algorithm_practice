class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {}

        def dp(i, last_char, last_char_count, k):
            if i == len(s):
                return 0

            if (i, last_char, last_char_count, k) in cache:
                return cache[(i, last_char, last_char_count, k)]

            delete_cost = float("inf")
            if k > 0:
                delete_cost = dp(i + 1, last_char, last_char_count, k - 1)

            keep_cost = float("inf")
            if s[i] == last_char:
                addition = 0
                if (
                    last_char_count == 1
                    or last_char_count == 9
                    or last_char_count == 99
                ):
                    addition = 1
                keep_cost = addition + dp(i + 1, last_char, last_char_count + 1, k)
            else:
                keep_cost = 1 + dp(i + 1, s[i], 1, k)

            cache[(i, last_char, last_char_count, k)] = min(delete_cost, keep_cost)
            return cache[(i, last_char, last_char_count, k)]

        return dp(0, "", 0, k)
