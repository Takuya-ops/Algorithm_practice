class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    if tree1 and tree2:
        newTree = BinaryTree(tree1.value + tree2.value)
        newTree.left = mergeBinaryTrees(tree1.left, tree2.left)
        newTree.right = mergeBinaryTrees(tree1.right, tree2.right)
        return newTree
    return tree1 or tree2
