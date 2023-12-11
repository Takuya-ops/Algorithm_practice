class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr)
        threshold = n // 4

        for i in range(n - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]
        return -1


solution = Solution()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = solution.findSpecialInteger(arr)
print(result)
