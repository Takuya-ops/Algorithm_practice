class Solution:
    def total_money(self, n):
        # 初日の預金額
        money = 1
        # 合計額
        total = 0
        # 現在の週の月曜日の預金額
        monday_deposit = 1

        for i in range(1, n + 1):
            total += money
            # 日曜日の次の日（月曜日）には、前の月曜日より1ドル多く預ける
            if i % 7 == 0:
                monday_deposit += 1
                money = monday_deposit
            else:
                # 火曜日から日曜日までは、前日より1ドル多く預ける
                money += 1

        return total


sol = Solution()

# テストケース
n1 = 4
n2 = 10
n3 = 20

total1 = sol.total_money(n1)
total2 = sol.total_money(n2)
total3 = sol.total_money(n3)

print(total1, total2, total3)
