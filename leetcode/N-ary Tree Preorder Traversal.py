from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return None
            
            ans.append(root)
            
            for child in root.children:
                dfs(child)
        
        return ans
        
