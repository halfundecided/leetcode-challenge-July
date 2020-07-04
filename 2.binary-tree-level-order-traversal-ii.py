"""
July 2, 2020
Binary Tree Level Order Traversal II 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        result = [[root.val]] + result
        print(result)

    def subarr(self, node: TreeNode) -> List[int]:

        # @lc code=end
