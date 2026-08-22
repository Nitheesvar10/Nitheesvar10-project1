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
        q=deque([root])
        
        while q:
            lenght=len(q)
            
            for i in range(lenght):
                e=q.popleft()
                if i <lenght-1:
                    e.nextRight=q[0]
                    
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        return 
                    
                