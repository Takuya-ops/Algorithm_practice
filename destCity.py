from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # 出発都市を保存するセットを作成
        starting_cities = set()
        for path in paths:
            starting_cities.add(path[0])

        # 目的地都市を探す
        for path in paths:
            if path[1] not in starting_cities:
                return path[1]


# 例を使ってテスト
sol = Solution()
example1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
example2 = [["B", "C"], ["D", "B"], ["C", "A"]]
example3 = [["A", "Z"]]

output1 = sol.destCity(example1)
output2 = sol.destCity(example2)
output3 = sol.destCity(example3)
print(output1, output2, output3)
