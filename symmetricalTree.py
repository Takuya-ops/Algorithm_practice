class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    if not tree:
        return True
    queue = [(tree.left, tree.right)]
    while queue:
        left, right = queue.pop(0)
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.value != right.value:
            return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    return True
