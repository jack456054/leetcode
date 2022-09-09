# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self._goodNodes(root, float(-inf))
        return self.count

    def _goodNodes(self, root: TreeNode, max_num: float):
        if root.val >= max_num:
            self.count += 1
            max_num = root.val
        if root.left:
            self._goodNodes(root.left, max_num)
        if root.right:
            self._goodNodes(root.right, max_num)
