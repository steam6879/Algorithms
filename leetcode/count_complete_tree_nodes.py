# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if root is None: 
#             return 0

#         leftN, rightN = 1, 1
#         while root.left is not None:
#             leftN += 1
#             root = root.left

#         while root.right is not None:
#             rightN += 1
#             root = root.right

#         if leftN == rightN:
#             return 2**leftN - 1
        
#         else:
#             return 2**leftN - 2
        
sol = Solution()
