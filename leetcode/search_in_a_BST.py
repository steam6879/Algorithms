# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val not in root:
            return []
        ptr = root
        stack = []
        while True:
            if ptr is None:
                return None
            
            if val == ptr.val:
                break
            elif val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right

        def subTreeStack(root):
            if root is not None:
                subTreeStack(root.left)
                stack.append(root.val)
                subTreeStack(root.right)
        
        subTreeStack(ptr)
        
        return stack

            
            

