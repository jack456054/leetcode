# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        balanced = True
        self._isBalanced(root, balanced)
        return balanced

    def _isBalanced(self, root, balanced):
        if not root:
            return 0
        left = self._isBalanced(root.left, balanced)
        right = self._isBalanced(root.right, balanced)
        if abs(left - right) >= 2:
            balanced = False
        return 1 + max(left, right)
