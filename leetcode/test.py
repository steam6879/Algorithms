from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        order = deque()
        
        # Perform in-order traversal to get the sorted order of values
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            order.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        # Construct the new tree using the sorted order
        dummy = TreeNode()
        current = dummy
        while order:
            current.right = TreeNode(val=order.popleft())
            current = current.right
        
        return dummy.right
