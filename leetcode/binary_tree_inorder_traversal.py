# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        while root.left is not None and root.right is not None:
            if root.left is not None:
                self.inorderTraversal(root.left)
            answer.append(root.val)
            if root.right is not None:
                self.inorderTraversal(root.right)

        return answer
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] \
            + self.inorderTraversal(root.right)
