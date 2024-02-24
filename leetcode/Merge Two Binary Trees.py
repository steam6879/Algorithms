from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root3 = TreeNode()
        root3.val = None
        root3.left = None
        root3.right = None

        def subMerge(root1, root2, root3):
            if root1 and root2:
                root3.val = root1.val + root2.val

            if not root1 and not root2:
                return None

            if root1 and not root2:
                root3.val = root1.val

            if not root1 and root2:
                root3.val = root2.val
            
            if root1 or root2:
                subMerge(root1.left, root2.left, root3.left)
                subMerge(root1.right, root2.right, root3.right)

        subMerge(root1, root2, root3)
        return root3
    

# chat gpt
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged
