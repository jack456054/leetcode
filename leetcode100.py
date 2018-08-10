# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
        elif p.val == q.val:
            return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)
        else:
            return False
