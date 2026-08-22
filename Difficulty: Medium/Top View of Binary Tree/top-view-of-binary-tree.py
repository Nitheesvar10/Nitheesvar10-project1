'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque 
class Solution:
    def topView(self, root):
        # code here
        d={}
        result=[]
        q=deque([[0,root]])
        while q:
            line,node=q.popleft()
            if line not in d:
                d[line]=node.data
                
            if node.left:
                q.append([line-1,node.left])
            if node.right:
                q.append([line+1,node.right])
                
        for line,val in sorted(d.items()):
            result.append(val)
            
        return result
            
            
            
                
            
            
            
            
        
        