class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                max_good = max(max_good, num[i : i + 3])

        return max_good


sol = Solution()
print(sol.largestGoodInteger("6777133339"))  # output: "777"
print(sol.largestGoodInteger("42352338"))  # Output: ""
