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
        if root == None:
            return []
        queue, result = [], []
        queue.append(root)
        # BFS
        while queue != []:
            size = len(queue)
            currentLevel = []
            for i in range(size):
                currentNode = queue.pop(0)
                currentLevel.append(currentNode.val)
                if currentNode.left != None:
                    queue.append(currentNode.left)
                if currentNode.right != None:
                    queue.append(currentNode.right)
            result.append(currentLevel)
        result.reverse()
        return result

        # @lc code=end
