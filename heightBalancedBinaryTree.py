class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.value = left
        self.value = right


def heightBalancedBinaryTree(tree):
    balanced = [True]
    heightBalancedBinaryTreeRec(tree, balanced)
    return balanced[0]


def heightBalancedBinaryTreeRec(tree, balanced):
    if tree is None:
        return 0
    left_height = heightBalancedBinaryTreeRec(tree.left, balanced)
    right_height = heightBalancedBinaryTreeRec(tree.right, balanced)

    if abs(left_height - right_height) > 1:
        balanced[0] = False
    height = max(left_height, right_height) + 1

    return height
