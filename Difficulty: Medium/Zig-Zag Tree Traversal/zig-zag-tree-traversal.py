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
        q1=deque([root])
        result=[]
        flag=True
        while q1:
            q2=deque([])
            l=len(q1)
            for _ in range(l):
                node=q1.popleft()
                
                if flag:
                    q2.append(node.data)
                else:
                
                    q2.appendleft(node.data)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
                    
            flag=not flag
            result.extend(q2)
            
        return result 
            
                
            
        