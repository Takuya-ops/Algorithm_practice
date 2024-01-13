class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        # Count the frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)

        # Calculate the differences in character counts
        diff = count_s - count_t

        # Sum the differences for all characters
        return sum(diff.values())
