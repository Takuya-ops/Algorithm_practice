class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent = (len(array) - 1) // 2
        for parent in reversed(range(first_parent + 1)):
            self.siftDown(parent, len(array) - 1, array)
        return array

    def siftDown(self, cidx, endidx, heap):
        child_one_idx = cidx * 2 + 1
        while child_one_idx <= endidx:
            child_two_idx = cidx * 2 + 2 if cidx * 2 + 2 <= endidx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                potential_swap_idx = child_two_idx
            else:
                potential_swap_idx = child_one_idx

            if heap[potential_swap_idx] < heap[cidx]:
                self.swap(cidx, potential_swap_idx, heap)
                cidx = potential_swap_idx
                child_one_idx = cidx * 2 + 1
            else:
                break

    def siftUp(self, idx, heap):
        parent_idx = (idx - 1) // 2
        while idx > 0 and heap[idx] < heap[parent_idx]:
            self.swap(idx, parent_idx, heap)
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        min_value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return min_value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, idx1, idx2, heap):
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]
