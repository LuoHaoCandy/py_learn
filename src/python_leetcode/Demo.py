class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode(1)
        node.next = head
        node1 = node
        node2 = node
        for i in range(n + 1):
            node2 = node2.next

        while node2.next is None:
            node1=node1.next
            node2=node2.next

        node1.next=node1.next.next

        return node.next

