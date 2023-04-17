# extracandiesを足したものが、足す前のリストの最大値以上になればTrueを返す
class Solution(object):
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        # 配列の最大値を取得
        maxCandies = max(candies)
        # 空のリストの作成
        result = []
        # リストの長さを取得
        for i in range(len(candies)):
            # 条件に当てはまるものを、true or falseでリストに追加
            result.append(candies[i] + extraCandies >= maxCandies)
        # 結果を返す
        return result
