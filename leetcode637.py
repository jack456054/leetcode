# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.results = defaultdict(list)
        list_result = []
        self.average_of_level(root, 0)
        for i in range(len(self.results)):
            list_result.append(round(sum(self.results[i]) / len(self.results[i]), 5))
        return list_result

    def average_of_level(self, root: Optional[TreeNode], level: int):
        self.results[level].append(root.val)
        if root.left:
            self.average_of_level(root.left, level + 1)
        if root.right:
            self.average_of_level(root.right, level + 1)
