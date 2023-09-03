class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    cache = []
    treesum = get_sum(tree, cache)
    if treesum % 2 > 0:
        return 0
    to_find = treesum // 2
    if to_find in cache:
        return to_find
    return 0


def get_sum(node, cache):
    if node is None:
        return 0
    right = get_sum(node.right, cache)
    left = get_sum(node.left, cache)
    cache.append(node.value + right + left)
    return node.value + right + left
