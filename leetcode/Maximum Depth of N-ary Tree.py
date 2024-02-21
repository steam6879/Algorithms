from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        que = deque(root)
        depth = 1
        que.append((root, depth))

        while que:
            node, depth = que.popleft()
            if node.children:
                for child in node.children:
                    que.append((child, depth + 1))
        
        return depth



class Solution:     #DFS reculsive algorithm
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        maxdepth=0
        for child in root.children:
            maxdepth=max(self.maxDepth(child),maxdepth)
        return maxdepth+1