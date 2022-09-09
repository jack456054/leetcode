# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.results = list()
        final_results = list()
        self._verticalTraversal(root, 0, 0)
        self.results = sorted(self.results, key=lambda x: (x[1], x[0], x[2]))
        for key, group in itertools.groupby(self.results, lambda x: x[1]):
            final_results.append([c[2] for c in group])
        return final_results

    def _verticalTraversal(self, root: Optional[TreeNode], row: int, col: int):
        self.results.append((row, col, root.val))
        if root.left:
            self._verticalTraversal(root.left, row + 1, col - 1)
        if root.right:
            self._verticalTraversal(root.right, row + 1, col + 1)
