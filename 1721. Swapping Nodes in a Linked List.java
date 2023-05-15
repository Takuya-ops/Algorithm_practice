class Solution {
  public ListNode swapNodes(ListNode head, int k) {
    int listLength = 0;
    ListNode frontNode = null;
    ListNode endNode = null;
    ListNode currentNode = head;
    while (currentNode != null) {
      listLength++;
      if (listLength == k) {
        frontNode = currentNode;
      }
      currentNode = currentNode.next;
    }
    endNode = head;
    for (int i = 1; i <= listLength - k; i++) {
      endNode = endNode.next;
    }
    int temp = frontNode.val;
    frontNode.val = endNode.val;
    endNode.val = temp;
    return head;
  }
}