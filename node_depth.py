def nodeDepths(root, depth=0):
    return (
        0
        if root is None
        else depth
        + nodeDepths(root.left, depth + 1)
        + nodeDepths(root.right, depth + 1)
    )


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
