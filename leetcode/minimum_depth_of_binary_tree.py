# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left or root.right:
            leftDepth = 1 + self.minDepth(root.left)
            rightDepth = 1 + self.minDepth(root.right)

        return min(leftDepth, rightDepth)