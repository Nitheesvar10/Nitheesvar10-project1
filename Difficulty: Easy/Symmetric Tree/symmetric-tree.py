'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def solve(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        
        if (node1 is None or node2 is None):
            return False 
        
     
        if node1.data !=node2.data:
            return False
            
        return self.solve(node1.left,node2.right )and self.solve(node1.right,node2.left)
        
        

        
    def isSymmetric(self, root):
        # code here
        return self.solve(root.left,root.right)
        