import collections
root1 = [4, 2, 7, 1, 3, 6, 9]


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        queue = collections.deque([root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root


a = Solution()
print(a.invertTree(root1))
