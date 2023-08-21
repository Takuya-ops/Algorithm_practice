class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    fast = linkedList
    slow = linkedList
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
