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
        
        dict={}
        q=deque([[0,root]])
        while q:
            line,node=q.popleft()
            if line not in dict:
                dict[line]=node.data
            
            if node.left:
                q.append([line-1,node.left])
                
            if node.right:
                q.append([line+1,node.right])
                
                
        result=[]
                
        for line,val in sorted(dict.items()):
            result.append(val)
            
        return result
        