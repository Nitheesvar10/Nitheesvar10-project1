''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        # code here
        result=[]
        q=deque([root])
        flag=True 
        while q:
            q2=deque([])
            
            leng=len(q)
            for _ in range(leng):
                e=q.popleft()
                
                if flag:
                    q2.append(e.data)
                else:
                    q2.appendleft(e.data)
                    
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
                    
            flag=not flag
            result.extend(q2)
            
        return result 
                