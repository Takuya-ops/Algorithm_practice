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
example2 = [
    ["London", "New York"],
    ["New York", "Lima"],
    ["Sao Paulo", "Lima"],
]


output1 = sol.destCity(example1)
output2 = sol.destCity(example2)
print(output1, output2)
