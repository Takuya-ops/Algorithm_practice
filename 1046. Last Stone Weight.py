# 関数内で型明示する
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # 入れ替え
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()

        while len(stones) > 1:
            stone1 = remove_largest()
            stone2 = remove_largest()
            # もし重さが上位２つの石の差が異なるなら、
            if stone1 != stone2:
                # その差をリストに加える。
                stones.append(stone1 - stone2)

        # リストに残った最後の要素を返す
        return stones[0] if stones else 0


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(Solution().lastStoneWeight(list1))
