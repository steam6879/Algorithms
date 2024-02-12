# Definition for a binary tree node.
from typing import Optional

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

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currentSum):
            if not root:    #root가 존재하지 않는 예외상황 처리.
                return False
            
            currentSum += root.val  #누적하여 합.
            if not root.left and not root.right:  # Leaf node
                return currentSum == targetSum  #진위판단.
            
            # Recursive calls for left and right subtrees
            return dfs(root.left, currentSum) or dfs(root.right, currentSum)
        
        return dfs(root, 0) #0부터 누적하여 summation.
        
if __name__ == '__main__':
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    s = Solution()
    print(s.hasPathSum(root, 22))