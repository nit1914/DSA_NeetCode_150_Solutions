# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        prev_group = dummy

        while True:
            # Find the kth node
            kth = prev_group

            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            # Save the node after this group
            next_group = kth.next

            # Reverse the k nodes
            prev = next_group
            curr = prev_group.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous group to reversed group
            temp = prev_group.next
            prev_group.next = kth

            # Move to the next group
            prev_group = temp