class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(value)
                    break

            elif value >= currentNode.value:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = BST(value)
                    break
        return self

    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if currentNode.value == value:
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False

    def remove(self, value, parentNode=None):
        parentNode, node = self.GetFirst(value, parentNode)
        if node is None:
            return
        if self.IsOnlyNode(parentNode, node):
            return

        if node.left and node.right:
            repNode = node.right.GetMinNode(node)
            node.value = repNode.value
            node.right.remove(repNode.value, node)

        elif node.left is None and node.right is None:
            if parentNode.left == node:
                parentNode.left = None
            elif parentNode.right == node:
                parentNode.right = None
        elif node.left:
            repNode = node.left.GetMaxNode(node)
            node.value = repNode.value
            node.left.remove(repNode.value, node)
        elif node.right:
            repNode = node.right.GetMinNode(node)
            node.value = repNode.value
            node.right.remove(repNode.value, node)
        return self

    def IsOnlyNode(self, parentNode, node):
        return parentNode is None and node.left is None and node.right is None

    def GetFirst(self, value, parentNode=None):
        node = self

        while node is not None:
            if value == node.value:
                return parentNode, node
            elif value < node.value:
                parentNode = node
                node = node.left
            else:
                parentNode = node
                node = node.right
        return None, None

    def GetMinNode(self, parentNode):
        node = self
        while node.left:
            parentNode = node
            node = node.left
        return node

    def GetMaxNode(self, parentNode):
        node = self
        while node.right:
            parentNode = node
            node = node.right
        return node
