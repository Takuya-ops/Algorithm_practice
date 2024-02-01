# 各配列内の差の最大値をkとする
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []  # 一時的にサブ配列を格納するリスト

        for num in nums:
            if not temp or num - temp[0] <= k:
                temp.append(num)
                if len(temp) == 3:  # tempの要素数の最大は３個まで
                    result.append(temp)
                    temp = []
            else:
                return []

        return result
