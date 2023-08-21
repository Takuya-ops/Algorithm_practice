class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    while cur.next is not None:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return linkedList
