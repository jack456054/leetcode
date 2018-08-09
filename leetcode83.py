# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        init = head
        if not head:
            return head
        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return init
