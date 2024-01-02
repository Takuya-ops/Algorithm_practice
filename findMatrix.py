from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Count the frequency of each number in nums
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Initialize the 2D array with enough rows for the most frequent number
        max_freq = max(freq.values())
        res = [[] for _ in range(max_freq)]

        # Step 2: Distribute the numbers across the rows
        for num in nums:
            for row in res:
                # Place the number in the first row where it's not present
                if num not in row:
                    row.append(num)
                    break

        return res


from collections import defaultdict


class Solution2:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        max_freq = max(freq.values())
        res = [[] for _ in range(max_freq)]

        for num in nums:
            for row in res:
                if num not in row:
                    row.append(num)
                    break
        return res
