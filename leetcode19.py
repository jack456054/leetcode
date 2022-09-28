# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = self.double_linked_list(head, None)
        if tail.previous:
            return self.remove_node(tail, n)
        else:
            return None
        
    def double_linked_list(self, node: Optional[ListNode], previous: Optional[ListNode]):
        node.previous = previous
        if node.next:
            return self.double_linked_list(node.next, node)
        else:
            return node
    
    def remove_node(self, node: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            if node.next:
                node.next.previous = node.previous
            if node.previous:
                node.previous.next = node.next
            else:
                return node.next
        if not node.previous:
            return node
        else:
            return self.remove_node(node.previous, n-1)
            # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = self.double_linked_list(head, None)
        if tail.previous:
            return self.remove_node(tail, n)
        else:
            return None
        
    def double_linked_list(self, node: Optional[ListNode], previous: Optional[ListNode]):
        node.previous = previous
        if node.next:
            return self.double_linked_list(node.next, node)
        else:
            return node
    
    def remove_node(self, node: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            if node.next:
                node.next.previous = node.previous
            if node.previous:
                node.previous.next = node.next
            else:
                return node.next
        if not node.previous:
            return node
        else:
            return self.remove_node(node.previous, n-1)
            