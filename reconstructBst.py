class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    root = BST(preOrderTraversalValues[0])
    left_values = []
    right_values = []
    for n in preOrderTraversalValues[1:]:
        if n < root.value:
            left_values.append(n)
        else:
            right_values.append(n)
    if left_values:
        root.left = reconstructBst(left_values)
    if right_values:
        root.right = reconstructBst(right_values)
    return root
