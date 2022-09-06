# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         is_prune = True
#         while is_prune:
#             if self.check_prune(root): # Base case.
#                 return None   
#             is_prune = self._pruneTree(root)
#         return root
        
#     def _pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         is_prune, left_is_prune, right_is_prune = False, False, False
#         if root.left:
#             if self.check_prune(root.left):
#                 root.left = None
#                 is_prune = True
#             else:
#                 left_is_prune = self._pruneTree(root.left)
#         if root.right:
#             if self.check_prune(root.right):
#                 root.right = None
#                 is_prune = True
#             else:
#                 right_is_prune = self._pruneTree(root.right)
#         return is_prune or left_is_prune or right_is_prune
        
            
#     def check_prune(self, root: Optional[TreeNode]) -> bool:
#         if root.val == 0 and not root.left and not root.right:
#             return True
#         return False

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.val and not root.left and not root.right:
            return None
        return root
