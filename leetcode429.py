"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.results = []
        if root:
            self._levelOrder(root, 0)
        return(self.results)
        
    def _levelOrder(self, root: 'Node', level: int):
        try:
            self.results[level]
        except IndexError:
            self.results.insert(level, [])
        self.results[level].append(root.val)
        for child in root.children:
            self._levelOrder(child, level + 1)
            