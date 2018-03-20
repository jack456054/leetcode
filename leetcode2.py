# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = [int(i) for i in str(Solution.oneList(l1) + Solution.oneList(l2))]
        invres = []
        for i in range(len(result)):
            invres.append(result[len(result) - 1 - i])
        return invres

    def oneList(l):
        if not l:
            return 0
        return l.val + Solution.oneList(l.next) * 10
