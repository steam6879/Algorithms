from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root == p or root == q:
                return root
            
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            
            if r and l:
                return root
            elif r:
                return r
            else:
                return l
출처: https://sofar-sogood.tistory.com/entry/LeetCode-236-Lowest-Common-Ancestor-of-a-Binary-Tree-Python [작심삼일:티스토리]