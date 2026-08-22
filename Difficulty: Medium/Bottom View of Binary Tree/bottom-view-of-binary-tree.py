'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        q=deque([[0,root]])
        result=[]
        d={}
        while q:
            line,e=q.popleft()
            d[line]=e
            
            if e.left:
                q.append([line-1,e.left])
            if e.right:
                q.append([line+1,e.right])
                
        for line,val in sorted(d.items()):
            result.append(val.data)
            
        return result 
        
                
            
        