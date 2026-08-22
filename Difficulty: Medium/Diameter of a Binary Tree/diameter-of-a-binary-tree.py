''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def solve(self,node):
        if node is None:
            return 0
            
        left=self.solve(node.left)
        right=self.solve(node.right)
        self.diameter=max(self.diameter,left+right)
        return 1 + max(left,right)
        
    def diameter(self, root):
        if root is None :
            return None 
        self.diameter=0
        
        self.solve(root)
        return self.diameter
        
        
        
        
        