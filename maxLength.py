class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isUnique(s):
            return len(s) == len(set(s))

        def backtrack(index, current):
            if index == len(arr):
                return len(current)

            include_length = 0
            if isUnique(current + arr[index]):
                include_length = backtrack(index + 1, current + arr[index])

            exclude_length = backtrack(index + 1, current)

            return max(include_length, exclude_length)

        return backtrack(0, "")
