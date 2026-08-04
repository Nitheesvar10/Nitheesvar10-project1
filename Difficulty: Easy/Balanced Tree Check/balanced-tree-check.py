''' Structure of binary tree node
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
        if left==-1:
            return -1
        right=self.solve(node.right)
        if right==-1:
            return -1

        if abs(left-right)>=2:
            return -1 
            
        return 1+max(left,right)
        
    def isBalanced(self, root):
        # code here
        
        c=self.solve(root)
        if c!=-1:
            return True 
        else:
            return False 
            
