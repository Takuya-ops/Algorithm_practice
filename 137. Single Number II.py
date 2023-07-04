class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums) - 1, 3):
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]

        return nums[len(nums) - 1]
