from typing import Optional

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        que=Deque()
        que.append(root)
        count=0
        while(que):
            n=len(que)
            for _ in range(n):
                cur=que.popleft()
                for i in cur.children:
                    que.append(i)
            count+=1
        return count
    
def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        queue = collections.deque()
        depth = 1
        queue.append((root,depth))
        while queue:
            node, depth = queue.popleft()
            if node.children:
                for child in node.children:
                    queue.append((child,depth+1))
        return depth