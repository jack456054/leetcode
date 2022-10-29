# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        new_head = head.next
        self._swapPairs(head)
        return new_head
    def _swapPairs(self, node, pre_node=None):
        next = node.next.next
        next_node = node.next
        node.next = next
        next_node.next = node
        if pre_node:
            pre_node.next = next_node
        if next:
            if next.next:
                self._swapPairs(next, node)
