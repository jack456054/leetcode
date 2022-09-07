# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        left = f'({self.tree2str(root.left)})' if root.left else ()
        right = f'({self.tree2str(root.right)})' if root.right else ''
        return f'{root.val}{left}{right}' if left or right else str(root.val)
