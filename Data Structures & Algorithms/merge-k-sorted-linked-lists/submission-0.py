# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2

        l1 = self.divide(lists, left, mid)
        l2 = self.divide(lists, mid + 1, right)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next