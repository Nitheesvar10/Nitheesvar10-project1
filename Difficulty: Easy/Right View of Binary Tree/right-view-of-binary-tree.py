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
        # code here
        
        result=[]
        q=deque([root])
        while q:
            lenght=len(q)
            for i in range(lenght):
                e=q.popleft()
                if i==lenght-1:
                    result.append(e.data)
                    
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                    
        return result 
                    
        