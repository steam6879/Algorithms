from typing import Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        if root.val == subRoot.val:
            self.isSubtree(root.left, subRoot.left)
            self.isSubtree(root.right, subRoot.right)

            return True
        
        else:
            self.isSubtree(root.left, subRoot.left)
            self.isSubtree(root.right, subRoot.right)

        return False
        