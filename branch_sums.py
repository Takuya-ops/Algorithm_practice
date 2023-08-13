# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return []

    branches = branchSums(root.left) + branchSums(root.right)
    return [x + root.value for x in branches] if branches else [root.value]
