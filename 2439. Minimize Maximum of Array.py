class Solution:
    def minimizeArrayValue(self, numbers: List[int]) -> int:
        # 初期化
        answer = 0
        # 累積和
        prefix_sum = 0

        for i in range(len(numbers)):
            # 累積和
            prefix_sum += numbers[i]
            # math.ceilは引数として与えた数以上の最小の整数を返す
            # 数の大きな方を取得
            answer = max(answer, math.ceil(prefix_sum / (i + 1)))

        return answer
