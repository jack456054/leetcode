# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        if not root:
            return 0
        return 1 + max(self.isBalanced(root.left), self.isBalanced(root.right))
