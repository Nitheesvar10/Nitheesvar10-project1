''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def levelOrder(self, root):
        # code here
        result=[]
        q=deque([root])
        while len(q)!=0:
            e=q.popleft()
            result.append(e.data)
            if e.left:
                q.append(e.left)
            if e.right:
                q.append(e.right)
                
        return result 
            