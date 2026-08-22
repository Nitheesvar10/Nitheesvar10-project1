''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def solve(self,node):
        if node==None:
            return 0 
            
        left=self.solve(node.left)
        if left==-1:
            return -1 
            
        right=self.solve(node.right)
        if right ==-1:
            return -1 
        
        if abs(right-left)>1:
            return -1 
        
            
        return 1+max(left,right)
    def isBalanced(self, root):
        # code here
        x=self.solve(root)
        if x==-1:
            return False 
        else:
            return True 
        
        
        