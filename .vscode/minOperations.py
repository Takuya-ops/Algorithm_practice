class Solution:
    def minOperations(self, num: str) -> int:
        count0, count1 = 0, 0
        for i, char in enumerate(num):
            if char == "0":
                if i % 2 == 0:
                    count1 += 1
                else:
                    count0 += 1
            else:
                if i % 2 == 0:
                    count0 += 1
                else:
                    count1 += 1
        return min(count0, count1)


class Solution2:
    def minOperations(self, s: str) -> int:
        # 初期化
        count1, count2 = 0, 0

        # 一つ目のパターン("010101...")と二つ目のパターン("101010...")で比較し、パターンから外れた場合にカウントを増やす
        for i in range(len(s)):
            if s[i] != str(i % 2):  # パターン1に対する比較
                count1 += 1
            if s[i] != str((i + 1) % 2):  # パターン2に対する比較
                count2 += 1

        # 二つのパターンのうち、より小さい方の変更回数を返す
        return min(count1, count2)


# テスト
sol = Solution2()

# ケース1: 1回の変更 ("0101"になる)
print(sol.minOperations("0100"))  # 出力: 1

# ケース2: 0回の変更 (すでに交互)
print(sol.minOperations("10"))  # 出力: 0

# ケース3: 2回の変更 ("1010"または"0101"になる)
print(sol.minOperations("1111"))  # 出力: 2
