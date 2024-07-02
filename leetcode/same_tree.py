# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None
        if not p and not q:
            return True
        # If one node is None and the other is not, they are not the same
        elif not p or not q:
            return False
        # Compare the values of the current nodes
        elif p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution_2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:

            node1, node2 = queue.popleft()

            if node1 and node2 and node1.val == node2.val:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

            elif node1 or node2:
                return False

        return True
