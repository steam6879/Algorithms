from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        def depth(root):
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        self.ans = 0
        depth(root)

        return self.ans
