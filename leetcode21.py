# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = previous = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                previous.next, l1 = l1, l1.next
            else:
                previous.next, l2 = l2, l2.next
            previous = previous.next
        if l1:
            previous.next = l1
        elif l2:
            previous.next = l2
        return head.next
