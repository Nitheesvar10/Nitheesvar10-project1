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
            lenght=len(q)
            for i in range(lenght):
                e=q.popleft()
                if i==0:
                    result.append(e.data)
                    
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                    
                    
        return result