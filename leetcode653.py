# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         num_list = self.to_list(root)
#         p1 = 0
#         p2 = len(num_list) - 1
#         while p1 != p2:
#             if num_list[p1] + num_list[p2] == k:
#                 return True
#             elif num_list[p1] + num_list[p2] < k:
#                 p1 += 1
#             else:
#                 p2 -= 1
#         return False
        
#     def to_list(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         return self.to_list(root.left) + [root.val] + self.to_list(root.right)
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self._findTarget(root, k, set())
    def _findTarget(self, root: Optional[TreeNode], k: int, s: Set[int]) -> bool:
        if not root:
            return False
        if root.val in s:
            return True
        s.add(k - root.val)
        return self._findTarget(root.left, k, s) or self._findTarget(root.right, k, s)
            