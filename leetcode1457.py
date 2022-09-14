class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        return self._pseudoPalindromicPaths(root, set())

    def _pseudoPalindromicPaths(self, root: Optional[TreeNode], remains: Set[int]):
        remains.remove(root.val) if root.val in remains else remains.add(root.val)
        if root.left and root.right:
            return self._pseudoPalindromicPaths(
                root.left, remains.copy()
            ) + self._pseudoPalindromicPaths(root.right, remains)
        elif root.left:
            return self._pseudoPalindromicPaths(root.left, remains.copy())
        elif root.right:
            return self._pseudoPalindromicPaths(root.right, remains.copy())
        else:
            return 1 if len(remains) <= 1 else 0
