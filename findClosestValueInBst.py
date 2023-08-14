def findClosestValueInBst(tree, target):
    print("Target:", target)

    def find_recursively(tree, closest):
        print("----")
        if tree is None:
            return closest
        print("Closest:", closest)
        print("Value:", tree.value)

        if abs(target - tree.value) < abs(target - closest):
            closest = tree.value
            print("Updated closest:", closest)

        if target > tree.value:
            print("Down to the right")
            return find_recursively(tree.right, closest)
        elif target < tree.value:
            print("Down to the left")
            return find_recursively(tree.left, closest)

        return closest

    return find_recursively(tree, float("inf"))


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
