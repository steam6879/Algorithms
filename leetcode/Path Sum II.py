from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, currentSum: int, path: list[int]):
            if not root:
                return None

            path.append(root.val)
            currentSum += root.val

            if not root.left and not root.right and currentSum == targetSum:
                self.ans.append(path[:])

            dfs(root.left, currentSum, path)
            dfs(root.right, currentSum, path)

            path.pop()

        self.ans = []
        dfs(root, 0, [])

        return self.ans
