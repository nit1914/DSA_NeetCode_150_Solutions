# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        # Dummy node handles the case where we remove the head
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # left.next is the node we need to remove
        left.next = left.next.next

        return dummy.next