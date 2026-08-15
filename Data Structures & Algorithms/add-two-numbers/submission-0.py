# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get current digits
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Add digits + carry
            total = x + y + carry

            # Current digit and new carry
            carry = total // 10
            digit = total % 10

            # Create result node
            curr.next = ListNode(digit)
            curr = curr.next

            # Move forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next