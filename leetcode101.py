# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return Solution.isMirror(root.left, root.right)

    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and Solution.isMirror(left.left, right.right) and Solution.isMirror(left.right, right.left)
