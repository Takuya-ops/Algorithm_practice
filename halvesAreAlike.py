class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        a = s[: n // 2]
        b = s[n // 2 :]

        a_vowel_count = 0
        for c in a:
            if c in "aiueoAIUEO":
                a_vowel_count += 1

        b_vowel_count = 0
        for c in b:
            if c in "aiueoAIUEO":
                b_vowel_count += 1
        return a_vowel_count == b_vowel_count
