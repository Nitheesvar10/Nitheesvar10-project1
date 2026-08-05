''' Structure of binary tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def solve(self,node,a,b,parent,depth):
        
        if node is None:
            return 
        
        if node.data==a:
            self.a_parent=parent
            self.depth_a=depth
        
        if node.data==b:
            self.b_parent=parent
            self.depth_b=depth
            
        self.solve(node.left,a,b,node,depth+1)
        self.solve(node.right,a,b,node,depth+1)
        
    def areCousins(self, root, a, b):
        self.a_parent=None
        self.b_parent=None
        self.depth_a=0
        self.depth_b=0
        self.solve(root,a,b,None,0)
        
        return (self.a_parent !=self.b_parent) and (self.depth_a==self.depth_b)

        
        # code here
        