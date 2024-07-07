from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        ans = []
        que = deque([root])

        while que:
            currLevel = []
            for _ in range(len(que)):
                node = que.popleft()

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

                currLevel.append(node.val)
            ans.append(currLevel)

        return ans
