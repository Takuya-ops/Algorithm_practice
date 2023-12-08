class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root):
        if not root:
            return ""

        result = str(root.val)

        if root.left:
            result += "(" + self.tree2str(root.left) + ")"

        if root.right:
            if not root.left:
                result += "()"
            result += "(" + self.tree2str(root.right) + ")"

        return result


# テスト
sol = Solution()

# 例1: [1,2,3,4]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

# 例2: [1,2,3,null,4]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)

result1 = sol.tree2str(root1)
result2 = sol.tree2str(root2)

print(result1, result2)
