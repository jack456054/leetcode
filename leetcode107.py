# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return None
        return [Solution.levelOrderBottom(self, root.left)] +[Solution.levelOrderBottom(self, root.right)] + [root.val]
