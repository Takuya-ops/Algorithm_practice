# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, a, b):
            if node:
                a, b = min(a, node.val), max(b, node.val)
                self.ans = max(self.ans, b - a)
                dfs(node.left, a, b), dfs(node.right, a, b)

        dfs(root, float("inf"), float("-inf"))
        return self.ans
