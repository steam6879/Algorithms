# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#         def dfs(root, currentSum):
#             if not root:
#                 return currentSum
            
#             if not root.left.left and not root.left.right:
#                 currentSum += root.left.val

#             dfs(root.left, currentSum)
#             dfs(root.right, currentSum)

#         return dfs(root, 0)
            
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)