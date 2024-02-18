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



# Definition for a binary tree node.
from typing import Optional
 
class Solution:
    longest: int = 0
 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
 
            # 가장 긴 경로
            self.longest = max(self.longest, left + right)
            # 상태값
            return max(left, right) + 1
 
        dfs(root)
        return self.longest

if __name__ == '__main__':
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    s = Solution()

    print(s.diameterOfBinaryTree(root))