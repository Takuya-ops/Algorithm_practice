from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_cost = float("inf")

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                total_cost = prices[i] + prices[j]
                if total_cost <= money:
                    min_cost = min(min_cost, total_cost)

        return money - min_cost if min_cost != float("inf") else money


class Solution2:
    def buyChoco(self, prices: List[int], haveMoney: int) -> int:
        # 初期値として設定してしておく必要がある（金額が足りずチョコが買えない場合があるため）
        min_cost = float("inf")

        for i in range(len(prices)):
            # 上のfor文で選択しているものを含めたくないので"+1"している。
            for j in range(i + 1, len(prices)):
                total_cost = prices[i] + prices[j]
                if total_cost <= haveMoney:
                    min_cost = total_cost
        if min_cost != float("inf"):
            return haveMoney - min_cost
        else:
            # 金額が足りずチョコが買えない場合は所持金を返す
            return haveMoney


# テストケース
sol = Solution2()
prices = [98, 54, 6, 34, 66, 63, 52, 39]
# 6と39が選択される
money = 62
print(sol.buyChoco(prices, money))
