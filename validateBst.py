class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, leftParent=None, rightParent=None):
    if tree is None:
        return True
    elif leftParent is not None and tree.value >= leftParent.value:
        return False
    elif rightParent is not None and tree.value < rightParent.value:
        return False
    return validateBst(tree.left, tree, rightParent) and validateBst(
        tree.right, leftParent, tree
    )
