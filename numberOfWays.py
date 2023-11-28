class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == "S"]

        # 椅子の総数が偶数でない、または椅子がない場合は0を返す
        if len(seats) % 2 != 0 or len(seats) == 0:
            return 0

        # 椅子がちょうど2つの場合、分割方法は1通り
        if len(seats) == 2:
            return 1

        ways = 1
        # 最後のペアを除いてループ
        for i in range(1, len(seats) - 1, 2):
            plants_between_seats = seats[i + 1] - seats[i] - 1
            ways = (ways * (plants_between_seats + 1)) % MOD

        return ways


# テスト
solution = Solution()
print(solution.numberOfWays("SSPPSPS"))  # 出力: 3
print(solution.numberOfWays("PPSPSP"))  # 出力: 1
print(solution.numberOfWays("S"))  # 出力: 0
