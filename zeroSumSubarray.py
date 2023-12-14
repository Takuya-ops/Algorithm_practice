def zeroSumSubarray(nums):
    for i in range(len(nums)):
        cumSum = 0
        for j in range(i, len(nums)):
            cumSum += nums[j]

            if cumSum == 0:
                return True
    return False
