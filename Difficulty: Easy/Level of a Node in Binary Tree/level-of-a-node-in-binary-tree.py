'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def getLevel(self,  root, target):
        # code here
        q=deque([root])
        level=0
        while q:
            level+=1
            for _ in range(len(q)):
                node=q.popleft()
                
                if node.data==target:
                    return level 
                else:
                
                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
                    
            
        return 0
