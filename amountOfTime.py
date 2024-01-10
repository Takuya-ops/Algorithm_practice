from collections import deque


# バイナリツリーノードの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # ツリーからグラフを作成
        graph = {}

        def build_graph(node, parent=None):
            if node:
                if node.val not in graph:
                    graph[node.val] = []
                if parent:
                    graph[node.val].append(parent)
                    graph[parent].append(node.val)
                build_graph(node.left, node.val)
                build_graph(node.right, node.val)

        build_graph(root)

        # startノードからの最長パスをBFSで見つける
        queue = deque([(start, 0)])
        visited = set()
        max_time = 0

        while queue:
            node, time = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            max_time = max(max_time, time)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, time + 1))

        return max_time


# 使用例
# テストケースに基づいてツリーを構築
root = TreeNode(
    1,
    TreeNode(5, None, TreeNode(4)),
    TreeNode(3, TreeNode(10), TreeNode(6, TreeNode(9), TreeNode(2))),
)
solution = Solution()
print(solution.amountOfTime(root, 3))  # 出力は4
