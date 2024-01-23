class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = -1
        actual_sum = 0

        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

            actual_sum += abs(num)

        expected_sum = n * (n + 1) // 2

        missing = expected_sum - (actual_sum - duplicate)

        return [duplicate, missing]
