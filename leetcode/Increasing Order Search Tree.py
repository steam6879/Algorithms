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
        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            order.append(root.val)
            dfs(root.right)

        dfs(root)
        ans = TreeNode()
        while order:
            ans.val = order.popleft()
            ans.right

        return ans