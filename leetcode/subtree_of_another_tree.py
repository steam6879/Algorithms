from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(root, subRoot):
            if not root and not subRoot:
                return True
            
            elif not root or not subRoot or root.val != subRoot.val:
                return False
            
            return root.val == subRoot.val and isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)
        
        def dfs(root, subRoot):
            if not root:
                return False
            
            if root.val == subRoot.val:
                return isIdentical(root, subRoot)
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)
    
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        if self.isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val \
                    and self.isSameTree(p.left, q.left) \
                    and self.isSameTree(p.right, q.right)
        
        return p is q


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        if self.isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
        

    def identical(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return identical(p.left, q.left) and identical(p.right, q.right)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root1, root2):
            if root1 == None or root2 == None: 
                return root1 == root2
            
            return root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
        
        def dfs(root, subRoot):
            if root == None: 
                return False
            
            return isEqual(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)