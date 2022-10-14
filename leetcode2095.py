# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer_one = pointer_two = head
        if not head.next:
            return None
        while True:
            pointer_two = pointer_two.next.next
            if pointer_two == None or pointer_two.next == None:
                pointer_one.next = pointer_one.next.next
                break
            pointer_one = pointer_one.next
        return head
