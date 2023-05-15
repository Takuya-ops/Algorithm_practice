class Solution {
public:
    ListNode * swapNodes(ListNode * head, int k) {
        int listLength = 0;
        ListNode * currentNode = head;
        while (currentNode) {
            listLength++;
            currentNode = currentNode -> next;
        }
        ListNode * frontNode = head;
        for (int i=1; i<k; i++) {
            frontNode = frontNode -> next;
        }
        ListNode * endNode = head;
        for (int i=1; i <= listLength - k; i++) {
            endNode = endNode -> next;
        }
        swap(frontNode -> val, endNode -> val);
        return head;
    }
};