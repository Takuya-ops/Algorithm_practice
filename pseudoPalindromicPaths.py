class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root):
        def isPseudoPalindrome(count):
            odd = 0
            for val in count.values():
                if val % 2 != 0:
                    odd += 1
                if odd > 1:
                    return False
            return True

        def dfs(node, count):
            if not node:
                return 0

            count[node.val] = count.get(node.val, 0) + 1

            if not node.left and not node.right:
                result = 1 if isPseudoPalindrome(count) else 0
            else:
                result = dfs(node.left, count) + dfs(node.right, count)

            count[node.val] -= 1

            return result

        return dfs(root, {})
