class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent = (len(array) - 1) // 2
        for parent in reversed(range(first_parent + 1)):
            self.siftDown(parent, len(array) - 1, array)
        return array
