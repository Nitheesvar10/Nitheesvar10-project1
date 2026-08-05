'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def rightView(self, root):
        
        if root is None:
            return []
            
        result=[]
        # code here
        q=deque([root])
        while q:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                
                if i==l-1:
                    result.append(node.data)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return result
            
        