# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # 3. Merge the two halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2