from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both arrays
        g.sort()
        s.sort()

        # Initialize counters
        contentChildren = 0
        i = 0  # Index for children
        j = 0  # Index for cookies

        # Iterate and assign cookies
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                contentChildren += 1
                i += 1
            j += 1

        # Return the count
        return contentChildren


# Example of using the Solution class
sol = Solution()
print(sol.findContentChildren([1, 2, 3], [1, 1]))  # Output: 1
print(sol.findContentChildren([1, 2], [1, 2, 3]))  # Output: 2
