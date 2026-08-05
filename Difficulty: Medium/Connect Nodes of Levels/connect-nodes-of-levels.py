'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
'''        
from collections import deque
class Solution:
    def connect(self, root):
        # code here 
        
        if root is None:
            return 
        
        q=deque([root])
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                
                if (i<size-1):
                    node.nextRight=q[0]
                else:
                    node.nextRight=None 
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
                
        return root 