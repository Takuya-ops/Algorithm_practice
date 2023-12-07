class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:  # 奇数の桁を見つける
                return num[: i + 1]  # その桁までの部分文字列を返す
        return ""  # 奇数が見つからない場合は空文字を返す


# テスト
sol = Solution()
print(sol.largestOddNumber("52"))  # 期待される出力: "5"
print(sol.largestOddNumber("4206"))  # 期待される出力: ""
print(sol.largestOddNumber("35427"))  # 期待される出力: "35427"
