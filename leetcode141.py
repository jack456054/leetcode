# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        seen = []
        if not head:
            return False
        elif head not in seen:
            seen.append(head)
        else:
            return True
        return self.hasCycle(head.next)
