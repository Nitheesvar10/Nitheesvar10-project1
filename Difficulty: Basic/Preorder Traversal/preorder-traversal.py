'''Structure of Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def dfs(self,node):
        if node is None:
            return 
        self.result.append(node.data)
        self.dfs(node.left)
        self.dfs(node.right)
        
        
    def preOrder(self, root):
        
    # code here
        self.result=[]
        self.dfs(root)
        
        return self.result
    
    