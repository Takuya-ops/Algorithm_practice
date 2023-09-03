class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    global longestPath
    longestPath = 0
    calcurateLongestPath(tree)
    return longestPath


def calcurateLongestPath(root):
    global longestPath
    if root is None:
        return 0
    leftDepth = calcurateLongestPath(root.left)
    rightDepth = calcurateLongestPath(root.right)

    curr_longestPath = leftDepth + rightDepth
    longestPath = max(curr_longestPath, longestPath)

    return max(leftDepth, rightDepth) + 1
