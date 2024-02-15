# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        countMap = {}
        def dfs(root):
            if not root:
                return None
            
            if root.val in countMap:
                countMap[root.val] += 1

            else:
                countMap[root.val] = 0

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        maxCount = max(countMap.values())
        ans = []
        for i in countMap:
            if countMap[i] == maxCount:
                ans.append(i)
        return ans