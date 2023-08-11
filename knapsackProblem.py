from typing import List, Tuple


def knapsackProblem(
    items: List[Tuple[int, int]], capacity: int
) -> Tuple[int, List[int]]:
    # ナップサック問題を再帰的に解く関数
    def dfs(
        i: int, capacity: int, currValue: int, indices: List[int]
    ) -> Tuple[int, List[int]]:
        # ベースケース: アイテムのインデックスが最大値を超えたり、容量が0以下の場合
        if i >= len(items) or capacity <= 0:
            return currValue, indices  # 現在の価値と選ばれたアイテムの組み合わせを返す

        # 現在のアイテムの価値と重さを取得
        value = items[i][0]
        weight = items[i][1]

        # 現在のアイテムを選ばない場合の再帰呼び出し
        exclude = dfs(i + 1, capacity, currValue, indices)

        # 現在のアイテムを選ぶ場合の条件判定
        if capacity - weight >= 0:
            # 現在のアイテムを選んだ場合の再帰呼び出し
            include = dfs(i + 1, capacity - weight, currValue + value, indices + [i])

            # 選ぶ場合と選ばない場合の価値を比較し、高い方を選ぶ
            if include[0] >= exclude[0]:
                return include[0], include[1]
            return exclude[0], exclude[1]
        else:
            # 容量が足りない場合は、アイテムを選ばないで次のステップへ進む
            return exclude[0], exclude[1]

    # dfs関数を初期値で呼び出して、ナップサック問題を解く
    return dfs(0, capacity, 0, [])


if __name__ == "__main__":
    capacity = 12
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    print(knapsackProblem(items, capacity))
