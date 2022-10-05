# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        else:
            self._addOneRow(root, val, depth - 1)
        return root

    def _addOneRow(self, node: Optional[TreeNode], val: int, depth: int):
        if not node:
            return
        if depth == 1:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
            return
        self._addOneRow(node.left, val, depth - 1)
        self._addOneRow(node.right, val, depth - 1)
