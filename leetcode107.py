# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        result = []
        level = 0
        if root:
            Solution._levelOrderBottom(root, level, result)
        result.reverse()
        return result

    def _levelOrderBottom(root, level, result):
        if len(result) <= level:
            result.append([])
        if root:
            result[level].append(root.val)
        if root.left:
            Solution._levelOrderBottom(root.left, level + 1, result)
        if root.right:
            Solution._levelOrderBottom(root.right, level + 1, result)
