from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = sorted([x for x, _ in points])

        max_width = 0

        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i - 1]
            max_width = max(max_width, width)

        return max_width


# テスト
solution = Solution()
points = [[8, 7], [9, 9], [7, 4], [9, 7]]
solution.maxWidthOfVerticalArea(points)
