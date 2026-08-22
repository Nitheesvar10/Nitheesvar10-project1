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
            self.parent_a=parent
            self.a_d=depth
        if node.data==b:
            self.parent_b=parent
            self.b_d=depth
        
        self.solve(node.left,a,b,node,depth+1)
        self.solve(node.right,a,b,node,depth+1)
        
    def areCousins(self, root, a, b):
        # code here
        self.parent_a=None
        self.parent_b=None
        self.a_d=-1
        self.b_d=-1
        
        self.solve(root,a,b,None,0)
        
        if (self.parent_a !=self.parent_b) and (self.a_d==self.b_d):
            return True 
        else:
            return False 