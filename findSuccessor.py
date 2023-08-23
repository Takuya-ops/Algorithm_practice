class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right != None:
        current = node.right
        while True:
            if current.left != None:
                current = current.left
            else:
                return current

    child = node
    parent = node.parent
    while True:
        if parent == None:
            return None
        if child == parent.left:
            return parent
        child = parent
        parent = parent.parent
