from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        ans = []
        que = deque([root])

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                curr = node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            ans.append(curr)

        return ans
