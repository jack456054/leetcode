# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        length = len(nums)
        result = TreeNode(nums[length // 2])
        result.left = Solution.sortedArrayToBST(self, nums[:length // 2])
        result.right = Solution.sortedArrayToBST(self, nums[length // 2 + 1:])
        return result
