# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        self.paths = []
        self.dfs(root, targetSum, [])
        return self.paths

    def dfs(self, root: TreeNode, targetSum: int, path: list[int]):
        if not root:
            return

        # Append current node's value to the path
        path.append(root.val)
        targetSum -= root.val

        # If leaf node and targetSum is 0, add current path to paths
        if not root.left and not root.right and targetSum == 0:
            self.paths.append(path[:])  # Make a copy of path

        # Recursively traverse left and right subtrees
        self.dfs(root.left, targetSum, path)
        self.dfs(root.right, targetSum, path)

        # Backtrack: remove current node from path
        path.pop()

# Example usage:
# Constructing the tree
"""
   5
  / \
 4   8
/   / \
11  13  4
/  \    / \
7   2  5   1
"""
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

solution = Solution()
target_sum = 22
result = solution.pathSum(root, target_sum)
print(result)  # Output: [[5, 4, 11, 2], [5, 8, 4, 5]]
