class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # 開始点
        x, y = 0, 0

        # 訪問済みの点を追跡するためのセット
        visited = {(x, y)}

        # 各方向のマッピング
        directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        # パスを辿る
        for move in path:
            dx, dy = directions[move]  # 座標の変化を取得
            x, y = x + dx, y + dy  # 現在位置を更新

            # 新しい位置が既に訪れた場所か確認
            if (x, y) in visited:
                return True  # パスが自身を交差している

            # 新しい位置を訪問済みとしてマーク
            visited.add((x, y))

        # 全ての移動を処理した後に交差が見つからなければFalseを返す
        return False


class Solution2:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(x, y)}
        directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        for move in path:
            dx, dy = directions[move]
            x, y = x + dx, y + dy

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False


# テスト
sol = Solution()
print(sol.isPathCrossing("NES"))  # False
print(sol.isPathCrossing("NESWW"))  # True
