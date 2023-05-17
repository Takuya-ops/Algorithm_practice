from typing import List


class Solution:
    def pairSum(self, head: List[int]) -> int:
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next

        # 対になる場合を足し合わせていく
        # はじめのインデックス
        i = 0
        # 最後のインデックス
        j = len(values) - 1
        maximumSum = 0
        while (i < j):
            maximumSum = max(maximumSum, values[i] + values[j])
            i = i + 1
            j = j - 1
        return maximumSum
