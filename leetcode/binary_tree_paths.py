# Definition for a binary tree node.
# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"
    
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root	

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(node, path):
            path += '->'
            path += str(node.val)

            if not node.left and not node.right:
                return ans.append(path[2:])

            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)
            
        ans = []
        dfs(root, "")
        return ans

    
if __name__ == '__main__':
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    s = Solution()
    print(s.binaryTreePaths(root))