''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''
from collections import deque
class Solution:
    
    
    def leftView(self, root):
        # code here
        if root is None:
            return []
        
        result=[]
        q=deque([root])
        while q:
            l=len(q)
            
            for i in range(l):
                node=q.popleft()
                
                if i ==0:
                    result.append(node.data)
                    
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
                
        return result 
        