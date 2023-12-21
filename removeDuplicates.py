class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


# テスト
test1 = [1, 1, 1, 2, 2, 3]
test2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]

solution = Solution()
k1 = solution.removeDuplicates(test1)
k2 = solution.removeDuplicates(test2)

k1, test1[:k1], k2, test2[:k2]
