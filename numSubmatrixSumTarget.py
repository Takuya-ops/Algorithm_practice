class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # 行ごとの累積和を計算
        for row in matrix:
            for col in range(1, cols):
                row[col] += row[col - 1]

        # すべての列のペアについてループ
        for col_start in range(cols):
            for col_end in range(col_start, cols):
                sums = collections.defaultdict(int)
                cur_sum = 0
                sums[0] = 1  # 空の部分行列

                # すべての行についてループ
                for row in range(rows):
                    # 現在の列のペアにおける行の累積和
                    cur_sum += matrix[row][col_end] - (
                        matrix[row][col_start - 1] if col_start > 0 else 0
                    )
                    # 目標値に達する部分行列の数を加算
                    count += sums[cur_sum - target]
                    # 現在の累積和の出現回数を記録
                    sums[cur_sum] += 1

        return count
