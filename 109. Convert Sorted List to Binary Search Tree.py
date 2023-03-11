class Solution:

    def findMiddle(self, head):
        prevPtr = None
        slowPtr = head
        fastPtr = head

        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        if prevPtr:
            prevPtr.next = None

        return slowPtr

    def sortedListToBST(self, head):
        if not head:
            return None

        mid = self.findMiddle(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
