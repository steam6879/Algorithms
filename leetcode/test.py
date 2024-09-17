from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True
        
        if not (min_val < root.val < max_val):
            return False
        
        return (self.isValidBST(root.left, min_val, root.val) and
                self.isValidBST(root.right, root.val, max_val))

# Time complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def isValidBST(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        # An empty tree is a valid BST
        if not node:
            return True
 
        # The current node's value must be between low and high
        if node.val <= low or node.val >= high:
            return False
 
        # Recursively validate the left and right subtree
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
 
    return validate(root)