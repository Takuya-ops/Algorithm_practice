import collections  # collectionsモジュールをインポート（キューを使用するため）


class Node:
    def __init__(self, name):
        self.children = []  # 子ノードのリストを初期化
        self.name = name  # ノードの名前を設定

    def addChild(self, name):
        self.children.append(Node(name))  # 新しい子ノードを追加して子ノードリストに格納
        return self  # メソッドチェーンのために自身を返す

    def breadthFirstSearch(self, array):
        # 幅優先探索のためのキューを作成し、初期ノードをキューに格納
        N = collections.deque([self])

        while N:
            n = N.popleft()  # キューからノードを取り出す（先入れ先出し）
            array.append(n.name)  # 取り出したノードの名前を結果配列に追加
            N.extend(n.children)  # 取り出したノードの子ノードをキューに追加（幅優先探索の特徴）

        return array  # 幅優先探索が終わったら結果の配列を返す
